# chemeleon2_preview_initial_training_e4s281344 Baseline Results
timestamp: 2026-06-08 12:39:25.029548
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.647907 |
|  1 | test       | CLS_RET        | mcc         | 0.562567 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.537669 |
|  3 | test       | CLS_RET        | roc_auc     | 0.867151 |
|  4 | test       | CLS_RET        | accuracy    | 0.896226 |
|  5 | test       | CLS_RET        | f1          | 0.592593 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.546121 |
|  1 | test       | RET            | explained_var       |   0.298038 |
|  2 | test       | RET            | r2                  |   0.271481 |
|  3 | test       | RET            | spearmanr           |   0.560545 |
|  4 | test       | RET            | mean_squared_error  | 865.048    |
|  5 | test       | RET            | mean_absolute_error |  22.3148   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.698354 |
|  1 | test       | CLS_KIT        | mcc         | 0.60735  |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.60735  |
|  3 | test       | CLS_KIT        | roc_auc     | 0.842843 |
|  4 | test       | CLS_KIT        | accuracy    | 0.87931  |
|  5 | test       | CLS_KIT        | f1          | 0.681818 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.601647 |
|  1 | test       | KIT            | explained_var       |   0.357997 |
|  2 | test       | KIT            | r2                  |   0.356311 |
|  3 | test       | KIT            | spearmanr           |   0.539704 |
|  4 | test       | KIT            | mean_squared_error  | 776.729    |
|  5 | test       | KIT            | mean_absolute_error |  22.1579   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.69394  |
|  1 | test       | EGFR           | explained_var       |   0.480619 |
|  2 | test       | EGFR           | r2                  |   0.469549 |
|  3 | test       | EGFR           | spearmanr           |   0.420341 |
|  4 | test       | EGFR           | mean_squared_error  | 427.421    |
|  5 | test       | EGFR           | mean_absolute_error |  16.494    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.663105 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.439696 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.427895 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.581422 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.310183 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.376354 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.487716 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.232676 |
|  2 | test       | LOG_RPPB       | r2                  | 0.222462 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.610435 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.690828 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.563051 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.666752 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.291619 |
|  2 | test       | LOG_HPPB       | r2                  | 0.286006 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.688823 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.432423 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.575335 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.810172 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.654988 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.652543 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.798912 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.172127 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.314128 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.733622 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.536763 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.53374  |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.736996 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.263224 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.400674 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.704314 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.482094 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.475052 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.702772 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.203895 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.346704 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.433805 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.46551 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.449206 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.673266 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.229169 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.39411 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.58762 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  |    0.94 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.635517 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.355178 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.676198 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.931152 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.365262 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.85729 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.897514 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.848558 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.55463 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6479065494414368,
    "polaris/pkis2-ret-wt-reg-v2": 865.047667195195,
    "polaris/pkis2-kit-wt-cls-v2": 0.6983544081212654,
    "polaris/pkis2-kit-wt-reg-v2": 776.7287512768553,
    "polaris/pkis2-egfr-wt-reg-v2": 427.42055699017624,
    "polaris/adme-fang-solu-1": 0.6631049068425865,
    "polaris/adme-fang-rppb-1": 0.4877159953533712,
    "polaris/adme-fang-hppb-1": 0.6667521420731904,
    "polaris/adme-fang-perm-1": 0.8101720477764272,
    "polaris/adme-fang-rclint-1": 0.7336223777471317,
    "polaris/adme-fang-hclint-1": 0.7043144230423272,
    "tdcommons/lipophilicity-astrazeneca": 0.4338047958612442,
    "tdcommons/ppbr-az": 8.46550628825889,
    "tdcommons/clearance-hepatocyte-az": 0.4492059676027582,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6732663188705693,
    "tdcommons/half-life-obach": 0.229169208796658,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.39410955098129946,
    "tdcommons/clearance-microsome-az": 0.5876198951512376,
    "tdcommons/dili": 0.9400000000000001,
    "tdcommons/bioavailability-ma": 0.6355171267043564,
    "tdcommons/vdss-lombardo": 0.3551782606279272,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6761980108499096,
    "tdcommons/pgp-broccatelli": 0.9311516928818981,
    "tdcommons/caco2-wang": 0.3652620557350914,
    "tdcommons/herg": 0.8572901325478646,
    "tdcommons/bbb-martins": 0.8975140712945592,
    "tdcommons/ames": 0.8485578335193562,
    "tdcommons/ld50-zhu": 0.5546301874662768
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.777945 |
|  1 | test       | CLS_RET        | mcc         | 0.655239 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.642161 |
|  3 | test       | CLS_RET        | roc_auc     | 0.881031 |
|  4 | test       | CLS_RET        | accuracy    | 0.915094 |
|  5 | test       | CLS_RET        | f1          | 0.689655 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.636484 |
|  1 | test       | RET            | explained_var       |   0.389803 |
|  2 | test       | RET            | r2                  |   0.298207 |
|  3 | test       | RET            | spearmanr           |   0.626367 |
|  4 | test       | RET            | mean_squared_error  | 833.313    |
|  5 | test       | RET            | mean_absolute_error |  21.2512   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.703101 |
|  1 | test       | CLS_KIT        | mcc         | 0.551257 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.551257 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.831238 |
|  4 | test       | CLS_KIT        | accuracy    | 0.862069 |
|  5 | test       | CLS_KIT        | f1          | 0.636364 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.587925 |
|  1 | test       | KIT            | explained_var       |   0.306438 |
|  2 | test       | KIT            | r2                  |   0.304278 |
|  3 | test       | KIT            | spearmanr           |   0.532043 |
|  4 | test       | KIT            | mean_squared_error  | 839.517    |
|  5 | test       | KIT            | mean_absolute_error |  21.9108   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.662162 |
|  1 | test       | EGFR           | explained_var       |   0.422242 |
|  2 | test       | EGFR           | r2                  |   0.421237 |
|  3 | test       | EGFR           | spearmanr           |   0.343695 |
|  4 | test       | EGFR           | mean_squared_error  | 466.349    |
|  5 | test       | EGFR           | mean_absolute_error |  16.951    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.666476 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.440542 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.437883 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.559567 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.304768 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.381953 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.800457 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.583446 |
|  2 | test       | LOG_RPPB       | r2                  | 0.564372 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.82     |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.387048 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.473437 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.798272 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.61953  |
|  2 | test       | LOG_HPPB       | r2                  | 0.61303  |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.796088 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.234364 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.400699 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.813352 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.65693  |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.656064 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.799859 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.170384 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.310678 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.752401 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.566071 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.557151 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.753734 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.250008 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.39376  |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.691613 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.471656 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.457351 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.686141 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.21077  |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.36002  |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  0.4362 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.00601 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.423651 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.678013 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.229099 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.38604 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.656054 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.925652 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.446625 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.413366 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.639354 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.913223 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.356857 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.853756 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.877658 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.854614 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.576139 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7779445052652872,
    "polaris/pkis2-ret-wt-reg-v2": 833.312868156522,
    "polaris/pkis2-kit-wt-cls-v2": 0.7031008769048372,
    "polaris/pkis2-kit-wt-reg-v2": 839.5171132769126,
    "polaris/pkis2-egfr-wt-reg-v2": 466.34868303466305,
    "polaris/adme-fang-solu-1": 0.6664761549252473,
    "polaris/adme-fang-rppb-1": 0.8004565083694395,
    "polaris/adme-fang-hppb-1": 0.7982721063201819,
    "polaris/adme-fang-perm-1": 0.8133515533717963,
    "polaris/adme-fang-rclint-1": 0.7524009598540498,
    "polaris/adme-fang-hclint-1": 0.6916131038631373,
    "tdcommons/lipophilicity-astrazeneca": 0.43620023312455136,
    "tdcommons/ppbr-az": 8.00600844163161,
    "tdcommons/clearance-hepatocyte-az": 0.42365063091203004,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6780133765961955,
    "tdcommons/half-life-obach": 0.22909875541542407,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.38603997277902563,
    "tdcommons/clearance-microsome-az": 0.6560544927266565,
    "tdcommons/dili": 0.9256521739130434,
    "tdcommons/bioavailability-ma": 0.4466245427336215,
    "tdcommons/vdss-lombardo": 0.4133657765019632,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6393535262206149,
    "tdcommons/pgp-broccatelli": 0.9132231404958677,
    "tdcommons/caco2-wang": 0.356857454191975,
    "tdcommons/herg": 0.8537555228276877,
    "tdcommons/bbb-martins": 0.8776579111944965,
    "tdcommons/ames": 0.8546143452975385,
    "tdcommons/ld50-zhu": 0.5761394123327748
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.669457 |
|  1 | test       | CLS_RET        | mcc         | 0.560157 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.55864  |
|  3 | test       | CLS_RET        | roc_auc     | 0.868473 |
|  4 | test       | CLS_RET        | accuracy    | 0.886792 |
|  5 | test       | CLS_RET        | f1          | 0.625    |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.577391 |
|  1 | test       | RET            | explained_var       |   0.324365 |
|  2 | test       | RET            | r2                  |   0.318643 |
|  3 | test       | RET            | spearmanr           |   0.597283 |
|  4 | test       | RET            | mean_squared_error  | 809.047    |
|  5 | test       | RET            | mean_absolute_error |  23.6138   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.689009 |
|  1 | test       | CLS_KIT        | mcc         | 0.60735  |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.60735  |
|  3 | test       | CLS_KIT        | roc_auc     | 0.841393 |
|  4 | test       | CLS_KIT        | accuracy    | 0.87931  |
|  5 | test       | CLS_KIT        | f1          | 0.681818 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.585507 |
|  1 | test       | KIT            | explained_var       |   0.331691 |
|  2 | test       | KIT            | r2                  |   0.331587 |
|  3 | test       | KIT            | spearmanr           |   0.52728  |
|  4 | test       | KIT            | mean_squared_error  | 806.563    |
|  5 | test       | KIT            | mean_absolute_error |  22.3828   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.702884 |
|  1 | test       | EGFR           | explained_var       |   0.480937 |
|  2 | test       | EGFR           | r2                  |   0.470059 |
|  3 | test       | EGFR           | spearmanr           |   0.470051 |
|  4 | test       | EGFR           | mean_squared_error  | 427.01     |
|  5 | test       | EGFR           | mean_absolute_error |  16.3584   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.648319 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.419605 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.406742 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.534799 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.321652 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.396151 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.762853 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.540162 |
|  2 | test       | LOG_RPPB       | r2                  | 0.539055 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.766087 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.409542 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.439889 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.803831 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.646109 |
|  2 | test       | LOG_HPPB       | r2                  | 0.579558 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.785851 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.254636 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.429419 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.803184 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.644078 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.641284 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.800752 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.177705 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.307573 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.738573 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.545459 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.536724 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.735034 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.26154  |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.402724 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.702363 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.461772 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.461713 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.701768 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.209076 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.355504 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.443734 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.31866 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.363409 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.708329 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.170822 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.429815 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.641733 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.91913 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.553043 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.415417 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.664444 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.926886 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.409873 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.839617 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.897006 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.845801 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.56446 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6694572275043594,
    "polaris/pkis2-ret-wt-reg-v2": 809.0470694427078,
    "polaris/pkis2-kit-wt-cls-v2": 0.6890089697524413,
    "polaris/pkis2-kit-wt-reg-v2": 806.5629599132101,
    "polaris/pkis2-egfr-wt-reg-v2": 427.01012648314827,
    "polaris/adme-fang-solu-1": 0.6483194717632208,
    "polaris/adme-fang-rppb-1": 0.7628534925911888,
    "polaris/adme-fang-hppb-1": 0.80383079881638,
    "polaris/adme-fang-perm-1": 0.8031843081923952,
    "polaris/adme-fang-rclint-1": 0.7385725153317731,
    "polaris/adme-fang-hclint-1": 0.7023633763521697,
    "tdcommons/lipophilicity-astrazeneca": 0.4437341366098041,
    "tdcommons/ppbr-az": 8.318657902152893,
    "tdcommons/clearance-hepatocyte-az": 0.3634087229550876,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7083292017611396,
    "tdcommons/half-life-obach": 0.1708220131046078,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4298153772526836,
    "tdcommons/clearance-microsome-az": 0.6417328495353957,
    "tdcommons/dili": 0.9191304347826087,
    "tdcommons/bioavailability-ma": 0.5530428999002328,
    "tdcommons/vdss-lombardo": 0.41541661922447454,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6644439421338155,
    "tdcommons/pgp-broccatelli": 0.9268861636896828,
    "tdcommons/caco2-wang": 0.4098734147814404,
    "tdcommons/herg": 0.8396170839469809,
    "tdcommons/bbb-martins": 0.8970059412132583,
    "tdcommons/ames": 0.8458007793377588,
    "tdcommons/ld50-zhu": 0.5644601028562398
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.748017 |
|  1 | test       | CLS_RET        | mcc         | 0.664769 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.660498 |
|  3 | test       | CLS_RET        | roc_auc     | 0.895572 |
|  4 | test       | CLS_RET        | accuracy    | 0.915094 |
|  5 | test       | CLS_RET        | f1          | 0.709677 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.695756 |
|  1 | test       | RET            | explained_var       |   0.480001 |
|  2 | test       | RET            | r2                  |   0.476934 |
|  3 | test       | RET            | spearmanr           |   0.615447 |
|  4 | test       | RET            | mean_squared_error  | 621.092    |
|  5 | test       | RET            | mean_absolute_error |  20.0826   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.728273 |
|  1 | test       | CLS_KIT        | mcc         | 0.556543 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.503667 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.839458 |
|  4 | test       | CLS_KIT        | accuracy    | 0.87931  |
|  5 | test       | CLS_KIT        | f1          | 0.5625   |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.60189  |
|  1 | test       | KIT            | explained_var       |   0.352671 |
|  2 | test       | KIT            | r2                  |   0.301295 |
|  3 | test       | KIT            | spearmanr           |   0.553887 |
|  4 | test       | KIT            | mean_squared_error  | 843.117    |
|  5 | test       | KIT            | mean_absolute_error |  21.6095   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.679698 |
|  1 | test       | EGFR           | explained_var       |   0.455478 |
|  2 | test       | EGFR           | r2                  |   0.453566 |
|  3 | test       | EGFR           | spearmanr           |   0.352933 |
|  4 | test       | EGFR           | mean_squared_error  | 440.299    |
|  5 | test       | EGFR           | mean_absolute_error |  16.5443   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.647242 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.41891  |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.417785 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.533368 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.315664 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.399138 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.667204 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.30132  |
|  2 | test       | LOG_RPPB       | r2                  | 0.244173 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.758261 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.671539 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.681566 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.799531 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.631135 |
|  2 | test       | LOG_HPPB       | r2                  | 0.523822 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.774085 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.288392 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.453131 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.792529 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.625399 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.610809 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.781583 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.192802 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.342895 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.750328 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.55885  |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.550084 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.751071 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.253997 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.401318 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.703154 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.477407 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.474378 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.695917 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.204157 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.351261 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.450767 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.03724 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.445743 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.505379 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.215006 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.433503 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.670602 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.911739 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.642833 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.386094 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.635059 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.917889 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.391983 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.856848 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.905234 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.842689 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.555559 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7480174376123322,
    "polaris/pkis2-ret-wt-reg-v2": 621.0916601307016,
    "polaris/pkis2-kit-wt-cls-v2": 0.7282725933194869,
    "polaris/pkis2-kit-wt-reg-v2": 843.1165672408586,
    "polaris/pkis2-egfr-wt-reg-v2": 440.29908041546815,
    "polaris/adme-fang-solu-1": 0.6472415095003305,
    "polaris/adme-fang-rppb-1": 0.6672043286939336,
    "polaris/adme-fang-hppb-1": 0.799531343188376,
    "polaris/adme-fang-perm-1": 0.7925293224459687,
    "polaris/adme-fang-rclint-1": 0.7503282600557972,
    "polaris/adme-fang-hclint-1": 0.7031539392691283,
    "tdcommons/lipophilicity-astrazeneca": 0.45076669586840135,
    "tdcommons/ppbr-az": 8.037242785131355,
    "tdcommons/clearance-hepatocyte-az": 0.44574284390920155,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5053789926523528,
    "tdcommons/half-life-obach": 0.21500558680084933,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.43350298279146227,
    "tdcommons/clearance-microsome-az": 0.6706018786268004,
    "tdcommons/dili": 0.9117391304347826,
    "tdcommons/bioavailability-ma": 0.642833388759561,
    "tdcommons/vdss-lombardo": 0.3860942587863743,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6350587703435805,
    "tdcommons/pgp-broccatelli": 0.9178885630498533,
    "tdcommons/caco2-wang": 0.391983210612035,
    "tdcommons/herg": 0.8568483063328425,
    "tdcommons/bbb-martins": 0.9052337398373985,
    "tdcommons/ames": 0.8426893027081007,
    "tdcommons/ld50-zhu": 0.5555589614675881
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.652327 |
|  1 | test       | CLS_RET        | mcc         | 0.5741   |
|  2 | test       | CLS_RET        | cohen_kappa | 0.562641 |
|  3 | test       | CLS_RET        | roc_auc     | 0.849967 |
|  4 | test       | CLS_RET        | accuracy    | 0.896226 |
|  5 | test       | CLS_RET        | f1          | 0.62069  |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.601785 |
|  1 | test       | RET            | explained_var       |   0.361651 |
|  2 | test       | RET            | r2                  |   0.305755 |
|  3 | test       | RET            | spearmanr           |   0.587533 |
|  4 | test       | RET            | mean_squared_error  | 824.351    |
|  5 | test       | RET            | mean_absolute_error |  21.2067   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.745613 |
|  1 | test       | CLS_KIT        | mcc         | 0.670028 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.662076 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.859284 |
|  4 | test       | CLS_KIT        | accuracy    | 0.905172 |
|  5 | test       | CLS_KIT        | f1          | 0.717949 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.569111 |
|  1 | test       | KIT            | explained_var       |   0.303968 |
|  2 | test       | KIT            | r2                  |   0.295857 |
|  3 | test       | KIT            | spearmanr           |   0.506952 |
|  4 | test       | KIT            | mean_squared_error  | 849.678    |
|  5 | test       | KIT            | mean_absolute_error |  21.9604   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.678296 |
|  1 | test       | EGFR           | explained_var       |   0.453682 |
|  2 | test       | EGFR           | r2                  |   0.453466 |
|  3 | test       | EGFR           | spearmanr           |   0.423516 |
|  4 | test       | EGFR           | mean_squared_error  | 440.38     |
|  5 | test       | EGFR           | mean_absolute_error |  16.6628   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.674621 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.454746 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.436156 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.542996 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.305704 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.385093 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.806548 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.570058 |
|  2 | test       | LOG_RPPB       | r2                  | 0.551623 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.821739 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.398375 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.493126 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.73347  |
|  1 | test       | LOG_HPPB       | explained_var       | 0.528723 |
|  2 | test       | LOG_HPPB       | r2                  | 0.226017 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.739094 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.468754 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.560324 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.803557 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.643496 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.64247  |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.790998 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.177118 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.310082 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.746128 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.554397 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.553877 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.747079 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.251856 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.397108 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.701559 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.47371  |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.473045 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.700967 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.204675 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.350087 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.431722 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.53173 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.433521 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.666189 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.133636 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.407462 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.610051 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.928261 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.57865 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.337093 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.650882 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.919088 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.439246 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.845214 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.908712 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.83638 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.559766 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6523266317870349,
    "polaris/pkis2-ret-wt-reg-v2": 824.3506176526663,
    "polaris/pkis2-kit-wt-cls-v2": 0.7456126670824446,
    "polaris/pkis2-kit-wt-reg-v2": 849.6780158679617,
    "polaris/pkis2-egfr-wt-reg-v2": 440.3801239141981,
    "polaris/adme-fang-solu-1": 0.6746210821894809,
    "polaris/adme-fang-rppb-1": 0.8065480532802662,
    "polaris/adme-fang-hppb-1": 0.7334704188449144,
    "polaris/adme-fang-perm-1": 0.8035571819237354,
    "polaris/adme-fang-rclint-1": 0.7461278318302421,
    "polaris/adme-fang-hclint-1": 0.7015594282730899,
    "tdcommons/lipophilicity-astrazeneca": 0.43172234242870694,
    "tdcommons/ppbr-az": 8.531728503341538,
    "tdcommons/clearance-hepatocyte-az": 0.4335210411552174,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.666189347220684,
    "tdcommons/half-life-obach": 0.1336364287439601,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.40746245059364455,
    "tdcommons/clearance-microsome-az": 0.6100508835840582,
    "tdcommons/dili": 0.9282608695652174,
    "tdcommons/bioavailability-ma": 0.5786498170934485,
    "tdcommons/vdss-lombardo": 0.33709283761694464,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.650881555153707,
    "tdcommons/pgp-broccatelli": 0.9190882431351639,
    "tdcommons/caco2-wang": 0.43924577316535707,
    "tdcommons/herg": 0.8452135493372607,
    "tdcommons/bbb-martins": 0.9087124765478425,
    "tdcommons/ames": 0.8363801915056102,
    "tdcommons/ld50-zhu": 0.5597658904563428
}
```
