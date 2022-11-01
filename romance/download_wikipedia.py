#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# If facing an error like "Fatal error condition occurred in aws-c-io",
# see https://github.com/huggingface/datasets/issues/3310#issuecomment-1291628759
# Until a proper fix is in place, the workaround is to install the newest pyarrow
# !pip install --extra-index-url https://pypi.fury.io/arrow-nightlies/ --prefer-binary --pre pyarrow --upgrade
import argparse
from pathlib import Path
from datasets import load_dataset


def main(language_code="es", date="20221020", output="./dump.jsonl"):
    path = Path(output.format(language_code=language_code, date=date))
    path.parent.mkdir(parents=True, exist_ok=True)
    print(f"Downloading Wikipedia dump for {language_code} from {date}")
    ds = load_dataset(
        "olm/wikipedia", language=language_code, date=date, split="train"
    )
    print(f"Writing dump file to {str(path)}")
    ds.to_json(path, lines=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=f"Downlodas text from Wikipedia in the given language."
    )
    parser.add_argument('--language_code', '-l',
        default="es",
        help='Wikipedia language code to download. Defaults to "es".',
    )
    parser.add_argument('--date', '-d',
        default="20221020",
        help='Date of the dump to download. Defaults to "20221020".',
    )
    parser.add_argument('--output', '-o',
        default="./{language_code}/0_raw/wikipedia/dump_{date}.jsonl",
        help='Output file. Defaults to "./{language_code}/0_raw/wikipedia/dump_{date}.jsonl".',
    )
    args = parser.parse_args()
    main(language_code=args.language_code, date=args.date, output=args.output)

