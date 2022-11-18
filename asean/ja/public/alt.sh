#/bin/bash

# Data Name: Asian Language Treebank(ALT)
# Data Size: 94MB - 210 dialogues

## 1.1. make directory & change directory
mkdir alt
cd ./alt

## 1.2. download data (by wget)
wget https://www2.nict.go.jp/astrec-att/member/mutiyama/ALT/Japanese-ALT-20210218.zip

wget https://www2.nict.go.jp/astrec-att/member/mutiyama/ALT/ALT-Parallel-Corpus-20191206.zip

## 1.3. extract data
unzip Japanese-ALT-20210218.zip

unzip ALT-Parallel-Corpus-20191206.zip