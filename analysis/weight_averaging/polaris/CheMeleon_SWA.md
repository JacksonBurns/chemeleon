# ChemProp Baseline Results
timestamp: 2025-07-08 23:35:22.543407
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.369548 |
|  1 | test       | CLS_RET        | accuracy    | 0.858491 |
|  2 | test       | CLS_RET        | pr_auc      | 0.611473 |
|  3 | test       | CLS_RET        | mcc         | 0.386661 |
|  4 | test       | CLS_RET        | roc_auc     | 0.807667 |
|  5 | test       | CLS_RET        | f1          | 0.444444 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.382837 |
|  1 | test       | RET            | r2                  |   0.2982   |
|  2 | test       | RET            | pearsonr            |   0.632296 |
|  3 | test       | RET            | mean_absolute_error |  21.5325   |
|  4 | test       | RET            | mean_squared_error  | 833.321    |
|  5 | test       | RET            | spearmanr           |   0.596985 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.478652 |
|  1 | test       | CLS_KIT        | accuracy    | 0.862069 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.641785 |
|  3 | test       | CLS_KIT        | mcc         | 0.495793 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.803675 |
|  5 | test       | CLS_KIT        | f1          | 0.555556 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.356552 |
|  1 | test       | KIT            | r2                  |   0.341239 |
|  2 | test       | KIT            | pearsonr            |   0.597923 |
|  3 | test       | KIT            | mean_absolute_error |  21.9319   |
|  4 | test       | KIT            | mean_squared_error  | 794.917    |
|  5 | test       | KIT            | spearmanr           |   0.528611 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.408234 |
|  1 | test       | EGFR           | r2                  |   0.393629 |
|  2 | test       | EGFR           | pearsonr            |   0.645062 |
|  3 | test       | EGFR           | mean_absolute_error |  17.7739   |
|  4 | test       | EGFR           | mean_squared_error  | 488.595    |
|  5 | test       | EGFR           | spearmanr           |   0.327928 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.362674 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.338869 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.608793 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.400016 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.358451 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.486684 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.361712 |
|  1 | test       | LOG_RPPB       | r2                  | 0.324316 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.673622 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.641044 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.600333 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.766957 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.512292 |
|  1 | test       | LOG_HPPB       | r2                  | 0.466657 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.723261 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.510625 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.323013 |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.720299 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.602248 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.597834 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.776049 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.320795 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.19923  |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.766151 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.496618 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.496239 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.706013 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.431861 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.284395 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.706687 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.465332 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.464763 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.690647 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.35963  |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.207892 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.69279  |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.514783 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.75838 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.344324 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.699073 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.219614 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.412475 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.605174 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.91913 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.538078 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.489889 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.619349 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.926353 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.399586 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.841679 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.885749 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.850165 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.531888 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6114725929188507,
    "polaris/pkis2-ret-wt-reg-v2": 833.3213905134234,
    "polaris/pkis2-kit-wt-cls-v2": 0.6417849512013913,
    "polaris/pkis2-kit-wt-reg-v2": 794.9165205693316,
    "polaris/pkis2-egfr-wt-reg-v2": 488.59470502033736,
    "polaris/adme-fang-solu-1": 0.6087929251577127,
    "polaris/adme-fang-rppb-1": 0.6736224797352013,
    "polaris/adme-fang-hppb-1": 0.7232605920367019,
    "polaris/adme-fang-perm-1": 0.776049384748928,
    "polaris/adme-fang-rclint-1": 0.7060131627118776,
    "polaris/adme-fang-hclint-1": 0.6906465874522146,
    "tdcommons/lipophilicity-astrazeneca": 0.5147827678918839,
    "tdcommons/ppbr-az": 7.758382223330585,
    "tdcommons/clearance-hepatocyte-az": 0.3443235088219049,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6990726760585178,
    "tdcommons/half-life-obach": 0.21961445865475507,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4124754820830927,
    "tdcommons/clearance-microsome-az": 0.6051744122051512,
    "tdcommons/dili": 0.9191304347826087,
    "tdcommons/bioavailability-ma": 0.5380778184236781,
    "tdcommons/vdss-lombardo": 0.48988879698196763,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6193490054249547,
    "tdcommons/pgp-broccatelli": 0.9263529725406557,
    "tdcommons/caco2-wang": 0.399585704564323,
    "tdcommons/herg": 0.841678939617084,
    "tdcommons/bbb-martins": 0.8857489055659787,
    "tdcommons/ames": 0.8501654624135973,
    "tdcommons/ld50-zhu": 0.5318882055689098
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0        |
|  1 | test       | CLS_RET        | accuracy    | 0.839623 |
|  2 | test       | CLS_RET        | pr_auc      | 0.528682 |
|  3 | test       | CLS_RET        | mcc         | 0        |
|  4 | test       | CLS_RET        | roc_auc     | 0.803701 |
|  5 | test       | CLS_RET        | f1          | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.522148 |
|  1 | test       | RET            | r2                  |   0.521523 |
|  2 | test       | RET            | pearsonr            |   0.737446 |
|  3 | test       | RET            | mean_absolute_error |  19.091    |
|  4 | test       | RET            | mean_squared_error  | 568.146    |
|  5 | test       | RET            | spearmanr           |   0.666862 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.361858 |
|  1 | test       | CLS_KIT        | accuracy    | 0.844828 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.670137 |
|  3 | test       | CLS_KIT        | mcc         | 0.399847 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.868472 |
|  5 | test       | CLS_KIT        | f1          | 0.4375   |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.248886 |
|  1 | test       | KIT            | r2                  |   0.244609 |
|  2 | test       | KIT            | pearsonr            |   0.561858 |
|  3 | test       | KIT            | mean_absolute_error |  22.4446   |
|  4 | test       | KIT            | mean_squared_error  | 911.518    |
|  5 | test       | KIT            | spearmanr           |   0.565015 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.407786 |
|  1 | test       | EGFR           | r2                  |   0.380373 |
|  2 | test       | EGFR           | pearsonr            |   0.642629 |
|  3 | test       | EGFR           | mean_absolute_error |  18.0556   |
|  4 | test       | EGFR           | mean_squared_error  | 499.276    |
|  5 | test       | EGFR           | spearmanr           |   0.298375 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.374074 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.363808 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.616662 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.416884 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.34493  |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.507267 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.381181 |
|  1 | test       | LOG_RPPB       | r2                  | 0.321459 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.706206 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.655058 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.602871 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.771304 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.0628    |
|  1 | test       | LOG_HPPB       | r2                  | 0.0616696 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.52661   |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.638627  |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.568289  |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.56536   |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.636071 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.608193 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.798249 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.334475 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.194098 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.791331 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.545215 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.54176  |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.739069 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.402124 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.258696 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.738837 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.476581 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.44831  |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.690694 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.363054 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.214282 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.695573 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.517259 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.94245 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.372102 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.688986 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.365634 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.42711 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.588169 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.900435 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.514466 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.560701 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.623644 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.937217 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.383155 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.838733 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.901071 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.836236 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.604246 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5286821967178013,
    "polaris/pkis2-ret-wt-reg-v2": 568.145588288843,
    "polaris/pkis2-kit-wt-cls-v2": 0.670136737988714,
    "polaris/pkis2-kit-wt-reg-v2": 911.5177980306921,
    "polaris/pkis2-egfr-wt-reg-v2": 499.2758104542528,
    "polaris/adme-fang-solu-1": 0.6166617359132774,
    "polaris/adme-fang-rppb-1": 0.7062059626827795,
    "polaris/adme-fang-hppb-1": 0.5266102148598336,
    "polaris/adme-fang-perm-1": 0.7982485223298732,
    "polaris/adme-fang-rclint-1": 0.739068564659179,
    "polaris/adme-fang-hclint-1": 0.6906944544571885,
    "tdcommons/lipophilicity-astrazeneca": 0.5172593407857986,
    "tdcommons/ppbr-az": 8.942453111570082,
    "tdcommons/clearance-hepatocyte-az": 0.37210228318491917,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6889855122491182,
    "tdcommons/half-life-obach": 0.36563384766619134,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.42711033177981905,
    "tdcommons/clearance-microsome-az": 0.5881692136961365,
    "tdcommons/dili": 0.9004347826086956,
    "tdcommons/bioavailability-ma": 0.5144662454273361,
    "tdcommons/vdss-lombardo": 0.5607006465006943,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6236437613019891,
    "tdcommons/pgp-broccatelli": 0.9372167422020794,
    "tdcommons/caco2-wang": 0.3831553903852861,
    "tdcommons/herg": 0.8387334315169367,
    "tdcommons/bbb-martins": 0.9010709818636647,
    "tdcommons/ames": 0.8362362685778065,
    "tdcommons/ld50-zhu": 0.6042457303187844
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0        |
|  1 | test       | CLS_RET        | accuracy    | 0.839623 |
|  2 | test       | CLS_RET        | pr_auc      | 0.65977  |
|  3 | test       | CLS_RET        | mcc         | 0        |
|  4 | test       | CLS_RET        | roc_auc     | 0.877726 |
|  5 | test       | CLS_RET        | f1          | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.403446 |
|  1 | test       | RET            | r2                  |   0.377725 |
|  2 | test       | RET            | pearsonr            |   0.661265 |
|  3 | test       | RET            | mean_absolute_error |  21.0708   |
|  4 | test       | RET            | mean_squared_error  | 738.893    |
|  5 | test       | RET            | spearmanr           |   0.648495 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.475    |
|  1 | test       | CLS_KIT        | accuracy    | 0.818966 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.64175  |
|  3 | test       | CLS_KIT        | mcc         | 0.482445 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.842843 |
|  5 | test       | CLS_KIT        | f1          | 0.588235 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.374566 |
|  1 | test       | KIT            | r2                  |   0.374545 |
|  2 | test       | KIT            | pearsonr            |   0.62576  |
|  3 | test       | KIT            | mean_absolute_error |  21.275    |
|  4 | test       | KIT            | mean_squared_error  | 754.727    |
|  5 | test       | KIT            | spearmanr           |   0.598448 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.306251 |
|  1 | test       | EGFR           | r2                  |   0.300016 |
|  2 | test       | EGFR           | pearsonr            |   0.558536 |
|  3 | test       | EGFR           | mean_absolute_error |  18.416    |
|  4 | test       | EGFR           | mean_squared_error  | 564.025    |
|  5 | test       | EGFR           | spearmanr           |   0.280034 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.358358 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.355565 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.603117 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.410992 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.349399 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.493708 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.456163 |
|  1 | test       | LOG_RPPB       | r2                  | 0.43965  |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.726097 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.559286 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.497861 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.765217 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.517227 |
|  1 | test       | LOG_HPPB       | r2                  | 0.501014 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.747962 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.484106 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.302205 |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.791352 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.597566 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.593216 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.775779 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.322752 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.201518 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.764219 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.513925 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.501574 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.718321 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.41454  |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.281383 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.720701 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.458879 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.458745 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.679767 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.36909  |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.210229 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.68386  |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.522419 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.41134 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.40604 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.681658 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.240403 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.440312 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.580579 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.86913 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.59694 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.555019 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.548146 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.929685 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.419586 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.841679 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.901423 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.852774 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.531114 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6597700783552711,
    "polaris/pkis2-ret-wt-reg-v2": 738.8927864191979,
    "polaris/pkis2-kit-wt-cls-v2": 0.6417503664539237,
    "polaris/pkis2-kit-wt-reg-v2": 754.7268157874337,
    "polaris/pkis2-egfr-wt-reg-v2": 564.024737907342,
    "polaris/adme-fang-solu-1": 0.6031168027190477,
    "polaris/adme-fang-rppb-1": 0.7260969612803633,
    "polaris/adme-fang-hppb-1": 0.7479619433913969,
    "polaris/adme-fang-perm-1": 0.7757792601336003,
    "polaris/adme-fang-rclint-1": 0.718321453041399,
    "polaris/adme-fang-hclint-1": 0.6797671857447576,
    "tdcommons/lipophilicity-astrazeneca": 0.5224186123836608,
    "tdcommons/ppbr-az": 8.411343691967469,
    "tdcommons/clearance-hepatocyte-az": 0.4060396152305089,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6816583532011786,
    "tdcommons/half-life-obach": 0.2404025932288021,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.44031231024642853,
    "tdcommons/clearance-microsome-az": 0.5805787130019546,
    "tdcommons/dili": 0.8691304347826088,
    "tdcommons/bioavailability-ma": 0.59694047223146,
    "tdcommons/vdss-lombardo": 0.5550186175921348,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5481464737793853,
    "tdcommons/pgp-broccatelli": 0.9296854172220742,
    "tdcommons/caco2-wang": 0.4195864221304423,
    "tdcommons/herg": 0.841678939617084,
    "tdcommons/bbb-martins": 0.9014227642276422,
    "tdcommons/ames": 0.852773698329711,
    "tdcommons/ld50-zhu": 0.5311137224263203
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0        |
|  1 | test       | CLS_RET        | accuracy    | 0.839623 |
|  2 | test       | CLS_RET        | pr_auc      | 0.460521 |
|  3 | test       | CLS_RET        | mcc         | 0        |
|  4 | test       | CLS_RET        | roc_auc     | 0.775281 |
|  5 | test       | CLS_RET        | f1          | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.434647 |
|  1 | test       | RET            | r2                  |   0.321234 |
|  2 | test       | RET            | pearsonr            |   0.665229 |
|  3 | test       | RET            | mean_absolute_error |  20.5192   |
|  4 | test       | RET            | mean_squared_error  | 805.97     |
|  5 | test       | RET            | spearmanr           |   0.586688 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.434633 |
|  1 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.538085 |
|  3 | test       | CLS_KIT        | mcc         | 0.455516 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.825435 |
|  5 | test       | CLS_KIT        | f1          | 0.514286 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.359819 |
|  1 | test       | KIT            | r2                  |   0.342118 |
|  2 | test       | KIT            | pearsonr            |   0.599852 |
|  3 | test       | KIT            | mean_absolute_error |  21.666    |
|  4 | test       | KIT            | mean_squared_error  | 793.856    |
|  5 | test       | KIT            | spearmanr           |   0.565357 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.374601 |
|  1 | test       | EGFR           | r2                  |   0.373538 |
|  2 | test       | EGFR           | pearsonr            |   0.624024 |
|  3 | test       | EGFR           | mean_absolute_error |  17.6596   |
|  4 | test       | EGFR           | mean_squared_error  | 504.783    |
|  5 | test       | EGFR           | spearmanr           |   0.305056 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.342259 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.331432 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.593357 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.425539 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.362483 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.491121 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.236338 |
|  1 | test       | LOG_RPPB       | r2                  | 0.196612 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.730487 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.72683  |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.713795 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.786957 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.403213 |
|  1 | test       | LOG_HPPB       | r2                  | 0.398947 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.719014 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.526194 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.364021 |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.694782 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.595501 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.594721 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.771804 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.332582 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.200772 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.753931 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.544626 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.543708 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.738023 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.404941 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.257597 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.738671 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.455201 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.454806 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.694941 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.357224 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.211759 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.694602 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.520375 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.67056 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.373697 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.577009 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.333898 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.427513 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.610911 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.919565 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.612571 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.530577 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.607821 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.92442 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.423597 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.838733 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.898257 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.847327 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.536118 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.46052148704340834,
    "polaris/pkis2-ret-wt-reg-v2": 805.9704006098791,
    "polaris/pkis2-kit-wt-cls-v2": 0.538084816130547,
    "polaris/pkis2-kit-wt-reg-v2": 793.856046278595,
    "polaris/pkis2-egfr-wt-reg-v2": 504.7833466268609,
    "polaris/adme-fang-solu-1": 0.593356501645239,
    "polaris/adme-fang-rppb-1": 0.7304874001705222,
    "polaris/adme-fang-hppb-1": 0.7190136511785277,
    "polaris/adme-fang-perm-1": 0.7718039705356593,
    "polaris/adme-fang-rclint-1": 0.7380233028913348,
    "polaris/adme-fang-hclint-1": 0.6949410360712291,
    "tdcommons/lipophilicity-astrazeneca": 0.5203753979092552,
    "tdcommons/ppbr-az": 8.670555007470528,
    "tdcommons/clearance-hepatocyte-az": 0.37369664929821067,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5770092976241114,
    "tdcommons/half-life-obach": 0.3338975713342908,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4275133164208781,
    "tdcommons/clearance-microsome-az": 0.6109111741249063,
    "tdcommons/dili": 0.9195652173913044,
    "tdcommons/bioavailability-ma": 0.6125706684403059,
    "tdcommons/vdss-lombardo": 0.5305771786051723,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6078209764918626,
    "tdcommons/pgp-broccatelli": 0.9244201546254333,
    "tdcommons/caco2-wang": 0.42359704744497445,
    "tdcommons/herg": 0.8387334315169367,
    "tdcommons/bbb-martins": 0.8982567229518449,
    "tdcommons/ames": 0.8473271456265052,
    "tdcommons/ld50-zhu": 0.5361177202277642
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.309348 |
|  1 | test       | CLS_RET        | accuracy    | 0.783019 |
|  2 | test       | CLS_RET        | pr_auc      | 0.540589 |
|  3 | test       | CLS_RET        | mcc         | 0.316418 |
|  4 | test       | CLS_RET        | roc_auc     | 0.810311 |
|  5 | test       | CLS_RET        | f1          | 0.439024 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.417789 |
|  1 | test       | RET            | r2                  |   0.361215 |
|  2 | test       | RET            | pearsonr            |   0.646774 |
|  3 | test       | RET            | mean_absolute_error |  20.2631   |
|  4 | test       | RET            | mean_squared_error  | 758.497    |
|  5 | test       | RET            | spearmanr           |   0.591188 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0        |
|  1 | test       | CLS_KIT        | accuracy    | 0.810345 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.556496 |
|  3 | test       | CLS_KIT        | mcc         | 0        |
|  4 | test       | CLS_KIT        | roc_auc     | 0.85735  |
|  5 | test       | CLS_KIT        | f1          | 0        |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.352682 |
|  1 | test       | KIT            | r2                  |   0.352097 |
|  2 | test       | KIT            | pearsonr            |   0.594923 |
|  3 | test       | KIT            | mean_absolute_error |  22.683    |
|  4 | test       | KIT            | mean_squared_error  | 781.815    |
|  5 | test       | KIT            | spearmanr           |   0.536988 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.328285 |
|  1 | test       | EGFR           | r2                  |   0.325366 |
|  2 | test       | EGFR           | pearsonr            |   0.602505 |
|  3 | test       | EGFR           | mean_absolute_error |  17.9244   |
|  4 | test       | EGFR           | mean_squared_error  | 543.599    |
|  5 | test       | EGFR           | spearmanr           |   0.311803 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.400043 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.370458 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.657979 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.380738 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.341324 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.525313 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.415391 |
|  1 | test       | LOG_RPPB       | r2                  | 0.414091 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.750072 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.586622 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.52057  |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.824348 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.310272 |
|  1 | test       | LOG_HPPB       | r2                  | 0.300852 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.682008 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.585089 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.423431 |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.719383 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.592835 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.580159 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.771864 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.324565 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.207986 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.762634 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.536678 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.51625  |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.736411 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.41439  |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.273098 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.732854 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.486309 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.48528  |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.697688 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.351229 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.199923 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.702665 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.497207 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.31616 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.358434 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.624847 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.270559 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.486194 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.61181 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.926087 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.604257 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.581504 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.607369 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.93635 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.348626 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.827541 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.906621 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.839578 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.530715 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5405886074925204,
    "polaris/pkis2-ret-wt-reg-v2": 758.4965502608273,
    "polaris/pkis2-kit-wt-cls-v2": 0.5564958885271902,
    "polaris/pkis2-kit-wt-reg-v2": 781.8146579312229,
    "polaris/pkis2-egfr-wt-reg-v2": 543.5987115779585,
    "polaris/adme-fang-solu-1": 0.657979231317221,
    "polaris/adme-fang-rppb-1": 0.7500723098986879,
    "polaris/adme-fang-hppb-1": 0.6820077945195948,
    "polaris/adme-fang-perm-1": 0.771863892514707,
    "polaris/adme-fang-rclint-1": 0.7364110867148405,
    "polaris/adme-fang-hclint-1": 0.6976884308757128,
    "tdcommons/lipophilicity-astrazeneca": 0.4972065416006815,
    "tdcommons/ppbr-az": 8.316158097050485,
    "tdcommons/clearance-hepatocyte-az": 0.3584336473634801,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6248473312076035,
    "tdcommons/half-life-obach": 0.2705591690675346,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.48619359407538687,
    "tdcommons/clearance-microsome-az": 0.61180992213016,
    "tdcommons/dili": 0.9260869565217392,
    "tdcommons/bioavailability-ma": 0.6042567342866645,
    "tdcommons/vdss-lombardo": 0.5815041371802688,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6073688969258589,
    "tdcommons/pgp-broccatelli": 0.9363503065849107,
    "tdcommons/caco2-wang": 0.34862561147876786,
    "tdcommons/herg": 0.8275405007363771,
    "tdcommons/bbb-martins": 0.906621325828643,
    "tdcommons/ames": 0.8395778260784429,
    "tdcommons/ld50-zhu": 0.5307154799682039
}
```
