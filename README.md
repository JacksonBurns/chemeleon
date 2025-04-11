Possible models to run as a comparison:
 - `MolE`
 - `IBM/molformer`

Other TODOs:
 - for finetuning, consider a two-stage strategy in which we first continue to train the masked reconstruction objective to ensure that the model is well-adapated for the chemical space of each problem and only _then_ attach a new task head for the actual regression target

Deps (formalize into reqs):
 - for not below but needed, version are flexible
 - chemprop 2.1+
 - zarr 3 for training < 3 for finetuning
 - polaris 0.11.6+ 
