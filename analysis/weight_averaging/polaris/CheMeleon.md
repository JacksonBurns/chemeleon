# ChemProp Baseline Results
timestamp: 2025-04-28 21:37:47.825214
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.531761 |
|  1 | test       | CLS_RET        | accuracy    | 0.839623 |
|  2 | test       | CLS_RET        | f1          | 0        |
|  3 | test       | CLS_RET        | cohen_kappa | 0        |
|  4 | test       | CLS_RET        | mcc         | 0        |
|  5 | test       | CLS_RET        | roc_auc     | 0.84534  |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.493314 |
|  1 | test       | RET            | pearsonr            |   0.709821 |
|  2 | test       | RET            | mean_absolute_error |  19.7225   |
|  3 | test       | RET            | spearmanr           |   0.636467 |
|  4 | test       | RET            | mean_squared_error  | 710.026    |
|  5 | test       | RET            | r2                  |   0.402035 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.709325 |
|  1 | test       | CLS_KIT        | accuracy    | 0.827586 |
|  2 | test       | CLS_KIT        | f1          | 0.230769 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.183099 |
|  4 | test       | CLS_KIT        | mcc         | 0.270121 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.84236  |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.380452 |
|  1 | test       | KIT            | pearsonr            |   0.627581 |
|  2 | test       | KIT            | mean_absolute_error |  21.2556   |
|  3 | test       | KIT            | spearmanr           |   0.556403 |
|  4 | test       | KIT            | mean_squared_error  | 763.734    |
|  5 | test       | KIT            | r2                  |   0.367081 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.438702 |
|  1 | test       | EGFR           | pearsonr            |   0.662988 |
|  2 | test       | EGFR           | mean_absolute_error |  17.8803   |
|  3 | test       | EGFR           | spearmanr           |   0.359461 |
|  4 | test       | EGFR           | mean_squared_error  | 485.443    |
|  5 | test       | EGFR           | r2                  |   0.39754  |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.424938 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.653649 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.371633 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.5568   |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.314718 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.419531 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.476103 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.707071 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.510989 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.78     |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.465503 |
|  5 | test       | LOG_RPPB       | r2                  | 0.47607  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.603335 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.780189 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.433632 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.746734 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.265172 |
|  5 | test       | LOG_HPPB       | r2                  | 0.562162 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.628472 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.792771 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.315529 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.785116 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.184735 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.627093 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.547699 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.741159 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.401377 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.748809 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.257651 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.543611 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.508836 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.716771 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.345089 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.71712  |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.194371 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.499573 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.45552 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.82584 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.407446 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.649098 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.297275 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.414619 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.605812 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.914783 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.580313 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.565279 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.616184 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.924087 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.405806 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.879381 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.880159 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.840622 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.517861 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5317612155073456,
    "polaris/pkis2-ret-wt-reg-v2": 710.0262995116599,
    "polaris/pkis2-kit-wt-cls-v2": 0.7093246006115614,
    "polaris/pkis2-kit-wt-reg-v2": 763.7338096098343,
    "polaris/pkis2-egfr-wt-reg-v2": 485.44344482812215,
    "polaris/adme-fang-solu-1": 0.6536492133297891,
    "polaris/adme-fang-rppb-1": 0.7070708728807016,
    "polaris/adme-fang-hppb-1": 0.780188627983479,
    "polaris/adme-fang-perm-1": 0.7927713240681578,
    "polaris/adme-fang-rclint-1": 0.7411589637767434,
    "polaris/adme-fang-hclint-1": 0.7167710317978941,
    "tdcommons/lipophilicity-astrazeneca": 0.45552008050963994,
    "tdcommons/ppbr-az": 7.825839714910134,
    "tdcommons/clearance-hepatocyte-az": 0.40744604550529934,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6490982528346334,
    "tdcommons/half-life-obach": 0.29727508394543817,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4146191937388589,
    "tdcommons/clearance-microsome-az": 0.6058123983049616,
    "tdcommons/dili": 0.9147826086956522,
    "tdcommons/bioavailability-ma": 0.5803126039241768,
    "tdcommons/vdss-lombardo": 0.5652787574255806,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6161844484629294,
    "tdcommons/pgp-broccatelli": 0.9240869101572914,
    "tdcommons/caco2-wang": 0.4058060832946107,
    "tdcommons/herg": 0.8793814432989691,
    "tdcommons/bbb-martins": 0.8801594746716698,
    "tdcommons/ames": 0.8406224911394389,
    "tdcommons/ld50-zhu": 0.5178606170969178
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.608151 |
|  1 | test       | CLS_RET        | accuracy    | 0.839623 |
|  2 | test       | CLS_RET        | f1          | 0        |
|  3 | test       | CLS_RET        | cohen_kappa | 0        |
|  4 | test       | CLS_RET        | mcc         | 0        |
|  5 | test       | CLS_RET        | roc_auc     | 0.841375 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.555964 |
|  1 | test       | RET            | pearsonr            |   0.75174  |
|  2 | test       | RET            | mean_absolute_error |  17.7473   |
|  3 | test       | RET            | spearmanr           |   0.683811 |
|  4 | test       | RET            | mean_squared_error  | 561.61     |
|  5 | test       | RET            | r2                  |   0.527027 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.686911 |
|  1 | test       | CLS_KIT        | accuracy    | 0.818966 |
|  2 | test       | CLS_KIT        | f1          | 0.571429 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.458185 |
|  4 | test       | CLS_KIT        | mcc         | 0.462046 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.843327 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.335478 |
|  1 | test       | KIT            | pearsonr            |   0.602646 |
|  2 | test       | KIT            | mean_absolute_error |  21.1921   |
|  3 | test       | KIT            | spearmanr           |   0.56388  |
|  4 | test       | KIT            | mean_squared_error  | 825.729    |
|  5 | test       | KIT            | r2                  |   0.315704 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.419264 |
|  1 | test       | EGFR           | pearsonr            |   0.64767  |
|  2 | test       | EGFR           | mean_absolute_error |  16.8415   |
|  3 | test       | EGFR           | spearmanr           |   0.336134 |
|  4 | test       | EGFR           | mean_squared_error  | 470.642    |
|  5 | test       | EGFR           | r2                  |   0.415909 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.446941 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.668539 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.368993 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.591982 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.299857 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.44694  |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.646602 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.830866 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.433681 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.81913  |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.316352 |
|  5 | test       | LOG_RPPB       | r2                  | 0.643941 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.541093 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.74104  |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.443376 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.713423 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.27825  |
|  5 | test       | LOG_HPPB       | r2                  | 0.540568 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.661674 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.813951 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.291911 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.809296 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.167609 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.661665 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.550877 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.742729 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.398225 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.744674 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.253819 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.550399 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.504391 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.713363 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.34208  |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.712826 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.194493 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.499258 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  0.4526 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  7.7239 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.401599 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.714902 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.291151 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.420967 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.629359 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.922609 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.551048 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.546659 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.612568 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.93655 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.347382 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.859352 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.899703 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.854362 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.543919 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6081510032034985,
    "polaris/pkis2-ret-wt-reg-v2": 561.6101160284434,
    "polaris/pkis2-kit-wt-cls-v2": 0.6869107409279265,
    "polaris/pkis2-kit-wt-reg-v2": 825.7285050373783,
    "polaris/pkis2-egfr-wt-reg-v2": 470.6422665049618,
    "polaris/adme-fang-solu-1": 0.6685387371281728,
    "polaris/adme-fang-rppb-1": 0.8308656047669836,
    "polaris/adme-fang-hppb-1": 0.741039610528003,
    "polaris/adme-fang-perm-1": 0.8139506884258298,
    "polaris/adme-fang-rclint-1": 0.7427290708544603,
    "polaris/adme-fang-hclint-1": 0.7133627139485433,
    "tdcommons/lipophilicity-astrazeneca": 0.4525998963117599,
    "tdcommons/ppbr-az": 7.723902495082249,
    "tdcommons/clearance-hepatocyte-az": 0.40159879139889854,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7149021430777118,
    "tdcommons/half-life-obach": 0.29115060403645315,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.42096676248632114,
    "tdcommons/clearance-microsome-az": 0.6293593687991198,
    "tdcommons/dili": 0.922608695652174,
    "tdcommons/bioavailability-ma": 0.5510475557033588,
    "tdcommons/vdss-lombardo": 0.5466590234966974,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6125678119349005,
    "tdcommons/pgp-broccatelli": 0.9365502532657958,
    "tdcommons/caco2-wang": 0.3473817895933047,
    "tdcommons/herg": 0.8593519882179677,
    "tdcommons/bbb-martins": 0.8997029393370857,
    "tdcommons/ames": 0.8543617458732303,
    "tdcommons/ld50-zhu": 0.5439187263126142
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.640322 |
|  1 | test       | CLS_RET        | accuracy    | 0.839623 |
|  2 | test       | CLS_RET        | f1          | 0        |
|  3 | test       | CLS_RET        | cohen_kappa | 0        |
|  4 | test       | CLS_RET        | mcc         | 0        |
|  5 | test       | CLS_RET        | roc_auc     | 0.861864 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.484587 |
|  1 | test       | RET            | pearsonr            |   0.703488 |
|  2 | test       | RET            | mean_absolute_error |  19.2485   |
|  3 | test       | RET            | spearmanr           |   0.66224  |
|  4 | test       | RET            | mean_squared_error  | 641.2      |
|  5 | test       | RET            | r2                  |   0.459999 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.62661  |
|  1 | test       | CLS_KIT        | accuracy    | 0.836207 |
|  2 | test       | CLS_KIT        | f1          | 0.24     |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.203757 |
|  4 | test       | CLS_KIT        | mcc         | 0.336801 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.838008 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.320478 |
|  1 | test       | KIT            | pearsonr            |   0.593278 |
|  2 | test       | KIT            | mean_absolute_error |  22.0735   |
|  3 | test       | KIT            | spearmanr           |   0.545657 |
|  4 | test       | KIT            | mean_squared_error  | 820.528    |
|  5 | test       | KIT            | r2                  |   0.320014 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.439134 |
|  1 | test       | EGFR           | pearsonr            |   0.672784 |
|  2 | test       | EGFR           | mean_absolute_error |  16.8102   |
|  3 | test       | EGFR           | spearmanr           |   0.371282 |
|  4 | test       | EGFR           | mean_squared_error  | 452.034    |
|  5 | test       | EGFR           | r2                  |   0.439002 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.400665 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.634649 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.383659 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.542921 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.325254 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.400099 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.623201 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.818279 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.426349 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.833913 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.334801 |
|  5 | test       | LOG_RPPB       | r2                  | 0.623176 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.613447 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.783672 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.441108 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.777447 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.265076 |
|  5 | test       | LOG_HPPB       | r2                  | 0.562321 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.633714 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.796288 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.310795 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.792671 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.182867 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.630865 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.55365  |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.744171 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.396892 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.744066 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.252388 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.552934 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.497232 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.713181 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.344226 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.719971 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.196406 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.494333 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.463681 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.05622 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.29365 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.701534 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.343693 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.431409 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.592912 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.888261 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.578317 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.542815 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.612794 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.929552 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.418196 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.860236 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.90283 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.84338 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.515131 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6403218252177856,
    "polaris/pkis2-ret-wt-reg-v2": 641.2001377701413,
    "polaris/pkis2-kit-wt-cls-v2": 0.6266104090655296,
    "polaris/pkis2-kit-wt-reg-v2": 820.5279427963466,
    "polaris/pkis2-egfr-wt-reg-v2": 452.0344983362219,
    "polaris/adme-fang-solu-1": 0.6346485607975018,
    "polaris/adme-fang-rppb-1": 0.8182788023318975,
    "polaris/adme-fang-hppb-1": 0.7836716148643688,
    "polaris/adme-fang-perm-1": 0.796287971929639,
    "polaris/adme-fang-rclint-1": 0.7441712499206925,
    "polaris/adme-fang-hclint-1": 0.7131814694684162,
    "tdcommons/lipophilicity-astrazeneca": 0.4636812979607355,
    "tdcommons/ppbr-az": 8.056217212711122,
    "tdcommons/clearance-hepatocyte-az": 0.293650393726857,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7015338307210306,
    "tdcommons/half-life-obach": 0.3436928366925081,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4314085494236235,
    "tdcommons/clearance-microsome-az": 0.5929123534533197,
    "tdcommons/dili": 0.8882608695652174,
    "tdcommons/bioavailability-ma": 0.5783172597273031,
    "tdcommons/vdss-lombardo": 0.5428147850578094,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6127938517179025,
    "tdcommons/pgp-broccatelli": 0.9295521194348174,
    "tdcommons/caco2-wang": 0.4181962071691157,
    "tdcommons/herg": 0.8602356406480118,
    "tdcommons/bbb-martins": 0.9028298936835523,
    "tdcommons/ames": 0.8433795453210362,
    "tdcommons/ld50-zhu": 0.5151310881490797
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.548253 |
|  1 | test       | CLS_RET        | accuracy    | 0.839623 |
|  2 | test       | CLS_RET        | f1          | 0        |
|  3 | test       | CLS_RET        | cohen_kappa | 0        |
|  4 | test       | CLS_RET        | mcc         | 0        |
|  5 | test       | CLS_RET        | roc_auc     | 0.808989 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.519593 |
|  1 | test       | RET            | pearsonr            |   0.72371  |
|  2 | test       | RET            | mean_absolute_error |  18.4861   |
|  3 | test       | RET            | spearmanr           |   0.634082 |
|  4 | test       | RET            | mean_squared_error  | 611.952    |
|  5 | test       | RET            | r2                  |   0.48463  |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.705488 |
|  1 | test       | CLS_KIT        | accuracy    | 0.818966 |
|  2 | test       | CLS_KIT        | f1          | 0.588235 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.475    |
|  4 | test       | CLS_KIT        | mcc         | 0.482445 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.818182 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.390769 |
|  1 | test       | KIT            | pearsonr            |   0.637728 |
|  2 | test       | KIT            | mean_absolute_error |  20.5781   |
|  3 | test       | KIT            | spearmanr           |   0.569894 |
|  4 | test       | KIT            | mean_squared_error  | 757.482    |
|  5 | test       | KIT            | r2                  |   0.372261 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.399283 |
|  1 | test       | EGFR           | pearsonr            |   0.650581 |
|  2 | test       | EGFR           | mean_absolute_error |  17.0088   |
|  3 | test       | EGFR           | spearmanr           |   0.337824 |
|  4 | test       | EGFR           | mean_squared_error  | 489.633    |
|  5 | test       | EGFR           | r2                  |   0.39234  |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.413863 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.645009 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.370036 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.56149  |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.318616 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.412342 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.481086 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.791308 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.555247 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.794783 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.461791 |
|  5 | test       | LOG_RPPB       | r2                  | 0.480247 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.564681 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.759798 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.512617 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.737871 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.341298 |
|  5 | test       | LOG_HPPB       | r2                  | 0.436465 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.676737 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.823254 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.292657 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.815289 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.160722 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.675566 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.560979 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.749085 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.392656 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.753029 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.248323 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.560134 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.525685 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.727528 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.331842 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.727949 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.186576 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.519641 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.462026 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.66818 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.399729 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.621876 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.351131 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.422476 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.589296 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.85913 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.574327 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.536187 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.592224 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.910091 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.350351 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.88056 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.877853 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.846233 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.521175 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5482528192999347,
    "polaris/pkis2-ret-wt-reg-v2": 611.9523863815442,
    "polaris/pkis2-kit-wt-cls-v2": 0.7054883965359975,
    "polaris/pkis2-kit-wt-reg-v2": 757.4821917636548,
    "polaris/pkis2-egfr-wt-reg-v2": 489.6330645457561,
    "polaris/adme-fang-solu-1": 0.6450086396884953,
    "polaris/adme-fang-rppb-1": 0.791307506847921,
    "polaris/adme-fang-hppb-1": 0.7597979594636685,
    "polaris/adme-fang-perm-1": 0.8232539216979715,
    "polaris/adme-fang-rclint-1": 0.749084690172475,
    "polaris/adme-fang-hclint-1": 0.7275277687194579,
    "tdcommons/lipophilicity-astrazeneca": 0.4620257613261541,
    "tdcommons/ppbr-az": 7.668181763241243,
    "tdcommons/clearance-hepatocyte-az": 0.3997291117476971,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6218755362650977,
    "tdcommons/half-life-obach": 0.3511311786321325,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.42247572891322843,
    "tdcommons/clearance-microsome-az": 0.5892957733006992,
    "tdcommons/dili": 0.8591304347826088,
    "tdcommons/bioavailability-ma": 0.5743265713335551,
    "tdcommons/vdss-lombardo": 0.5361865278279186,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5922242314647379,
    "tdcommons/pgp-broccatelli": 0.9100906424953346,
    "tdcommons/caco2-wang": 0.35035140581685165,
    "tdcommons/herg": 0.880559646539028,
    "tdcommons/bbb-martins": 0.8778533458411507,
    "tdcommons/ames": 0.8462325481211694,
    "tdcommons/ld50-zhu": 0.5211747007363543
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.594504 |
|  1 | test       | CLS_RET        | accuracy    | 0.839623 |
|  2 | test       | CLS_RET        | f1          | 0        |
|  3 | test       | CLS_RET        | cohen_kappa | 0        |
|  4 | test       | CLS_RET        | mcc         | 0        |
|  5 | test       | CLS_RET        | roc_auc     | 0.836748 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.445614 |
|  1 | test       | RET            | pearsonr            |   0.670922 |
|  2 | test       | RET            | mean_absolute_error |  20.3461   |
|  3 | test       | RET            | spearmanr           |   0.633687 |
|  4 | test       | RET            | mean_squared_error  | 664.25     |
|  5 | test       | RET            | r2                  |   0.440586 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.737108 |
|  1 | test       | CLS_KIT        | accuracy    | 0.87931  |
|  2 | test       | CLS_KIT        | f1          | 0.631579 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.561555 |
|  4 | test       | CLS_KIT        | mcc         | 0.571739 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.865087 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.336942 |
|  1 | test       | KIT            | pearsonr            |   0.59362  |
|  2 | test       | KIT            | mean_absolute_error |  21.7072   |
|  3 | test       | KIT            | spearmanr           |   0.532432 |
|  4 | test       | KIT            | mean_squared_error  | 832.23     |
|  5 | test       | KIT            | r2                  |   0.310316 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.404601 |
|  1 | test       | EGFR           | pearsonr            |   0.636359 |
|  2 | test       | EGFR           | mean_absolute_error |  16.9582   |
|  3 | test       | EGFR           | spearmanr           |   0.391001 |
|  4 | test       | EGFR           | mean_squared_error  | 481.225    |
|  5 | test       | EGFR           | r2                  |   0.402776 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.45759  |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.676851 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.367986 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.571987 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.296613 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.452924 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.519618 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.792607 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.548085 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.82     |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.447034 |
|  5 | test       | LOG_RPPB       | r2                  | 0.496856 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.524027 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.733018 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.483017 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.729162 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.312347 |
|  5 | test       | LOG_HPPB       | r2                  | 0.484269 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.633324 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.796132 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.305457 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.791481 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.181945 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.632726 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.568456 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.754079 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.388338 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.758999 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.243668 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.56838  |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.51219  |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.720122 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.331272 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.721771 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.190262 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.510151 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.444617 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.80289 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.402595 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.652448 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.339788 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.43875 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.599766 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.922609 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.610575 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.536802 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.613246 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.934151 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.355979 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.855817 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.869098 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.851019 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.53636 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5945037187051706,
    "polaris/pkis2-ret-wt-reg-v2": 664.25045522087,
    "polaris/pkis2-kit-wt-cls-v2": 0.7371076596000532,
    "polaris/pkis2-kit-wt-reg-v2": 832.2304574484438,
    "polaris/pkis2-egfr-wt-reg-v2": 481.22461955817533,
    "polaris/adme-fang-solu-1": 0.6768512300853301,
    "polaris/adme-fang-rppb-1": 0.7926067862358107,
    "polaris/adme-fang-hppb-1": 0.7330177969647812,
    "polaris/adme-fang-perm-1": 0.796131616717727,
    "polaris/adme-fang-rclint-1": 0.7540787213203008,
    "polaris/adme-fang-hclint-1": 0.7201224436011495,
    "tdcommons/lipophilicity-astrazeneca": 0.44461670050734564,
    "tdcommons/ppbr-az": 7.80288519106952,
    "tdcommons/clearance-hepatocyte-az": 0.4025948972482501,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6524479568457082,
    "tdcommons/half-life-obach": 0.33978790147375665,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.43874957502411227,
    "tdcommons/clearance-microsome-az": 0.5997660171292877,
    "tdcommons/dili": 0.922608695652174,
    "tdcommons/bioavailability-ma": 0.610575324243432,
    "tdcommons/vdss-lombardo": 0.5368017810384472,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.613245931283906,
    "tdcommons/pgp-broccatelli": 0.9341508930951746,
    "tdcommons/caco2-wang": 0.35597873534294383,
    "tdcommons/herg": 0.8558173784977908,
    "tdcommons/bbb-martins": 0.8690978736710445,
    "tdcommons/ames": 0.8510192093050579,
    "tdcommons/ld50-zhu": 0.5363596582980538
}
```
