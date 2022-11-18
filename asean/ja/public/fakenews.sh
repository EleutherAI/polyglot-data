#/bin/bash

# Data Name: Fake News
# Data Size: 22.01MB

## 1.1. make directory & change directory
mkdir fakenews
cd ./fakenews

## 1.2. download data (by wget)
wget 'https://storage.googleapis.com/kaggle-data-sets/1310358/2182770/compressed/fakenews.csv.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20221114%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221114T035845Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=827a3f9d072acdfa0c394af735074350a88e6fa17764842d3c27b1616d38ac1cea06d57e68ce82f97e9e591273a35d82228cf971c78c21d5f291bd6da9eac0446de8fd2620715a13389fef7472e88744ebe6f147e3efc04af7fbd818a62d309d44043187a58966d4048ebf2d3c89865ec82b868b4ea787bc7f1bc6c7680b92507ebfa890fb06540c3a8cd2b708d210f99966c6f63336384d3ffa398fba6d909a04543aa544442711e7627ed23c2015671fb1619a2bd8fac6bdb29bd6078e50bc00adda330d36a81e3f7795d6dc1244627d20ccace17ea72914890f383eebf1ddcc1e416eeb30dba2b4579e15345999a6410aa7bdaf6eeb4ccddfdc0fdef3a2b6' --output-document=fakenews.csv.zip
unzip fakenews.csv.zip
