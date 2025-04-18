cd ../models/chemprop_mpnn
python evaluate.py output/direct
python evaluate.py output/pretrained chemprop_pretrain_baseline.pt
cd ../descriptor_mlp
python evaluate.py output/direct
python evaluate.py output/pretrained descriptor_mlpplr_pretrain_baseline.pt
