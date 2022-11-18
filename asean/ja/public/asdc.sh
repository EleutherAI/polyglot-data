#/bin/bash

# Data Name: Accommodation Search Dialog Corpus(ASDC)
# Data Size: ??KB

## 1.1. download data (by git clone)
git clone https://github.com/megagonlabs/asdc tmp_asdc
cd ./tmp_asdc
mc data ../asdc
cd ..
rm -rf tmp_asdc