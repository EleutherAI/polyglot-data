# Import Module
import argparse
import requests
from bs4 import BeautifulSoup

# Website URL
URL_CORPORA = 'https://pcai056.informatik.uni-leipzig.de/downloads/corpora/{}'


def main(language="Spanish", downloads="1M"):
    URL = f"https://wortschatz.uni-leipzig.de/en/download/{language}"
    print("Exploring and downloading files from the page: {}".format(URL))
    print("Files to download will have the name")
    # class list set
    list_of_files = []
    class_list = set()

    # Page content from Website URL
    page = requests.get( URL )

    # parse html content
    soup = BeautifulSoup( page.content , 'html.parser')

    class_list = soup.find_all("a", class_="link_corpora_download")

    for i in class_list:
        if i.has_attr("data-corpora-file"):
            list_of_files.append(i.attrs["data-corpora-file"])

    # We will download only the files with "1M" in the name (the large ones)
    files_to_download = [fn for fn in list_of_files if downloads in fn]

    print("Number of files found {}".format(len(files_to_download)))

    for ftd in files_to_download:
        print("File downloading: {}".format(ftd))
        response = requests.get(URL_CORPORA.format(ftd))
        open(ftd, "wb").write(response.content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=f"Downloads sentences from https://wortschatz.uni-leipzig.de/en/download in the given language."
    )
    parser.add_argument('--language',
        default="Spanish",
        help='Language to download.',
    )
    parser.add_argument('--downloads',
        default="1M",
        help='Number of sentences to download. Defaults to "1M"',
    )
    args = parser.parse_args()
    main(language=args.language, downloads=args.downloads)
