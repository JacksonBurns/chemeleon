Possible models to run as a comparison:
 - `MolE`
 - `IBM/molformer`

Other TODOs:
 - for finetuning, consider a two-stage strategy in which we first continue to train the masked reconstruction objective to ensure that the model is well-adapated for the chemical space of each problem and only _then_ attach a new task head for the actual regression target
