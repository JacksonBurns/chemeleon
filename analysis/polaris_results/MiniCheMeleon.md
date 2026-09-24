# ChemProp Baseline Results
timestamp: 2026-09-24 14:15:50.696783
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |     Score |
|---:|:-----------|:---------------|:------------|----------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.0739979 |
|  1 | test       | CLS_RET        | f1          | 0.105263  |
|  2 | test       | CLS_RET        | mcc         | 0.128346  |
|  3 | test       | CLS_RET        | roc_auc     | 0.812954  |
|  4 | test       | CLS_RET        | pr_auc      | 0.572103  |
|  5 | test       | CLS_RET        | accuracy    | 0.839623  |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.49753  |
|  1 | test       | RET            | mean_squared_error  | 933.8      |
|  2 | test       | RET            | explained_var       |   0.244858 |
|  3 | test       | RET            | mean_absolute_error |  23.8281   |
|  4 | test       | RET            | spearmanr           |   0.468626 |
|  5 | test       | RET            | r2                  |   0.213579 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.229331 |
|  1 | test       | CLS_KIT        | f1          | 0.372093 |
|  2 | test       | CLS_KIT        | mcc         | 0.229424 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.759188 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.438601 |
|  5 | test       | CLS_KIT        | accuracy    | 0.767241 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.490374 |
|  1 | test       | KIT            | mean_squared_error  | 969.536    |
|  2 | test       | KIT            | explained_var       |   0.213858 |
|  3 | test       | KIT            | mean_absolute_error |  23.6662   |
|  4 | test       | KIT            | spearmanr           |   0.434261 |
|  5 | test       | KIT            | r2                  |   0.196529 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.550606 |
|  1 | test       | EGFR           | mean_squared_error  | 563.396    |
|  2 | test       | EGFR           | explained_var       |   0.301447 |
|  3 | test       | EGFR           | mean_absolute_error |  18.8114   |
|  4 | test       | EGFR           | spearmanr           |   0.275123 |
|  5 | test       | EGFR           | r2                  |   0.300797 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.62254  |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.335637 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.387534 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.387588 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.495099 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.380948 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | LOG_RPPB       | pearsonr            |  0.556474  |
|  1 | test       | LOG_RPPB       | mean_squared_error  |  0.894781  |
|  2 | test       | LOG_RPPB       | explained_var       |  0.0286603 |
|  3 | test       | LOG_RPPB       | mean_absolute_error |  0.808119  |
|  4 | test       | LOG_RPPB       | spearmanr           |  0.652174  |
|  5 | test       | LOG_RPPB       | r2                  | -0.0070892 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | LOG_HPPB       | pearsonr            |  0.277323   |
|  1 | test       | LOG_HPPB       | mean_squared_error  |  0.639752   |
|  2 | test       | LOG_HPPB       | explained_var       |  0.00361216 |
|  3 | test       | LOG_HPPB       | mean_absolute_error |  0.700704   |
|  4 | test       | LOG_HPPB       | spearmanr           |  0.289862   |
|  5 | test       | LOG_HPPB       | r2                  | -0.0563255  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.747991 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.218298 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.559365 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.354222 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.758134 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.559343 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.71646  |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.275314 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.512849 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.419115 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.731816 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.512324 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.63471  |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.238127 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.387395 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.383599 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.66129  |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.386917 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.498982 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  7.8911 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.362291 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.616048 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.339502 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.387466 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.535884 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  |    0.93 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.659129 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.501389 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.55278 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.896028 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.314804 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.826657 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.898609 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.823517 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.632442 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.572102636945758,
    "polaris/pkis2-ret-wt-reg-v2": 933.7997424232619,
    "polaris/pkis2-kit-wt-cls-v2": 0.4386014543594316,
    "polaris/pkis2-kit-wt-reg-v2": 969.536040035088,
    "polaris/pkis2-egfr-wt-reg-v2": 563.3957610951874,
    "polaris/adme-fang-solu-1": 0.6225399631693301,
    "polaris/adme-fang-rppb-1": 0.556473779977037,
    "polaris/adme-fang-hppb-1": 0.27732271598490943,
    "polaris/adme-fang-perm-1": 0.7479910848321956,
    "polaris/adme-fang-rclint-1": 0.7164596785971581,
    "polaris/adme-fang-hclint-1": 0.6347104225287561,
    "tdcommons/lipophilicity-astrazeneca": 0.49898194121746786,
    "tdcommons/ppbr-az": 7.891095384246335,
    "tdcommons/clearance-hepatocyte-az": 0.3622909254991424,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6160478609634006,
    "tdcommons/half-life-obach": 0.3395021398863371,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.38746639522818255,
    "tdcommons/clearance-microsome-az": 0.5358843419990694,
    "tdcommons/dili": 0.9299999999999999,
    "tdcommons/bioavailability-ma": 0.6591286997006983,
    "tdcommons/vdss-lombardo": 0.5013887621942842,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5527802893309223,
    "tdcommons/pgp-broccatelli": 0.8960277259397494,
    "tdcommons/caco2-wang": 0.3148038981963106,
    "tdcommons/herg": 0.8266568483063328,
    "tdcommons/bbb-martins": 0.8986085053158224,
    "tdcommons/ames": 0.8235172022166088,
    "tdcommons/ld50-zhu": 0.6324422481637524
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.264618 |
|  1 | test       | CLS_RET        | f1          | 0.3      |
|  2 | test       | CLS_RET        | mcc         | 0.390492 |
|  3 | test       | CLS_RET        | roc_auc     | 0.827495 |
|  4 | test       | CLS_RET        | pr_auc      | 0.671855 |
|  5 | test       | CLS_RET        | accuracy    | 0.867925 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.549286 |
|  1 | test       | RET            | mean_squared_error  | 871.677    |
|  2 | test       | RET            | explained_var       |   0.289428 |
|  3 | test       | RET            | mean_absolute_error |  22.9582   |
|  4 | test       | RET            | spearmanr           |   0.507526 |
|  5 | test       | RET            | r2                  |   0.265898 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.301606 |
|  1 | test       | CLS_KIT        | f1          | 0.4      |
|  2 | test       | CLS_KIT        | mcc         | 0.316097 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.788201 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.491606 |
|  5 | test       | CLS_KIT        | accuracy    | 0.818966 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.499112 |
|  1 | test       | KIT            | mean_squared_error  | 972.036    |
|  2 | test       | KIT            | explained_var       |   0.230056 |
|  3 | test       | KIT            | mean_absolute_error |  23.7881   |
|  4 | test       | KIT            | spearmanr           |   0.47497  |
|  5 | test       | KIT            | r2                  |   0.194457 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.54355  |
|  1 | test       | EGFR           | mean_squared_error  | 576.121    |
|  2 | test       | EGFR           | explained_var       |   0.293366 |
|  3 | test       | EGFR           | mean_absolute_error |  18.766    |
|  4 | test       | EGFR           | spearmanr           |   0.217695 |
|  5 | test       | EGFR           | r2                  |   0.285005 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.617738 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.336674 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.381025 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.396601 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.507416 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.379035 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.436396 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.723442 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.188268 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.599439 |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.56     |
|  5 | test       | LOG_RPPB       | r2                  | 0.185755 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.723895 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.342158 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.523304 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.48248  |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.74704  |
|  5 | test       | LOG_HPPB       | r2                  | 0.435045 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.761407 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.210744 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.57974  |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.349378 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.767909 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.574591 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.689588 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.298179 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.475012 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.43901  |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.699294 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.471823 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.655093 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.226535 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.42467  |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.377257 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.673178 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.416762 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.484875 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.74821 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.37535 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.642823 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |        Score |
|---:|:-----------|:---------------|:----------|-------------:|
|  0 | test       | Y              | spearmanr | -0.000195125 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.354101 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.558895 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.931739 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.627203 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.507671 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.592563 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.902359 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.335619 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.830339 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.890303 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.834598 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.646464 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6718550461017827,
    "polaris/pkis2-ret-wt-reg-v2": 871.6766075191902,
    "polaris/pkis2-kit-wt-cls-v2": 0.4916062163561982,
    "polaris/pkis2-kit-wt-reg-v2": 972.0359458402828,
    "polaris/pkis2-egfr-wt-reg-v2": 576.1207534647201,
    "polaris/adme-fang-solu-1": 0.6177380461289217,
    "polaris/adme-fang-rppb-1": 0.4363957923283367,
    "polaris/adme-fang-hppb-1": 0.7238945195030351,
    "polaris/adme-fang-perm-1": 0.7614073322808801,
    "polaris/adme-fang-rclint-1": 0.6895880580650061,
    "polaris/adme-fang-hclint-1": 0.6550933758302928,
    "tdcommons/lipophilicity-astrazeneca": 0.48487520864463984,
    "tdcommons/ppbr-az": 7.748205843466552,
    "tdcommons/clearance-hepatocyte-az": 0.37534961482470314,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6428232735270917,
    "tdcommons/half-life-obach": -0.00019512504586691998,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3541011046922578,
    "tdcommons/clearance-microsome-az": 0.5588945976475244,
    "tdcommons/dili": 0.9317391304347826,
    "tdcommons/bioavailability-ma": 0.627203192550715,
    "tdcommons/vdss-lombardo": 0.5076706720921208,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5925632911392404,
    "tdcommons/pgp-broccatelli": 0.9023593708344441,
    "tdcommons/caco2-wang": 0.33561909182886823,
    "tdcommons/herg": 0.830338733431517,
    "tdcommons/bbb-martins": 0.8903025328330206,
    "tdcommons/ames": 0.834598288589947,
    "tdcommons/ld50-zhu": 0.646463957705259
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.094984 |
|  1 | test       | CLS_RET        | f1          | 0.111111 |
|  2 | test       | CLS_RET        | mcc         | 0.223293 |
|  3 | test       | CLS_RET        | roc_auc     | 0.825512 |
|  4 | test       | CLS_RET        | pr_auc      | 0.612956 |
|  5 | test       | CLS_RET        | accuracy    | 0.849057 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.474456 |
|  1 | test       | RET            | mean_squared_error  | 923.298    |
|  2 | test       | RET            | explained_var       |   0.22407  |
|  3 | test       | RET            | mean_absolute_error |  24.4492   |
|  4 | test       | RET            | spearmanr           |   0.460789 |
|  5 | test       | RET            | r2                  |   0.222424 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.340909 |
|  1 | test       | CLS_KIT        | f1          | 0.424242 |
|  2 | test       | CLS_KIT        | mcc         | 0.368815 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.78675  |
|  4 | test       | CLS_KIT        | pr_auc      | 0.518638 |
|  5 | test       | CLS_KIT        | accuracy    | 0.836207 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.517421 |
|  1 | test       | KIT            | mean_squared_error  | 913.76     |
|  2 | test       | KIT            | explained_var       |   0.248013 |
|  3 | test       | KIT            | mean_absolute_error |  23.5499   |
|  4 | test       | KIT            | spearmanr           |   0.479502 |
|  5 | test       | KIT            | r2                  |   0.242751 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.583421 |
|  1 | test       | EGFR           | mean_squared_error  | 534.037    |
|  2 | test       | EGFR           | explained_var       |   0.33851  |
|  3 | test       | EGFR           | mean_absolute_error |  18.1265   |
|  4 | test       | EGFR           | spearmanr           |   0.24352  |
|  5 | test       | EGFR           | r2                  |   0.337232 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.577445 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.362888 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.332363 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.414697 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.485752 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.330685 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | LOG_RPPB       | pearsonr            | -0.00303795  |
|  1 | test       | LOG_RPPB       | mean_squared_error  |  0.927797    |
|  2 | test       | LOG_RPPB       | explained_var       | -0.000259521 |
|  3 | test       | LOG_RPPB       | mean_absolute_error |  0.825328    |
|  4 | test       | LOG_RPPB       | spearmanr           |  0.21913     |
|  5 | test       | LOG_RPPB       | r2                  | -0.0442497   |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.650376  |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.5913    |
|  2 | test       | LOG_HPPB       | explained_var       | 0.133389  |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.686841  |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.677668  |
|  5 | test       | LOG_HPPB       | r2                  | 0.0236748 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.747462 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.223763 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.558007 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.364218 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.759101 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.548311 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.725959 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.268109 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.525827 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.408396 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.748034 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.525087 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.661223 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.230085 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.413965 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.376295 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.667793 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.407623 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.497613 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.83057 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.368103 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.57245 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0983418 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.373118 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.474162 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.911739 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.622547 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.444386 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.568377 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.89816 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.335055 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.820471 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.882778 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.842711 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.639783 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6129559965520487,
    "polaris/pkis2-ret-wt-reg-v2": 923.2979270591288,
    "polaris/pkis2-kit-wt-cls-v2": 0.5186382256133156,
    "polaris/pkis2-kit-wt-reg-v2": 913.7597284553752,
    "polaris/pkis2-egfr-wt-reg-v2": 534.0372834391551,
    "polaris/adme-fang-solu-1": 0.5774449968611113,
    "polaris/adme-fang-rppb-1": -0.003037949379397947,
    "polaris/adme-fang-hppb-1": 0.65037614743803,
    "polaris/adme-fang-perm-1": 0.747461787753048,
    "polaris/adme-fang-rclint-1": 0.7259593427661447,
    "polaris/adme-fang-hclint-1": 0.6612227134236691,
    "tdcommons/lipophilicity-astrazeneca": 0.497612626007625,
    "tdcommons/ppbr-az": 7.830574638080087,
    "tdcommons/clearance-hepatocyte-az": 0.3681029890462702,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5724496849157008,
    "tdcommons/half-life-obach": 0.098341803585391,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.37311779913941606,
    "tdcommons/clearance-microsome-az": 0.47416196568262,
    "tdcommons/dili": 0.9117391304347826,
    "tdcommons/bioavailability-ma": 0.6225473894246758,
    "tdcommons/vdss-lombardo": 0.4443855016226736,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5683770343580471,
    "tdcommons/pgp-broccatelli": 0.8981604905358571,
    "tdcommons/caco2-wang": 0.3350554673688282,
    "tdcommons/herg": 0.8204712812960235,
    "tdcommons/bbb-martins": 0.8827782989368355,
    "tdcommons/ames": 0.8427108421938945,
    "tdcommons/ld50-zhu": 0.6397832294871907
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.137799 |
|  1 | test       | CLS_RET        | f1          | 0.190476 |
|  2 | test       | CLS_RET        | mcc         | 0.183279 |
|  3 | test       | CLS_RET        | roc_auc     | 0.817581 |
|  4 | test       | CLS_RET        | pr_auc      | 0.556132 |
|  5 | test       | CLS_RET        | accuracy    | 0.839623 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.507629 |
|  1 | test       | RET            | mean_squared_error  | 888.834    |
|  2 | test       | RET            | explained_var       |   0.257504 |
|  3 | test       | RET            | mean_absolute_error |  23.5814   |
|  4 | test       | RET            | spearmanr           |   0.471826 |
|  5 | test       | RET            | r2                  |   0.251449 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.388759 |
|  1 | test       | CLS_KIT        | f1          | 0.470588 |
|  2 | test       | CLS_KIT        | mcc         | 0.413319 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.809478 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.562676 |
|  5 | test       | CLS_KIT        | accuracy    | 0.844828 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.513563 |
|  1 | test       | KIT            | mean_squared_error  | 947.811    |
|  2 | test       | KIT            | explained_var       |   0.243197 |
|  3 | test       | KIT            | mean_absolute_error |  23.5319   |
|  4 | test       | KIT            | spearmanr           |   0.481776 |
|  5 | test       | KIT            | r2                  |   0.214533 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.505413 |
|  1 | test       | EGFR           | mean_squared_error  | 603.623    |
|  2 | test       | EGFR           | explained_var       |   0.254202 |
|  3 | test       | EGFR           | mean_absolute_error |  20.0558   |
|  4 | test       | EGFR           | spearmanr           |   0.186674 |
|  5 | test       | EGFR           | r2                  |   0.250872 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.593813 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.352251 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.352179 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.403507 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.498563 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.350304 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.467745 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.707476 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.218347 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.649962 |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.581739 |
|  5 | test       | LOG_RPPB       | r2                  | 0.203724 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.75286  |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.344844 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.566244 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.476771 |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.746887 |
|  5 | test       | LOG_HPPB       | r2                  | 0.430611 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.751082 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.216968 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.564038 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.355174 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.754551 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.562028 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.726376 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.267253 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.527613 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.411554 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.746281 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.526602 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.653815 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.230498 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.407615 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.37573  |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.67557  |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.406561 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.488051 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.75657 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.376908 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.570312 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |      Score |
|---:|:-----------|:---------------|:----------|-----------:|
|  0 | test       | Y              | spearmanr | 0.00635743 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.381098 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.51911 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.885652 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.563352 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.46588 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.598666 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.903226 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.331954 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.798233 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.891729 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.833414 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.645292 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5561318285999379,
    "polaris/pkis2-ret-wt-reg-v2": 888.8337747202851,
    "polaris/pkis2-kit-wt-cls-v2": 0.5626764444266182,
    "polaris/pkis2-kit-wt-reg-v2": 947.8106081861805,
    "polaris/pkis2-egfr-wt-reg-v2": 603.6234297473216,
    "polaris/adme-fang-solu-1": 0.593812747879707,
    "polaris/adme-fang-rppb-1": 0.4677452312792675,
    "polaris/adme-fang-hppb-1": 0.752859516197475,
    "polaris/adme-fang-perm-1": 0.7510817179966566,
    "polaris/adme-fang-rclint-1": 0.7263757229200902,
    "polaris/adme-fang-hclint-1": 0.6538153424971517,
    "tdcommons/lipophilicity-astrazeneca": 0.4880506450619016,
    "tdcommons/ppbr-az": 7.7565661956841705,
    "tdcommons/clearance-hepatocyte-az": 0.3769079336056327,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5703118159550231,
    "tdcommons/half-life-obach": 0.006357433405130812,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.38109759130696175,
    "tdcommons/clearance-microsome-az": 0.5191102099830606,
    "tdcommons/dili": 0.8856521739130435,
    "tdcommons/bioavailability-ma": 0.5633521782507482,
    "tdcommons/vdss-lombardo": 0.4658804923626329,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5986663652802894,
    "tdcommons/pgp-broccatelli": 0.9032258064516129,
    "tdcommons/caco2-wang": 0.33195387908117285,
    "tdcommons/herg": 0.7982326951399117,
    "tdcommons/bbb-martins": 0.891729205753596,
    "tdcommons/ames": 0.8334136168712918,
    "tdcommons/ld50-zhu": 0.6452924820728329
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.094984 |
|  1 | test       | CLS_RET        | f1          | 0.111111 |
|  2 | test       | CLS_RET        | mcc         | 0.223293 |
|  3 | test       | CLS_RET        | roc_auc     | 0.833443 |
|  4 | test       | CLS_RET        | pr_auc      | 0.596627 |
|  5 | test       | CLS_RET        | accuracy    | 0.849057 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.489762 |
|  1 | test       | RET            | mean_squared_error  | 930.879    |
|  2 | test       | RET            | explained_var       |   0.239606 |
|  3 | test       | RET            | mean_absolute_error |  23.8589   |
|  4 | test       | RET            | spearmanr           |   0.459175 |
|  5 | test       | RET            | r2                  |   0.216039 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.434633 |
|  1 | test       | CLS_KIT        | f1          | 0.514286 |
|  2 | test       | CLS_KIT        | mcc         | 0.455516 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.817215 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.54114  |
|  5 | test       | CLS_KIT        | accuracy    | 0.853448 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.494483 |
|  1 | test       | KIT            | mean_squared_error  | 979.782    |
|  2 | test       | KIT            | explained_var       |   0.224678 |
|  3 | test       | KIT            | mean_absolute_error |  23.8248   |
|  4 | test       | KIT            | spearmanr           |   0.464265 |
|  5 | test       | KIT            | r2                  |   0.188038 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.529081 |
|  1 | test       | EGFR           | mean_squared_error  | 581.507    |
|  2 | test       | EGFR           | explained_var       |   0.278785 |
|  3 | test       | EGFR           | mean_absolute_error |  19.4284   |
|  4 | test       | EGFR           | spearmanr           |   0.227123 |
|  5 | test       | EGFR           | r2                  |   0.27832  |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.603223 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.350686 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.363073 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.397759 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.489771 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.353192 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.633887  |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.840821  |
|  2 | test       | LOG_RPPB       | explained_var       | 0.0882401 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.783228  |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.7       |
|  5 | test       | LOG_RPPB       | r2                  | 0.053643  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.791291 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.330649 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.59269  |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.497338 |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.81366  |
|  5 | test       | LOG_HPPB       | r2                  | 0.45405  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.732179 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.231366 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.53588  |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.37169  |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.747122 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.532965 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.710795 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.280056 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.50393  |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.422696 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.731117 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.503925 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.670057 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.223079 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.435175 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.37181  |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.70016  |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.425661 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.477217 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.69319 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.364073 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.542441 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0737561 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.40658 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.605914 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.90913 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.575324 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0434339 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.586347 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.906425 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.30716 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.822533 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.868785 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.834191 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.666222 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5966267686917963,
    "polaris/pkis2-ret-wt-reg-v2": 930.8792413877337,
    "polaris/pkis2-kit-wt-cls-v2": 0.5411403061021564,
    "polaris/pkis2-kit-wt-reg-v2": 979.7820603868457,
    "polaris/pkis2-egfr-wt-reg-v2": 581.5071130121115,
    "polaris/adme-fang-solu-1": 0.6032232866719306,
    "polaris/adme-fang-rppb-1": 0.6338873834641683,
    "polaris/adme-fang-hppb-1": 0.7912911232304966,
    "polaris/adme-fang-perm-1": 0.7321794462898669,
    "polaris/adme-fang-rclint-1": 0.7107947405809039,
    "polaris/adme-fang-hclint-1": 0.6700567302175949,
    "tdcommons/lipophilicity-astrazeneca": 0.47721672183559055,
    "tdcommons/ppbr-az": 7.693192040404181,
    "tdcommons/clearance-hepatocyte-az": 0.36407271447550865,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.542441197713958,
    "tdcommons/half-life-obach": 0.0737561377441683,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4065795095405495,
    "tdcommons/clearance-microsome-az": 0.6059141425300436,
    "tdcommons/dili": 0.9091304347826087,
    "tdcommons/bioavailability-ma": 0.575324243431992,
    "tdcommons/vdss-lombardo": 0.04343388230048987,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5863471971066908,
    "tdcommons/pgp-broccatelli": 0.9064249533457743,
    "tdcommons/caco2-wang": 0.30715956771213415,
    "tdcommons/herg": 0.8225331369661266,
    "tdcommons/bbb-martins": 0.8687851782363977,
    "tdcommons/ames": 0.8341909964949383,
    "tdcommons/ld50-zhu": 0.6662220612243323
}
```
