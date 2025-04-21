cd ../models/chemprop_mpnn
python evaluate.py output/direct_all
python evaluate.py output/pretrained_all chemprop_pretrain_baseline.pt
cd ../descriptor_mlp
python evaluate.py output/direct_all
python evaluate.py output/pretrained_all e16_n2_h4096_best.pt
cd ../rf_fingerprint
python evaluate.py output/all
cd ../molformer_transformer
python evaluate.py output/all
