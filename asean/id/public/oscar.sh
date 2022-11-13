# Data Name: OSCAR-2019(id), OSCAR-2109(deduplicated-id), OSCAR-2201(id)
# Data Size: 16.5GB, 22GB, 17GB
# Description: huge multilingual corpus obtained by language classification and filtering of the Common Crawl corpus using the Ungoliant architecture.

# Requirements
## 1. install git-lfs (https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage)
## 1.0 To install git-lfs in stabilityai server, follow bellow step!!
## 1.1. Download https://github.com/git-lfs/git-lfs/releases/download/v3.2.0/git-lfs-linux-amd64-v3.2.0.tar.gz then extract
## 1.2. Change the prefix in install.sh to my own home directory (e.g. prefix="/fsx/home-xxxx")
## 1.3. Run install.sh

## 2. "Sign Up" about OSCAR-2109 & OSCAR-2201 dataset to access


# 1. OSCAR-2019

## 1.1. make directory & change directory
mkdir oscar-2019
cd ./oscar-2019

## 1.2. download data (by wget)
for var in {1..9}
do
     wget https://s3.amazonaws.com/datasets.huggingface.co/oscar/1.0/unshuffled/deduplicated/id/id_part_$var.txt.gz
done

## 1.3. extract data
gzip -d id_part_*.txt.gz


# 2. OSCAR-2109 dataset
### Sign Up in https://huggingface.co/datasets/oscar-corpus/OSCAR-2109 

## 2.0. clone github repository (Ask for Huggingface Username & Password)
GIT_LFS_SKIP_SMUDGE=1 git clone "https://huggingface.co/datasets/oscar-corpus/OSCAR-2109"
### If OS is Window, use command bellow not the above.
:<<END
set GIT_LFS_SKIP_SMUDGE=1
git clone "https://huggingface.co/datasets/oscar-corpus/OSCAR-2109"
END

## 2.1. change directory
cd ./OSCAR-2109

## 2.2. download data (by git-lfs) (Ask for Huggingface Username & Password)
git lfs pull --include "packaged/id/id_meta_part_*.jsonl.gz"
git lfs pull --include "packaged/id/id_part_*.txt.gz"

## 2.3. extract data
gzip -d packaged/id/id_meta_part_*.jsonl.gz
gzip -d packaged/id/id_part_*.txt.gz


# 3. OSCAR-2201 dataset
### Sign Up in https://huggingface.co/datasets/oscar-corpus/OSCAR-2201 

## 3.0. clone github repository (Ask for Huggingface Username & Password)
GIT_LFS_SKIP_SMUDGE=1 git clone "https://huggingface.co/datasets/oscar-corpus/OSCAR-2201"
### If OS is Window, use command bellow not the above.
:<<END
set GIT_LFS_SKIP_SMUDGE=1
git clone "https://huggingface.co/datasets/oscar-corpus/OSCAR-2201"
END

## 3.1. change directory
cd ./OSCAR-2201

## 3.2. download data (by git-lfs) (Ask for Huggingface Username & Password)
git lfs pull --include "compressed/id_meta/id_meta_part_*.jsonl.gz"

## 3.3. extract data
gzip -d compressed/id_meta/id_meta_part_*.jsonl.gz
