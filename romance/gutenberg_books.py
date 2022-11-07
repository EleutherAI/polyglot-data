'''
Process a downloaded Gutenberg book dump, and create a dataset from it

The dump must be a text dump for a single language, downloaded using the
procedure defined in https://www.gutenberg.org/policy/robot_access.html
'''

import sys
from pathlib import Path
import datetime
import re
import zipfile
import json
import lzma
import gzip
from enum import Enum, auto
import argparse
from typing import Dict, List, Set


# Language mapping: ISO 639-1 codes to Gutenberg names
LANG_MAP = {
    "pt": ["Portuguese", "Portugese"],
    "es": ["Spanish"],
    "fr": ["French"],
    "it": ["Italian"],
    "ro": ["Romanian"],
    "en": ["English"]
}

# Encoding maps
ENC_MAP = {
    "iso latin-1": "iso-8859-1",
    "unicode utf-8": "utf-8",
    "iso-646-us (us-ascii)": "ascii"
}


# Regexes for book parsing
META = br"""
(Title|
 Author|
 Release \s Date|
 Language|
 (?:Character \s set \s e|E)ncoding
)
:\s+
(\S.*\S)
"""

START = br"""
\*\*\* \s* START \s OF \s TH(IS|E) \s PROJECT \s GUTENBERG \s EBOOK \s |
\* END \s THE \s SMALL \s PRINT! \s |
The \s Project \s Gutenberg \s Etext \s of \s 
"""

END = br"""
\s* \*\*\* \s* END \s OF \s TH(?:IS|E) \s PROJECT \s GUTENBERG \s EBOOK \s |
End \s of \s the \s Project \s Gutenberg \s EBook \s |
End \s of \s Project \s Gutenberg's \s Etext \s |
End \s of \s this \s is \s COPYRIGHTED \s Project \s Gutenberg \s Etext
"""

PROD = br"""
Produced \s by \s |This \s Project \s Gutenberg \s Etext \s prepared \s by \s 
"""

LANG = r', \s+ | (?: \s+ (?: with | and ) \s+ ) | \s* / \s*'


def log(msg, *args):
    print(msg, *args, file=sys.stderr)


def openfile(name: Path):
    """
    Open the Zip containing the book and return a file-like object pointing to
    the first file in it
    """
    if name.suffix == ".zip":
        zf = zipfile.ZipFile(name)
        filelist = zf.namelist()
        return zf.open(filelist[0])
    else:
        raise Exception('unsupported file type '+name)


def gid(filename: str) -> str:
    """
    Compose the Gutenberg Book Id from the filename
    """
    name = Path(filename).stem
    m = re.match(r'(\d+)(?:-\d+)', name)
    return m.group(1) if m else name


class ParseStatus(Enum):
    HEADER = auto()
    START = auto()
    PROD = auto()
    BOOK = auto()


def _process_book(filename: str, language: Set, multilang: bool = False,
                  encoding: str = "utf-8", fmt: str = "gz") -> Dict:
    """
    Open a text book, parse it and dump it to an output file, cropping out
    the header and footers, and extracting metadata from the header
    """
    log("  book:", filename)

    book = {"dataset": "Gutenberg", "src": str(filename), "id": gid(filename)}
    meta = {}
    words, chars, prod, text, bookenc = (0, 0, b"", b"", "")
    status = ParseStatus.HEADER

    lang_map = {name: iso for iso, nlist in LANG_MAP.items() for name in nlist}

    with openfile(filename) as fin:
        for line in fin:
            #print(status.name, line, end="\n")
            if re.match(END, line, flags=re.X):

                enc = bookenc or encoding
                enc = ENC_MAP.get(enc, enc)
                if enc == "ascii":
                    enc = "iso-8859-1"

                book.update({k.decode(enc).lower(): v.decode(enc)
                             for k, v in meta.items()})
                book.update({"words": words, "characters": chars,
                             "original_encoding": bookenc})
                if prod:
                    book["production"] = prod.decode(enc)

                try:
                    book["text"] = text.decode(encoding=enc)
                except UnicodeDecodeError as e:
                    log("Warning: book decoding error:", str(e))
                    return
                return book

            elif re.match(START, line, flags=re.X):

                status = ParseStatus.START

            elif status == ParseStatus.HEADER:

                m = re.match(META, line, flags=re.X)
                if not m:
                    continue

                nam, val = m.groups()
                if nam == b"Language":
                    book_lang = re.split(LANG, val.decode("ascii"), flags=re.X)
                    book_lang = [lang_map.get(v, v) for v in book_lang]
                    if len(book_lang) > 1 and not multilang:
                        log(f"Warning: Skipping book. Multiple languages: {book_lang}")
                        return
                    if language not in set(book_lang):
                        log(f"Warning: Skipping book. Invalid language for {filename}: {val.decode('ascii')}")
                        return
                    meta[b"language"] = ",".join(book_lang).encode("ascii")
                elif re.search(rb"(e|E)ncoding", nam):
                    bookenc = val.decode("ascii").lower()
                else:
                    meta[nam] = val

            else:

                if status == ParseStatus.START:
                    if line.isspace() or line.endswith(b"***\n"):
                        continue
                    elif re.match(PROD, line, flags=re.X):
                        status = ParseStatus.PROD

                if status == ParseStatus.PROD:
                    if line.isspace():
                        status = ParseStatus.BOOK
                    else:
                        prod += line
                    continue

                text += line
                chars += len(line)
                words += len(line.split())

    log("Warning: Skipping book. No end of book detected:", filename)
    return


