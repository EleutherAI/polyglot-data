git clone https://github.com/TheophileBlard/french-sentiment-analysis-with-bert.git
mv french-sentiment-analysis-with-bert/allocine_dataset .
rm -rf french-sentiment-analysis-with-bert
cd allocine_dataset
bzip2 -d data.tar.bz2
tar -xvf data.tar
