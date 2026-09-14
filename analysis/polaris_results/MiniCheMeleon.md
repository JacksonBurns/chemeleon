# ChemProp Baseline Results
timestamp: 2026-09-13 20:40:01.149778
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.190476 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.137799 |
|  2 | test       | CLS_RET        | pr_auc      | 0.591497 |
|  3 | test       | CLS_RET        | accuracy    | 0.839623 |
|  4 | test       | CLS_RET        | mcc         | 0.183279 |
|  5 | test       | CLS_RET        | roc_auc     | 0.836087 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  20.9388   |
|  1 | test       | RET            | r2                  |   0.337292 |
|  2 | test       | RET            | pearsonr            |   0.618854 |
|  3 | test       | RET            | mean_squared_error  | 786.903    |
|  4 | test       | RET            | explained_var       |   0.381584 |
|  5 | test       | RET            | spearmanr           |   0.598007 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.5      |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.432763 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.594479 |
|  3 | test       | CLS_KIT        | accuracy    | 0.862069 |
|  4 | test       | CLS_KIT        | mcc         | 0.478195 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.830271 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  21.44     |
|  1 | test       | KIT            | r2                  |   0.345086 |
|  2 | test       | KIT            | pearsonr            |   0.603371 |
|  3 | test       | KIT            | mean_squared_error  | 790.274    |
|  4 | test       | KIT            | explained_var       |   0.360182 |
|  5 | test       | KIT            | spearmanr           |   0.520288 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  16.7248   |
|  1 | test       | EGFR           | r2                  |   0.422714 |
|  2 | test       | EGFR           | pearsonr            |   0.654106 |
|  3 | test       | EGFR           | mean_squared_error  | 465.159    |
|  4 | test       | EGFR           | explained_var       |   0.423055 |
|  5 | test       | EGFR           | spearmanr           |   0.336777 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.38441  |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.389809 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.624858 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.330832 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.390223 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.520104 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.552329 |
|  1 | test       | LOG_RPPB       | r2                  | 0.254698 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.51845  |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.662188 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.255996 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.61913  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.475982 |
|  1 | test       | LOG_HPPB       | r2                  | 0.472004 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.726158 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.319775 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.484041 |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.739705 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.306148 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.640787 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.801529 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.177951 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.642416 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.797021 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.420582 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.513232 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.71765  |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.274801 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.514919 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.719539 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.34022  |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.480214 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.711332 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.20189  |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.487546 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.727803 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.440537 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.60957 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.40438 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.679779 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.210997 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.445133 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.58602 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  |    0.94 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.62155 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.448871 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.589512 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.908224 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.397955 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.853461 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.908908 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.835785 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.596457 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5914965787605049,
    "polaris/pkis2-ret-wt-reg-v2": 786.9031116190356,
    "polaris/pkis2-kit-wt-cls-v2": 0.5944792481116347,
    "polaris/pkis2-kit-wt-reg-v2": 790.2742589577775,
    "polaris/pkis2-egfr-wt-reg-v2": 465.15852942474237,
    "polaris/adme-fang-solu-1": 0.6248577943348814,
    "polaris/adme-fang-rppb-1": 0.5184498978803097,
    "polaris/adme-fang-hppb-1": 0.7261579975394454,
    "polaris/adme-fang-perm-1": 0.8015287711105197,
    "polaris/adme-fang-rclint-1": 0.7176502846613254,
    "polaris/adme-fang-hclint-1": 0.7113322053900346,
    "tdcommons/lipophilicity-astrazeneca": 0.44053705002012705,
    "tdcommons/ppbr-az": 7.609568089193436,
    "tdcommons/clearance-hepatocyte-az": 0.40438043462779233,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6797791430319774,
    "tdcommons/half-life-obach": 0.21099724881665727,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.44513315115360746,
    "tdcommons/clearance-microsome-az": 0.5860196948585655,
    "tdcommons/dili": 0.9400000000000001,
    "tdcommons/bioavailability-ma": 0.6215497173262388,
    "tdcommons/vdss-lombardo": 0.44887137065839733,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.589511754068716,
    "tdcommons/pgp-broccatelli": 0.9082244734737402,
    "tdcommons/caco2-wang": 0.3979547808974046,
    "tdcommons/herg": 0.853460972017673,
    "tdcommons/bbb-martins": 0.9089079111944964,
    "tdcommons/ames": 0.8357849184436742,
    "tdcommons/ld50-zhu": 0.5964574935032969
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.5      |
|  1 | test       | CLS_RET        | cohen_kappa | 0.448395 |
|  2 | test       | CLS_RET        | pr_auc      | 0.649078 |
|  3 | test       | CLS_RET        | accuracy    | 0.886792 |
|  4 | test       | CLS_RET        | mcc         | 0.504899 |
|  5 | test       | CLS_RET        | roc_auc     | 0.817581 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  23.3349   |
|  1 | test       | RET            | r2                  |   0.268146 |
|  2 | test       | RET            | pearsonr            |   0.533673 |
|  3 | test       | RET            | mean_squared_error  | 869.007    |
|  4 | test       | RET            | explained_var       |   0.279213 |
|  5 | test       | RET            | spearmanr           |   0.496824 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.585366 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.496939 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.59233  |
|  3 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  4 | test       | CLS_KIT        | mcc         | 0.498909 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.826402 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  21.8872   |
|  1 | test       | KIT            | r2                  |   0.303302 |
|  2 | test       | KIT            | pearsonr            |   0.585192 |
|  3 | test       | KIT            | mean_squared_error  | 840.694    |
|  4 | test       | KIT            | explained_var       |   0.313811 |
|  5 | test       | KIT            | spearmanr           |   0.539077 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  16.9219   |
|  1 | test       | EGFR           | r2                  |   0.389532 |
|  2 | test       | EGFR           | pearsonr            |   0.635652 |
|  3 | test       | EGFR           | mean_squared_error  | 491.896    |
|  4 | test       | EGFR           | explained_var       |   0.399157 |
|  5 | test       | EGFR           | spearmanr           |   0.293126 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.382396 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.401498 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.636045 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.324495 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.404414 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.5335   |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.55846  |
|  1 | test       | LOG_RPPB       | r2                  | 0.331222 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.577276 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.594197 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.333052 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.713913 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.472486 |
|  1 | test       | LOG_HPPB       | r2                  | 0.504475 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.719692 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.300109 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.508007 |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.764612 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.302787 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.647551 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.804878 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.174601 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.64757  |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.786972 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.418684 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.503033 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.711677 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.28056  |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.504703 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.714191 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.348067 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.481199 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.715822 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.201507 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.482517 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.732692 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.43642 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.50186 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.399569 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.663351 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.27715 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.403349 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.643289 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.933478 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.512471 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.385674 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.586234 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.896828 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.290953 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.826215 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.900641 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.81936 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.636025 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6490782395630562,
    "polaris/pkis2-ret-wt-reg-v2": 869.0070860095718,
    "polaris/pkis2-kit-wt-cls-v2": 0.5923295101835825,
    "polaris/pkis2-kit-wt-reg-v2": 840.6943068788136,
    "polaris/pkis2-egfr-wt-reg-v2": 491.89575720082826,
    "polaris/adme-fang-solu-1": 0.636045235734588,
    "polaris/adme-fang-rppb-1": 0.5772756582846823,
    "polaris/adme-fang-hppb-1": 0.7196921379086856,
    "polaris/adme-fang-perm-1": 0.8048781383708034,
    "polaris/adme-fang-rclint-1": 0.7116768596862499,
    "polaris/adme-fang-hclint-1": 0.7158222946117839,
    "tdcommons/lipophilicity-astrazeneca": 0.43641964828968055,
    "tdcommons/ppbr-az": 7.501855315616177,
    "tdcommons/clearance-hepatocyte-az": 0.39956923537825095,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6633510411153378,
    "tdcommons/half-life-obach": 0.27714985544737747,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.40334936054685977,
    "tdcommons/clearance-microsome-az": 0.6432891842566627,
    "tdcommons/dili": 0.9334782608695652,
    "tdcommons/bioavailability-ma": 0.5124709012304622,
    "tdcommons/vdss-lombardo": 0.38567396588981484,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5862341772151898,
    "tdcommons/pgp-broccatelli": 0.8968275126632897,
    "tdcommons/caco2-wang": 0.29095252095175944,
    "tdcommons/herg": 0.8262150220913107,
    "tdcommons/bbb-martins": 0.9006410256410255,
    "tdcommons/ames": 0.819360081458419,
    "tdcommons/ld50-zhu": 0.6360254555651881
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.434783 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.383169 |
|  2 | test       | CLS_RET        | pr_auc      | 0.634144 |
|  3 | test       | CLS_RET        | accuracy    | 0.877358 |
|  4 | test       | CLS_RET        | mcc         | 0.449209 |
|  5 | test       | CLS_RET        | roc_auc     | 0.859881 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  23.4896   |
|  1 | test       | RET            | r2                  |   0.264463 |
|  2 | test       | RET            | pearsonr            |   0.522891 |
|  3 | test       | RET            | mean_squared_error  | 873.38     |
|  4 | test       | RET            | explained_var       |   0.270312 |
|  5 | test       | RET            | spearmanr           |   0.509885 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.473684 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.37365  |
|  2 | test       | CLS_KIT        | pr_auc      | 0.545058 |
|  3 | test       | CLS_KIT        | accuracy    | 0.827586 |
|  4 | test       | CLS_KIT        | mcc         | 0.380427 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.826402 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  21.4643   |
|  1 | test       | KIT            | r2                  |   0.317929 |
|  2 | test       | KIT            | pearsonr            |   0.586819 |
|  3 | test       | KIT            | mean_squared_error  | 823.044    |
|  4 | test       | KIT            | explained_var       |   0.331718 |
|  5 | test       | KIT            | spearmanr           |   0.541143 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  16.6028   |
|  1 | test       | EGFR           | r2                  |   0.45263  |
|  2 | test       | EGFR           | pearsonr            |   0.681174 |
|  3 | test       | EGFR           | mean_squared_error  | 441.053    |
|  4 | test       | EGFR           | explained_var       |   0.456613 |
|  5 | test       | EGFR           | spearmanr           |   0.293664 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.433514 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.305563 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.558805 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.376509 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.30773  |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.458332 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.518943 |
|  1 | test       | LOG_RPPB       | r2                  | 0.470398 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.689538 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.470541 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.472845 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.725217 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.671527 |
|  1 | test       | LOG_HPPB       | r2                  | 0.063881 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.725994 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.56695  |
|  4 | test       | LOG_HPPB       | explained_var       | 0.172776 |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.773474 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.316035 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.628168 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.799974 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.184203 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.63657  |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.787697 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.413386 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.511923 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.720832 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.275541 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.51596  |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.72411  |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.346453 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.500169 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.712452 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.194139 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.505326 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.720948 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.442169 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  7.3194 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.406159 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.643007 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.264418 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.377625 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.570263 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.917826 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.633854 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.498195 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.619236 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.89816 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.388625 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.82813 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.925891 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.836507 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.577055 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6341444049467269,
    "polaris/pkis2-ret-wt-reg-v2": 873.3801296902406,
    "polaris/pkis2-kit-wt-cls-v2": 0.5450581972044334,
    "polaris/pkis2-kit-wt-reg-v2": 823.0444552014746,
    "polaris/pkis2-egfr-wt-reg-v2": 441.0531777809659,
    "polaris/adme-fang-solu-1": 0.5588045332310028,
    "polaris/adme-fang-rppb-1": 0.6895380567784354,
    "polaris/adme-fang-hppb-1": 0.7259939638633426,
    "polaris/adme-fang-perm-1": 0.7999739830513813,
    "polaris/adme-fang-rclint-1": 0.7208319681572363,
    "polaris/adme-fang-hclint-1": 0.7124515391950407,
    "tdcommons/lipophilicity-astrazeneca": 0.4421690295821144,
    "tdcommons/ppbr-az": 7.319401446838925,
    "tdcommons/clearance-hepatocyte-az": 0.4061589142945287,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6430071667169308,
    "tdcommons/half-life-obach": 0.2644182531108877,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3776247354918095,
    "tdcommons/clearance-microsome-az": 0.5702625851378702,
    "tdcommons/dili": 0.9178260869565218,
    "tdcommons/bioavailability-ma": 0.6338543398736283,
    "tdcommons/vdss-lombardo": 0.4981945873345483,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6192359855334539,
    "tdcommons/pgp-broccatelli": 0.898160490535857,
    "tdcommons/caco2-wang": 0.38862487987664196,
    "tdcommons/herg": 0.8281296023564065,
    "tdcommons/bbb-martins": 0.925891181988743,
    "tdcommons/ames": 0.8365074702853001,
    "tdcommons/ld50-zhu": 0.5770553535518207
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.684211 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.616174 |
|  2 | test       | CLS_RET        | pr_auc      | 0.651111 |
|  3 | test       | CLS_RET        | accuracy    | 0.886792 |
|  4 | test       | CLS_RET        | mcc         | 0.62128  |
|  5 | test       | CLS_RET        | roc_auc     | 0.856576 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  21.7808   |
|  1 | test       | RET            | r2                  |   0.345924 |
|  2 | test       | RET            | pearsonr            |   0.601177 |
|  3 | test       | RET            | mean_squared_error  | 776.654    |
|  4 | test       | RET            | explained_var       |   0.361414 |
|  5 | test       | RET            | spearmanr           |   0.534301 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.344828 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.278796 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.620433 |
|  3 | test       | CLS_KIT        | accuracy    | 0.836207 |
|  4 | test       | CLS_KIT        | mcc         | 0.339135 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.845745 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  20.8877   |
|  1 | test       | KIT            | r2                  |   0.335846 |
|  2 | test       | KIT            | pearsonr            |   0.627077 |
|  3 | test       | KIT            | mean_squared_error  | 801.424    |
|  4 | test       | KIT            | explained_var       |   0.390879 |
|  5 | test       | KIT            | spearmanr           |   0.577097 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  17.7579   |
|  1 | test       | EGFR           | r2                  |   0.390196 |
|  2 | test       | EGFR           | pearsonr            |   0.632444 |
|  3 | test       | EGFR           | mean_squared_error  | 491.361    |
|  4 | test       | EGFR           | explained_var       |   0.398596 |
|  5 | test       | EGFR           | spearmanr           |   0.300036 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.406154 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.34457  |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.594087 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.35536  |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.345548 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.507879 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.648495 |
|  1 | test       | LOG_RPPB       | r2                  | 0.194341 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.454542 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.715814 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.205905 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.602609 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.498332 |
|  1 | test       | LOG_HPPB       | r2                  | 0.237395 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.71312  |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.461863 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.296506 |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.705783 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.335709 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.60293  |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.779086 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.196705 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.606479 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.782146 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.411903 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.516771 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.720922 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.272803 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.516801 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.721096 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.330582 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.516626 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.723253 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.187747 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.517087 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.735977 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.437107 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.49115 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.398851 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.495312 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.125418 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.417043 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.578068 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.931304 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.577652 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.47367 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.617315 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.910957 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.332174 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.80486 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.890752 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.844036 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.599177 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6511108499343794,
    "polaris/pkis2-ret-wt-reg-v2": 776.6536579757516,
    "polaris/pkis2-kit-wt-cls-v2": 0.6204334089203766,
    "polaris/pkis2-kit-wt-reg-v2": 801.4241895686089,
    "polaris/pkis2-egfr-wt-reg-v2": 491.3612341870682,
    "polaris/adme-fang-solu-1": 0.594087091226341,
    "polaris/adme-fang-rppb-1": 0.45454224688983796,
    "polaris/adme-fang-hppb-1": 0.7131202077468463,
    "polaris/adme-fang-perm-1": 0.7790858246947887,
    "polaris/adme-fang-rclint-1": 0.7209221361926956,
    "polaris/adme-fang-hclint-1": 0.7232529977592291,
    "tdcommons/lipophilicity-astrazeneca": 0.43710691389583406,
    "tdcommons/ppbr-az": 7.491154134405748,
    "tdcommons/clearance-hepatocyte-az": 0.39885117327347863,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.4953122135236273,
    "tdcommons/half-life-obach": 0.12541799569682058,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4170431254428226,
    "tdcommons/clearance-microsome-az": 0.5780678703839297,
    "tdcommons/dili": 0.9313043478260871,
    "tdcommons/bioavailability-ma": 0.5776521449950116,
    "tdcommons/vdss-lombardo": 0.4736703406355849,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6173146473779385,
    "tdcommons/pgp-broccatelli": 0.9109570781125034,
    "tdcommons/caco2-wang": 0.33217408491485934,
    "tdcommons/herg": 0.8048600883652429,
    "tdcommons/bbb-martins": 0.8907520325203252,
    "tdcommons/ames": 0.844036499637745,
    "tdcommons/ld50-zhu": 0.5991766014886323
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.64     |
|  1 | test       | CLS_RET        | cohen_kappa | 0.598823 |
|  2 | test       | CLS_RET        | pr_auc      | 0.66478  |
|  3 | test       | CLS_RET        | accuracy    | 0.915094 |
|  4 | test       | CLS_RET        | mcc         | 0.653736 |
|  5 | test       | CLS_RET        | roc_auc     | 0.782551 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  23.6618   |
|  1 | test       | RET            | r2                  |   0.234902 |
|  2 | test       | RET            | pearsonr            |   0.499414 |
|  3 | test       | RET            | mean_squared_error  | 908.481    |
|  4 | test       | RET            | explained_var       |   0.247996 |
|  5 | test       | RET            | spearmanr           |   0.500611 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.5      |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.413483 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.622858 |
|  3 | test       | CLS_KIT        | accuracy    | 0.844828 |
|  4 | test       | CLS_KIT        | mcc         | 0.428291 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.830754 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  21.3503   |
|  1 | test       | KIT            | r2                  |   0.307998 |
|  2 | test       | KIT            | pearsonr            |   0.574276 |
|  3 | test       | KIT            | mean_squared_error  | 835.027    |
|  4 | test       | KIT            | explained_var       |   0.321034 |
|  5 | test       | KIT            | spearmanr           |   0.52768  |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  16.357    |
|  1 | test       | EGFR           | r2                  |   0.417725 |
|  2 | test       | EGFR           | pearsonr            |   0.648646 |
|  3 | test       | EGFR           | mean_squared_error  | 469.178    |
|  4 | test       | EGFR           | explained_var       |   0.420627 |
|  5 | test       | EGFR           | spearmanr           |   0.339924 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.37112  |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.402042 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.641829 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.3242   |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.406162 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.536358 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.659397 |
|  1 | test       | LOG_RPPB       | r2                  | 0.156826 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.412516 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.749145 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.170095 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.56     |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.459969 |
|  1 | test       | LOG_HPPB       | r2                  | 0.457578 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.754066 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.328512 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.564178 |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.795172 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.327849 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.619861 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.799488 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.188318 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.63484  |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.789028 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.397206 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.544118 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.744845 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.257365 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.554717 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.752587 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.339161 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.496567 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.717009 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.195538 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.496608 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.726015 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.43454 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.50725 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.39204 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.544189 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.296106 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.441781 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.604697 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.933043 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.434985 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.37388 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.633476 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.904026 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.406955 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.822828 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.911976 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.84649 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.599848 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6647801940462181,
    "polaris/pkis2-ret-wt-reg-v2": 908.4814078187601,
    "polaris/pkis2-kit-wt-cls-v2": 0.622857657307479,
    "polaris/pkis2-kit-wt-reg-v2": 835.027473626124,
    "polaris/pkis2-egfr-wt-reg-v2": 469.1784565858816,
    "polaris/adme-fang-solu-1": 0.6418285888386599,
    "polaris/adme-fang-rppb-1": 0.4125157097610532,
    "polaris/adme-fang-hppb-1": 0.7540662044220251,
    "polaris/adme-fang-perm-1": 0.7994880650642332,
    "polaris/adme-fang-rclint-1": 0.7448452336723327,
    "polaris/adme-fang-hclint-1": 0.7170092297553246,
    "tdcommons/lipophilicity-astrazeneca": 0.4345404066585359,
    "tdcommons/ppbr-az": 7.507251037706843,
    "tdcommons/clearance-hepatocyte-az": 0.39203976151114145,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5441890331159976,
    "tdcommons/half-life-obach": 0.29610627676875106,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4417808548488349,
    "tdcommons/clearance-microsome-az": 0.604696516782091,
    "tdcommons/dili": 0.9330434782608696,
    "tdcommons/bioavailability-ma": 0.43498503491852347,
    "tdcommons/vdss-lombardo": 0.3738796754755943,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6334764918625678,
    "tdcommons/pgp-broccatelli": 0.9040255931751534,
    "tdcommons/caco2-wang": 0.4069549455365192,
    "tdcommons/herg": 0.8228276877761415,
    "tdcommons/bbb-martins": 0.9119762351469668,
    "tdcommons/ames": 0.8464900428831581,
    "tdcommons/ld50-zhu": 0.599848174705557
}
```
