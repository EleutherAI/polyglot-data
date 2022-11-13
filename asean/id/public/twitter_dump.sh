# Data Name: Twitter Dump(?)
# Data Size: 11GB

# 0. URL
export twitter1="https://depia.wiki/files/twitter-dump/2011-10.jsonl.gz"
export twitter2="https://depia.wiki/files/twitter-dump/2011-11.jsonl.gz"

# 1. make directory & change directory
mkdir twitter_dump
cd ./twitter_dump

# 2. download dataset (by wget)
wget ${twitter1}
wget ${twitter2}

# 3. extract dataset
gzip -d 2011-10.jsonl.gz
gzip -d 2011-11.jsonl.gz