# chemeleon2_preview_initial_training_e4s281344 Baseline Results
timestamp: 2026-06-30 09:41:01.334614
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.757436 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.509672 |
|  2 | test       | CLS_RET        | f1          | 0.56     |
|  3 | test       | CLS_RET        | pr_auc      | 0.610506 |
|  4 | test       | CLS_RET        | accuracy    | 0.896226 |
|  5 | test       | CLS_RET        | mcc         | 0.55641  |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  21.5992   |
|  1 | test       | RET            | spearmanr           |   0.544943 |
|  2 | test       | RET            | explained_var       |   0.340028 |
|  3 | test       | RET            | pearsonr            |   0.585229 |
|  4 | test       | RET            | r2                  |   0.307041 |
|  5 | test       | RET            | mean_squared_error  | 822.823    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.710348 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.283146 |
|  2 | test       | CLS_KIT        | f1          | 0.388889 |
|  3 | test       | CLS_KIT        | pr_auc      | 0.418678 |
|  4 | test       | CLS_KIT        | accuracy    | 0.810345 |
|  5 | test       | CLS_KIT        | mcc         | 0.293286 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | mean_absolute_error |   27.2349    |
|  1 | test       | KIT            | spearmanr           |    0.403763  |
|  2 | test       | KIT            | explained_var       |    0.0578051 |
|  3 | test       | KIT            | pearsonr            |    0.402286  |
|  4 | test       | KIT            | r2                  |    0.0578049 |
|  5 | test       | KIT            | mean_squared_error  | 1136.93      |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  20.4064   |
|  1 | test       | EGFR           | spearmanr           |   0.246978 |
|  2 | test       | EGFR           | explained_var       |   0.201318 |
|  3 | test       | EGFR           | pearsonr            |   0.465077 |
|  4 | test       | EGFR           | r2                  |   0.196202 |
|  5 | test       | EGFR           | mean_squared_error  | 647.675    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.43716  |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.469438 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.335407 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.579353 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.334762 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.360678 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.592994 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.646957 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.317408 |
|  3 | test       | LOG_RPPB       | pearsonr            | 0.569015 |
|  4 | test       | LOG_RPPB       | r2                  | 0.294186 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.627103 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.540871 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.658568 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.3949   |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.64013  |
|  4 | test       | LOG_HPPB       | r2                  | 0.352648 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.392061 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.381397 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.697864 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.485965 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.698548 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.485948 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.254657 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.446388 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.677748 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.439554 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.667103 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.436057 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.31837  |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.408124 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.639859 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.343291 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.616644 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.338645 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.256877 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.582695 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.45412 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.413418 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.613672 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.223881 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.345469 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.530144 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.891739 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.56568 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.387795 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.637658 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.906292 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.456584 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.825626 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.850258 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.781834 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.601741 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6105060934912863,
    "polaris/pkis2-ret-wt-reg-v2": 822.8232205349819,
    "polaris/pkis2-kit-wt-cls-v2": 0.4186781455262259,
    "polaris/pkis2-kit-wt-reg-v2": 1136.931752299768,
    "polaris/pkis2-egfr-wt-reg-v2": 647.6750902448077,
    "polaris/adme-fang-solu-1": 0.5793534169943834,
    "polaris/adme-fang-rppb-1": 0.5690146183153298,
    "polaris/adme-fang-hppb-1": 0.640130478035874,
    "polaris/adme-fang-perm-1": 0.6985477258284012,
    "polaris/adme-fang-rclint-1": 0.6671028450784044,
    "polaris/adme-fang-hclint-1": 0.6166444022771987,
    "tdcommons/lipophilicity-astrazeneca": 0.5826945296980085,
    "tdcommons/ppbr-az": 9.454122420090895,
    "tdcommons/clearance-hepatocyte-az": 0.41341797151167575,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6136719811259786,
    "tdcommons/half-life-obach": 0.22388132650168419,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3454686751913898,
    "tdcommons/clearance-microsome-az": 0.5301435878878863,
    "tdcommons/dili": 0.8917391304347826,
    "tdcommons/bioavailability-ma": 0.5656800798137679,
    "tdcommons/vdss-lombardo": 0.3877952427447965,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6376582278481012,
    "tdcommons/pgp-broccatelli": 0.9062916555585178,
    "tdcommons/caco2-wang": 0.4565839241960799,
    "tdcommons/herg": 0.8256259204712812,
    "tdcommons/bbb-martins": 0.8502579737335836,
    "tdcommons/ames": 0.781834380935597,
    "tdcommons/ld50-zhu": 0.6017413050789633
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.697951 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.54033  |
|  2 | test       | CLS_RET        | f1          | 0.583333 |
|  3 | test       | CLS_RET        | pr_auc      | 0.609806 |
|  4 | test       | CLS_RET        | accuracy    | 0.90566  |
|  5 | test       | CLS_RET        | mcc         | 0.608418 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  21.0778   |
|  1 | test       | RET            | spearmanr           |   0.563092 |
|  2 | test       | RET            | explained_var       |   0.378204 |
|  3 | test       | RET            | pearsonr            |   0.616374 |
|  4 | test       | RET            | r2                  |   0.367492 |
|  5 | test       | RET            | mean_squared_error  | 751.043    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.709865 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.252927 |
|  2 | test       | CLS_KIT        | f1          | 0.352941 |
|  3 | test       | CLS_KIT        | pr_auc      | 0.445092 |
|  4 | test       | CLS_KIT        | accuracy    | 0.810345 |
|  5 | test       | CLS_KIT        | mcc         | 0.268906 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | mean_absolute_error |   27.1573    |
|  1 | test       | KIT            | spearmanr           |    0.384955  |
|  2 | test       | KIT            | explained_var       |    0.0673003 |
|  3 | test       | KIT            | pearsonr            |    0.412833  |
|  4 | test       | KIT            | r2                  |    0.0660202 |
|  5 | test       | KIT            | mean_squared_error  | 1127.02      |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  20.3322   |
|  1 | test       | EGFR           | spearmanr           |   0.259257 |
|  2 | test       | EGFR           | explained_var       |   0.214747 |
|  3 | test       | EGFR           | pearsonr            |   0.504449 |
|  4 | test       | EGFR           | r2                  |   0.204027 |
|  5 | test       | EGFR           | mean_squared_error  | 641.37     |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.443363 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.46331  |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.280314 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.529456 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.260662 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.400853 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.583849 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.793913 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.497168 |
|  3 | test       | LOG_RPPB       | pearsonr            | 0.716868 |
|  4 | test       | LOG_RPPB       | r2                  | 0.471742 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.469348 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.416564 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.781114 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.582534 |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.779029 |
|  4 | test       | LOG_HPPB       | r2                  | 0.516622 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.292752 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.386537 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.703989 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.476245 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.691421 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.475814 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.259678 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.438432 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.693957 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.466666 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.683661 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.460635 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.304495 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.390745 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.644041 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.379842 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.625021 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.369663 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.244829 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.572627 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.25639 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.315058 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.689198 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.289363 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.352463 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.539874 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.913043 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.486531 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0476711 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.605222 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.906292 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.45149 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.792489 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.855515 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.800268 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.633425 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6098064475401533,
    "polaris/pkis2-ret-wt-reg-v2": 751.0432108028609,
    "polaris/pkis2-kit-wt-cls-v2": 0.4450917765492179,
    "polaris/pkis2-kit-wt-reg-v2": 1127.0185729742045,
    "polaris/pkis2-egfr-wt-reg-v2": 641.3703473370717,
    "polaris/adme-fang-solu-1": 0.5294559395390772,
    "polaris/adme-fang-rppb-1": 0.716867631939837,
    "polaris/adme-fang-hppb-1": 0.7790287308201702,
    "polaris/adme-fang-perm-1": 0.6914207857207317,
    "polaris/adme-fang-rclint-1": 0.683661134071421,
    "polaris/adme-fang-hclint-1": 0.6250209508859702,
    "tdcommons/lipophilicity-astrazeneca": 0.5726271357706615,
    "tdcommons/ppbr-az": 9.256391676355134,
    "tdcommons/clearance-hepatocyte-az": 0.31505838847680245,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6891979386716839,
    "tdcommons/half-life-obach": 0.2893627729837706,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3524627276858404,
    "tdcommons/clearance-microsome-az": 0.5398744409135997,
    "tdcommons/dili": 0.9130434782608695,
    "tdcommons/bioavailability-ma": 0.4865314266711008,
    "tdcommons/vdss-lombardo": 0.047671131077461217,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6052215189873417,
    "tdcommons/pgp-broccatelli": 0.9062916555585178,
    "tdcommons/caco2-wang": 0.45149000216141594,
    "tdcommons/herg": 0.7924889543446244,
    "tdcommons/bbb-martins": 0.8555151657285806,
    "tdcommons/ames": 0.8002682645048855,
    "tdcommons/ld50-zhu": 0.6334250913182518
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.737607 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.509672 |
|  2 | test       | CLS_RET        | f1          | 0.56     |
|  3 | test       | CLS_RET        | pr_auc      | 0.583643 |
|  4 | test       | CLS_RET        | accuracy    | 0.896226 |
|  5 | test       | CLS_RET        | mcc         | 0.55641  |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  21.2757   |
|  1 | test       | RET            | spearmanr           |   0.529821 |
|  2 | test       | RET            | explained_var       |   0.330627 |
|  3 | test       | RET            | pearsonr            |   0.575437 |
|  4 | test       | RET            | r2                  |   0.311459 |
|  5 | test       | RET            | mean_squared_error  | 817.577    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.742263 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.348315 |
|  2 | test       | CLS_KIT        | f1          | 0.444444 |
|  3 | test       | CLS_KIT        | pr_auc      | 0.500747 |
|  4 | test       | CLS_KIT        | accuracy    | 0.827586 |
|  5 | test       | CLS_KIT        | mcc         | 0.360788 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | mean_absolute_error |   27.3544    |
|  1 | test       | KIT            | spearmanr           |    0.373185  |
|  2 | test       | KIT            | explained_var       |    0.068055  |
|  3 | test       | KIT            | pearsonr            |    0.370074  |
|  4 | test       | KIT            | r2                  |    0.0680442 |
|  5 | test       | KIT            | mean_squared_error  | 1124.58      |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  18.829    |
|  1 | test       | EGFR           | spearmanr           |   0.26819  |
|  2 | test       | EGFR           | explained_var       |   0.305479 |
|  3 | test       | EGFR           | pearsonr            |   0.553474 |
|  4 | test       | EGFR           | r2                  |   0.296812 |
|  5 | test       | EGFR           | mean_squared_error  | 566.606    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.443637 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.482188 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.312088 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.559102 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.311971 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.373035 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.556686 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.766957 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.527674 |
|  3 | test       | LOG_RPPB       | pearsonr            | 0.726527 |
|  4 | test       | LOG_RPPB       | r2                  | 0.514097 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.431716 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.447281 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.773168 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.544511 |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.759051 |
|  4 | test       | LOG_HPPB       | r2                  | 0.459276 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.327483 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.426654 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.660447 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.42516  |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.652072 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.421696 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.286488 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.45438  |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.662707 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.42746  |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.65387  |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.422852 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.325825 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.394555 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.624464 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.373284 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.616489 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.370048 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.244679 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.557052 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.65049 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.311683 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.62037 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.155785 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.330282 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.448414 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.909565 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.65281 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.225451 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.609064 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.886097 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.440616 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.785272 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.863684 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.800237 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.580657 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5836431176092929,
    "polaris/pkis2-ret-wt-reg-v2": 817.5766667709589,
    "polaris/pkis2-kit-wt-cls-v2": 0.5007468192192421,
    "polaris/pkis2-kit-wt-reg-v2": 1124.5761932975865,
    "polaris/pkis2-egfr-wt-reg-v2": 566.6063944959601,
    "polaris/adme-fang-solu-1": 0.5591019142461229,
    "polaris/adme-fang-rppb-1": 0.7265266799045309,
    "polaris/adme-fang-hppb-1": 0.7590514841663274,
    "polaris/adme-fang-perm-1": 0.6520724744912764,
    "polaris/adme-fang-rclint-1": 0.6538700083807868,
    "polaris/adme-fang-hclint-1": 0.6164889940046068,
    "tdcommons/lipophilicity-astrazeneca": 0.5570522949752353,
    "tdcommons/ppbr-az": 9.650491437826686,
    "tdcommons/clearance-hepatocyte-az": 0.31168338426404807,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6203699783818664,
    "tdcommons/half-life-obach": 0.15578520759330067,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3302822130151151,
    "tdcommons/clearance-microsome-az": 0.44841389887917493,
    "tdcommons/dili": 0.9095652173913044,
    "tdcommons/bioavailability-ma": 0.6528101097439308,
    "tdcommons/vdss-lombardo": 0.22545050285929066,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6090641952983724,
    "tdcommons/pgp-broccatelli": 0.8860970407891229,
    "tdcommons/caco2-wang": 0.4406157563428606,
    "tdcommons/herg": 0.7852724594992636,
    "tdcommons/bbb-martins": 0.8636843339587241,
    "tdcommons/ames": 0.800236934343731,
    "tdcommons/ld50-zhu": 0.5806570379214615
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.756114 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.483121 |
|  2 | test       | CLS_RET        | f1          | 0.551724 |
|  3 | test       | CLS_RET        | pr_auc      | 0.614943 |
|  4 | test       | CLS_RET        | accuracy    | 0.877358 |
|  5 | test       | CLS_RET        | mcc         | 0.49296  |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  22.4641   |
|  1 | test       | RET            | spearmanr           |   0.426365 |
|  2 | test       | RET            | explained_var       |   0.306122 |
|  3 | test       | RET            | pearsonr            |   0.557732 |
|  4 | test       | RET            | r2                  |   0.268777 |
|  5 | test       | RET            | mean_squared_error  | 868.258    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.749033 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.301606 |
|  2 | test       | CLS_KIT        | f1          | 0.4      |
|  3 | test       | CLS_KIT        | pr_auc      | 0.495439 |
|  4 | test       | CLS_KIT        | accuracy    | 0.818966 |
|  5 | test       | CLS_KIT        | mcc         | 0.316097 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | mean_absolute_error |   25.574    |
|  1 | test       | KIT            | spearmanr           |    0.448116 |
|  2 | test       | KIT            | explained_var       |    0.171429 |
|  3 | test       | KIT            | pearsonr            |    0.478251 |
|  4 | test       | KIT            | r2                  |    0.137477 |
|  5 | test       | KIT            | mean_squared_error  | 1040.79     |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | EGFR           | mean_absolute_error |  22.3889    |
|  1 | test       | EGFR           | spearmanr           |   0.0821898 |
|  2 | test       | EGFR           | explained_var       |   0.044956  |
|  3 | test       | EGFR           | pearsonr            |   0.299985  |
|  4 | test       | EGFR           | r2                  |   0.041682  |
|  5 | test       | EGFR           | mean_squared_error  | 772.182     |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.429696 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.503973 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.329158 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.573737 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.326202 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.365319 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.559165 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.708696 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.409179 |
|  3 | test       | LOG_RPPB       | pearsonr            | 0.642033 |
|  4 | test       | LOG_RPPB       | r2                  | 0.406444 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.527364 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.435528 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.765223 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.54405  |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.757318 |
|  4 | test       | LOG_HPPB       | r2                  | 0.489329 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.309282 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.397443 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.710674 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.474092 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.688746 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.473694 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.260728 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.457738 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.671973 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.442618 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.66548  |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.424725 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.324767 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.401296 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.645012 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.364089 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.625394 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.339211 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.256657 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.570235 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.17461 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.333431 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.594551 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.259206 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.391381 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.541625 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.916522 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.583638 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.520371 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.623192 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.907025 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.439988 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.80972 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.844121 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.793094 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.661452 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6149430014190129,
    "polaris/pkis2-ret-wt-reg-v2": 868.2579594423274,
    "polaris/pkis2-kit-wt-cls-v2": 0.4954392369016728,
    "polaris/pkis2-kit-wt-reg-v2": 1040.7929662509982,
    "polaris/pkis2-egfr-wt-reg-v2": 772.1823936921157,
    "polaris/adme-fang-solu-1": 0.5737370573939453,
    "polaris/adme-fang-rppb-1": 0.6420333886313263,
    "polaris/adme-fang-hppb-1": 0.7573182089640107,
    "polaris/adme-fang-perm-1": 0.6887464105273466,
    "polaris/adme-fang-rclint-1": 0.665480183695943,
    "polaris/adme-fang-hclint-1": 0.625394144099101,
    "tdcommons/lipophilicity-astrazeneca": 0.5702349758148193,
    "tdcommons/ppbr-az": 9.174612366432367,
    "tdcommons/clearance-hepatocyte-az": 0.33343129834651175,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5945508506822734,
    "tdcommons/half-life-obach": 0.25920623391778497,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.39138102893343946,
    "tdcommons/clearance-microsome-az": 0.5416246338463032,
    "tdcommons/dili": 0.9165217391304348,
    "tdcommons/bioavailability-ma": 0.5836381775856335,
    "tdcommons/vdss-lombardo": 0.5203706808323818,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6231916817359855,
    "tdcommons/pgp-broccatelli": 0.9070247933884298,
    "tdcommons/caco2-wang": 0.4399884111326114,
    "tdcommons/herg": 0.809720176730486,
    "tdcommons/bbb-martins": 0.8441213258286429,
    "tdcommons/ames": 0.7930936576005012,
    "tdcommons/ld50-zhu": 0.6614522416440012
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.771976 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.567347 |
|  2 | test       | CLS_RET        | f1          | 0.615385 |
|  3 | test       | CLS_RET        | pr_auc      | 0.629639 |
|  4 | test       | CLS_RET        | accuracy    | 0.90566  |
|  5 | test       | CLS_RET        | mcc         | 0.604725 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  22.408    |
|  1 | test       | RET            | spearmanr           |   0.532216 |
|  2 | test       | RET            | explained_var       |   0.327146 |
|  3 | test       | RET            | pearsonr            |   0.572714 |
|  4 | test       | RET            | r2                  |   0.257756 |
|  5 | test       | RET            | mean_squared_error  | 881.345    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.709381 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.20288  |
|  2 | test       | CLS_KIT        | f1          | 0.275862 |
|  3 | test       | CLS_KIT        | pr_auc      | 0.428257 |
|  4 | test       | CLS_KIT        | accuracy    | 0.818966 |
|  5 | test       | CLS_KIT        | mcc         | 0.246788 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | mean_absolute_error |   26.2025    |
|  1 | test       | KIT            | spearmanr           |    0.385117  |
|  2 | test       | KIT            | explained_var       |    0.087937  |
|  3 | test       | KIT            | pearsonr            |    0.395965  |
|  4 | test       | KIT            | r2                  |    0.0846532 |
|  5 | test       | KIT            | mean_squared_error  | 1104.53      |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  20.0266   |
|  1 | test       | EGFR           | spearmanr           |   0.221834 |
|  2 | test       | EGFR           | explained_var       |   0.144714 |
|  3 | test       | EGFR           | pearsonr            |   0.39065  |
|  4 | test       | EGFR           | r2                  |   0.12488  |
|  5 | test       | EGFR           | mean_squared_error  | 705.144    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.419338 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.486793 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.326041 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.578534 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.280312 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.390199 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.51874  |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.791304 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.615908 |
|  3 | test       | LOG_RPPB       | pearsonr            | 0.787753 |
|  4 | test       | LOG_RPPB       | r2                  | 0.586813 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.367109 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.391083 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.770724 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.607799 |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.779671 |
|  4 | test       | LOG_HPPB       | r2                  | 0.576971 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.256203 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.416513 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.666764 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.427845 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.658167 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.427748 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.28349  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.434813 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.701825 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.473379 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.692474 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.466937 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.300937 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.395944 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.648117 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.373725 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.62468  |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.373134 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.243481 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.584468 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.23152 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.334504 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.578246 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.31377 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.364002 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.574929 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.947391 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.704357 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.378249 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.625791 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.894961 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.377172 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.796613 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.850375 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.798038 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.630122 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6296392727468353,
    "polaris/pkis2-ret-wt-reg-v2": 881.3448084208305,
    "polaris/pkis2-kit-wt-cls-v2": 0.4282571323008074,
    "polaris/pkis2-kit-wt-reg-v2": 1104.534388241341,
    "polaris/pkis2-egfr-wt-reg-v2": 705.1439138285757,
    "polaris/adme-fang-solu-1": 0.5785337760204676,
    "polaris/adme-fang-rppb-1": 0.787752633381034,
    "polaris/adme-fang-hppb-1": 0.7796708833607753,
    "polaris/adme-fang-perm-1": 0.6581666026298937,
    "polaris/adme-fang-rclint-1": 0.6924743590378497,
    "polaris/adme-fang-hclint-1": 0.6246798903276765,
    "tdcommons/lipophilicity-astrazeneca": 0.58446755139033,
    "tdcommons/ppbr-az": 9.231523107211364,
    "tdcommons/clearance-hepatocyte-az": 0.33450386489337697,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5782464615526762,
    "tdcommons/half-life-obach": 0.3137704473960416,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.36400201690824546,
    "tdcommons/clearance-microsome-az": 0.5749294398260738,
    "tdcommons/dili": 0.947391304347826,
    "tdcommons/bioavailability-ma": 0.7043565014965082,
    "tdcommons/vdss-lombardo": 0.3782489529987513,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6257911392405063,
    "tdcommons/pgp-broccatelli": 0.8949613436416956,
    "tdcommons/caco2-wang": 0.37717173508884316,
    "tdcommons/herg": 0.7966126656848306,
    "tdcommons/bbb-martins": 0.850375234521576,
    "tdcommons/ames": 0.7980379486576985,
    "tdcommons/ld50-zhu": 0.6301224315705254
}
```
