# CheMeleon Flow Results
timestamp: 2026-10-09 09:49:43.251647
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.832452 |
|  1 | test       | CLS_RET        | pr_auc      | 0.563899 |
|  2 | test       | CLS_RET        | mcc         | 0.49296  |
|  3 | test       | CLS_RET        | cohen_kappa | 0.483121 |
|  4 | test       | CLS_RET        | f1          | 0.551724 |
|  5 | test       | CLS_RET        | accuracy    | 0.877358 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.217826 |
|  1 | test       | RET            | explained_var       |   0.246351 |
|  2 | test       | RET            | pearsonr            |   0.520992 |
|  3 | test       | RET            | spearmanr           |   0.48212  |
|  4 | test       | RET            | mean_squared_error  | 928.758    |
|  5 | test       | RET            | mean_absolute_error |  22.6354   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.744681 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.41621  |
|  2 | test       | CLS_KIT        | mcc         | 0.252885 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.24838  |
|  4 | test       | CLS_KIT        | f1          | 0.368421 |
|  5 | test       | CLS_KIT        | accuracy    | 0.793103 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | r2                  |    0.163095 |
|  1 | test       | KIT            | explained_var       |    0.168166 |
|  2 | test       | KIT            | pearsonr            |    0.464737 |
|  3 | test       | KIT            | spearmanr           |    0.448183 |
|  4 | test       | KIT            | mean_squared_error  | 1009.88     |
|  5 | test       | KIT            | mean_absolute_error |   25.6729   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.195465 |
|  1 | test       | EGFR           | explained_var       |   0.195681 |
|  2 | test       | EGFR           | pearsonr            |   0.514567 |
|  3 | test       | EGFR           | spearmanr           |   0.378701 |
|  4 | test       | EGFR           | mean_squared_error  | 648.269    |
|  5 | test       | EGFR           | mean_absolute_error |  20.3179   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.348918 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.349461 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.602029 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.471484 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.353003 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.452728 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.608261 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.609293 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.800211 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.84087  |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.348053 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.43334  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.598535 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.617801 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.786264 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.762167 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.243143 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.365403 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.546812 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.547999 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.744783 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.731815 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.224506 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.366964 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.465703 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.465886 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.692765 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.697899 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.301634 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.437643 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.409383 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.409414 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.663953 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.665234 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.229401 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.382032 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.522532 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.07826 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.403661 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.571308 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.119702 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.326667 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.502284 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.881304 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.633854 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0963583 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.635737 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.889829 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.307458 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.72813 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.862785 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.824304 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.639292 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5638991521609266,
    "polaris/pkis2-ret-wt-reg-v2": 928.7575201464286,
    "polaris/pkis2-kit-wt-cls-v2": 0.4162101058954005,
    "polaris/pkis2-kit-wt-reg-v2": 1009.8802541347503,
    "polaris/pkis2-egfr-wt-reg-v2": 648.2691636167835,
    "polaris/adme-fang-solu-1": 0.6020287099964149,
    "polaris/adme-fang-rppb-1": 0.8002114657258914,
    "polaris/adme-fang-hppb-1": 0.7862644682199024,
    "polaris/adme-fang-perm-1": 0.7447834557394404,
    "polaris/adme-fang-rclint-1": 0.6927646896335309,
    "polaris/adme-fang-hclint-1": 0.6639527518059944,
    "tdcommons/lipophilicity-astrazeneca": 0.5225322443499828,
    "tdcommons/ppbr-az": 9.078263312865827,
    "tdcommons/clearance-hepatocyte-az": 0.4036612957172495,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5713081008877812,
    "tdcommons/half-life-obach": 0.11970233634465995,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.32666727169463206,
    "tdcommons/clearance-microsome-az": 0.5022842407566614,
    "tdcommons/dili": 0.8813043478260869,
    "tdcommons/bioavailability-ma": 0.6338543398736282,
    "tdcommons/vdss-lombardo": 0.09635829462595281,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6357368896925859,
    "tdcommons/pgp-broccatelli": 0.8898293788323115,
    "tdcommons/caco2-wang": 0.3074583825677216,
    "tdcommons/herg": 0.7281296023564064,
    "tdcommons/bbb-martins": 0.862785334584115,
    "tdcommons/ames": 0.8243043725156161,
    "tdcommons/ld50-zhu": 0.6392915306148584
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.832452 |
|  1 | test       | CLS_RET        | pr_auc      | 0.563899 |
|  2 | test       | CLS_RET        | mcc         | 0.49296  |
|  3 | test       | CLS_RET        | cohen_kappa | 0.483121 |
|  4 | test       | CLS_RET        | f1          | 0.551724 |
|  5 | test       | CLS_RET        | accuracy    | 0.877358 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.217826 |
|  1 | test       | RET            | explained_var       |   0.246351 |
|  2 | test       | RET            | pearsonr            |   0.520992 |
|  3 | test       | RET            | spearmanr           |   0.48212  |
|  4 | test       | RET            | mean_squared_error  | 928.757    |
|  5 | test       | RET            | mean_absolute_error |  22.6354   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.744681 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.41621  |
|  2 | test       | CLS_KIT        | mcc         | 0.252885 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.24838  |
|  4 | test       | CLS_KIT        | f1          | 0.368421 |
|  5 | test       | CLS_KIT        | accuracy    | 0.793103 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | r2                  |    0.163094 |
|  1 | test       | KIT            | explained_var       |    0.168166 |
|  2 | test       | KIT            | pearsonr            |    0.464737 |
|  3 | test       | KIT            | spearmanr           |    0.448183 |
|  4 | test       | KIT            | mean_squared_error  | 1009.88     |
|  5 | test       | KIT            | mean_absolute_error |   25.6729   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.195465 |
|  1 | test       | EGFR           | explained_var       |   0.195681 |
|  2 | test       | EGFR           | pearsonr            |   0.514567 |
|  3 | test       | EGFR           | spearmanr           |   0.378701 |
|  4 | test       | EGFR           | mean_squared_error  | 648.269    |
|  5 | test       | EGFR           | mean_absolute_error |  20.3179   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.348918 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.349461 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.602029 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.471484 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.353003 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.452728 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.608261 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.609293 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.800211 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.84087  |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.348053 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.43334  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.598535 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.617801 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.786264 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.762167 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.243143 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.365403 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.546812 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.547999 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.744783 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.731815 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.224506 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.366964 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.465703 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.465886 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.692765 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.697899 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.301634 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.437643 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.409383 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.409414 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.663953 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.665234 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.229401 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.382032 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.522532 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.07826 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.403956 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.571146 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.119702 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.326667 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.502284 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.881304 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.633854 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0963146 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.635737 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.889829 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.307458 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.72813 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.862746 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.824304 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.639292 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5638991521609266,
    "polaris/pkis2-ret-wt-reg-v2": 928.7572868919867,
    "polaris/pkis2-kit-wt-cls-v2": 0.4162101058954005,
    "polaris/pkis2-kit-wt-reg-v2": 1009.8805246180208,
    "polaris/pkis2-egfr-wt-reg-v2": 648.2690176353349,
    "polaris/adme-fang-solu-1": 0.6020287304796316,
    "polaris/adme-fang-rppb-1": 0.8002114638983746,
    "polaris/adme-fang-hppb-1": 0.7862644299298215,
    "polaris/adme-fang-perm-1": 0.7447834351782984,
    "polaris/adme-fang-rclint-1": 0.6927646780081488,
    "polaris/adme-fang-hclint-1": 0.6639527572353019,
    "tdcommons/lipophilicity-astrazeneca": 0.5225322434734251,
    "tdcommons/ppbr-az": 9.078263567697205,
    "tdcommons/clearance-hepatocyte-az": 0.4039557787820022,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5711459810308939,
    "tdcommons/half-life-obach": 0.11970233634465995,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.32666727169463206,
    "tdcommons/clearance-microsome-az": 0.5022842407566614,
    "tdcommons/dili": 0.8813043478260869,
    "tdcommons/bioavailability-ma": 0.6338543398736282,
    "tdcommons/vdss-lombardo": 0.09631462784285404,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6357368896925859,
    "tdcommons/pgp-broccatelli": 0.8898293788323115,
    "tdcommons/caco2-wang": 0.307458352350179,
    "tdcommons/herg": 0.7281296023564064,
    "tdcommons/bbb-martins": 0.8627462476547841,
    "tdcommons/ames": 0.8243043725156161,
    "tdcommons/ld50-zhu": 0.6392915573770818
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.832452 |
|  1 | test       | CLS_RET        | pr_auc      | 0.563899 |
|  2 | test       | CLS_RET        | mcc         | 0.49296  |
|  3 | test       | CLS_RET        | cohen_kappa | 0.483121 |
|  4 | test       | CLS_RET        | f1          | 0.551724 |
|  5 | test       | CLS_RET        | accuracy    | 0.877358 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.217826 |
|  1 | test       | RET            | explained_var       |   0.246351 |
|  2 | test       | RET            | pearsonr            |   0.520991 |
|  3 | test       | RET            | spearmanr           |   0.48212  |
|  4 | test       | RET            | mean_squared_error  | 928.758    |
|  5 | test       | RET            | mean_absolute_error |  22.6354   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.744681 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.41621  |
|  2 | test       | CLS_KIT        | mcc         | 0.252885 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.24838  |
|  4 | test       | CLS_KIT        | f1          | 0.368421 |
|  5 | test       | CLS_KIT        | accuracy    | 0.793103 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | r2                  |    0.163095 |
|  1 | test       | KIT            | explained_var       |    0.168166 |
|  2 | test       | KIT            | pearsonr            |    0.464737 |
|  3 | test       | KIT            | spearmanr           |    0.448183 |
|  4 | test       | KIT            | mean_squared_error  | 1009.88     |
|  5 | test       | KIT            | mean_absolute_error |   25.6729   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.195465 |
|  1 | test       | EGFR           | explained_var       |   0.195681 |
|  2 | test       | EGFR           | pearsonr            |   0.514567 |
|  3 | test       | EGFR           | spearmanr           |   0.378701 |
|  4 | test       | EGFR           | mean_squared_error  | 648.269    |
|  5 | test       | EGFR           | mean_absolute_error |  20.3179   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.348918 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.349461 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.602029 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.471484 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.353003 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.452728 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.608261 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.609293 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.800211 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.84087  |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.348053 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.43334  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.598535 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.617801 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.786264 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.762167 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.243143 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.365403 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.546812 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.547999 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.744783 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.731815 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.224506 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.366964 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.465703 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.465886 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.692765 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.697899 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.301634 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.437643 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.409383 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.409414 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.663953 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.665234 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.229401 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.382032 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.522532 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.07826 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.403921 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.571146 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.119702 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.326667 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.502284 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.881304 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.633854 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0963302 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.635737 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.889829 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.307458 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.72813 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.862746 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.824304 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.639292 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5638991521609266,
    "polaris/pkis2-ret-wt-reg-v2": 928.7576531456124,
    "polaris/pkis2-kit-wt-cls-v2": 0.4162101058954005,
    "polaris/pkis2-kit-wt-reg-v2": 1009.8804544336425,
    "polaris/pkis2-egfr-wt-reg-v2": 648.2689931634245,
    "polaris/adme-fang-solu-1": 0.6020287295969002,
    "polaris/adme-fang-rppb-1": 0.8002114589945739,
    "polaris/adme-fang-hppb-1": 0.7862644732577976,
    "polaris/adme-fang-perm-1": 0.7447834330444127,
    "polaris/adme-fang-rclint-1": 0.692764692847856,
    "polaris/adme-fang-hclint-1": 0.6639527598496067,
    "tdcommons/lipophilicity-astrazeneca": 0.5225322674956187,
    "tdcommons/ppbr-az": 9.078262454201314,
    "tdcommons/clearance-hepatocyte-az": 0.40392133140495545,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5711459810308939,
    "tdcommons/half-life-obach": 0.11970233634465995,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.32666727169463206,
    "tdcommons/clearance-microsome-az": 0.5022842407566614,
    "tdcommons/dili": 0.8813043478260869,
    "tdcommons/bioavailability-ma": 0.6338543398736282,
    "tdcommons/vdss-lombardo": 0.09633022312253217,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6357368896925859,
    "tdcommons/pgp-broccatelli": 0.8898293788323115,
    "tdcommons/caco2-wang": 0.3074583595298104,
    "tdcommons/herg": 0.7281296023564064,
    "tdcommons/bbb-martins": 0.8627462476547841,
    "tdcommons/ames": 0.8243043725156161,
    "tdcommons/ld50-zhu": 0.6392915633581358
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.832452 |
|  1 | test       | CLS_RET        | pr_auc      | 0.563899 |
|  2 | test       | CLS_RET        | mcc         | 0.49296  |
|  3 | test       | CLS_RET        | cohen_kappa | 0.483121 |
|  4 | test       | CLS_RET        | f1          | 0.551724 |
|  5 | test       | CLS_RET        | accuracy    | 0.877358 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.217826 |
|  1 | test       | RET            | explained_var       |   0.246351 |
|  2 | test       | RET            | pearsonr            |   0.520992 |
|  3 | test       | RET            | spearmanr           |   0.48212  |
|  4 | test       | RET            | mean_squared_error  | 928.758    |
|  5 | test       | RET            | mean_absolute_error |  22.6354   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.744681 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.41621  |
|  2 | test       | CLS_KIT        | mcc         | 0.252885 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.24838  |
|  4 | test       | CLS_KIT        | f1          | 0.368421 |
|  5 | test       | CLS_KIT        | accuracy    | 0.793103 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | r2                  |    0.163095 |
|  1 | test       | KIT            | explained_var       |    0.168166 |
|  2 | test       | KIT            | pearsonr            |    0.464737 |
|  3 | test       | KIT            | spearmanr           |    0.448183 |
|  4 | test       | KIT            | mean_squared_error  | 1009.88     |
|  5 | test       | KIT            | mean_absolute_error |   25.6729   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.195465 |
|  1 | test       | EGFR           | explained_var       |   0.195681 |
|  2 | test       | EGFR           | pearsonr            |   0.514567 |
|  3 | test       | EGFR           | spearmanr           |   0.378701 |
|  4 | test       | EGFR           | mean_squared_error  | 648.269    |
|  5 | test       | EGFR           | mean_absolute_error |  20.3179   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.348918 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.349461 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.602029 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.471484 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.353003 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.452728 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.608261 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.609293 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.800211 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.84087  |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.348053 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.43334  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.598535 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.617801 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.786264 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.762167 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.243143 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.365403 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.546812 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.547999 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.744783 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.731815 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.224506 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.366964 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.465703 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.465886 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.692765 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.697899 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.301634 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.437643 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.409383 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.409414 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.663953 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.665234 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.229401 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.382032 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.522532 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.07826 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.404328 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.571146 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.119851 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.326667 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.502284 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.881304 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.633854 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0963391 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.635737 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.889829 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.307458 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.72813 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.862785 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.824304 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.639292 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5638991521609266,
    "polaris/pkis2-ret-wt-reg-v2": 928.7575379479458,
    "polaris/pkis2-kit-wt-cls-v2": 0.4162101058954005,
    "polaris/pkis2-kit-wt-reg-v2": 1009.8804003021944,
    "polaris/pkis2-egfr-wt-reg-v2": 648.2691256381954,
    "polaris/adme-fang-solu-1": 0.6020287502814798,
    "polaris/adme-fang-rppb-1": 0.8002114289322183,
    "polaris/adme-fang-hppb-1": 0.7862644491492623,
    "polaris/adme-fang-perm-1": 0.7447834301463054,
    "polaris/adme-fang-rclint-1": 0.6927647061534082,
    "polaris/adme-fang-hclint-1": 0.6639527555430554,
    "tdcommons/lipophilicity-astrazeneca": 0.5225322627106384,
    "tdcommons/ppbr-az": 9.078261837323364,
    "tdcommons/clearance-hepatocyte-az": 0.40432797849009167,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5711459810308939,
    "tdcommons/half-life-obach": 0.11985111973641215,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.32666727169463206,
    "tdcommons/clearance-microsome-az": 0.5022842407566614,
    "tdcommons/dili": 0.8813043478260869,
    "tdcommons/bioavailability-ma": 0.6338543398736282,
    "tdcommons/vdss-lombardo": 0.09633906044768312,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6357368896925859,
    "tdcommons/pgp-broccatelli": 0.8898293788323115,
    "tdcommons/caco2-wang": 0.30745834876163847,
    "tdcommons/herg": 0.7281296023564064,
    "tdcommons/bbb-martins": 0.862785334584115,
    "tdcommons/ames": 0.8243043725156161,
    "tdcommons/ld50-zhu": 0.6392915672084981
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.832452 |
|  1 | test       | CLS_RET        | pr_auc      | 0.563899 |
|  2 | test       | CLS_RET        | mcc         | 0.49296  |
|  3 | test       | CLS_RET        | cohen_kappa | 0.483121 |
|  4 | test       | CLS_RET        | f1          | 0.551724 |
|  5 | test       | CLS_RET        | accuracy    | 0.877358 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.217826 |
|  1 | test       | RET            | explained_var       |   0.246351 |
|  2 | test       | RET            | pearsonr            |   0.520991 |
|  3 | test       | RET            | spearmanr           |   0.48212  |
|  4 | test       | RET            | mean_squared_error  | 928.758    |
|  5 | test       | RET            | mean_absolute_error |  22.6354   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.744681 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.41621  |
|  2 | test       | CLS_KIT        | mcc         | 0.252885 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.24838  |
|  4 | test       | CLS_KIT        | f1          | 0.368421 |
|  5 | test       | CLS_KIT        | accuracy    | 0.793103 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | r2                  |    0.163095 |
|  1 | test       | KIT            | explained_var       |    0.168166 |
|  2 | test       | KIT            | pearsonr            |    0.464737 |
|  3 | test       | KIT            | spearmanr           |    0.448183 |
|  4 | test       | KIT            | mean_squared_error  | 1009.88     |
|  5 | test       | KIT            | mean_absolute_error |   25.6729   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.195465 |
|  1 | test       | EGFR           | explained_var       |   0.195681 |
|  2 | test       | EGFR           | pearsonr            |   0.514567 |
|  3 | test       | EGFR           | spearmanr           |   0.378701 |
|  4 | test       | EGFR           | mean_squared_error  | 648.269    |
|  5 | test       | EGFR           | mean_absolute_error |  20.3179   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.348918 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.349461 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.602029 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.471484 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.353003 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.452728 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.608261 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.609293 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.800211 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.84087  |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.348053 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.43334  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.598535 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.617801 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.786264 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.762167 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.243143 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.365403 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.546812 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.547999 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.744783 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.731815 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.224506 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.366964 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.465703 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.465886 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.692765 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.697899 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.301634 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.437643 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.409383 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.409414 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.663953 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.665234 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.229401 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.382032 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.522532 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.07826 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.403441 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.571308 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.119851 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.326667 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.502284 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.881304 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.633854 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0963515 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.635737 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.889829 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.307458 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.728424 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.862785 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.824304 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.639292 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5638991521609266,
    "polaris/pkis2-ret-wt-reg-v2": 928.7578233652077,
    "polaris/pkis2-kit-wt-cls-v2": 0.4162101058954005,
    "polaris/pkis2-kit-wt-reg-v2": 1009.8804057653011,
    "polaris/pkis2-egfr-wt-reg-v2": 648.2691161149578,
    "polaris/adme-fang-solu-1": 0.6020287142811476,
    "polaris/adme-fang-rppb-1": 0.8002114300468101,
    "polaris/adme-fang-hppb-1": 0.7862644746812851,
    "polaris/adme-fang-perm-1": 0.7447834462179719,
    "polaris/adme-fang-rclint-1": 0.6927647005886697,
    "polaris/adme-fang-hclint-1": 0.663952747071277,
    "tdcommons/lipophilicity-astrazeneca": 0.5225322538852785,
    "tdcommons/ppbr-az": 9.078264211182406,
    "tdcommons/clearance-hepatocyte-az": 0.403441168576122,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5713081008877812,
    "tdcommons/half-life-obach": 0.11985111973641215,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.32666727169463206,
    "tdcommons/clearance-microsome-az": 0.5022842407566614,
    "tdcommons/dili": 0.8813043478260869,
    "tdcommons/bioavailability-ma": 0.6338543398736282,
    "tdcommons/vdss-lombardo": 0.09635153667142562,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6357368896925859,
    "tdcommons/pgp-broccatelli": 0.8898293788323115,
    "tdcommons/caco2-wang": 0.3074583468358794,
    "tdcommons/herg": 0.7284241531664212,
    "tdcommons/bbb-martins": 0.862785334584115,
    "tdcommons/ames": 0.8243043725156161,
    "tdcommons/ld50-zhu": 0.6392915423603767
}
```
