# Data Name: Oscar_Indo_May_2022, KoPI-CC, KoPI-CC_News
# Data Size: 21GB, 122GB, 13GB

# Requirements
## 1. install git-lfs (https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage)
## 1.0 To install git-lfs in stabilityai server, follow bellow step!!
## 1.1. Download https://github.com/git-lfs/git-lfs/releases/download/v3.2.0/git-lfs-linux-amd64-v3.2.0.tar.gz then extract
## 1.2. Change the prefix in install.sh to my own home directory (e.g. prefix="/fsx/home-xxxx")
## 1.3. Run install.sh

## 2. install zstd


## 1. munggok/Oscar_Indo_May_2022 

## 1.0. clone github repository
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/datasets/munggok/Oscar_Indo_May_2022
### If OS is Window, use command bellow not the above.
:<<END
set GIT_LFS_SKIP_SMUDGE=1
git clone https://huggingface.co/datasets/munggok/Oscar_Indo_May_2022
END

## 1.1. change directory
cd ./Oscar_Indo_May_2022

## 1.2. download data (by git-lfs)
git lfs pull --include "meta/id_meta_*.jsonl"

# 2. munggok/KoPI-CC

## 2.0. clone github repository
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/datasets/munggok/KoPI-CC
### If OS is Window, use command bellow not the above.
:<<END
set GIT_LFS_SKIP_SMUDGE=1
git clone https://huggingface.co/datasets/munggok/KoPI-CC
END

## 2.1. change directory
cd ./KoPI-CC

## 2.2. download data (by git-lfs)
git lfs pull --include "2020-40/id_meta_*.jsonl.zst"
git lfs pull --include "2020-45/id_meta_*.jsonl.zst"
git lfs pull --include "2020-50/id_meta_*.jsonl.zst"
git lfs pull --include "2021-04/id_meta_*.jsonl.zst"
#git lfs pull --include "2021_10/dedup/oscar-*.json.gz"
git lfs pull --include "2021_17/dedup/oscar-*.json.gz"
git lfs pull --include "2021_21/dedup/oscar-*.json.gz"
git lfs pull --include "2021_25/dedup/oscar-*.json.gz"
git lfs pull --include "2021_31/dedup/oscar-*.json.gz"
git lfs pull --include "2021_39/dedup/oscar-*.json.gz"
git lfs pull --include "2021_43/dedup/oscar-*.json.gz"
#git lfs pull --include "2021_49/dedup/oscar-*.json.gz"
git lfs pull --include "2022-33/raw/id_meta_*.jsonl.zst"
git lfs pull --include "2022_05/dedup/oscar-*.json.gz"
git lfs pull --include "2022_21/dedup/oscar-*.json.gz"
git lfs pull --include "2022_27/dedup/oscar-*.json.gz"

## 2.3. extract data
zstd -d 2020-40/id_meta_*.jsonl.zst
zstd -d 2020-45/id_meta_*.jsonl.zst
zstd -d 2020-50/id_meta_*.jsonl.zst
zstd -d 2021-04/id_meta_*.jsonl.zst
#gzip -d 2021_10/dedup/oscar-*.json.gz
gzip -d 2021_17/dedup/oscar-*.json.gz
gzip -d 2021_21/dedup/oscar-*.json.gz
gzip -d 2021_25/dedup/oscar-*.json.gz
gzip -d 2021_31/dedup/oscar-*.json.gz
gzip -d 2021_39/dedup/oscar-*.json.gz
gzip -d 2021_43/dedup/oscar-*.json.gz
#gzip -d 2021_49/dedup/oscar-*.json.gz
zstd -d 2022-33/raw/id_meta_*.jsonl.zst
gzip -d 2022_05/dedup/oscar-*.json.gz
gzip -d 2022_21/dedup/oscar-*.json.gz
gzip -d 2022_27/dedup/oscar-*.json.gz

## 3.4. remove .zst files
rm -rf 2020-40/id_meta_*.jsonl.zst
rm -rf 2020-45/id_meta_*.jsonl.zst
rm -rf 2020-50/id_meta_*.jsonl.zst
rm -rf 2020-04/id_meta_*.jsonl.zst
rm -rf 2022-33/raw/id_meta_*.jsonl.zst


# 3. munggok/KoPI-CC_News

## 3.0. clone github repository
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/datasets/munggok/KoPI-CC_News
### If OS is Window, use command bellow not the above.
:<<END
set GIT_LFS_SKIP_SMUDGE=1
git clone https://huggingface.co/datasets/munggok/KoPI-CC_News
END

## 3.1. change directory
cd ./KoPI-CC_News

## 3.2. download data (by git-lfs)
git lfs pull --include "data/cc_news_*_id.jsonl.zst"

## 3.3. extract data
zstd -d data/cc_news_*_id.jsonl.zst

## 3.4. remove .zst files
rm -rf data/cc_news_*_id.jsonl.zst