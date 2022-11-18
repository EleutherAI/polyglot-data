#/bin/bash

# Data Name: Japanese Question Answering Dataset(JaQuAD)
# Data Size: 24.6MB

## 1.1. download data (by git clone)
git clone https://github.com/SkelterLabsInc/JaQuAD tmp_JaQuAD
cd ./tmp_JaQuAD
mv data ../JaQuAD
cd ..
rm -rf tmp_JaQuAD