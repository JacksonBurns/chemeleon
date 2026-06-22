# chemeleon2_preview_initial_training_e4s281344 Baseline Results
timestamp: 2026-06-22 11:14:14.455359
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.915094 |
|  1 | test       | CLS_RET        | pr_auc      | 0.68769  |
|  2 | test       | CLS_RET        | roc_auc     | 0.879709 |
|  3 | test       | CLS_RET        | f1          | 0.727273 |
|  4 | test       | CLS_RET        | mcc         | 0.677484 |
|  5 | test       | CLS_RET        | cohen_kappa | 0.677048 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 828.098    |
|  1 | test       | RET            | pearsonr            |   0.564655 |
|  2 | test       | RET            | explained_var       |   0.318027 |
|  3 | test       | RET            | r2                  |   0.302599 |
|  4 | test       | RET            | spearmanr           |   0.566159 |
|  5 | test       | RET            | mean_absolute_error |  21.6568   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.87069  |
|  1 | test       | CLS_KIT        | pr_auc      | 0.671738 |
|  2 | test       | CLS_KIT        | roc_auc     | 0.850097 |
|  3 | test       | CLS_KIT        | f1          | 0.680851 |
|  4 | test       | CLS_KIT        | mcc         | 0.602112 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.600184 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_squared_error  | 851.047    |
|  1 | test       | KIT            | pearsonr            |   0.609299 |
|  2 | test       | KIT            | explained_var       |   0.316429 |
|  3 | test       | KIT            | r2                  |   0.294723 |
|  4 | test       | KIT            | spearmanr           |   0.528626 |
|  5 | test       | KIT            | mean_absolute_error |  21.496    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 419.652    |
|  1 | test       | EGFR           | pearsonr            |   0.699389 |
|  2 | test       | EGFR           | explained_var       |   0.488119 |
|  3 | test       | EGFR           | r2                  |   0.47919  |
|  4 | test       | EGFR           | spearmanr           |   0.442251 |
|  5 | test       | EGFR           | mean_absolute_error |  15.4514   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.321042 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.657976 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.432826 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.407867 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.543402 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.36014  |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.487541 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.712748 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.498282 |
|  3 | test       | LOG_RPPB       | r2                  | 0.451265 |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.783478 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.530891 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.290396 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.736561 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.534219 |
|  3 | test       | LOG_HPPB       | r2                  | 0.520513 |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.692337 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.440704 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.161874 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.822034 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.674567 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.673241 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.798753 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.287354 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.253084 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.746239 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.552434 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.551701 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.744051 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.389463 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.189853 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.728374 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.511773 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.511204 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.728476 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.323765 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.442452 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.24619 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.433981 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.671753 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0974029 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.376866 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.59891 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.923913 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.660126 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.637279 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.609968 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.938616 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.309696 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.854639 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.911058 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.837101 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.547704 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6876902251925017,
    "polaris/pkis2-ret-wt-reg-v2": 828.0976398844268,
    "polaris/pkis2-kit-wt-cls-v2": 0.6717381987127597,
    "polaris/pkis2-kit-wt-reg-v2": 851.0467158065444,
    "polaris/pkis2-egfr-wt-reg-v2": 419.65242454887897,
    "polaris/adme-fang-solu-1": 0.6579762654340681,
    "polaris/adme-fang-rppb-1": 0.7127475440240764,
    "polaris/adme-fang-hppb-1": 0.7365610531335255,
    "polaris/adme-fang-perm-1": 0.8220344177787814,
    "polaris/adme-fang-rclint-1": 0.7462392382705036,
    "polaris/adme-fang-hclint-1": 0.7283744261083543,
    "tdcommons/lipophilicity-astrazeneca": 0.44245222486200786,
    "tdcommons/ppbr-az": 8.246193907162796,
    "tdcommons/clearance-hepatocyte-az": 0.4339807095016552,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6717525407669754,
    "tdcommons/half-life-obach": 0.09740288307493475,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3768660196434197,
    "tdcommons/clearance-microsome-az": 0.5989099261480394,
    "tdcommons/dili": 0.923913043478261,
    "tdcommons/bioavailability-ma": 0.6601263717991354,
    "tdcommons/vdss-lombardo": 0.6372786565195037,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6099683544303797,
    "tdcommons/pgp-broccatelli": 0.938616368968275,
    "tdcommons/caco2-wang": 0.3096958032965022,
    "tdcommons/herg": 0.8546391752577319,
    "tdcommons/bbb-martins": 0.9110576923076923,
    "tdcommons/ames": 0.837100785212164,
    "tdcommons/ld50-zhu": 0.5477043705393079
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.839623 |
|  1 | test       | CLS_RET        | pr_auc      | 0.656832 |
|  2 | test       | CLS_RET        | roc_auc     | 0.874422 |
|  3 | test       | CLS_RET        | f1          | 0        |
|  4 | test       | CLS_RET        | mcc         | 0        |
|  5 | test       | CLS_RET        | cohen_kappa | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 809.913    |
|  1 | test       | RET            | pearsonr            |   0.565841 |
|  2 | test       | RET            | explained_var       |   0.320176 |
|  3 | test       | RET            | r2                  |   0.317913 |
|  4 | test       | RET            | spearmanr           |   0.559695 |
|  5 | test       | RET            | mean_absolute_error |  22.5004   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.87069  |
|  1 | test       | CLS_KIT        | pr_auc      | 0.696883 |
|  2 | test       | CLS_KIT        | roc_auc     | 0.838491 |
|  3 | test       | CLS_KIT        | f1          | 0.651163 |
|  4 | test       | CLS_KIT        | mcc         | 0.572083 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.57185  |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_squared_error  | 892.448    |
|  1 | test       | KIT            | pearsonr            |   0.582959 |
|  2 | test       | KIT            | explained_var       |   0.274878 |
|  3 | test       | KIT            | r2                  |   0.260413 |
|  4 | test       | KIT            | spearmanr           |   0.529531 |
|  5 | test       | KIT            | mean_absolute_error |  22.6732   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 479.577    |
|  1 | test       | EGFR           | pearsonr            |   0.636775 |
|  2 | test       | EGFR           | explained_var       |   0.405473 |
|  3 | test       | EGFR           | r2                  |   0.40482  |
|  4 | test       | EGFR           | spearmanr           |   0.305774 |
|  5 | test       | EGFR           | mean_absolute_error |  17.2717   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.313433 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.653228 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.42214  |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.421901 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.561054 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.375337 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.325135 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.835429 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.654088 |
|  3 | test       | LOG_RPPB       | r2                  | 0.634056 |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.837391 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.473949 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.287193 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.755618 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.570321 |
|  3 | test       | LOG_HPPB       | r2                  | 0.525802 |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.746887 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.434546 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.162628 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.823864 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.677365 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.67172  |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.800699 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.283348 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.240565 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.760322 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.576202 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.573877 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.755122 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.381714 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.206833 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.706506 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.46752  |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.467489 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.704251 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.346552 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.433354 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.81379 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.392346 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.631355 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.355602 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.374546 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.582527 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.90913 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.33289 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.56505 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.604995 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.931552 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.351268 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.851252 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.913325 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.83983 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  0.5671 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6568322051481444,
    "polaris/pkis2-ret-wt-reg-v2": 809.9133217853125,
    "polaris/pkis2-kit-wt-cls-v2": 0.696882674663176,
    "polaris/pkis2-kit-wt-reg-v2": 892.4481977244084,
    "polaris/pkis2-egfr-wt-reg-v2": 479.5772152335851,
    "polaris/adme-fang-solu-1": 0.6532275271467134,
    "polaris/adme-fang-rppb-1": 0.8354294306428125,
    "polaris/adme-fang-hppb-1": 0.7556177008848377,
    "polaris/adme-fang-perm-1": 0.8238639114161371,
    "polaris/adme-fang-rclint-1": 0.7603221489118369,
    "polaris/adme-fang-hclint-1": 0.7065061856625839,
    "tdcommons/lipophilicity-astrazeneca": 0.433353619149753,
    "tdcommons/ppbr-az": 8.81379072841037,
    "tdcommons/clearance-hepatocyte-az": 0.3923463490622588,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6313548945049835,
    "tdcommons/half-life-obach": 0.3556024148660574,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3745457020854334,
    "tdcommons/clearance-microsome-az": 0.5825269594959834,
    "tdcommons/dili": 0.9091304347826087,
    "tdcommons/bioavailability-ma": 0.3328899235118058,
    "tdcommons/vdss-lombardo": 0.565049506695148,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6049954792043399,
    "tdcommons/pgp-broccatelli": 0.9315515862436684,
    "tdcommons/caco2-wang": 0.35126826060412064,
    "tdcommons/herg": 0.8512518409425626,
    "tdcommons/bbb-martins": 0.9133247342088804,
    "tdcommons/ames": 0.8398304255027512,
    "tdcommons/ld50-zhu": 0.5670995536340913
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.915094 |
|  1 | test       | CLS_RET        | pr_auc      | 0.670723 |
|  2 | test       | CLS_RET        | roc_auc     | 0.877065 |
|  3 | test       | CLS_RET        | f1          | 0.742857 |
|  4 | test       | CLS_RET        | mcc         | 0.692465 |
|  5 | test       | CLS_RET        | cohen_kappa | 0.692059 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 825.407    |
|  1 | test       | RET            | pearsonr            |   0.585026 |
|  2 | test       | RET            | explained_var       |   0.339311 |
|  3 | test       | RET            | r2                  |   0.304865 |
|  4 | test       | RET            | spearmanr           |   0.537794 |
|  5 | test       | RET            | mean_absolute_error |  20.744    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.844828 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.727935 |
|  2 | test       | CLS_KIT        | roc_auc     | 0.852515 |
|  3 | test       | CLS_KIT        | f1          | 0.625    |
|  4 | test       | CLS_KIT        | mcc         | 0.530957 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.528029 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_squared_error  | 839.668    |
|  1 | test       | KIT            | pearsonr            |   0.587863 |
|  2 | test       | KIT            | explained_var       |   0.321047 |
|  3 | test       | KIT            | r2                  |   0.304152 |
|  4 | test       | KIT            | spearmanr           |   0.537553 |
|  5 | test       | KIT            | mean_absolute_error |  22.4746   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 356.869    |
|  1 | test       | EGFR           | pearsonr            |   0.757013 |
|  2 | test       | EGFR           | explained_var       |   0.56336  |
|  3 | test       | EGFR           | r2                  |   0.557108 |
|  4 | test       | EGFR           | spearmanr           |   0.508531 |
|  5 | test       | EGFR           | mean_absolute_error |  14.4128   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.34515  |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.615246 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.377031 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.363401 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.540176 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.382446 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.337206 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.812719 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.621813 |
|  3 | test       | LOG_RPPB       | r2                  | 0.62047  |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.88     |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.402747 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.531985 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.675345 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.220827 |
|  3 | test       | LOG_HPPB       | r2                  | 0.121613 |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.721675 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.662992 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.166665 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.816258 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.663716 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.66357  |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.813018 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.285501 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.263806 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.735666 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.540318 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.53271  |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.730184 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.40809  |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.204495 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.714862 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.474446 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.473507 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.712425 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.3353   |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.451332 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.73816 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.317259 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.667088 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.217827 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.365376 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.579019 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.902174 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.536748 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.61507 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.617315 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.916289 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.281996 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.859205 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.90197 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.851591 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.591311 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6707226771894039,
    "polaris/pkis2-ret-wt-reg-v2": 825.4069507992627,
    "polaris/pkis2-kit-wt-cls-v2": 0.7279353443247014,
    "polaris/pkis2-kit-wt-reg-v2": 839.6684426525679,
    "polaris/pkis2-egfr-wt-reg-v2": 356.8685395893995,
    "polaris/adme-fang-solu-1": 0.6152461986329414,
    "polaris/adme-fang-rppb-1": 0.8127185398584235,
    "polaris/adme-fang-hppb-1": 0.67534496333695,
    "polaris/adme-fang-perm-1": 0.8162578197972346,
    "polaris/adme-fang-rclint-1": 0.7356655329383878,
    "polaris/adme-fang-hclint-1": 0.7148618631472903,
    "tdcommons/lipophilicity-astrazeneca": 0.45133172033514296,
    "tdcommons/ppbr-az": 7.738161164421943,
    "tdcommons/clearance-hepatocyte-az": 0.3172585163786266,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6670881672023357,
    "tdcommons/half-life-obach": 0.21782689103944547,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3653760171409596,
    "tdcommons/clearance-microsome-az": 0.5790194532941972,
    "tdcommons/dili": 0.9021739130434783,
    "tdcommons/bioavailability-ma": 0.5367475889590954,
    "tdcommons/vdss-lombardo": 0.6150697729444011,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6173146473779386,
    "tdcommons/pgp-broccatelli": 0.9162889896027726,
    "tdcommons/caco2-wang": 0.2819963118796549,
    "tdcommons/herg": 0.8592047128129602,
    "tdcommons/bbb-martins": 0.901969981238274,
    "tdcommons/ames": 0.8515909847461277,
    "tdcommons/ld50-zhu": 0.5913108303137175
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.896226 |
|  1 | test       | CLS_RET        | pr_auc      | 0.648374 |
|  2 | test       | CLS_RET        | roc_auc     | 0.883014 |
|  3 | test       | CLS_RET        | f1          | 0.592593 |
|  4 | test       | CLS_RET        | mcc         | 0.562567 |
|  5 | test       | CLS_RET        | cohen_kappa | 0.537669 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 775.896    |
|  1 | test       | RET            | pearsonr            |   0.616875 |
|  2 | test       | RET            | explained_var       |   0.368673 |
|  3 | test       | RET            | r2                  |   0.346562 |
|  4 | test       | RET            | spearmanr           |   0.508797 |
|  5 | test       | RET            | mean_absolute_error |  20.7492   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.698665 |
|  2 | test       | CLS_KIT        | roc_auc     | 0.844294 |
|  3 | test       | CLS_KIT        | f1          | 0.604651 |
|  4 | test       | CLS_KIT        | mcc         | 0.514974 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.514764 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_squared_error  | 904.526    |
|  1 | test       | KIT            | pearsonr            |   0.58016  |
|  2 | test       | KIT            | explained_var       |   0.280196 |
|  3 | test       | KIT            | r2                  |   0.250404 |
|  4 | test       | KIT            | spearmanr           |   0.535987 |
|  5 | test       | KIT            | mean_absolute_error |  22.153    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 396.841    |
|  1 | test       | EGFR           | pearsonr            |   0.716861 |
|  2 | test       | EGFR           | explained_var       |   0.507854 |
|  3 | test       | EGFR           | r2                  |   0.5075   |
|  4 | test       | EGFR           | spearmanr           |   0.437007 |
|  5 | test       | EGFR           | mean_absolute_error |  15.2323   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.337841 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.625775 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.390815 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.376883 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.544856 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.370586 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.498531 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.738491 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.480427 |
|  3 | test       | LOG_RPPB       | r2                  | 0.438896 |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.827826 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.578611 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.317436 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.731234 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.529561 |
|  3 | test       | LOG_HPPB       | r2                  | 0.475866 |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.720147 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.479623 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.170068 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.812842 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.656806 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.656701 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.800273 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.306327 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.26076  |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.736427 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.539978 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.538105 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.733982 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.402351 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.188584 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.721691 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.51512  |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.514472 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.720133 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.335846 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.450511 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.56863 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.35176 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.64233 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.47557 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.366121 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.600267 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.910435 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.644164 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.629959 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.637319 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.942215 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.306035 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.847275 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.931696 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.840616 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.559736 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6483744140963109,
    "polaris/pkis2-ret-wt-reg-v2": 775.8956625121236,
    "polaris/pkis2-kit-wt-cls-v2": 0.6986649200958017,
    "polaris/pkis2-kit-wt-reg-v2": 904.5259919176625,
    "polaris/pkis2-egfr-wt-reg-v2": 396.84113485050204,
    "polaris/adme-fang-solu-1": 0.6257745720743472,
    "polaris/adme-fang-rppb-1": 0.7384905709737297,
    "polaris/adme-fang-hppb-1": 0.7312337231741671,
    "polaris/adme-fang-perm-1": 0.8128424474022389,
    "polaris/adme-fang-rclint-1": 0.7364267401737662,
    "polaris/adme-fang-hclint-1": 0.7216909960976128,
    "tdcommons/lipophilicity-astrazeneca": 0.4505109481754757,
    "tdcommons/ppbr-az": 7.568626900879343,
    "tdcommons/clearance-hepatocyte-az": 0.3517598642438813,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6423298769971577,
    "tdcommons/half-life-obach": 0.4755703174796808,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.366120647264802,
    "tdcommons/clearance-microsome-az": 0.6002668545954737,
    "tdcommons/dili": 0.9104347826086956,
    "tdcommons/bioavailability-ma": 0.6441636182241437,
    "tdcommons/vdss-lombardo": 0.6299587501788071,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6373191681735986,
    "tdcommons/pgp-broccatelli": 0.9422154092242069,
    "tdcommons/caco2-wang": 0.3060348419580481,
    "tdcommons/herg": 0.8472754050073638,
    "tdcommons/bbb-martins": 0.9316955909943715,
    "tdcommons/ames": 0.8406156376666862,
    "tdcommons/ld50-zhu": 0.5597355528245599
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.867925 |
|  1 | test       | CLS_RET        | pr_auc      | 0.549127 |
|  2 | test       | CLS_RET        | roc_auc     | 0.829478 |
|  3 | test       | CLS_RET        | f1          | 0.416667 |
|  4 | test       | CLS_RET        | mcc         | 0.40138  |
|  5 | test       | CLS_RET        | cohen_kappa | 0.356461 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 778.374    |
|  1 | test       | RET            | pearsonr            |   0.601765 |
|  2 | test       | RET            | explained_var       |   0.359594 |
|  3 | test       | RET            | r2                  |   0.344475 |
|  4 | test       | RET            | spearmanr           |   0.576477 |
|  5 | test       | RET            | mean_absolute_error |  21.1476   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.818966 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.650701 |
|  2 | test       | CLS_KIT        | roc_auc     | 0.841876 |
|  3 | test       | CLS_KIT        | f1          | 0.222222 |
|  4 | test       | CLS_KIT        | mcc         | 0.222155 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.163462 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_squared_error  | 920.13     |
|  1 | test       | KIT            | pearsonr            |   0.556678 |
|  2 | test       | KIT            | explained_var       |   0.25211  |
|  3 | test       | KIT            | r2                  |   0.237473 |
|  4 | test       | KIT            | spearmanr           |   0.489156 |
|  5 | test       | KIT            | mean_absolute_error |  22.7011   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 442.618    |
|  1 | test       | EGFR           | pearsonr            |   0.689526 |
|  2 | test       | EGFR           | explained_var       |   0.461238 |
|  3 | test       | EGFR           | r2                  |   0.450688 |
|  4 | test       | EGFR           | spearmanr           |   0.40682  |
|  5 | test       | EGFR           | mean_absolute_error |  15.9375   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.325095 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.635117 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.401495 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.400391 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.54482  |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.386162 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.306355 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.836752 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.664964 |
|  3 | test       | LOG_RPPB       | r2                  | 0.655193 |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.826957 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.434198 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.422048 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.754678 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.569439 |
|  3 | test       | LOG_HPPB       | r2                  | 0.303136 |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.729773 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.536556 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.173748 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.807348 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.649289 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.649273 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.800225 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.2992   |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.253899 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.748795 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.557472 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.550257 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.747251 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.391749 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.204576 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.712854 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.476295 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.473298 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.711617 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.340523 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.435727 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.15712 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.372198 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.656807 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.414406 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.377332 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.594882 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.915652 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.583306 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.589558 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.661279 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.938216 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.339605 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.835935 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.900446 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.851951 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.548691 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5491265076367282,
    "polaris/pkis2-ret-wt-reg-v2": 778.3738999412171,
    "polaris/pkis2-kit-wt-cls-v2": 0.6507010651958798,
    "polaris/pkis2-kit-wt-reg-v2": 920.1295920816822,
    "polaris/pkis2-egfr-wt-reg-v2": 442.61824593760167,
    "polaris/adme-fang-solu-1": 0.6351167605882269,
    "polaris/adme-fang-rppb-1": 0.8367521680190751,
    "polaris/adme-fang-hppb-1": 0.7546779004558716,
    "polaris/adme-fang-perm-1": 0.8073479864794535,
    "polaris/adme-fang-rclint-1": 0.7487951931505722,
    "polaris/adme-fang-hclint-1": 0.7128539310449163,
    "tdcommons/lipophilicity-astrazeneca": 0.43572702702454164,
    "tdcommons/ppbr-az": 8.157122262807993,
    "tdcommons/clearance-hepatocyte-az": 0.3721975138334974,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6568069420913988,
    "tdcommons/half-life-obach": 0.4144058582058664,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3773324145563277,
    "tdcommons/clearance-microsome-az": 0.5948823637238254,
    "tdcommons/dili": 0.9156521739130435,
    "tdcommons/bioavailability-ma": 0.5833056202194878,
    "tdcommons/vdss-lombardo": 0.589558281212935,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6612793851717902,
    "tdcommons/pgp-broccatelli": 0.938216475606505,
    "tdcommons/caco2-wang": 0.3396046024594151,
    "tdcommons/herg": 0.8359351988217967,
    "tdcommons/bbb-martins": 0.9004455909943715,
    "tdcommons/ames": 0.8519512815994046,
    "tdcommons/ld50-zhu": 0.5486912873504287
}
```
