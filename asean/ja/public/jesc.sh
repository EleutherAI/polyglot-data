#/bin/bash

# Data Name: Japanese-English Subtitle Corpus(JESC)
# Data Size: ?

## 1.1. make directory & change directory
mkdir JESC
cd JESC

## 1.2. download data (by wget)
wget https://nlp.stanford.edu/projects/jesc/data/raw.tar.gz --output-document=JESC.tar.gz

## 1.3. extract data
tar -zxvf JESC.tar.gz

mv ./raw/raw JESC.txt