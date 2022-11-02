git lfs install
GIT_LFS_SKIP_SMUDGE=1
git clone https://huggingface.co/datasets/oscar-corpus/OSCAR-2201
cd c4
git lfs pull --include "multilingual/c4-vi.*.json.gz"
