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
cd ../pca_mlp
python evaluate.py output/direct_all --gpu --pca-method on-the-fly --explained-variance 0.95
python evaluate.py output/pretrained_all --gpu --pca-method pretrained --pca-model-path /home/jwburns/fastprop_foundation/models/pca_mlp/output/foundation_pca.pt