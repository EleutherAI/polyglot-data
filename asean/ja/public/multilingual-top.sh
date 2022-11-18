#/bin/bash

# Data Name: multilingual-top
# Data Size: ?

## 1.1. download data (by wget)
git clone https://github.com/awslabs/multilingual-top tmp_multilingual-top

mv tmp_multilingual-top/processed_data/ja multilingual-top
cd multilingual-top

find . -type f -name "*.mrl" -exec rm {} \;