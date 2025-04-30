cd ../models/rf_fingerprint
mkdir -p output
BENCHMARK_SET=moleculeace python evaluate.py output/moleculeace
BENCHMARK_SET=polaris python evaluate.py output/polaris

cd ../chemprop_mpnn
mkdir -p output
BENCHMARK_SET=moleculeace python evaluate.py output/direct_moleculeace
BENCHMARK_SET=polaris python evaluate.py output/direct_polaris
BENCHMARK_SET=moleculeace python evaluate.py output/pretrained_moleculeace chemprop_pretrain_baseline.pt
BENCHMARK_SET=polaris python evaluate.py output/pretrained_polaris chemprop_pretrain_baseline.pt

cd ../descriptor_mlp
mkdir -p output
BENCHMARK_SET=moleculeace python evaluate.py output/direct_moleculeace
BENCHMARK_SET=polaris python evaluate.py output/direct_polaris
BENCHMARK_SET=moleculeace python evaluate.py output/pretrained_1MM_moleculeace e16_n2_h4096_best.pt
BENCHMARK_SET=polaris python evaluate.py output/pretrained_1MM_polaris e16_n2_h4096_best.pt
BENCHMARK_SET=moleculeace python evaluate.py output/pretrained_10MM_moleculeace 10MM_best.pt
BENCHMARK_SET=polaris python evaluate.py output/pretrained_10MM_polaris 10MM_best.pt

cd ../molformer_transformer
mkdir -p output
BENCHMARK_SET=moleculeace python evaluate.py output/moleculeace
BENCHMARK_SET=polaris python evaluate.py output/polaris

# cd ../pca_mlp
# python evaluate.py output/direct_all --gpu --pca-method on-the-fly --explained-variance 0.95
# python evaluate.py output/pretrained_all --gpu --pca-method pretrained --pca-model-path /home/jwburns/fastprop_foundation/models/pca_mlp/output/foundation_pca.pt
