import argparse
import requests
from bs4 import BeautifulSoup

# Website URLS
CORPORA_URL = "https://pcai056.informatik.uni-leipzig.de/downloads/corpora"
WORTSCHATZ_URL = "https://wortschatz.uni-leipzig.de/en/download"


def _extract_download_elements_from_url(url: str):
    page = requests.get(url)  # Page content from Website URL
    soup = BeautifulSoup(page.content, "html.parser")  # parse html content
    return soup.find_all("a", class_="link_corpora_download")


def _files_to_download_from_elements(elements, filter_keyword: str) -> list:
    list_of_files = list()
    for i in elements:
        if i.has_attr("data-corpora-file"):
            list_of_files.append(i.attrs["data-corpora-file"])
    return [fn for fn in list_of_files if filter_keyword in fn]


def _download_files(files_to_download: list):
    for file in files_to_download:
        print(f"Downloading file: {file}")
        response = requests.get(f"{CORPORA_URL}/{file}")
        open(file, "wb").write(response.content)


def main(language: str = "Spanish", downloads: str = "1M"):
    language_url = f"https://wortschatz.uni-leipzig.de/en/download/{language}"
    print(f"Exploring and downloading files from: {language_url}")

    download_elements = _extract_download_elements_from_url(language_url)
    files_to_download = _files_to_download_from_elements(
        download_elements, filter_keyword=downloads
    )
    print(f"Found {len(files_to_download)} files")
    _download_files(files_to_download)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=f"Downloads sentences from https://wortschatz.uni-leipzig.de/en/download in the given language."
    )
    parser.add_argument(
        "--language",
        default="Spanish",
        help="Language to download.",
    )
    parser.add_argument(
        "--downloads",
        default="1M",
        help='Number of sentences to download. Defaults to "1M"',
    )
    args = parser.parse_args()
    main(language=args.language, downloads=args.downloads)
