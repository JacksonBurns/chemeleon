# chemeleon2_preview_initial_training_e4s281344 Baseline Results
timestamp: 2026-06-27 12:27:11.214537
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.71996  |
|  1 | test       | CLS_RET        | cohen_kappa | 0        |
|  2 | test       | CLS_RET        | accuracy    | 0.839623 |
|  3 | test       | CLS_RET        | f1          | 0        |
|  4 | test       | CLS_RET        | roc_auc     | 0.869795 |
|  5 | test       | CLS_RET        | mcc         | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.621996 |
|  1 | test       | RET            | spearmanr           |   0.599567 |
|  2 | test       | RET            | mean_absolute_error |  20.7713   |
|  3 | test       | RET            | explained_var       |   0.38101  |
|  4 | test       | RET            | mean_squared_error  | 815.396    |
|  5 | test       | RET            | r2                  |   0.313296 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.539978 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.139466 |
|  2 | test       | CLS_KIT        | accuracy    | 0.827586 |
|  3 | test       | CLS_KIT        | f1          | 0.166667 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.799323 |
|  5 | test       | CLS_KIT        | mcc         | 0.273788 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.575167 |
|  1 | test       | KIT            | spearmanr           |   0.522316 |
|  2 | test       | KIT            | mean_absolute_error |  22.6334   |
|  3 | test       | KIT            | explained_var       |   0.304567 |
|  4 | test       | KIT            | mean_squared_error  | 841.974    |
|  5 | test       | KIT            | r2                  |   0.302241 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.713027 |
|  1 | test       | EGFR           | spearmanr           |   0.466158 |
|  2 | test       | EGFR           | mean_absolute_error |  16.1154   |
|  3 | test       | EGFR           | explained_var       |   0.489274 |
|  4 | test       | EGFR           | mean_squared_error  | 425.877    |
|  5 | test       | EGFR           | r2                  |   0.471465 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.654572 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.540009 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.373434 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.427301 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.311885 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.424755 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.624569 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.661739 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.563689 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.381696 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.563177 |
|  5 | test       | LOG_RPPB       | r2                  | 0.366136 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.731949 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.702575 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.472005 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.528791 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.322838 |
|  5 | test       | LOG_HPPB       | r2                  | 0.466946 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.816636 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.798246 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.299167 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.661605 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.168231 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.660409 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.71742  |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.713957 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.416804 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.514298 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.275904 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.511279 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.719474 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.719654 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.333152 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.502432 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.193409 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.502048 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.488473 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.43294 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.356707 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.703452 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.365291 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.37775 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.557761 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.916522 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.686066 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.568325 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.663766 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.942349 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.418628 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.868041 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.899351 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.851722 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.566124 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7199595447867206,
    "polaris/pkis2-ret-wt-reg-v2": 815.3957551364582,
    "polaris/pkis2-kit-wt-cls-v2": 0.5399781219717663,
    "polaris/pkis2-kit-wt-reg-v2": 841.9741058201242,
    "polaris/pkis2-egfr-wt-reg-v2": 425.87680298404825,
    "polaris/adme-fang-solu-1": 0.6545715386456153,
    "polaris/adme-fang-rppb-1": 0.6245688384340873,
    "polaris/adme-fang-hppb-1": 0.7319491017425022,
    "polaris/adme-fang-perm-1": 0.816635878693894,
    "polaris/adme-fang-rclint-1": 0.7174204877599092,
    "polaris/adme-fang-hclint-1": 0.7194738237761157,
    "tdcommons/lipophilicity-astrazeneca": 0.48847290687901634,
    "tdcommons/ppbr-az": 8.432937837167374,
    "tdcommons/clearance-hepatocyte-az": 0.35670672182199303,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7034520242457152,
    "tdcommons/half-life-obach": 0.3652911593043876,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.37774956557909356,
    "tdcommons/clearance-microsome-az": 0.5577612201082187,
    "tdcommons/dili": 0.9165217391304348,
    "tdcommons/bioavailability-ma": 0.6860658463584969,
    "tdcommons/vdss-lombardo": 0.5683248892656023,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6637658227848102,
    "tdcommons/pgp-broccatelli": 0.9423487070114636,
    "tdcommons/caco2-wang": 0.4186284119271416,
    "tdcommons/herg": 0.8680412371134021,
    "tdcommons/bbb-martins": 0.8993511569731082,
    "tdcommons/ames": 0.8517221797959624,
    "tdcommons/ld50-zhu": 0.5661244892473957
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.67847  |
|  1 | test       | CLS_RET        | cohen_kappa | 0        |
|  2 | test       | CLS_RET        | accuracy    | 0.839623 |
|  3 | test       | CLS_RET        | f1          | 0        |
|  4 | test       | CLS_RET        | roc_auc     | 0.834765 |
|  5 | test       | CLS_RET        | mcc         | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.680318 |
|  1 | test       | RET            | spearmanr           |   0.641423 |
|  2 | test       | RET            | mean_absolute_error |  18.998    |
|  3 | test       | RET            | explained_var       |   0.45986  |
|  4 | test       | RET            | mean_squared_error  | 641.969    |
|  5 | test       | RET            | r2                  |   0.459351 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.56161  |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.509786 |
|  2 | test       | CLS_KIT        | accuracy    | 0.836207 |
|  3 | test       | CLS_KIT        | f1          | 0.612245 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.806576 |
|  5 | test       | CLS_KIT        | mcc         | 0.514082 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.526759 |
|  1 | test       | KIT            | spearmanr           |   0.508888 |
|  2 | test       | KIT            | mean_absolute_error |  23.2956   |
|  3 | test       | KIT            | explained_var       |   0.192312 |
|  4 | test       | KIT            | mean_squared_error  | 979.703    |
|  5 | test       | KIT            | r2                  |   0.188103 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.684041 |
|  1 | test       | EGFR           | spearmanr           |   0.30599  |
|  2 | test       | EGFR           | mean_absolute_error |  16.8486   |
|  3 | test       | EGFR           | explained_var       |   0.430236 |
|  4 | test       | EGFR           | mean_squared_error  | 469.982    |
|  5 | test       | EGFR           | r2                  |   0.416729 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.660106 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.558993 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.370313 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.421816 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.315132 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.418767 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.722432 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.738261 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.546535 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.511504 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.44232  |
|  5 | test       | LOG_RPPB       | r2                  | 0.502162 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.722845 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.711743 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.512645 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.483658 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.352795 |
|  5 | test       | LOG_HPPB       | r2                  | 0.417483 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.804263 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.77564  |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.313878 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.646414 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.175424 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.645888 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.7218   |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.718546 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.414855 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.520592 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.271074 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.519835 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.698983 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.697948 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.348997 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.483374 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.200691 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.483301 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.483583 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.95135 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.395416 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.744479 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.394457 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.356095 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.617383 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.914783 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.37712 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.577224 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.633476 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.931085 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.319271 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.866127 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.903963 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.831268 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.569767 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6784701859928708,
    "polaris/pkis2-ret-wt-reg-v2": 641.9692233071326,
    "polaris/pkis2-kit-wt-cls-v2": 0.5616099945974102,
    "polaris/pkis2-kit-wt-reg-v2": 979.703277793784,
    "polaris/pkis2-egfr-wt-reg-v2": 469.9815620149463,
    "polaris/adme-fang-solu-1": 0.6601062506010529,
    "polaris/adme-fang-rppb-1": 0.7224319036513879,
    "polaris/adme-fang-hppb-1": 0.7228447220555256,
    "polaris/adme-fang-perm-1": 0.804262793677972,
    "polaris/adme-fang-rclint-1": 0.7217996221356229,
    "polaris/adme-fang-hclint-1": 0.6989832233589691,
    "tdcommons/lipophilicity-astrazeneca": 0.48358308816523776,
    "tdcommons/ppbr-az": 7.951351187335783,
    "tdcommons/clearance-hepatocyte-az": 0.3954163969078166,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7444792681018404,
    "tdcommons/half-life-obach": 0.3944567370031497,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.35609478640243825,
    "tdcommons/clearance-microsome-az": 0.6173825597661147,
    "tdcommons/dili": 0.9147826086956521,
    "tdcommons/bioavailability-ma": 0.3771200532091786,
    "tdcommons/vdss-lombardo": 0.5772237081826826,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6334764918625678,
    "tdcommons/pgp-broccatelli": 0.9310850439882699,
    "tdcommons/caco2-wang": 0.31927136415520974,
    "tdcommons/herg": 0.8661266568483064,
    "tdcommons/bbb-martins": 0.9039634146341464,
    "tdcommons/ames": 0.8312675008322075,
    "tdcommons/ld50-zhu": 0.5697666880694068
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.694241 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.264618 |
|  2 | test       | CLS_RET        | accuracy    | 0.867925 |
|  3 | test       | CLS_RET        | f1          | 0.3      |
|  4 | test       | CLS_RET        | roc_auc     | 0.868473 |
|  5 | test       | CLS_RET        | mcc         | 0.390492 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.652181 |
|  1 | test       | RET            | spearmanr           |   0.602822 |
|  2 | test       | RET            | mean_absolute_error |  19.7528   |
|  3 | test       | RET            | explained_var       |   0.424359 |
|  4 | test       | RET            | mean_squared_error  | 723.295    |
|  5 | test       | RET            | r2                  |   0.390861 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.572827 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.360721 |
|  2 | test       | CLS_KIT        | accuracy    | 0.810345 |
|  3 | test       | CLS_KIT        | f1          | 0.47619  |
|  4 | test       | CLS_KIT        | roc_auc     | 0.810928 |
|  5 | test       | CLS_KIT        | mcc         | 0.361332 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.591505 |
|  1 | test       | KIT            | spearmanr           |   0.519869 |
|  2 | test       | KIT            | mean_absolute_error |  22.2033   |
|  3 | test       | KIT            | explained_var       |   0.315411 |
|  4 | test       | KIT            | mean_squared_error  | 849.978    |
|  5 | test       | KIT            | r2                  |   0.295609 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.679883 |
|  1 | test       | EGFR           | spearmanr           |   0.357875 |
|  2 | test       | EGFR           | mean_absolute_error |  15.6685   |
|  3 | test       | EGFR           | explained_var       |   0.461882 |
|  4 | test       | EGFR           | mean_squared_error  | 438.921    |
|  5 | test       | EGFR           | r2                  |   0.455277 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.654714 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.559985 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.368338 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.427594 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.310466 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.427374 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.784309 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.794783 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.521916 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.540779 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.414624 |
|  5 | test       | LOG_RPPB       | r2                  | 0.533334 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.791349 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.764459 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.564937 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.455769 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.405233 |
|  5 | test       | LOG_HPPB       | r2                  | 0.3309   |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.786887 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.782125 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.308053 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.615738 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.190872 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.614705 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.727531 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.726969 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.407467 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.521329 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.270252 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.521292 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.703504 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.705114 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.343418 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.479407 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.202237 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.479322 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.478897 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.22118 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.371547 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.730803 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0673327 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.397918 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.61429 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.91913 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.608913 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.515074 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.612455 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.874833 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.346057 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.843004 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.920927 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.841943 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.592193 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.694240568641517,
    "polaris/pkis2-ret-wt-reg-v2": 723.2947176888474,
    "polaris/pkis2-kit-wt-cls-v2": 0.5728267356932646,
    "polaris/pkis2-kit-wt-reg-v2": 849.977911395594,
    "polaris/pkis2-egfr-wt-reg-v2": 438.92059370991865,
    "polaris/adme-fang-solu-1": 0.6547136647343441,
    "polaris/adme-fang-rppb-1": 0.7843086572849214,
    "polaris/adme-fang-hppb-1": 0.7913489996041846,
    "polaris/adme-fang-perm-1": 0.7868869208680527,
    "polaris/adme-fang-rclint-1": 0.7275305703926348,
    "polaris/adme-fang-hclint-1": 0.703504045003523,
    "tdcommons/lipophilicity-astrazeneca": 0.478897096713384,
    "tdcommons/ppbr-az": 8.221175171062217,
    "tdcommons/clearance-hepatocyte-az": 0.3715471179789486,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.730802981911717,
    "tdcommons/half-life-obach": 0.06733269309734713,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.397918416861498,
    "tdcommons/clearance-microsome-az": 0.6142901156139106,
    "tdcommons/dili": 0.9191304347826086,
    "tdcommons/bioavailability-ma": 0.6089125374127037,
    "tdcommons/vdss-lombardo": 0.5150738793335238,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6124547920433996,
    "tdcommons/pgp-broccatelli": 0.8748333777659291,
    "tdcommons/caco2-wang": 0.3460573023656155,
    "tdcommons/herg": 0.8430044182621502,
    "tdcommons/bbb-martins": 0.9209271419637274,
    "tdcommons/ames": 0.8419432532456089,
    "tdcommons/ld50-zhu": 0.5921928441947142
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.736291 |
|  1 | test       | CLS_RET        | cohen_kappa | 0        |
|  2 | test       | CLS_RET        | accuracy    | 0.839623 |
|  3 | test       | CLS_RET        | f1          | 0        |
|  4 | test       | CLS_RET        | roc_auc     | 0.874422 |
|  5 | test       | CLS_RET        | mcc         | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.659745 |
|  1 | test       | RET            | spearmanr           |   0.60554  |
|  2 | test       | RET            | mean_absolute_error |  19.1117   |
|  3 | test       | RET            | explained_var       |   0.426966 |
|  4 | test       | RET            | mean_squared_error  | 690.972    |
|  5 | test       | RET            | r2                  |   0.418082 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.621242 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.413483 |
|  2 | test       | CLS_KIT        | accuracy    | 0.844828 |
|  3 | test       | CLS_KIT        | f1          | 0.5      |
|  4 | test       | CLS_KIT        | roc_auc     | 0.826886 |
|  5 | test       | CLS_KIT        | mcc         | 0.428291 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.606537 |
|  1 | test       | KIT            | spearmanr           |   0.575461 |
|  2 | test       | KIT            | mean_absolute_error |  21.7047   |
|  3 | test       | KIT            | explained_var       |   0.353425 |
|  4 | test       | KIT            | mean_squared_error  | 868.824    |
|  5 | test       | KIT            | r2                  |   0.27999  |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.699165 |
|  1 | test       | EGFR           | spearmanr           |   0.426947 |
|  2 | test       | EGFR           | mean_absolute_error |  15.7443   |
|  3 | test       | EGFR           | explained_var       |   0.468747 |
|  4 | test       | EGFR           | mean_squared_error  | 442.121    |
|  5 | test       | EGFR           | r2                  |   0.451305 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.651789 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.552641 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.379492 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.406507 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.321939 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.406212 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.788078 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.749565 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.573108 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.450162 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.493828 |
|  5 | test       | LOG_RPPB       | r2                  | 0.444189 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.70525  |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.705172 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.478428 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.49602  |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.327911 |
|  5 | test       | LOG_HPPB       | r2                  | 0.45857  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.820452 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.801611 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.290858 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.670399 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.163366 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.67023  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.743297 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.739755 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.399704 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.55249  |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.252869 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.552082 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.731443 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.737941 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.323186 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.526684 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.183847 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.526668 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.486764 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.87924 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.423421 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.628249 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.367723 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.386201 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.618336 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.91913 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.598271 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.587107 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.656985 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.924753 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.360659 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.862445 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.855144 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.840778 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.603362 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7362909068056127,
    "polaris/pkis2-ret-wt-reg-v2": 690.9719413754812,
    "polaris/pkis2-kit-wt-cls-v2": 0.6212415605842787,
    "polaris/pkis2-kit-wt-reg-v2": 868.8244492081858,
    "polaris/pkis2-egfr-wt-reg-v2": 442.1208843900035,
    "polaris/adme-fang-solu-1": 0.651789443491875,
    "polaris/adme-fang-rppb-1": 0.7880784290714582,
    "polaris/adme-fang-hppb-1": 0.7052504154370026,
    "polaris/adme-fang-perm-1": 0.8204520636133363,
    "polaris/adme-fang-rclint-1": 0.7432968806266228,
    "polaris/adme-fang-hclint-1": 0.7314425342902612,
    "tdcommons/lipophilicity-astrazeneca": 0.48676436868735723,
    "tdcommons/ppbr-az": 7.879235226762531,
    "tdcommons/clearance-hepatocyte-az": 0.42342087682094565,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6282493722820588,
    "tdcommons/half-life-obach": 0.36772290518850403,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.38620149796679487,
    "tdcommons/clearance-microsome-az": 0.6183360186004516,
    "tdcommons/dili": 0.9191304347826087,
    "tdcommons/bioavailability-ma": 0.5982707016960426,
    "tdcommons/vdss-lombardo": 0.5871069166388526,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6569846292947559,
    "tdcommons/pgp-broccatelli": 0.924753399093575,
    "tdcommons/caco2-wang": 0.3606588483442035,
    "tdcommons/herg": 0.8624447717231223,
    "tdcommons/bbb-martins": 0.8551438398999375,
    "tdcommons/ames": 0.8407781628776754,
    "tdcommons/ld50-zhu": 0.6033622883227585
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.73129  |
|  1 | test       | CLS_RET        | cohen_kappa | 0.537669 |
|  2 | test       | CLS_RET        | accuracy    | 0.896226 |
|  3 | test       | CLS_RET        | f1          | 0.592593 |
|  4 | test       | CLS_RET        | roc_auc     | 0.849306 |
|  5 | test       | CLS_RET        | mcc         | 0.562567 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.562746 |
|  1 | test       | RET            | spearmanr           |   0.54066  |
|  2 | test       | RET            | mean_absolute_error |  21.7486   |
|  3 | test       | RET            | explained_var       |   0.30163  |
|  4 | test       | RET            | mean_squared_error  | 852.807    |
|  5 | test       | RET            | r2                  |   0.281789 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.598419 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.542907 |
|  2 | test       | CLS_KIT        | accuracy    | 0.844828 |
|  3 | test       | CLS_KIT        | f1          | 0.64     |
|  4 | test       | CLS_KIT        | roc_auc     | 0.825435 |
|  5 | test       | CLS_KIT        | mcc         | 0.549321 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.572151 |
|  1 | test       | KIT            | spearmanr           |   0.546557 |
|  2 | test       | KIT            | mean_absolute_error |  21.8725   |
|  3 | test       | KIT            | explained_var       |   0.285712 |
|  4 | test       | KIT            | mean_squared_error  | 875.238    |
|  5 | test       | KIT            | r2                  |   0.274675 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.657655 |
|  1 | test       | EGFR           | spearmanr           |   0.271942 |
|  2 | test       | EGFR           | mean_absolute_error |  17.6344   |
|  3 | test       | EGFR           | explained_var       |   0.406036 |
|  4 | test       | EGFR           | mean_squared_error  | 537.778    |
|  5 | test       | EGFR           | r2                  |   0.332589 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.648984 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.568988 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.366727 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.417146 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.321227 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.407526 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.86185  |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.876522 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.508607 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.616518 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.376477 |
|  5 | test       | LOG_RPPB       | r2                  | 0.57627  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.706762 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.667889 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.521809 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.496857 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.41025  |
|  5 | test       | LOG_HPPB       | r2                  | 0.322616 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.792864 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.784647 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.305324 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.626202 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.185428 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.625695 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.734259 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.731341 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.399203 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.532573 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.265184 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.530268 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.718709 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.723553 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.336534 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.498589 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.194758 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.498575 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.486976 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.23331 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.392109 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.688133 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.39176 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.365074 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.581378 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.922174 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.613901 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.476037 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.669643 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.932685 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.310652 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.833284 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.906993 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.827296 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.58573 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7312899924123051,
    "polaris/pkis2-ret-wt-reg-v2": 852.8068468569194,
    "polaris/pkis2-kit-wt-cls-v2": 0.5984192923298047,
    "polaris/pkis2-kit-wt-reg-v2": 875.238047439378,
    "polaris/pkis2-egfr-wt-reg-v2": 537.7783732641751,
    "polaris/adme-fang-solu-1": 0.6489837984845466,
    "polaris/adme-fang-rppb-1": 0.8618502736234258,
    "polaris/adme-fang-hppb-1": 0.7067620113740866,
    "polaris/adme-fang-perm-1": 0.7928642234065061,
    "polaris/adme-fang-rclint-1": 0.7342592709596473,
    "polaris/adme-fang-hclint-1": 0.7187085589464776,
    "tdcommons/lipophilicity-astrazeneca": 0.48697591563633513,
    "tdcommons/ppbr-az": 9.233307632146026,
    "tdcommons/clearance-hepatocyte-az": 0.39210867300126756,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.688132755497783,
    "tdcommons/half-life-obach": 0.3917598717762352,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3650743318832589,
    "tdcommons/clearance-microsome-az": 0.5813779586386604,
    "tdcommons/dili": 0.9221739130434783,
    "tdcommons/bioavailability-ma": 0.6139008979048886,
    "tdcommons/vdss-lombardo": 0.4760369261719622,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6696428571428571,
    "tdcommons/pgp-broccatelli": 0.9326846174353505,
    "tdcommons/caco2-wang": 0.3106522821295435,
    "tdcommons/herg": 0.8332842415316641,
    "tdcommons/bbb-martins": 0.9069926516572858,
    "tdcommons/ames": 0.8272964029058724,
    "tdcommons/ld50-zhu": 0.5857302666413767
}
```
