# Data Name: mc4-id
# Data Size: 256GB
# Description: colossal, cleaned version of Common Crawl's web crawl corpus 

# Requirements
## 1. install git-lfs (https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage)
## 1.0 To install git-lfs in stabilityai server, follow bellow step!!
## 1.1. Download https://github.com/git-lfs/git-lfs/releases/download/v3.2.0/git-lfs-linux-amd64-v3.2.0.tar.gz then extract
## 1.2. Change the prefix in install.sh to my own home directory (e.g. prefix="/fsx/home-xxxx")
## 1.3. Run install.sh

# 0. clone github repository
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/datasets/allenai/c4
# If OS is Window, use command bellow not the above.
:<<END
set GIT_LFS_SKIP_SMUDGE=1
git clone https://huggingface.co/datasets/allenai/c4
END

# 1. make directory & change directory
mkdir mc4-id 
cd c4

# 2. download data (by git-lfs) & move data
git lfs pull --include "multilingual/c4-id.*.json.gz"
mv multilingual/c4-id.*.json.gz ../mc4-id

# 3. extract data
gzip -d ../mc4-id/c4-id.*.json.gz