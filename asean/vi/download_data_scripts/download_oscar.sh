git lfs install
GIT_LFS_SKIP_SMUDGE=1
git clone https://huggingface.co/datasets/oscar-corpus/OSCAR-2201
cd OSCAR-2201
git lfs pull --include "compressed/vi_meta/*.jsonl.gz"
