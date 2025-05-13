# Random Forest Baseline Results
timestamp: 2025-04-28 15:49:28.360997
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.686581 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.480816 |
|  2 | test       | CLS_RET        | mcc         | 0.512494 |
|  3 | test       | CLS_RET        | f1          | 0.538462 |
|  4 | test       | CLS_RET        | roc_auc     | 0.942168 |
|  5 | test       | CLS_RET        | accuracy    | 0.886792 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.458857 |
|  1 | test       | RET            | mean_absolute_error |  18.9349   |
|  2 | test       | RET            | r2                  |   0.423043 |
|  3 | test       | RET            | spearmanr           |   0.634811 |
|  4 | test       | RET            | pearsonr            |   0.678593 |
|  5 | test       | RET            | mean_squared_error  | 685.082    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.618431 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.31125  |
|  2 | test       | CLS_KIT        | mcc         | 0.352891 |
|  3 | test       | CLS_KIT        | f1          | 0.387097 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.833414 |
|  5 | test       | CLS_KIT        | accuracy    | 0.836207 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.269877 |
|  1 | test       | KIT            | mean_absolute_error |  23.2162   |
|  2 | test       | KIT            | r2                  |   0.240105 |
|  3 | test       | KIT            | spearmanr           |   0.506529 |
|  4 | test       | KIT            | pearsonr            |   0.547364 |
|  5 | test       | KIT            | mean_squared_error  | 916.954    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.441583 |
|  1 | test       | EGFR           | mean_absolute_error |  16.0041   |
|  2 | test       | EGFR           | r2                  |   0.441281 |
|  3 | test       | EGFR           | spearmanr           |   0.453799 |
|  4 | test       | EGFR           | pearsonr            |   0.664532 |
|  5 | test       | EGFR           | mean_squared_error  | 450.198    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.272359 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.443587 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.266971 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.440267 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.541329 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.397433 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.220863 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.661256 |
|  2 | test       | LOG_RPPB       | r2                  | 0.217871 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.70087  |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.632976 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.694908 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.327601 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.552277 |
|  2 | test       | LOG_HPPB       | r2                  | 0.297465 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.591947 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.587569 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.425482 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.43402  |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.41659  |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.428978 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.654774 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.681763 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.28288  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.293591 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.518901 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.29348  |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.54485  |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.544521 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.398861 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.246019 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.446032 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.234688 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.494974 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.496213 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.297255 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.722673 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.88811 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.277262 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.666288 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.292146 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.367514 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.425684 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.883478 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.662122 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.516587 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.661166 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.921288 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.404402 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.791016 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.860831 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.839694 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.632347 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6865807217789315,
    "polaris/pkis2-ret-wt-reg-v2": 685.08223375891,
    "polaris/pkis2-kit-wt-cls-v2": 0.618430670580088,
    "polaris/pkis2-kit-wt-reg-v2": 916.9535612260539,
    "polaris/pkis2-egfr-wt-reg-v2": 450.19825428858013,
    "polaris/adme-fang-solu-1": 0.5413291082203111,
    "polaris/adme-fang-rppb-1": 0.6329759851222143,
    "polaris/adme-fang-hppb-1": 0.5875692214302443,
    "polaris/adme-fang-perm-1": 0.681762568329249,
    "polaris/adme-fang-rclint-1": 0.5445207961384646,
    "polaris/adme-fang-hclint-1": 0.4962132904658961,
    "tdcommons/lipophilicity-astrazeneca": 0.7226734750566893,
    "tdcommons/ppbr-az": 9.88811203905344,
    "tdcommons/clearance-hepatocyte-az": 0.27726193982500863,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6662877159722462,
    "tdcommons/half-life-obach": 0.2921455897498776,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3675142933589661,
    "tdcommons/clearance-microsome-az": 0.42568405794054537,
    "tdcommons/dili": 0.8834782608695652,
    "tdcommons/bioavailability-ma": 0.6621217159960092,
    "tdcommons/vdss-lombardo": 0.5165871585045967,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6611663652802894,
    "tdcommons/pgp-broccatelli": 0.9212876566249001,
    "tdcommons/caco2-wang": 0.40440190137052606,
    "tdcommons/herg": 0.7910162002945508,
    "tdcommons/bbb-martins": 0.8608309881175735,
    "tdcommons/ames": 0.8396943351152362,
    "tdcommons/ld50-zhu": 0.6323473486318598
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.667876 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.420521 |
|  2 | test       | CLS_RET        | mcc         | 0.459084 |
|  3 | test       | CLS_RET        | f1          | 0.48     |
|  4 | test       | CLS_RET        | roc_auc     | 0.938533 |
|  5 | test       | CLS_RET        | accuracy    | 0.877358 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.462033 |
|  1 | test       | RET            | mean_absolute_error |  18.6015   |
|  2 | test       | RET            | r2                  |   0.423375 |
|  3 | test       | RET            | spearmanr           |   0.623892 |
|  4 | test       | RET            | pearsonr            |   0.679891 |
|  5 | test       | RET            | mean_squared_error  | 684.687    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.584706 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.31125  |
|  2 | test       | CLS_KIT        | mcc         | 0.352891 |
|  3 | test       | CLS_KIT        | f1          | 0.387097 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.816006 |
|  5 | test       | CLS_KIT        | accuracy    | 0.836207 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.289214 |
|  1 | test       | KIT            | mean_absolute_error |  23.0032   |
|  2 | test       | KIT            | r2                  |   0.25865  |
|  3 | test       | KIT            | spearmanr           |   0.548138 |
|  4 | test       | KIT            | pearsonr            |   0.561126 |
|  5 | test       | KIT            | mean_squared_error  | 894.576    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.4149   |
|  1 | test       | EGFR           | mean_absolute_error |  16.1858   |
|  2 | test       | EGFR           | r2                  |   0.414315 |
|  3 | test       | EGFR           | spearmanr           |   0.454184 |
|  4 | test       | EGFR           | pearsonr            |   0.64434  |
|  5 | test       | EGFR           | mean_squared_error  | 471.927    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.262131 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.443923 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.255793 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.440581 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.533715 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.403493 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.210554 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.674484 |
|  2 | test       | LOG_RPPB       | r2                  | 0.209973 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.626957 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.606417 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.701925 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.323892 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.584342 |
|  2 | test       | LOG_HPPB       | r2                  | 0.283319 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.611353 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.588891 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.43405  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.420213 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.417427 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.415587 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.650218 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.669075 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.289514 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.300875 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.513142 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.300826 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.548409 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.552128 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.394714 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.253124 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.44351  |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.242343 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.500351 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.503466 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.294281 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.713804 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.83405 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.244719 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.648856 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.309607 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.377802 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.440424 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.887174 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.645494 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.511249 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.650769 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.913856 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.394374 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.792342 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.864583 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.842545 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.634471 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6678755873767952,
    "polaris/pkis2-ret-wt-reg-v2": 684.6868990607968,
    "polaris/pkis2-kit-wt-cls-v2": 0.5847064757112542,
    "polaris/pkis2-kit-wt-reg-v2": 894.5757508225576,
    "polaris/pkis2-egfr-wt-reg-v2": 471.92666311381174,
    "polaris/adme-fang-solu-1": 0.5337150075382253,
    "polaris/adme-fang-rppb-1": 0.6064171784391643,
    "polaris/adme-fang-hppb-1": 0.5888909612421069,
    "polaris/adme-fang-perm-1": 0.6690752552438191,
    "polaris/adme-fang-rclint-1": 0.5521277445579383,
    "polaris/adme-fang-hclint-1": 0.503466296018658,
    "tdcommons/lipophilicity-astrazeneca": 0.713804243197279,
    "tdcommons/ppbr-az": 9.834048602347265,
    "tdcommons/clearance-hepatocyte-az": 0.2447192170360795,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6488555198591134,
    "tdcommons/half-life-obach": 0.3096068848764195,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3778022799351436,
    "tdcommons/clearance-microsome-az": 0.4404236552354421,
    "tdcommons/dili": 0.8871739130434783,
    "tdcommons/bioavailability-ma": 0.6454938476887262,
    "tdcommons/vdss-lombardo": 0.5112494085643206,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6507685352622061,
    "tdcommons/pgp-broccatelli": 0.9138563049853372,
    "tdcommons/caco2-wang": 0.3943740500180797,
    "tdcommons/herg": 0.7923416789396172,
    "tdcommons/bbb-martins": 0.8645833333333333,
    "tdcommons/ames": 0.8425453797802972,
    "tdcommons/ld50-zhu": 0.6344712633465429
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.724006 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.420521 |
|  2 | test       | CLS_RET        | mcc         | 0.459084 |
|  3 | test       | CLS_RET        | f1          | 0.48     |
|  4 | test       | CLS_RET        | roc_auc     | 0.94382  |
|  5 | test       | CLS_RET        | accuracy    | 0.877358 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.470486 |
|  1 | test       | RET            | mean_absolute_error |  18.8799   |
|  2 | test       | RET            | r2                  |   0.432363 |
|  3 | test       | RET            | spearmanr           |   0.629946 |
|  4 | test       | RET            | pearsonr            |   0.688595 |
|  5 | test       | RET            | mean_squared_error  | 674.015    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.603784 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.31125  |
|  2 | test       | CLS_KIT        | mcc         | 0.352891 |
|  3 | test       | CLS_KIT        | f1          | 0.387097 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.840426 |
|  5 | test       | CLS_KIT        | accuracy    | 0.836207 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.236033 |
|  1 | test       | KIT            | mean_absolute_error |  23.7068   |
|  2 | test       | KIT            | r2                  |   0.209216 |
|  3 | test       | KIT            | spearmanr           |   0.504255 |
|  4 | test       | KIT            | pearsonr            |   0.528725 |
|  5 | test       | KIT            | mean_squared_error  | 954.226    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.40801  |
|  1 | test       | EGFR           | mean_absolute_error |  16.1185   |
|  2 | test       | EGFR           | r2                  |   0.407922 |
|  3 | test       | EGFR           | spearmanr           |   0.460237 |
|  4 | test       | EGFR           | pearsonr            |   0.639238 |
|  5 | test       | EGFR           | mean_squared_error  | 477.078    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.25874  |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.446432 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.253377 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.434005 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.527574 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.404803 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.297502 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.626197 |
|  2 | test       | LOG_RPPB       | r2                  | 0.289176 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.752174 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.765176 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.631554 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.298482 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.581021 |
|  2 | test       | LOG_HPPB       | r2                  | 0.269495 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.544732 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.556271 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.442422 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.418834 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.420767 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.415538 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.654564 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.669355 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.289538 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.299292 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.513934 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.299239 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.550653 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.551361 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.39561  |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.258564 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.440047 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.246299 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.505741 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.509253 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.292745 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.71461 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.84974 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.265702 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.645968 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.324327 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.362484 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.439101 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.867826 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.630196 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.501486 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.648734 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.915889 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.417765 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  |  0.7757 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.877072 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.839688 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.617307 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7240064895702975,
    "polaris/pkis2-ret-wt-reg-v2": 674.0153337591719,
    "polaris/pkis2-kit-wt-cls-v2": 0.6037842433329393,
    "polaris/pkis2-kit-wt-reg-v2": 954.2261018467435,
    "polaris/pkis2-egfr-wt-reg-v2": 477.07815371971446,
    "polaris/adme-fang-solu-1": 0.5275738893261084,
    "polaris/adme-fang-rppb-1": 0.7651763650413219,
    "polaris/adme-fang-hppb-1": 0.5562711139553016,
    "polaris/adme-fang-perm-1": 0.6693549609873073,
    "polaris/adme-fang-rclint-1": 0.551361086183535,
    "polaris/adme-fang-hclint-1": 0.5092530356905982,
    "tdcommons/lipophilicity-astrazeneca": 0.7146101539115646,
    "tdcommons/ppbr-az": 9.849738877184235,
    "tdcommons/clearance-hepatocyte-az": 0.2657024891253087,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6459683170348046,
    "tdcommons/half-life-obach": 0.3243266664225405,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.36248417139316114,
    "tdcommons/clearance-microsome-az": 0.4391005285405176,
    "tdcommons/dili": 0.8678260869565217,
    "tdcommons/bioavailability-ma": 0.6301962088460259,
    "tdcommons/vdss-lombardo": 0.5014857136501926,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6487341772151899,
    "tdcommons/pgp-broccatelli": 0.9158890962410023,
    "tdcommons/caco2-wang": 0.4177653749528826,
    "tdcommons/herg": 0.775699558173785,
    "tdcommons/bbb-martins": 0.877071607254534,
    "tdcommons/ames": 0.8396884607100197,
    "tdcommons/ld50-zhu": 0.6173065279735299
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.635526 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.420521 |
|  2 | test       | CLS_RET        | mcc         | 0.459084 |
|  3 | test       | CLS_RET        | f1          | 0.48     |
|  4 | test       | CLS_RET        | roc_auc     | 0.921018 |
|  5 | test       | CLS_RET        | accuracy    | 0.877358 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.470215 |
|  1 | test       | RET            | mean_absolute_error |  18.7764   |
|  2 | test       | RET            | r2                  |   0.438822 |
|  3 | test       | RET            | spearmanr           |   0.634553 |
|  4 | test       | RET            | pearsonr            |   0.687536 |
|  5 | test       | RET            | mean_squared_error  | 666.345    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.633133 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.290954 |
|  2 | test       | CLS_KIT        | mcc         | 0.321498 |
|  3 | test       | CLS_KIT        | f1          | 0.375    |
|  4 | test       | CLS_KIT        | roc_auc     | 0.854932 |
|  5 | test       | CLS_KIT        | accuracy    | 0.827586 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.284845 |
|  1 | test       | KIT            | mean_absolute_error |  22.6707   |
|  2 | test       | KIT            | r2                  |   0.264457 |
|  3 | test       | KIT            | spearmanr           |   0.559493 |
|  4 | test       | KIT            | pearsonr            |   0.56423  |
|  5 | test       | KIT            | mean_squared_error  | 887.568    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.420087 |
|  1 | test       | EGFR           | mean_absolute_error |  16.0279   |
|  2 | test       | EGFR           | r2                  |   0.419759 |
|  3 | test       | EGFR           | spearmanr           |   0.463777 |
|  4 | test       | EGFR           | pearsonr            |   0.648191 |
|  5 | test       | EGFR           | mean_squared_error  | 467.54     |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.248593 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.449005 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.243489 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.421313 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.511542 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.410164 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.248484 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.663536 |
|  2 | test       | LOG_RPPB       | r2                  | 0.248052 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.677391 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.697237 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.668092 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.283077 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.574021 |
|  2 | test       | LOG_HPPB       | r2                  | 0.256773 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.514936 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.539719 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.450127 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.411834 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.422901 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.407656 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.645341 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.661066 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.293443 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.28967  |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.516839 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.289484 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.540869 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.540907 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.401117 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.258179 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.443671 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.245914 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.504948 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.509301 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.292894 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.716139 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.91438 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.264579 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.645492 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.292838 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.358152 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.448494 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.859348 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.643332 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.510001 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.655289 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.905325 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.425815 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.792636 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.863235 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.843166 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.633083 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6355258243925477,
    "polaris/pkis2-ret-wt-reg-v2": 666.3454346063942,
    "polaris/pkis2-kit-wt-cls-v2": 0.6331327100023025,
    "polaris/pkis2-kit-wt-reg-v2": 887.5680849553916,
    "polaris/pkis2-egfr-wt-reg-v2": 467.5395500162037,
    "polaris/adme-fang-solu-1": 0.5115415720041263,
    "polaris/adme-fang-rppb-1": 0.6972369071219323,
    "polaris/adme-fang-hppb-1": 0.539719341287714,
    "polaris/adme-fang-perm-1": 0.6610659686653804,
    "polaris/adme-fang-rclint-1": 0.5409074243662966,
    "polaris/adme-fang-hclint-1": 0.5093007724691986,
    "tdcommons/lipophilicity-astrazeneca": 0.7161387370777371,
    "tdcommons/ppbr-az": 9.914376427317144,
    "tdcommons/clearance-hepatocyte-az": 0.26457880533209344,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6454915183457948,
    "tdcommons/half-life-obach": 0.292838285352048,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3581519357253623,
    "tdcommons/clearance-microsome-az": 0.4484936486667008,
    "tdcommons/dili": 0.8593478260869565,
    "tdcommons/bioavailability-ma": 0.6433322248087795,
    "tdcommons/vdss-lombardo": 0.5100012650498482,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6552893309222424,
    "tdcommons/pgp-broccatelli": 0.9053252466009064,
    "tdcommons/caco2-wang": 0.42581469694561763,
    "tdcommons/herg": 0.7926362297496318,
    "tdcommons/bbb-martins": 0.8632348342714197,
    "tdcommons/ames": 0.8431661085981712,
    "tdcommons/ld50-zhu": 0.6330833495698408
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.712002 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.420521 |
|  2 | test       | CLS_RET        | mcc         | 0.459084 |
|  3 | test       | CLS_RET        | f1          | 0.48     |
|  4 | test       | CLS_RET        | roc_auc     | 0.940185 |
|  5 | test       | CLS_RET        | accuracy    | 0.877358 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.448977 |
|  1 | test       | RET            | mean_absolute_error |  18.8695   |
|  2 | test       | RET            | r2                  |   0.409809 |
|  3 | test       | RET            | spearmanr           |   0.629172 |
|  4 | test       | RET            | pearsonr            |   0.670117 |
|  5 | test       | RET            | mean_squared_error  | 700.796    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.608766 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.31125  |
|  2 | test       | CLS_KIT        | mcc         | 0.352891 |
|  3 | test       | CLS_KIT        | f1          | 0.387097 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.834865 |
|  5 | test       | CLS_KIT        | accuracy    | 0.836207 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.306182 |
|  1 | test       | KIT            | mean_absolute_error |  22.7332   |
|  2 | test       | KIT            | r2                  |   0.282008 |
|  3 | test       | KIT            | spearmanr           |   0.545645 |
|  4 | test       | KIT            | pearsonr            |   0.569629 |
|  5 | test       | KIT            | mean_squared_error  | 866.389    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.438061 |
|  1 | test       | EGFR           | mean_absolute_error |  15.8958   |
|  2 | test       | EGFR           | r2                  |   0.437308 |
|  3 | test       | EGFR           | spearmanr           |   0.489083 |
|  4 | test       | EGFR           | pearsonr            |   0.661999 |
|  5 | test       | EGFR           | mean_squared_error  | 453.399    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.261    |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.446874 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.255005 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.429121 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.528509 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.40392  |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.287908 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.647088 |
|  2 | test       | LOG_RPPB       | r2                  | 0.287504 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.826087 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.792598 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.63304  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.308875 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.579192 |
|  2 | test       | LOG_HPPB       | r2                  | 0.274615 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.556956 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.570667 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.439321 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.424225 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.418182 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.418442 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.655788 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.676742 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.288099 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.297142 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.51617  |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.296712 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.545827 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.548642 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.397037 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.264389 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.440888 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.252929 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.512553 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.515304 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.29017  |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.716045 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.94999 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.26712 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.64659 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.310458 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.365523 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.434106 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.878913 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.629697 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.521562 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.656307 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.920455 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.430886 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.795729 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.869938 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.835625 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.629882 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.712002437952606,
    "polaris/pkis2-ret-wt-reg-v2": 700.7960553396227,
    "polaris/pkis2-kit-wt-cls-v2": 0.608765820026847,
    "polaris/pkis2-kit-wt-reg-v2": 866.3890361944447,
    "polaris/pkis2-egfr-wt-reg-v2": 453.3993568987268,
    "polaris/adme-fang-solu-1": 0.5285093268992189,
    "polaris/adme-fang-rppb-1": 0.7925975952230433,
    "polaris/adme-fang-hppb-1": 0.570667499270064,
    "polaris/adme-fang-perm-1": 0.6767420605689841,
    "polaris/adme-fang-rclint-1": 0.5486419204750083,
    "polaris/adme-fang-hclint-1": 0.5153037781016855,
    "tdcommons/lipophilicity-astrazeneca": 0.7160445409580499,
    "tdcommons/ppbr-az": 9.949992307749891,
    "tdcommons/clearance-hepatocyte-az": 0.2671198009452371,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6465898836762471,
    "tdcommons/half-life-obach": 0.31045811996500217,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3655228894738914,
    "tdcommons/clearance-microsome-az": 0.43410627917380196,
    "tdcommons/dili": 0.8789130434782608,
    "tdcommons/bioavailability-ma": 0.6296973727968075,
    "tdcommons/vdss-lombardo": 0.5215615380506136,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6563065099457506,
    "tdcommons/pgp-broccatelli": 0.9204545454545454,
    "tdcommons/caco2-wang": 0.43088618700484926,
    "tdcommons/herg": 0.7957290132547864,
    "tdcommons/bbb-martins": 0.8699382426516572,
    "tdcommons/ames": 0.8356253304352935,
    "tdcommons/ld50-zhu": 0.6298823162213482
}
```
