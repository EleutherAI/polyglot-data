#/bin/bash

# Data Name: Shinzo-Abe Twitter
# Data Size: 61KB

## 1.1. make directory & change directory
mkdir twitter
cd ./twitter

## 1.2. download data (by wget)
wget https://storage.googleapis.com/kagglesdsdata/datasets/3384/5666/Shinzo%20Abe%20Tweet%2020171024%20-%20Tweet.csv\?X-Goog-Algorithm\=GOOG4-RSA-SHA256\&X-Goog-Credential\=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20221114%2Fauto%2Fstorage%2Fgoog4_request\&X-Goog-Date\=20221114T032832Z\&X-Goog-Expires\=259200\&X-Goog-SignedHeaders\=host\&X-Goog-Signature\=31545480007463c7dc8b7322751bbb8b587e002626a5c6ce095c24c1e828bc27ab3d4f715bf3cb4e79f4b4945482e862042ed64529c4e6a9b3c40ddb7b77f24603cc0007e8fbb713f3df4845866839d0854a35eb3a9411496af4d2e70712fd42cb3e702351153d6ecf4a3c3b09bfa24c4ccde7f7341d3ec83c7b3151b7177e83da15295baa206e8e0c72bc02b8633909e9ce3f8a85b32ad004056ee78728992127d6b6ff7d069ced7dcc088b02d009177d167091340801cac15113e8c802ec7b3ea9d21ff509ca8ef6775cf7e8e80070782b709320bee2c70004e81043d1cfe252f3e3c3a9d5360fe80e5b0f5601eee51a16c0c9f30735bf78990cf525e57736 --output-document=shinzo-abe.csv