def process_book(book, *args, **kwargs) -> Dict:
    try:
        return _process_book(book, *args, **kwargs)
    except Exception as e:
        log("Error while processing: {}: {}".format(book, e))

# --------------------------------------------------------------------

def better(new: Dict, current: Dict) -> bool:
    """
    Decide if the `new` version is better than the `current` one
    """
    if current is None:
        return True
    cur_enc = current["original_encoding"]
    if cur_enc == "utf-8":
        return False
    elif cur_enc == "ascii":
        return True



class BookParser:

    def __init__(self, language, book_encoding, dest, out_fmt, chunk_size: int,
                 multilang: bool):
        self.language = language
        self.book_encoding = book_encoding
        self.dest = Path(dest)
        self.fmt = out_fmt
        self.size = chunk_size
        self.multilang = multilang
        self.meta = []
        if not self.dest.is_dir():
            self.dest.mkdir(parents=True)


    def add_book(self, book: Dict):
        num = len(self.meta) + 1
        if self.fmt == "jsonl":
            outfile = self.dest / f"{num//self.size:02}.jsonl.gz"
            with gzip.open(outfile, "at", encoding="utf-8") as fout:
                json.dump(book, fout, ensure_ascii=False)
            book.pop("text")
            book["file"] = str(outfile.name)
        else:
            outdir = self.dest / f"{num//self.size:02}"
            if not outdir.is_dir():
                outdir.mkdir(parents=True)
            mod = lzma if self.fmt == "xz" else gzip
            outname = outdir / (Path(book["src"]).stem + ".txt." + self.fmt)
            with mod.open(outname, "wt", encoding="utf-8") as fout:
                fout.write(book.pop("text"))
            book["file"] = str(outname.relative_to(outname.parents[2]))

        self.meta.append(book)


    def iter_booksdir(self, orig: Path):
        subd = []
        books = []
        for elem in orig.iterdir():
            if elem.is_dir():
                subd.append(elem)
            elif elem.suffix == ".zip":
                books.append(elem)

        # Parse all books in the folder
        if books:
            books = [process_book(b, self.language, multilang=self.multilang,
                                  encoding=self.book_encoding)
                     for b in books]

            # All files in the same final folder are for the same book
            chosen = None
            for b in filter(None, books):
                if better(b, chosen):
                    chosen = b

            if not chosen:
                log("Warning: no valid book for", elem)
            else:
                self.add_book(chosen)

        # Recurse through subdirectories
        for s in subd:
            self.iter_booksdir(s)


# --------------------------------------------------------------------

def extract_books(orig: Path, dest: Path, language: Set, out_format: str,
                  chunk_size: int, multilang: bool = False):

    start = datetime.datetime.now()
    log(". Start:", start)
    prs = BookParser(language, "iso-8859-1", dest / "DATA", out_format,
                     chunk_size, multilang)
    prs.iter_booksdir(orig)
    log(". End process:", datetime.datetime.now())

    log(". Saving JSON index")
    with open(dest / "index.json", "w") as f:
        json.dump(prs.meta, f, indent=2, ensure_ascii=False)

    log(". Done. Total elapsed: ", datetime.datetime.now() - start)

    words = sum(b.get("words", 0) for b in prs.meta)
    characters = sum(b.get("characters", 0) for b in prs.meta)
    log(". Stats:")
    log("  books:", len(prs.meta))
    log("  words:", words)
    log("  characters:", characters)


def parse_args(args: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="process a dump of Gutenberg books")

    g0 = parser.add_argument_group("Input/output paths")
    g0.add_argument("indir", help="directory holding the Gutenberg crawling")
    g0.add_argument("outdir", help="destination directory")

    g1 = parser.add_argument_group("Options")
    g1.add_argument("--lang", "--language", required=True,
                    help="set the required language")
    g1.add_argument("--allow-multi", action="store_true",
                    help="allow multi-language books")
    g1.add_argument("--chunk-size", type=int, default=100,
                    help="number of books to join together (default: %(default)d)")
    g1.add_argument("--output-format", choices=("jsonl", "gz", "xz"),
                    default="gz",
                    help="book output format (default: %(default)s)")
    return parser.parse_args(args)


def main(args: List[str] = None):
    if args is None:
        args = sys.argv[1:]
    args = parse_args(args)
    extract_books(Path(args.indir), Path(args.outdir), args.lang,
                  out_format=args.output_format, chunk_size=args.chunk_size,
                  multilang=args.allow_multi)


if __name__ == "__main__":
    main()
