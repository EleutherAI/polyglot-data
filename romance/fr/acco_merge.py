# $ python acco_merge.py --do_extraction --do transform --show_progress
import os
import tarfile
import argparse
import glob
import json
import docx2txt
from tqdm import tqdm

#ACCO_PATH = '/fsx/polyglot_data/romance/fr/0_raw/acco/'

def extract_from_tar(args):
    for each_tar in tqdm(glob.glob(args.ACCO_PATH+'*.tar.gz'), disable=args.show_progress):
        try:
            with tarfile.open(each_tar, "r:gz") as tar:
                for tarinfo in tar:
                    if not (tarinfo.isreg() and tarinfo.name.endswith('.docx')):
                        continue
                    tarinfo.name = os.path.basename(tarinfo.name)
                    tar.extract(tarinfo, args.ACCO_PATH+args.extract_path)
        except Exception as e:
            print(e)

def docx_to_json(args):
    output_file = []
    for each_doc in tqdm(glob.glob(args.ACCO_PATH+args.extract_path+'/*.docx'), disable=args.show_progress):
        try:
            name = os.path.basename(each_doc)[:-5]  # without file extension
            each_doc = docx2txt.process(args.ACCO_PATH+args.extract_path+'/'+each_doc)
            text = each_doc.replace('\xa0', ' ')
            output_file.append({"name": name, "text": text})
        except Exception as e:
            print(e)

    with open(args.ACCO_PATH+'acco.json', mode="w") as f:
        json.dump(output_file, f)


def main(args):
    if not args.do_extraction:
        extract_from_tar(args)
    if not args.do_transform:
        docx_to_json(args)

    if args.do_extraction and args.do_transform:
        extract_from_tar(args)
        docx_to_json(args)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--ACCO_PATH", default='/fsx/polyglot_data/romance/fr/0_raw/acco/', help='ACCO directory')
    parser.add_argument("--extract_path", default='tmp_dir', help='directory name to extract tar files')
    parser.add_argument("--do_extraction", action='store_false', help='extract from tar file')
    parser.add_argument("--do_transform", action='store_false', help='transform multiple docx files to a json file')
    parser.add_argument("--show_progress", action='store_false', help='show the progress bar')
    args = parser.parse_args()

    main(args)
