# ChemProp Baseline Results
timestamp: 2025-07-09 16:53:51.061183
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | mcc         | 0        |
|  1 | test       | CLS_RET        | accuracy    | 0.839623 |
|  2 | test       | CLS_RET        | pr_auc      | 0.555742 |
|  3 | test       | CLS_RET        | f1          | 0        |
|  4 | test       | CLS_RET        | roc_auc     | 0.842036 |
|  5 | test       | CLS_RET        | cohen_kappa | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 650.933    |
|  1 | test       | RET            | mean_absolute_error |  18.9253   |
|  2 | test       | RET            | pearsonr            |   0.695244 |
|  3 | test       | RET            | r2                  |   0.451802 |
|  4 | test       | RET            | explained_var       |   0.481797 |
|  5 | test       | RET            | spearmanr           |   0.642213 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | mcc         | 0.599989 |
|  1 | test       | CLS_KIT        | accuracy    | 0.887931 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.705518 |
|  3 | test       | CLS_KIT        | f1          | 0.648649 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.838008 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.584802 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_squared_error  | 764.709    |
|  1 | test       | KIT            | mean_absolute_error |  21.0387   |
|  2 | test       | KIT            | pearsonr            |   0.63416  |
|  3 | test       | KIT            | r2                  |   0.366273 |
|  4 | test       | KIT            | explained_var       |   0.399208 |
|  5 | test       | KIT            | spearmanr           |   0.574188 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 466.868    |
|  1 | test       | EGFR           | mean_absolute_error |  16.3665   |
|  2 | test       | EGFR           | pearsonr            |   0.651699 |
|  3 | test       | EGFR           | r2                  |   0.420593 |
|  4 | test       | EGFR           | explained_var       |   0.423823 |
|  5 | test       | EGFR           | spearmanr           |   0.37202  |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.301099 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.363122 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.672093 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.444651 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.451333 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.576761 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.464618 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.511858 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.705329 |
|  3 | test       | LOG_RPPB       | r2                  | 0.477065 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.477139 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.761739 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.269742 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.432867 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.767233 |
|  3 | test       | LOG_HPPB       | r2                  | 0.554615 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.584891 |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.751318 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.178588 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.306354 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.80105  |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.639502 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.641644 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.795575 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.258447 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.402126 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.737742 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.542202 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.544093 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.745486 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.192375 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.344061 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.715366 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.50471  |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.506055 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.719804 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.466875 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.69951 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.416021 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.684685 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.277216 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.417484 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.589613 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.922174 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.574327 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.612651 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.584765 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.92442 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.391382 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.865243 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.860069 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.846185 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.529736 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5557421689392213,
    "polaris/pkis2-ret-wt-reg-v2": 650.9334804775049,
    "polaris/pkis2-kit-wt-cls-v2": 0.705517640202499,
    "polaris/pkis2-kit-wt-reg-v2": 764.7085305589604,
    "polaris/pkis2-egfr-wt-reg-v2": 466.868113582471,
    "polaris/adme-fang-solu-1": 0.6720933698360827,
    "polaris/adme-fang-rppb-1": 0.7053294111321101,
    "polaris/adme-fang-hppb-1": 0.7672332191886078,
    "polaris/adme-fang-perm-1": 0.8010499555976429,
    "polaris/adme-fang-rclint-1": 0.7377417376092842,
    "polaris/adme-fang-hclint-1": 0.7153661200562557,
    "tdcommons/lipophilicity-astrazeneca": 0.4668748945054554,
    "tdcommons/ppbr-az": 7.699514675515709,
    "tdcommons/clearance-hepatocyte-az": 0.416020671110098,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6846850496039931,
    "tdcommons/half-life-obach": 0.27721625368996533,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4174840125711724,
    "tdcommons/clearance-microsome-az": 0.5896133460787883,
    "tdcommons/dili": 0.9221739130434783,
    "tdcommons/bioavailability-ma": 0.574326571333555,
    "tdcommons/vdss-lombardo": 0.6126509029059873,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5847649186256781,
    "tdcommons/pgp-broccatelli": 0.9244201546254331,
    "tdcommons/caco2-wang": 0.39138182986594405,
    "tdcommons/herg": 0.8652430044182622,
    "tdcommons/bbb-martins": 0.8600687929956221,
    "tdcommons/ames": 0.8461845738119016,
    "tdcommons/ld50-zhu": 0.5297357326708886
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | mcc         | 0        |
|  1 | test       | CLS_RET        | accuracy    | 0.839623 |
|  2 | test       | CLS_RET        | pr_auc      | 0.574881 |
|  3 | test       | CLS_RET        | f1          | 0        |
|  4 | test       | CLS_RET        | roc_auc     | 0.808989 |
|  5 | test       | CLS_RET        | cohen_kappa | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 619.455    |
|  1 | test       | RET            | mean_absolute_error |  19.4599   |
|  2 | test       | RET            | pearsonr            |   0.718776 |
|  3 | test       | RET            | r2                  |   0.478312 |
|  4 | test       | RET            | explained_var       |   0.494345 |
|  5 | test       | RET            | spearmanr           |   0.66389  |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | mcc         | 0.431661 |
|  1 | test       | CLS_KIT        | accuracy    | 0.801724 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.628658 |
|  3 | test       | CLS_KIT        | f1          | 0.54902  |
|  4 | test       | CLS_KIT        | roc_auc     | 0.808027 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.425    |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_squared_error  | 839.414    |
|  1 | test       | KIT            | mean_absolute_error |  21.8902   |
|  2 | test       | KIT            | pearsonr            |   0.594058 |
|  3 | test       | KIT            | r2                  |   0.304363 |
|  4 | test       | KIT            | explained_var       |   0.328248 |
|  5 | test       | KIT            | spearmanr           |   0.565257 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 453.958    |
|  1 | test       | EGFR           | mean_absolute_error |  16.539    |
|  2 | test       | EGFR           | pearsonr            |   0.663157 |
|  3 | test       | EGFR           | r2                  |   0.436615 |
|  4 | test       | EGFR           | explained_var       |   0.437078 |
|  5 | test       | EGFR           | spearmanr           |   0.346243 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.317262 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.36999  |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.649399 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.414838 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.421607 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.549086 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.31662  |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.432615 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.850825 |
|  3 | test       | LOG_RPPB       | r2                  | 0.64364  |
|  4 | test       | LOG_RPPB       | explained_var       | 0.644743 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.842609 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.251432 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.434139 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.783575 |
|  3 | test       | LOG_HPPB       | r2                  | 0.584849 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.606057 |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.741233 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.163882 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.290803 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.818142 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.669187 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.669247 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.809308 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.258312 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.40625  |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.73706  |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.542441 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.542505 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.745004 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.192938 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.342331 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.714092 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.503263 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.504269 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.713296 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.449875 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.60365 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.372729 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.70291 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.228315 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.431232 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.598512 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.908261 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.63585 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.528833 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.624322 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.932951 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.353605 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.85081 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.914947 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.838772 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.535769 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5748809976063137,
    "polaris/pkis2-ret-wt-reg-v2": 619.4554071892535,
    "polaris/pkis2-kit-wt-cls-v2": 0.6286580981288653,
    "polaris/pkis2-kit-wt-reg-v2": 839.4138209168603,
    "polaris/pkis2-egfr-wt-reg-v2": 453.9578640894623,
    "polaris/adme-fang-solu-1": 0.6493988536505653,
    "polaris/adme-fang-rppb-1": 0.8508247039100262,
    "polaris/adme-fang-hppb-1": 0.7835749188220995,
    "polaris/adme-fang-perm-1": 0.8181424572445769,
    "polaris/adme-fang-rclint-1": 0.7370595899123179,
    "polaris/adme-fang-hclint-1": 0.7140922508682094,
    "tdcommons/lipophilicity-astrazeneca": 0.44987520453475766,
    "tdcommons/ppbr-az": 8.603650484852798,
    "tdcommons/clearance-hepatocyte-az": 0.37272938975758696,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.702909738152286,
    "tdcommons/half-life-obach": 0.2283145966373464,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4312319035066947,
    "tdcommons/clearance-microsome-az": 0.5985116330612723,
    "tdcommons/dili": 0.9082608695652173,
    "tdcommons/bioavailability-ma": 0.6358496840705021,
    "tdcommons/vdss-lombardo": 0.52883334963751,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6243218806509945,
    "tdcommons/pgp-broccatelli": 0.932951213009864,
    "tdcommons/caco2-wang": 0.3536049856323243,
    "tdcommons/herg": 0.8508100147275405,
    "tdcommons/bbb-martins": 0.9149468417761101,
    "tdcommons/ames": 0.8387720534962503,
    "tdcommons/ld50-zhu": 0.535768945977233
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | mcc         | 0        |
|  1 | test       | CLS_RET        | accuracy    | 0.839623 |
|  2 | test       | CLS_RET        | pr_auc      | 0.501699 |
|  3 | test       | CLS_RET        | f1          | 0        |
|  4 | test       | CLS_RET        | roc_auc     | 0.814937 |
|  5 | test       | CLS_RET        | cohen_kappa | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 631.388    |
|  1 | test       | RET            | mean_absolute_error |  20.0121   |
|  2 | test       | RET            | pearsonr            |   0.694361 |
|  3 | test       | RET            | r2                  |   0.468262 |
|  4 | test       | RET            | explained_var       |   0.469993 |
|  5 | test       | RET            | spearmanr           |   0.66751  |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | mcc         | 0.558327 |
|  1 | test       | CLS_KIT        | accuracy    | 0.87069  |
|  2 | test       | CLS_KIT        | pr_auc      | 0.698011 |
|  3 | test       | CLS_KIT        | f1          | 0.634146 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.823501 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.556122 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_squared_error  | 780.073    |
|  1 | test       | KIT            | mean_absolute_error |  21.3112   |
|  2 | test       | KIT            | pearsonr            |   0.612435 |
|  3 | test       | KIT            | r2                  |   0.35354  |
|  4 | test       | KIT            | explained_var       |   0.359785 |
|  5 | test       | KIT            | spearmanr           |   0.568693 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 446.337    |
|  1 | test       | EGFR           | mean_absolute_error |  16.3221   |
|  2 | test       | EGFR           | pearsonr            |   0.678248 |
|  3 | test       | EGFR           | r2                  |   0.446073 |
|  4 | test       | EGFR           | explained_var       |   0.452319 |
|  5 | test       | EGFR           | spearmanr           |   0.391739 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.326935 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.378926 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.641009 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.396998 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.410766 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.563387 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.373947 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.467343 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.795529 |
|  3 | test       | LOG_RPPB       | r2                  | 0.579117 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.579284 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.768696 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.271143 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.446866 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.775145 |
|  3 | test       | LOG_HPPB       | r2                  | 0.552303 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.586892 |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.80052  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.174476 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.302657 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.805023 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.647803 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.648062 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.792537 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.25092  |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.392283 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.75008  |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.555535 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.560059 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.751551 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.19596  |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.345226 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.711706 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.495481 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.496833 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.71708  |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.453495 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.88357 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.389657 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.705605 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.235718 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.444966 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.600206 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.885217 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.60592 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.487024 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.633363 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.914823 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.322066 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.858468 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.910608 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.839684 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.527523 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5016986708872335,
    "polaris/pkis2-ret-wt-reg-v2": 631.3880427450616,
    "polaris/pkis2-kit-wt-cls-v2": 0.6980107187614644,
    "polaris/pkis2-kit-wt-reg-v2": 780.073416425915,
    "polaris/pkis2-egfr-wt-reg-v2": 446.33731105962374,
    "polaris/adme-fang-solu-1": 0.6410094771736129,
    "polaris/adme-fang-rppb-1": 0.795528529935994,
    "polaris/adme-fang-hppb-1": 0.7751452684640561,
    "polaris/adme-fang-perm-1": 0.8050231267169468,
    "polaris/adme-fang-rclint-1": 0.750080090124415,
    "polaris/adme-fang-hclint-1": 0.7117063939400967,
    "tdcommons/lipophilicity-astrazeneca": 0.45349451721282236,
    "tdcommons/ppbr-az": 7.883565611864886,
    "tdcommons/clearance-hepatocyte-az": 0.38965727607040196,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.70560540809731,
    "tdcommons/half-life-obach": 0.2357180851628964,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.44496578130188436,
    "tdcommons/clearance-microsome-az": 0.6002057332835649,
    "tdcommons/dili": 0.8852173913043478,
    "tdcommons/bioavailability-ma": 0.6059195211173927,
    "tdcommons/vdss-lombardo": 0.48702419577051387,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6333634719710669,
    "tdcommons/pgp-broccatelli": 0.9148227139429486,
    "tdcommons/caco2-wang": 0.322065509261649,
    "tdcommons/herg": 0.8584683357879235,
    "tdcommons/bbb-martins": 0.9106081926203877,
    "tdcommons/ames": 0.8396835653723395,
    "tdcommons/ld50-zhu": 0.5275226756755328
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | mcc         | 0        |
|  1 | test       | CLS_RET        | accuracy    | 0.839623 |
|  2 | test       | CLS_RET        | pr_auc      | 0.514176 |
|  3 | test       | CLS_RET        | f1          | 0        |
|  4 | test       | CLS_RET        | roc_auc     | 0.823529 |
|  5 | test       | CLS_RET        | cohen_kappa | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 637.682    |
|  1 | test       | RET            | mean_absolute_error |  19.4296   |
|  2 | test       | RET            | pearsonr            |   0.695411 |
|  3 | test       | RET            | r2                  |   0.462962 |
|  4 | test       | RET            | explained_var       |   0.479993 |
|  5 | test       | RET            | spearmanr           |   0.617543 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | mcc         | 0.594191 |
|  1 | test       | CLS_KIT        | accuracy    | 0.87931  |
|  2 | test       | CLS_KIT        | pr_auc      | 0.766519 |
|  3 | test       | CLS_KIT        | f1          | 0.666667 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.855416 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.593186 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_squared_error  | 786.402    |
|  1 | test       | KIT            | mean_absolute_error |  20.7629   |
|  2 | test       | KIT            | pearsonr            |   0.63179  |
|  3 | test       | KIT            | r2                  |   0.348295 |
|  4 | test       | KIT            | explained_var       |   0.386057 |
|  5 | test       | KIT            | spearmanr           |   0.588197 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 477.195    |
|  1 | test       | EGFR           | mean_absolute_error |  16.6139   |
|  2 | test       | EGFR           | pearsonr            |   0.655917 |
|  3 | test       | EGFR           | r2                  |   0.407776 |
|  4 | test       | EGFR           | explained_var       |   0.416884 |
|  5 | test       | EGFR           | spearmanr           |   0.375849 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.337175 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.3846   |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.62223  |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.378111 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.38118  |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.541609 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.540686 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.590373 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.713335 |
|  3 | test       | LOG_RPPB       | r2                  | 0.391449 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.391465 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.764348 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.324883 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.496356 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.759007 |
|  3 | test       | LOG_HPPB       | r2                  | 0.463569 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.572979 |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.740775 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.171999 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.30182  |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.80882  |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.652803 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.652827 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.794612 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.244334 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.392433 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.753379 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.567201 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.567563 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.756601 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.18938  |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.339066 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.72147  |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.512423 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.51562  |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.728473 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.463522 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.06158 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.435646 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.62649 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.328341 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.397256 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.595757 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.916087 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.637845 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.517298 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.612342 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.92682 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.466172 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.869367 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.882427 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.845445 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.525901 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5141764229172273,
    "polaris/pkis2-ret-wt-reg-v2": 637.681627211847,
    "polaris/pkis2-kit-wt-cls-v2": 0.766518955643287,
    "polaris/pkis2-kit-wt-reg-v2": 786.4017955637985,
    "polaris/pkis2-egfr-wt-reg-v2": 477.19524249952116,
    "polaris/adme-fang-solu-1": 0.6222304596196249,
    "polaris/adme-fang-rppb-1": 0.7133349530930755,
    "polaris/adme-fang-hppb-1": 0.7590072374223459,
    "polaris/adme-fang-perm-1": 0.8088203083444551,
    "polaris/adme-fang-rclint-1": 0.7533788601657186,
    "polaris/adme-fang-hclint-1": 0.7214703821371464,
    "tdcommons/lipophilicity-astrazeneca": 0.4635217479751223,
    "tdcommons/ppbr-az": 8.061583413548886,
    "tdcommons/clearance-hepatocyte-az": 0.43564561734760143,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6264901813078645,
    "tdcommons/half-life-obach": 0.32834057327487626,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.39725564192769375,
    "tdcommons/clearance-microsome-az": 0.5957574419554125,
    "tdcommons/dili": 0.9160869565217391,
    "tdcommons/bioavailability-ma": 0.6378450282673761,
    "tdcommons/vdss-lombardo": 0.5172979096301366,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6123417721518987,
    "tdcommons/pgp-broccatelli": 0.9268195147960544,
    "tdcommons/caco2-wang": 0.46617189134494663,
    "tdcommons/herg": 0.8693667157584684,
    "tdcommons/bbb-martins": 0.8824265165728581,
    "tdcommons/ames": 0.8454453778221622,
    "tdcommons/ld50-zhu": 0.5259011757957758
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | mcc         | 0        |
|  1 | test       | CLS_RET        | accuracy    | 0.839623 |
|  2 | test       | CLS_RET        | pr_auc      | 0.571275 |
|  3 | test       | CLS_RET        | f1          | 0        |
|  4 | test       | CLS_RET        | roc_auc     | 0.829478 |
|  5 | test       | CLS_RET        | cohen_kappa | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 655.385    |
|  1 | test       | RET            | mean_absolute_error |  19.0993   |
|  2 | test       | RET            | pearsonr            |   0.691813 |
|  3 | test       | RET            | r2                  |   0.448052 |
|  4 | test       | RET            | explained_var       |   0.477957 |
|  5 | test       | RET            | spearmanr           |   0.626863 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | mcc         | 0.523828 |
|  1 | test       | CLS_KIT        | accuracy    | 0.87069  |
|  2 | test       | CLS_KIT        | pr_auc      | 0.728639 |
|  3 | test       | CLS_KIT        | f1          | 0.482759 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.856383 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.430628 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_squared_error  | 787.73     |
|  1 | test       | KIT            | mean_absolute_error |  21.113    |
|  2 | test       | KIT            | pearsonr            |   0.612962 |
|  3 | test       | KIT            | r2                  |   0.347195 |
|  4 | test       | KIT            | explained_var       |   0.372386 |
|  5 | test       | KIT            | spearmanr           |   0.551828 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 440.335    |
|  1 | test       | EGFR           | mean_absolute_error |  16.3187   |
|  2 | test       | EGFR           | pearsonr            |   0.674682 |
|  3 | test       | EGFR           | r2                  |   0.453521 |
|  4 | test       | EGFR           | explained_var       |   0.453672 |
|  5 | test       | EGFR           | spearmanr           |   0.397254 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.298003 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.366224 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.672838 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.45036  |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.452517 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.583525 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.327823 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.441684 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.835479 |
|  3 | test       | LOG_RPPB       | r2                  | 0.63103  |
|  4 | test       | LOG_RPPB       | explained_var       | 0.631036 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.847826 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.323438 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.506694 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.755573 |
|  3 | test       | LOG_HPPB       | r2                  | 0.465956 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.546626 |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.760333 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.186434 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.307576 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.790832 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.623664 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.625129 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.791459 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.245223 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.389613 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.752919 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.565625 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.56672  |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.7573   |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.191594 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.335286 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.721133 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.506723 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.511901 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.728454 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.443001 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.93663 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.391167 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.656195 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.31514 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.434347 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.588152 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.928261 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.618557 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.534917 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.605108 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.934884 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.325096 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.857437 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.880746 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.837996 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.508605 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5712749215779835,
    "polaris/pkis2-ret-wt-reg-v2": 655.3854003681157,
    "polaris/pkis2-kit-wt-cls-v2": 0.7286387073814247,
    "polaris/pkis2-kit-wt-reg-v2": 787.729708884401,
    "polaris/pkis2-egfr-wt-reg-v2": 440.3354181071984,
    "polaris/adme-fang-solu-1": 0.6728376522477822,
    "polaris/adme-fang-rppb-1": 0.8354788089327978,
    "polaris/adme-fang-hppb-1": 0.7555725595187077,
    "polaris/adme-fang-perm-1": 0.7908324327398866,
    "polaris/adme-fang-rclint-1": 0.7529188897660675,
    "polaris/adme-fang-hclint-1": 0.7211325385514884,
    "tdcommons/lipophilicity-astrazeneca": 0.4430008897213709,
    "tdcommons/ppbr-az": 7.936627359134353,
    "tdcommons/clearance-hepatocyte-az": 0.3911669992181576,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6561949895279332,
    "tdcommons/half-life-obach": 0.3151403639219791,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4343473790139429,
    "tdcommons/clearance-microsome-az": 0.5881516023256164,
    "tdcommons/dili": 0.9282608695652174,
    "tdcommons/bioavailability-ma": 0.6185567010309279,
    "tdcommons/vdss-lombardo": 0.5349170714022574,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6051084990958409,
    "tdcommons/pgp-broccatelli": 0.9348840309250867,
    "tdcommons/caco2-wang": 0.32509597294435616,
    "tdcommons/herg": 0.8574374079528718,
    "tdcommons/bbb-martins": 0.8807457786116322,
    "tdcommons/ames": 0.8379956529401399,
    "tdcommons/ld50-zhu": 0.5086048892670297
}
```
