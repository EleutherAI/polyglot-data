# Data Name: indo4B
# Data Size: 23GB

# 0. URL
export indo4b="https://storage.googleapis.com/babert-pretraining/IndoNLU_finals/dataset/preprocessed/dataset_wot_uncased_blanklines.tar.xz"

# 1. download dataset (by wget)
wget -O cc_100_id.tar.xz ${indo4b}

# 2. extract dataset & change directory name
tar -xvf cc_100_id.tar.xz
mv processed_uncased_blanklines indo4b