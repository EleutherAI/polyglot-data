# Data Name: CC-100-id
# Data Size: 149GB
# Description: Jan/Dec 2018 Common Crawl 

# 0. URL
export cc_100_id="https://data.statmt.org/cc-100/id.txt.xz"

# 1. download dataset (by wget)
wget -O cc_100_id.tar.xz ${cc_100_id}

# 2. extract dataset
tar -xvf cc_100_id.tar.xz