# MLP on PCA-reduced Descriptors (Pretrained PCA) Results
timestamp: 2025-04-24 14:27:24.258836
GPU: True (CUDA_VISIBLE_DEVICES=None)
Using pretrained PCA from /home/jwburns/fastprop_foundation/models/pca_mlp/output/foundation_pca.pt with 142 components

## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.612694 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.215541 |
|  2 | test       | CLS_RET        | f1          | 0.272727 |
|  3 | test       | CLS_RET        | mcc         | 0.266557 |
|  4 | test       | CLS_RET        | roc_auc     | 0.848645 |
|  5 | test       | CLS_RET        | accuracy    | 0.849057 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  22.3125   |
|  1 | test       | RET            | r2                  |   0.264836 |
|  2 | test       | RET            | mean_squared_error  | 872.937    |
|  3 | test       | RET            | spearmanr           |   0.543966 |
|  4 | test       | RET            | explained_var       |   0.279047 |
|  5 | test       | RET            | pearsonr            |   0.528491 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.521754 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.265419 |
|  2 | test       | CLS_KIT        | f1          | 0.378378 |
|  3 | test       | CLS_KIT        | mcc         | 0.272311 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.753385 |
|  5 | test       | CLS_KIT        | accuracy    | 0.801724 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | mean_absolute_error |   26.6264   |
|  1 | test       | KIT            | r2                  |    0.118214 |
|  2 | test       | KIT            | mean_squared_error  | 1064.04     |
|  3 | test       | KIT            | spearmanr           |    0.422002 |
|  4 | test       | KIT            | explained_var       |    0.131517 |
|  5 | test       | KIT            | pearsonr            |    0.429764 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  18.9152   |
|  1 | test       | EGFR           | r2                  |   0.30462  |
|  2 | test       | EGFR           | mean_squared_error  | 560.315    |
|  3 | test       | EGFR           | spearmanr           |   0.31425  |
|  4 | test       | EGFR           | explained_var       |   0.309375 |
|  5 | test       | EGFR           | pearsonr            |   0.556946 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.431593 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.303437 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.377662 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.452496 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.308484 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.55709  |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.567205 |
|  1 | test       | LOG_RPPB       | r2                  | 0.292414 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.628677 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.690435 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.301498 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.570209 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.434977 |
|  1 | test       | LOG_HPPB       | r2                  | 0.552769 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.27086  |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.829093 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.624181 |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.790085 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.365503 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.535525 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.230098 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.73903  |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.536203 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.732376 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.468328 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.374584 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.353074 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.632467 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.375107 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.61617  |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.387458 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.378102 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.241551 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.649284 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.379153 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.628639 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.900108 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.77703 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.301081 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.655613 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.364966 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.376103 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.548281 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.894348 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.685401 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.35874 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.59505 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.914756 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.285538 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.848454 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.900563 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.837483 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.621156 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.612694143431975,
    "polaris/pkis2-ret-wt-reg-v2": 872.9373366617222,
    "polaris/pkis2-kit-wt-cls-v2": 0.5217539148524118,
    "polaris/pkis2-kit-wt-reg-v2": 1064.0366364832278,
    "polaris/pkis2-egfr-wt-reg-v2": 560.3150241148206,
    "polaris/adme-fang-solu-1": 0.5570902973883476,
    "polaris/adme-fang-rppb-1": 0.5702087357249375,
    "polaris/adme-fang-hppb-1": 0.7900846585720698,
    "polaris/adme-fang-perm-1": 0.7323761355010836,
    "polaris/adme-fang-rclint-1": 0.6161699966432539,
    "polaris/adme-fang-hclint-1": 0.6286386128608306,
    "tdcommons/lipophilicity-astrazeneca": 0.9001080727463676,
    "tdcommons/ppbr-az": 8.77703416500194,
    "tdcommons/clearance-hepatocyte-az": 0.3010811381242973,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6556127152747978,
    "tdcommons/half-life-obach": 0.36496643446255184,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3761030793146672,
    "tdcommons/clearance-microsome-az": 0.5482809211914268,
    "tdcommons/dili": 0.8943478260869565,
    "tdcommons/bioavailability-ma": 0.6854007316262055,
    "tdcommons/vdss-lombardo": 0.3587400576727557,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5950497287522605,
    "tdcommons/pgp-broccatelli": 0.9147560650493202,
    "tdcommons/caco2-wang": 0.28553772458097026,
    "tdcommons/herg": 0.8484536082474227,
    "tdcommons/bbb-martins": 0.9005628517823641,
    "tdcommons/ames": 0.8374826215512345,
    "tdcommons/ld50-zhu": 0.6211564368885489
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.650451 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.239234 |
|  2 | test       | CLS_RET        | f1          | 0.285714 |
|  3 | test       | CLS_RET        | mcc         | 0.318193 |
|  4 | test       | CLS_RET        | roc_auc     | 0.848645 |
|  5 | test       | CLS_RET        | accuracy    | 0.858491 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  20.4588   |
|  1 | test       | RET            | r2                  |   0.382667 |
|  2 | test       | RET            | mean_squared_error  | 733.024    |
|  3 | test       | RET            | spearmanr           |   0.616187 |
|  4 | test       | RET            | explained_var       |   0.394169 |
|  5 | test       | RET            | pearsonr            |   0.628264 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.470504 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.235092 |
|  2 | test       | CLS_KIT        | f1          | 0.342857 |
|  3 | test       | CLS_KIT        | mcc         | 0.246387 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.779981 |
|  5 | test       | CLS_KIT        | accuracy    | 0.801724 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | mean_absolute_error |   26.2607   |
|  1 | test       | KIT            | r2                  |    0.142719 |
|  2 | test       | KIT            | mean_squared_error  | 1034.47     |
|  3 | test       | KIT            | spearmanr           |    0.412652 |
|  4 | test       | KIT            | explained_var       |    0.147548 |
|  5 | test       | KIT            | pearsonr            |    0.446223 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  18.5597   |
|  1 | test       | EGFR           | r2                  |   0.332898 |
|  2 | test       | EGFR           | mean_squared_error  | 537.53     |
|  3 | test       | EGFR           | spearmanr           |   0.342585 |
|  4 | test       | EGFR           | explained_var       |   0.333892 |
|  5 | test       | EGFR           | pearsonr            |   0.577968 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.435615 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.299653 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.379713 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.472318 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.300077 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.549063 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.41353  |
|  1 | test       | LOG_RPPB       | r2                  | 0.608859 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.347522 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.867826 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.610629 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.798019 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.567544 |
|  1 | test       | LOG_HPPB       | r2                  | 0.282453 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.434574 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.649553 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.398743 |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.632934 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.372392 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.52804  |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.233805 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.736192 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.528375 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.727071 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.446914 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.421827 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.326404 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.652304 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.42335  |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.652139 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.384074 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.392713 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.235876 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.647091 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.393154 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.62878  |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.578233 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.56442 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr |   0.331 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.690586 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.278899 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.368669 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr |  0.4995 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.882174 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.63718 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.441195 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.595954 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.908424 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.322574 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.823417 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.905625 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.839836 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.660835 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6504507572801145,
    "polaris/pkis2-ret-wt-reg-v2": 733.0244797290597,
    "polaris/pkis2-kit-wt-cls-v2": 0.47050397085391743,
    "polaris/pkis2-kit-wt-reg-v2": 1034.4676549167007,
    "polaris/pkis2-egfr-wt-reg-v2": 537.5299383651613,
    "polaris/adme-fang-solu-1": 0.5490626715014512,
    "polaris/adme-fang-rppb-1": 0.7980193709278918,
    "polaris/adme-fang-hppb-1": 0.6329340423565647,
    "polaris/adme-fang-perm-1": 0.7270714177152552,
    "polaris/adme-fang-rclint-1": 0.6521390475269866,
    "polaris/adme-fang-hclint-1": 0.6287795282858388,
    "tdcommons/lipophilicity-astrazeneca": 0.5782329411279586,
    "tdcommons/ppbr-az": 8.564420343170438,
    "tdcommons/clearance-hepatocyte-az": 0.3309999334035689,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6905858272942065,
    "tdcommons/half-life-obach": 0.2788990058928795,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.36866867586448315,
    "tdcommons/clearance-microsome-az": 0.4995002111615056,
    "tdcommons/dili": 0.8821739130434783,
    "tdcommons/bioavailability-ma": 0.6371799135350847,
    "tdcommons/vdss-lombardo": 0.44119496483420223,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5959538878842677,
    "tdcommons/pgp-broccatelli": 0.9084244201546254,
    "tdcommons/caco2-wang": 0.32257398683402944,
    "tdcommons/herg": 0.8234167893961708,
    "tdcommons/bbb-martins": 0.9056246091307067,
    "tdcommons/ames": 0.8398362999079676,
    "tdcommons/ld50-zhu": 0.6608347254889905
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.622655 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.288272 |
|  2 | test       | CLS_RET        | f1          | 0.347826 |
|  3 | test       | CLS_RET        | mcc         | 0.337956 |
|  4 | test       | CLS_RET        | roc_auc     | 0.850628 |
|  5 | test       | CLS_RET        | accuracy    | 0.858491 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  22.6629   |
|  1 | test       | RET            | r2                  |   0.259793 |
|  2 | test       | RET            | mean_squared_error  | 878.925    |
|  3 | test       | RET            | spearmanr           |   0.526495 |
|  4 | test       | RET            | explained_var       |   0.294969 |
|  5 | test       | RET            | pearsonr            |   0.545928 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.457181 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.184143 |
|  2 | test       | CLS_KIT        | f1          | 0.266667 |
|  3 | test       | CLS_KIT        | mcc         | 0.215457 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.739845 |
|  5 | test       | CLS_KIT        | accuracy    | 0.810345 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | mean_absolute_error |   26.2278   |
|  1 | test       | KIT            | r2                  |    0.144139 |
|  2 | test       | KIT            | mean_squared_error  | 1032.75     |
|  3 | test       | KIT            | spearmanr           |    0.39519  |
|  4 | test       | KIT            | explained_var       |    0.146083 |
|  5 | test       | KIT            | pearsonr            |    0.436628 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  17.6736   |
|  1 | test       | EGFR           | r2                  |   0.389398 |
|  2 | test       | EGFR           | mean_squared_error  | 492.004    |
|  3 | test       | EGFR           | spearmanr           |   0.344613 |
|  4 | test       | EGFR           | explained_var       |   0.394193 |
|  5 | test       | EGFR           | pearsonr            |   0.629767 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.449168 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.259621 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.401417 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.424298 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.263277 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.514385 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.455888 |
|  1 | test       | LOG_RPPB       | r2                  | 0.570368 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.38172  |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.877391 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.574998 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.821882 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.532987 |
|  1 | test       | LOG_HPPB       | r2                  | 0.361125 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.386928 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.673543 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.464566 |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.685279 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.375998 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.509992 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.242746 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.729089 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.510119 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.714439 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.456111 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.411755 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.33209  |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.649336 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.41263  |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.643892 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.391461 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.377795 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.241671 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.642483 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.379662 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.617314 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.579463 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.71023 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.323086 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.698925 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0272285 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.253779 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.481831 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.888696 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.562022 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.364011 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.608612 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.918022 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.333797 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.833432 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.899429 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.85461 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.654128 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6226553692410516,
    "polaris/pkis2-ret-wt-reg-v2": 878.924991682554,
    "polaris/pkis2-kit-wt-cls-v2": 0.4571808864978055,
    "polaris/pkis2-kit-wt-reg-v2": 1032.7533431438687,
    "polaris/pkis2-egfr-wt-reg-v2": 492.0040129336329,
    "polaris/adme-fang-solu-1": 0.5143854245070465,
    "polaris/adme-fang-rppb-1": 0.8218821410424483,
    "polaris/adme-fang-hppb-1": 0.6852793034941298,
    "polaris/adme-fang-perm-1": 0.7144392159495945,
    "polaris/adme-fang-rclint-1": 0.6438922215193693,
    "polaris/adme-fang-hclint-1": 0.6173142294567067,
    "tdcommons/lipophilicity-astrazeneca": 0.5794627527168819,
    "tdcommons/ppbr-az": 8.710232453866594,
    "tdcommons/clearance-hepatocyte-az": 0.3230862672914223,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6989251357881213,
    "tdcommons/half-life-obach": 0.027228547024046743,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.25377870712696904,
    "tdcommons/clearance-microsome-az": 0.4818314420164456,
    "tdcommons/dili": 0.888695652173913,
    "tdcommons/bioavailability-ma": 0.5620219487861656,
    "tdcommons/vdss-lombardo": 0.36401126631391234,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.608612115732369,
    "tdcommons/pgp-broccatelli": 0.91802186083711,
    "tdcommons/caco2-wang": 0.33379652492023526,
    "tdcommons/herg": 0.8334315169366715,
    "tdcommons/bbb-martins": 0.8994293308317699,
    "tdcommons/ames": 0.8546104290273941,
    "tdcommons/ld50-zhu": 0.654128475320194
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.217368 |
|  1 | test       | CLS_RET        | cohen_kappa | 0        |
|  2 | test       | CLS_RET        | f1          | 0        |
|  3 | test       | CLS_RET        | mcc         | 0        |
|  4 | test       | CLS_RET        | roc_auc     | 0.589557 |
|  5 | test       | CLS_RET        | accuracy    | 0.839623 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  22.3569   |
|  1 | test       | RET            | r2                  |   0.291715 |
|  2 | test       | RET            | mean_squared_error  | 841.021    |
|  3 | test       | RET            | spearmanr           |   0.540407 |
|  4 | test       | RET            | explained_var       |   0.304873 |
|  5 | test       | RET            | pearsonr            |   0.552324 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.507806 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.329295 |
|  2 | test       | CLS_KIT        | f1          | 0.432432 |
|  3 | test       | CLS_KIT        | mcc         | 0.337847 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.760638 |
|  5 | test       | CLS_KIT        | accuracy    | 0.818966 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  23.9851   |
|  1 | test       | KIT            | r2                  |   0.207188 |
|  2 | test       | KIT            | mean_squared_error  | 956.674    |
|  3 | test       | KIT            | spearmanr           |   0.474696 |
|  4 | test       | KIT            | explained_var       |   0.211228 |
|  5 | test       | KIT            | pearsonr            |   0.499226 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  19.0183   |
|  1 | test       | EGFR           | r2                  |   0.300044 |
|  2 | test       | EGFR           | mean_squared_error  | 564.002    |
|  3 | test       | EGFR           | spearmanr           |   0.292055 |
|  4 | test       | EGFR           | explained_var       |   0.30516  |
|  5 | test       | EGFR           | pearsonr            |   0.552644 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.442928 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.289896 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.385003 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.447846 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.290708 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.539938 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.604008 |
|  1 | test       | LOG_RPPB       | r2                  | 0.286465 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.633963 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.608696 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.286869 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.561205 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.392723 |
|  1 | test       | LOG_HPPB       | r2                  | 0.613741 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.233933 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.852319 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.71217  |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.850642 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.369495 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.519465 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.238054 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.734368 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.519478 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.721048 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.469081 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.336595 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.374521 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.643804 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.336713 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.592204 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.391139 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.372971 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.243544 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.639217 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.373415 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.612624 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.584225 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.69517 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.349976 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.622471 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.259665 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.279276 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.544774 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.859565 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.634852 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.395577 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.614263 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.909224 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.293368 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.841679 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.914947 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.845858 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.657785 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.21736807722212273,
    "polaris/pkis2-ret-wt-reg-v2": 841.0212465805951,
    "polaris/pkis2-kit-wt-cls-v2": 0.5078059219020483,
    "polaris/pkis2-kit-wt-reg-v2": 956.6736436035341,
    "polaris/pkis2-egfr-wt-reg-v2": 564.00210905174,
    "polaris/adme-fang-solu-1": 0.5399375855078592,
    "polaris/adme-fang-rppb-1": 0.5612046895228426,
    "polaris/adme-fang-hppb-1": 0.8506421223574014,
    "polaris/adme-fang-perm-1": 0.7210475354413789,
    "polaris/adme-fang-rclint-1": 0.5922038575341163,
    "polaris/adme-fang-hclint-1": 0.6126238735370644,
    "tdcommons/lipophilicity-astrazeneca": 0.5842248783281871,
    "tdcommons/ppbr-az": 8.6951686227215,
    "tdcommons/clearance-hepatocyte-az": 0.3499764537510789,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6224708996973102,
    "tdcommons/half-life-obach": 0.2596645075875423,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.2792764825452409,
    "tdcommons/clearance-microsome-az": 0.5447739821241152,
    "tdcommons/dili": 0.8595652173913044,
    "tdcommons/bioavailability-ma": 0.6348520119720651,
    "tdcommons/vdss-lombardo": 0.3955766568365628,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6142631103074141,
    "tdcommons/pgp-broccatelli": 0.9092242068781659,
    "tdcommons/caco2-wang": 0.2933679935312796,
    "tdcommons/herg": 0.8416789396170841,
    "tdcommons/bbb-martins": 0.9149468417761101,
    "tdcommons/ames": 0.8458575652548512,
    "tdcommons/ld50-zhu": 0.6577853700369395
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.720371 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.356461 |
|  2 | test       | CLS_RET        | f1          | 0.416667 |
|  3 | test       | CLS_RET        | mcc         | 0.40138  |
|  4 | test       | CLS_RET        | roc_auc     | 0.876404 |
|  5 | test       | CLS_RET        | accuracy    | 0.867925 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  21.9591   |
|  1 | test       | RET            | r2                  |   0.288945 |
|  2 | test       | RET            | mean_squared_error  | 844.31     |
|  3 | test       | RET            | spearmanr           |   0.569652 |
|  4 | test       | RET            | explained_var       |   0.306042 |
|  5 | test       | RET            | pearsonr            |   0.553304 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.474005 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.301606 |
|  2 | test       | CLS_KIT        | f1          | 0.4      |
|  3 | test       | CLS_KIT        | mcc         | 0.316097 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.754352 |
|  5 | test       | CLS_KIT        | accuracy    | 0.818966 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | mean_absolute_error |   26.3695   |
|  1 | test       | KIT            | r2                  |    0.130116 |
|  2 | test       | KIT            | mean_squared_error  | 1049.68     |
|  3 | test       | KIT            | spearmanr           |    0.373855 |
|  4 | test       | KIT            | explained_var       |    0.132041 |
|  5 | test       | KIT            | pearsonr            |    0.408994 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  19.4457   |
|  1 | test       | EGFR           | r2                  |   0.222623 |
|  2 | test       | EGFR           | mean_squared_error  | 626.386    |
|  3 | test       | EGFR           | spearmanr           |   0.271653 |
|  4 | test       | EGFR           | explained_var       |   0.228925 |
|  5 | test       | EGFR           | pearsonr            |   0.481991 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.440951 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.275686 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.392707 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.456824 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.287945 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.537436 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.412148 |
|  1 | test       | LOG_RPPB       | r2                  | 0.659456 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.302568 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.837391 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.661078 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.831117 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.46858  |
|  1 | test       | LOG_HPPB       | r2                  | 0.509284 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.297196 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.757277 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.576118 |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.761694 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.385949 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.493053 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.251138 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.715979 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.493074 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.702255 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.454972 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.411613 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.33217  |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.648577 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.412625 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.643941 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.383468 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.390056 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.236908 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.66244  |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.391769 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.640721 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.89051 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  8.7223 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.309278 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.622956 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.13985 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.375405 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.535389 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.876087 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.581975 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.399713 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.612003 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.923754 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.316471 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.834021 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.909983 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.844177 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.669631 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.720370778374785,
    "polaris/pkis2-ret-wt-reg-v2": 844.3102107411337,
    "polaris/pkis2-kit-wt-cls-v2": 0.4740050596759458,
    "polaris/pkis2-kit-wt-reg-v2": 1049.675278366389,
    "polaris/pkis2-egfr-wt-reg-v2": 626.3861889120407,
    "polaris/adme-fang-solu-1": 0.5374363941020999,
    "polaris/adme-fang-rppb-1": 0.8311165618345706,
    "polaris/adme-fang-hppb-1": 0.7616935555062004,
    "polaris/adme-fang-perm-1": 0.702255172984575,
    "polaris/adme-fang-rclint-1": 0.6439414432312557,
    "polaris/adme-fang-hclint-1": 0.6407207441331051,
    "tdcommons/lipophilicity-astrazeneca": 0.8905096012410663,
    "tdcommons/ppbr-az": 8.722302105516354,
    "tdcommons/clearance-hepatocyte-az": 0.30927841326842126,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6229561401157518,
    "tdcommons/half-life-obach": 0.1398501200332584,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3754054701013212,
    "tdcommons/clearance-microsome-az": 0.535388815528945,
    "tdcommons/dili": 0.8760869565217392,
    "tdcommons/bioavailability-ma": 0.5819753907549052,
    "tdcommons/vdss-lombardo": 0.39971252823193193,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.612002712477396,
    "tdcommons/pgp-broccatelli": 0.9237536656891496,
    "tdcommons/caco2-wang": 0.31647051945210564,
    "tdcommons/herg": 0.834020618556701,
    "tdcommons/bbb-martins": 0.9099828017510945,
    "tdcommons/ames": 0.8441774853629403,
    "tdcommons/ld50-zhu": 0.669630514133283
}
```
