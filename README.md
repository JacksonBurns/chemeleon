Possible models to run as a comparison:
 - `MolE`
 - `IBM/molformer`

Thought process for model comparison:
 - direct prediction on descriptors (fastprop, random forest baseline) - supervised
 - direct training on graph (chemprop) - supervised
 - pretraining on descriptors (this study) - uunsupervised + supervised
 - pretraining on qm descriptors (GraphQPT https://github.com/aidd-msca/GraphQPT)  - uunsupervised + supervised
 - pretraining on multitask (MolE (mini version available here https://codeocean.com/capsule/2105466/tree/v1), Graphium 1B MPNN (https://openreview.net/forum?id=Zc2aIcucwc) and MolGPS (https://arxiv.org/abs/2404.11568)) - uunsupervised + supervised
 - pretraining on smiles (ChemBERTa-2 and MolFormer) - uunsupervised + supervised

Note on code duplication:
 - each directory under `models` contains all of the code needed to run _that_ model.
 Wherever possible, you can copy the individual file and run it without anything else.
 This, of course, leads to some code duplication.

Broadly speaking all of the `evaluate` scripts look like this:
```python

```

Other TODOs:
 - for finetuning, consider a two-stage strategy in which we first continue to train the masked reconstruction objective to ensure that the model is well-adapated for the chemical space of each problem and only _then_ attach a new task head for the actual regression target

Deps (formalize into reqs):
 - for not below but needed, version are flexible
 - chemprop 2.1+
 - zarr 3 for training < 3 for finetuning
 - polaris 0.11.6+ 

Load the chemprop pretrained model which is actually a MaskedDescriptorsMPNN and then dump it straight back to a file as a normal chemprop model so it can be easily loaded.
