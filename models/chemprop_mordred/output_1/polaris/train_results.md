# ChemProp Baseline Results
timestamp: 2025-06-06 22:34:51.383007
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.630315 |
|  1 | test       | CLS_RET        | f1          | 0.6      |
|  2 | test       | CLS_RET        | accuracy    | 0.886792 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.535427 |
|  4 | test       | CLS_RET        | mcc         | 0.541965 |
|  5 | test       | CLS_RET        | roc_auc     | 0.832783 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 925.795    |
|  1 | test       | RET            | pearsonr            |   0.531272 |
|  2 | test       | RET            | spearmanr           |   0.509617 |
|  3 | test       | RET            | r2                  |   0.220321 |
|  4 | test       | RET            | mean_absolute_error |  23.9127   |
|  5 | test       | RET            | explained_var       |   0.221971 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.465715 |
|  1 | test       | CLS_KIT        | f1          | 0.4      |
|  2 | test       | CLS_KIT        | accuracy    | 0.767241 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.255703 |
|  4 | test       | CLS_KIT        | mcc         | 0.255801 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.761122 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | mean_squared_error  | 1579.31     |
|  1 | test       | KIT            | pearsonr            |    0.369256 |
|  2 | test       | KIT            | spearmanr           |    0.298543 |
|  3 | test       | KIT            | r2                  |   -0.308803 |
|  4 | test       | KIT            | mean_absolute_error |   32.3676   |
|  5 | test       | KIT            | explained_var       |   -0.295868 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | EGFR           | mean_squared_error  | 764.534     |
|  1 | test       | EGFR           | pearsonr            |   0.44298   |
|  2 | test       | EGFR           | spearmanr           |   0.31348   |
|  3 | test       | EGFR           | r2                  |   0.0511745 |
|  4 | test       | EGFR           | mean_absolute_error |  22.2648    |
|  5 | test       | EGFR           | explained_var       |   0.0628756 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.354778 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.597664 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.468898 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.345644 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.402974 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.352387 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.42529  |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.723217 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.815652 |
|  3 | test       | LOG_RPPB       | r2                  | 0.52133  |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.445833 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.522412 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.369689 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.646424 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.576973 |
|  3 | test       | LOG_HPPB       | r2                  | 0.389589 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.518485 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.390717 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.255891 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.707022 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.713756 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.483457 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.397258 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.495117 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.34725  |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.643925 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.660161 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.384902 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.461742 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.392106 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.257788 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.619756 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.64192  |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.336299 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.396599 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.342454 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.834605 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.21866 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.332082 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.636922 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.192919 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.366317 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.312179 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.848261 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.688061 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.066543 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.594485 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.910957 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.311057 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.830486 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.910256 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.829803 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.632592 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6303152235985714,
    "polaris/pkis2-ret-wt-reg-v2": 925.7953949154528,
    "polaris/pkis2-kit-wt-cls-v2": 0.46571451419535426,
    "polaris/pkis2-kit-wt-reg-v2": 1579.3122349644214,
    "polaris/pkis2-egfr-wt-reg-v2": 764.5336424686672,
    "polaris/adme-fang-solu-1": 0.5976635019383318,
    "polaris/adme-fang-rppb-1": 0.7232172089258064,
    "polaris/adme-fang-hppb-1": 0.6464236245441958,
    "polaris/adme-fang-perm-1": 0.7070221955941198,
    "polaris/adme-fang-rclint-1": 0.6439249330352733,
    "polaris/adme-fang-hclint-1": 0.6197559668393406,
    "tdcommons/lipophilicity-astrazeneca": 0.8346052435750052,
    "tdcommons/ppbr-az": 9.21866024665628,
    "tdcommons/clearance-hepatocyte-az": 0.33208168036470004,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6369224380552418,
    "tdcommons/half-life-obach": 0.19291891331708713,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.36631695420560834,
    "tdcommons/clearance-microsome-az": 0.31217915384006273,
    "tdcommons/dili": 0.8482608695652174,
    "tdcommons/bioavailability-ma": 0.6880611905553708,
    "tdcommons/vdss-lombardo": 0.06654301360490902,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.594484629294756,
    "tdcommons/pgp-broccatelli": 0.9109570781125035,
    "tdcommons/caco2-wang": 0.31105720192143377,
    "tdcommons/herg": 0.8304860088365243,
    "tdcommons/bbb-martins": 0.9102564102564102,
    "tdcommons/ames": 0.8298028157982336,
    "tdcommons/ld50-zhu": 0.6325923925865649
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.53118  |
|  1 | test       | CLS_RET        | f1          | 0.285714 |
|  2 | test       | CLS_RET        | accuracy    | 0.858491 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.239234 |
|  4 | test       | CLS_RET        | mcc         | 0.318193 |
|  5 | test       | CLS_RET        | roc_auc     | 0.842036 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 816.656    |
|  1 | test       | RET            | pearsonr            |   0.59874  |
|  2 | test       | RET            | spearmanr           |   0.590606 |
|  3 | test       | RET            | r2                  |   0.312235 |
|  4 | test       | RET            | mean_absolute_error |  20.9286   |
|  5 | test       | RET            | explained_var       |   0.346324 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.412566 |
|  1 | test       | CLS_KIT        | f1          | 0.478261 |
|  2 | test       | CLS_KIT        | accuracy    | 0.793103 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.349533 |
|  4 | test       | CLS_KIT        | mcc         | 0.350047 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.742747 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | mean_squared_error  | 1175.04      |
|  1 | test       | KIT            | pearsonr            |    0.405159  |
|  2 | test       | KIT            | spearmanr           |    0.410797  |
|  3 | test       | KIT            | r2                  |    0.0262253 |
|  4 | test       | KIT            | mean_absolute_error |   26.7824    |
|  5 | test       | KIT            | explained_var       |    0.0376407 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 525.123    |
|  1 | test       | EGFR           | pearsonr            |   0.614614 |
|  2 | test       | EGFR           | spearmanr           |   0.346486 |
|  3 | test       | EGFR           | r2                  |   0.348295 |
|  4 | test       | EGFR           | mean_absolute_error |  18.1457   |
|  5 | test       | EGFR           | explained_var       |   0.370514 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.385845 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.549538 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.467301 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.288344 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.429523 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.289775 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.378293 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.799678 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.795652 |
|  3 | test       | LOG_RPPB       | r2                  | 0.574225 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.466012 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.583113 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.458047 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.656684 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.679807 |
|  3 | test       | LOG_HPPB       | r2                  | 0.243696 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.506346 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.303667 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.238674 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.727502 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.736564 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.518213 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.379983 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.518721 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.341072 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.649081 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.65396  |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.395844 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.461906 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.396274 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.268852 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.630879 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.651491 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.307813 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.407608 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.308264 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.542296 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.50957 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.322398 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.639943 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.191743 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.354771 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.41351 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.855652 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.645161 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.224482 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.62387 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.915822 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.297575 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.821502 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.912992 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.802677 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.650092 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5311799874519111,
    "polaris/pkis2-ret-wt-reg-v2": 816.6555014624173,
    "polaris/pkis2-kit-wt-cls-v2": 0.41256629677092355,
    "polaris/pkis2-kit-wt-reg-v2": 1175.0384192976705,
    "polaris/pkis2-egfr-wt-reg-v2": 525.1230604118564,
    "polaris/adme-fang-solu-1": 0.5495384601780113,
    "polaris/adme-fang-rppb-1": 0.7996775320700069,
    "polaris/adme-fang-hppb-1": 0.65668433609613,
    "polaris/adme-fang-perm-1": 0.7275018446655402,
    "polaris/adme-fang-rclint-1": 0.6490807802522913,
    "polaris/adme-fang-hclint-1": 0.6308793736994094,
    "tdcommons/lipophilicity-astrazeneca": 0.5422959252709434,
    "tdcommons/ppbr-az": 8.509574210997771,
    "tdcommons/clearance-hepatocyte-az": 0.322398135870975,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6399427554008312,
    "tdcommons/half-life-obach": 0.19174328491573892,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3547707171197285,
    "tdcommons/clearance-microsome-az": 0.4135104349431565,
    "tdcommons/dili": 0.8556521739130435,
    "tdcommons/bioavailability-ma": 0.6451612903225806,
    "tdcommons/vdss-lombardo": 0.22448169142816307,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.623869801084991,
    "tdcommons/pgp-broccatelli": 0.9158224473473742,
    "tdcommons/caco2-wang": 0.29757458972174683,
    "tdcommons/herg": 0.8215022091310751,
    "tdcommons/bbb-martins": 0.9129924953095685,
    "tdcommons/ames": 0.802676770643639,
    "tdcommons/ld50-zhu": 0.6500918132507106
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.538172 |
|  1 | test       | CLS_RET        | f1          | 0.285714 |
|  2 | test       | CLS_RET        | accuracy    | 0.858491 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.239234 |
|  4 | test       | CLS_RET        | mcc         | 0.318193 |
|  5 | test       | CLS_RET        | roc_auc     | 0.828156 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 941.309    |
|  1 | test       | RET            | pearsonr            |   0.550272 |
|  2 | test       | RET            | spearmanr           |   0.553918 |
|  3 | test       | RET            | r2                  |   0.207256 |
|  4 | test       | RET            | mean_absolute_error |  23.0341   |
|  5 | test       | RET            | explained_var       |   0.244926 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.442913 |
|  1 | test       | CLS_KIT        | f1          | 0.285714 |
|  2 | test       | CLS_KIT        | accuracy    | 0.784483 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.168578 |
|  4 | test       | CLS_KIT        | mcc         | 0.176678 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.730174 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | mean_squared_error  | 1000.04     |
|  1 | test       | KIT            | pearsonr            |    0.476626 |
|  2 | test       | KIT            | spearmanr           |    0.456847 |
|  3 | test       | KIT            | r2                  |    0.171247 |
|  4 | test       | KIT            | mean_absolute_error |   24.9853   |
|  5 | test       | KIT            | explained_var       |    0.180144 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 517.633    |
|  1 | test       | EGFR           | pearsonr            |   0.623809 |
|  2 | test       | EGFR           | spearmanr           |   0.400959 |
|  3 | test       | EGFR           | r2                  |   0.357591 |
|  4 | test       | EGFR           | mean_absolute_error |  17.9554   |
|  5 | test       | EGFR           | explained_var       |   0.357644 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.403336 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.52258  |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.450131 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.256084 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.443789 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.268582 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.472752 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.760954 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.783478 |
|  3 | test       | LOG_RPPB       | r2                  | 0.46791  |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.539564 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.559288 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.384481 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.774684 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.771335 |
|  3 | test       | LOG_HPPB       | r2                  | 0.365164 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.51398  |
|  5 | test       | LOG_HPPB       | explained_var       | 0.453865 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.257672 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.715962 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.723998 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.479864 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.403563 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.509405 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.312061 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.682194 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.694647 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.447233 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.431364 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.448321 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.24586  |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.632027 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.651794 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.36701  |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.390739 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.368906 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.554328 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.44473 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.284778 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.662691 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.215002 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.393771 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.514453 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.888261 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.52012 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.231916 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.638336 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.89936 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.300661 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.824448 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.905214 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.827684 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.63942 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.538171719700947,
    "polaris/pkis2-ret-wt-reg-v2": 941.3088410630669,
    "polaris/pkis2-kit-wt-cls-v2": 0.4429128997803057,
    "polaris/pkis2-kit-wt-reg-v2": 1000.0433332266393,
    "polaris/pkis2-egfr-wt-reg-v2": 517.6325982247716,
    "polaris/adme-fang-solu-1": 0.5225801885807986,
    "polaris/adme-fang-rppb-1": 0.7609539409922452,
    "polaris/adme-fang-hppb-1": 0.7746842161424928,
    "polaris/adme-fang-perm-1": 0.7159616324166385,
    "polaris/adme-fang-rclint-1": 0.6821941332181384,
    "polaris/adme-fang-hclint-1": 0.6320270914781958,
    "tdcommons/lipophilicity-astrazeneca": 0.5543284549429303,
    "tdcommons/ppbr-az": 9.44473167296599,
    "tdcommons/clearance-hepatocyte-az": 0.2847780257273495,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6626909636744307,
    "tdcommons/half-life-obach": 0.21500219038307578,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.39377100627992684,
    "tdcommons/clearance-microsome-az": 0.514453129677354,
    "tdcommons/dili": 0.8882608695652174,
    "tdcommons/bioavailability-ma": 0.5201197206518124,
    "tdcommons/vdss-lombardo": 0.2319155055468115,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6383363471971067,
    "tdcommons/pgp-broccatelli": 0.8993601706211677,
    "tdcommons/caco2-wang": 0.3006613420520826,
    "tdcommons/herg": 0.8244477172312225,
    "tdcommons/bbb-martins": 0.9052141963727329,
    "tdcommons/ames": 0.8276841136501595,
    "tdcommons/ld50-zhu": 0.6394196249899909
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.525986 |
|  1 | test       | CLS_RET        | f1          | 0.347826 |
|  2 | test       | CLS_RET        | accuracy    | 0.858491 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.288272 |
|  4 | test       | CLS_RET        | mcc         | 0.337956 |
|  5 | test       | CLS_RET        | roc_auc     | 0.825512 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 884.106    |
|  1 | test       | RET            | pearsonr            |   0.543899 |
|  2 | test       | RET            | spearmanr           |   0.520618 |
|  3 | test       | RET            | r2                  |   0.255431 |
|  4 | test       | RET            | mean_absolute_error |  22.8022   |
|  5 | test       | RET            | explained_var       |   0.271249 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.452648 |
|  1 | test       | CLS_KIT        | f1          | 0.421053 |
|  2 | test       | CLS_KIT        | accuracy    | 0.810345 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.311015 |
|  4 | test       | CLS_KIT        | mcc         | 0.316656 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.780464 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | mean_squared_error  | 1098.26      |
|  1 | test       | KIT            | pearsonr            |    0.428396  |
|  2 | test       | KIT            | spearmanr           |    0.41117   |
|  3 | test       | KIT            | r2                  |    0.0898525 |
|  4 | test       | KIT            | mean_absolute_error |   25.9556    |
|  5 | test       | KIT            | explained_var       |    0.126784  |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 581.538    |
|  1 | test       | EGFR           | pearsonr            |   0.607953 |
|  2 | test       | EGFR           | spearmanr           |   0.377323 |
|  3 | test       | EGFR           | r2                  |   0.278281 |
|  4 | test       | EGFR           | mean_absolute_error |  18.6101   |
|  5 | test       | EGFR           | explained_var       |   0.278361 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.378429 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.566939 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.481622 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.302022 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.411708 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.321383 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.244506 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.868717 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.890435 |
|  3 | test       | LOG_RPPB       | r2                  | 0.724805 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.379036 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.729456 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.513096 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.648881 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.714493 |
|  3 | test       | LOG_HPPB       | r2                  | 0.152801 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.47203  |
|  5 | test       | LOG_HPPB       | explained_var       | 0.228366 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.240634 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.726583 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.719824 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.514255 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.377091 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.518826 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.338596 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.639316 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.647751 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.400229 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.45897  |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.404227 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.246108 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.642993 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.667372 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.366372 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.385023 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.377712 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.566719 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.06004 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.348401 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.594749 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.259405 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.328337 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.468833 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.901739 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.630196 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.136131 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.610759 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.91389 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.302118 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.821502 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.865932 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.828309 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.644206 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5259862208757204,
    "polaris/pkis2-ret-wt-reg-v2": 884.1055593435588,
    "polaris/pkis2-kit-wt-cls-v2": 0.45264753868975277,
    "polaris/pkis2-kit-wt-reg-v2": 1098.2604290104741,
    "polaris/pkis2-egfr-wt-reg-v2": 581.5384452371991,
    "polaris/adme-fang-solu-1": 0.5669391780056838,
    "polaris/adme-fang-rppb-1": 0.8687166318534356,
    "polaris/adme-fang-hppb-1": 0.6488813545520784,
    "polaris/adme-fang-perm-1": 0.7265830483274613,
    "polaris/adme-fang-rclint-1": 0.6393157380265064,
    "polaris/adme-fang-hclint-1": 0.64299252374566,
    "tdcommons/lipophilicity-astrazeneca": 0.5667189569927397,
    "tdcommons/ppbr-az": 9.060044471317626,
    "tdcommons/clearance-hepatocyte-az": 0.3484013257755016,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5947492357847507,
    "tdcommons/half-life-obach": 0.25940533363316676,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3283372008274524,
    "tdcommons/clearance-microsome-az": 0.46883343083419154,
    "tdcommons/dili": 0.9017391304347826,
    "tdcommons/bioavailability-ma": 0.6301962088460259,
    "tdcommons/vdss-lombardo": 0.13613126707121168,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6107594936708861,
    "tdcommons/pgp-broccatelli": 0.9138896294321515,
    "tdcommons/caco2-wang": 0.3021182801514008,
    "tdcommons/herg": 0.8215022091310751,
    "tdcommons/bbb-martins": 0.8659318323952471,
    "tdcommons/ames": 0.8283087587381778,
    "tdcommons/ld50-zhu": 0.6442062618638892
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.704412 |
|  1 | test       | CLS_RET        | f1          | 0.642857 |
|  2 | test       | CLS_RET        | accuracy    | 0.90566  |
|  3 | test       | CLS_RET        | cohen_kappa | 0.591365 |
|  4 | test       | CLS_RET        | mcc         | 0.609983 |
|  5 | test       | CLS_RET        | roc_auc     | 0.858559 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 823.8      |
|  1 | test       | RET            | pearsonr            |   0.584229 |
|  2 | test       | RET            | spearmanr           |   0.5277   |
|  3 | test       | RET            | r2                  |   0.306218 |
|  4 | test       | RET            | mean_absolute_error |  22.1812   |
|  5 | test       | RET            | explained_var       |   0.327778 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.410195 |
|  1 | test       | CLS_KIT        | f1          | 0.333333 |
|  2 | test       | CLS_KIT        | accuracy    | 0.758621 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.186373 |
|  4 | test       | CLS_KIT        | mcc         | 0.186688 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.752901 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | mean_squared_error  | 1049.44     |
|  1 | test       | KIT            | pearsonr            |    0.428213 |
|  2 | test       | KIT            | spearmanr           |    0.413613 |
|  3 | test       | KIT            | r2                  |    0.130307 |
|  4 | test       | KIT            | mean_absolute_error |   26.0693   |
|  5 | test       | KIT            | explained_var       |    0.135288 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 616.554    |
|  1 | test       | EGFR           | pearsonr            |   0.531337 |
|  2 | test       | EGFR           | spearmanr           |   0.397812 |
|  3 | test       | EGFR           | r2                  |   0.234825 |
|  4 | test       | EGFR           | mean_absolute_error |  19.3447   |
|  5 | test       | EGFR           | explained_var       |   0.263589 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.391081 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.539329 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.434482 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.278686 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.440077 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.281548 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.329884 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.8364   |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.884348 |
|  3 | test       | LOG_RPPB       | r2                  | 0.628711 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.484633 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.696463 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  |  0.694134 |
|  1 | test       | LOG_HPPB       | pearsonr            |  0.610166 |
|  2 | test       | LOG_HPPB       | spearmanr           |  0.739552 |
|  3 | test       | LOG_HPPB       | r2                  | -0.146119 |
|  4 | test       | LOG_HPPB       | mean_absolute_error |  0.530423 |
|  5 | test       | LOG_HPPB       | explained_var       |  0.03873  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.26512  |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.712197 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.697667 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.464828 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.396846 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.466551 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.317798 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.669885 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.676961 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.437071 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.449152 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.439153 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.239258 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.623075 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.632201 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.384006 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.390519 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.387647 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.767064 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.82958 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.388224 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   |   0.615 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.284053 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.326906 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.444112 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.873043 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.536748 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.332059 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.616637 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.919088 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.318787 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.830339 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.884264 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.829204 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.606236 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7044124156492677,
    "polaris/pkis2-ret-wt-reg-v2": 823.8001388236644,
    "polaris/pkis2-kit-wt-cls-v2": 0.41019548272563494,
    "polaris/pkis2-kit-wt-reg-v2": 1049.4449692525989,
    "polaris/pkis2-egfr-wt-reg-v2": 616.5539692859485,
    "polaris/adme-fang-solu-1": 0.5393290693391475,
    "polaris/adme-fang-rppb-1": 0.8363997314987655,
    "polaris/adme-fang-hppb-1": 0.6101662478910607,
    "polaris/adme-fang-perm-1": 0.712196775736983,
    "polaris/adme-fang-rclint-1": 0.669884633866767,
    "polaris/adme-fang-hclint-1": 0.6230748844863753,
    "tdcommons/lipophilicity-astrazeneca": 0.7670636195625578,
    "tdcommons/ppbr-az": 8.82958199707468,
    "tdcommons/clearance-hepatocyte-az": 0.38822429643999024,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.615000286981326,
    "tdcommons/half-life-obach": 0.2840529391479043,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3269056806988712,
    "tdcommons/clearance-microsome-az": 0.4441116114937219,
    "tdcommons/dili": 0.8730434782608696,
    "tdcommons/bioavailability-ma": 0.5367475889590955,
    "tdcommons/vdss-lombardo": 0.3320586800284704,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6166365280289331,
    "tdcommons/pgp-broccatelli": 0.919088243135164,
    "tdcommons/caco2-wang": 0.3187868777691684,
    "tdcommons/herg": 0.8303387334315169,
    "tdcommons/bbb-martins": 0.8842636022514071,
    "tdcommons/ames": 0.8292036264661536,
    "tdcommons/ld50-zhu": 0.6062357093019963
}
```
