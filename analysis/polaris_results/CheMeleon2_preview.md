# chemeleon2_preview_initial_training_e4s281344 Baseline Results
timestamp: 2026-05-15 10:47:16.947549
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.834765 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.55864  |
|  2 | test       | CLS_RET        | f1          | 0.625    |
|  3 | test       | CLS_RET        | accuracy    | 0.886792 |
|  4 | test       | CLS_RET        | mcc         | 0.560157 |
|  5 | test       | CLS_RET        | pr_auc      | 0.631734 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.297516 |
|  1 | test       | RET            | explained_var       |   0.333138 |
|  2 | test       | RET            | spearmanr           |   0.58363  |
|  3 | test       | RET            | mean_squared_error  | 834.133    |
|  4 | test       | RET            | mean_absolute_error |  21.345    |
|  5 | test       | RET            | pearsonr            |   0.577539 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.706963 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.340909 |
|  2 | test       | CLS_KIT        | f1          | 0.424242 |
|  3 | test       | CLS_KIT        | accuracy    | 0.836207 |
|  4 | test       | CLS_KIT        | mcc         | 0.368815 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.493386 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.19495  |
|  1 | test       | KIT            | explained_var       |   0.23625  |
|  2 | test       | KIT            | spearmanr           |   0.447731 |
|  3 | test       | KIT            | mean_squared_error  | 971.441    |
|  4 | test       | KIT            | mean_absolute_error |  24.0265   |
|  5 | test       | KIT            | pearsonr            |   0.512544 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.40875  |
|  1 | test       | EGFR           | explained_var       |   0.429519 |
|  2 | test       | EGFR           | spearmanr           |   0.461916 |
|  3 | test       | EGFR           | mean_squared_error  | 476.41     |
|  4 | test       | EGFR           | mean_absolute_error |  17.7403   |
|  5 | test       | EGFR           | pearsonr            |   0.659622 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.318566 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.320226 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.441187 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.369459 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.437851 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.565928 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.202843 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.219574 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.471304 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.70826  |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.67048  |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.493638 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.215021 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.448361 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.680877 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.475414 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.546787 |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.680915 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.493686 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.493717 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.683319 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.250824 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.390598 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.702788 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.438367 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.462014 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.688361 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.317066 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.443418 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.686317 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.398879 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.40015  |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.644579 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.233481 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.374337 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.648787 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.526326 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.41666 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.296141 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.50303 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.208416 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.38236 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.542224 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.897391 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.513801 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.451024 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.558657 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.898827 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.430047 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.770103 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.836304 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.795608 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.611337 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.631734157861344,
    "polaris/pkis2-ret-wt-reg-v2": 834.1325363122577,
    "polaris/pkis2-kit-wt-cls-v2": 0.4933858279817519,
    "polaris/pkis2-kit-wt-reg-v2": 971.4410017468483,
    "polaris/pkis2-egfr-wt-reg-v2": 476.41023211121137,
    "polaris/adme-fang-solu-1": 0.5659277076277539,
    "polaris/adme-fang-rppb-1": 0.4936376294848318,
    "polaris/adme-fang-hppb-1": 0.6809146126726968,
    "polaris/adme-fang-perm-1": 0.7027878775944182,
    "polaris/adme-fang-rclint-1": 0.6863167477932773,
    "polaris/adme-fang-hclint-1": 0.6487871988959685,
    "tdcommons/lipophilicity-astrazeneca": 0.5263261670328322,
    "tdcommons/ppbr-az": 9.4166632440393,
    "tdcommons/clearance-hepatocyte-az": 0.29614137063316276,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5030301237703466,
    "tdcommons/half-life-obach": 0.2084157546950656,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.38236005552250496,
    "tdcommons/clearance-microsome-az": 0.542224156618252,
    "tdcommons/dili": 0.897391304347826,
    "tdcommons/bioavailability-ma": 0.5138011306950448,
    "tdcommons/vdss-lombardo": 0.45102430013705247,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5586573236889693,
    "tdcommons/pgp-broccatelli": 0.8988269794721407,
    "tdcommons/caco2-wang": 0.4300473875900101,
    "tdcommons/herg": 0.7701030927835052,
    "tdcommons/bbb-martins": 0.8363039399624764,
    "tdcommons/ames": 0.7956079030331512,
    "tdcommons/ld50-zhu": 0.6113374760754215
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.83807  |
|  1 | test       | CLS_RET        | cohen_kappa | 0.486766 |
|  2 | test       | CLS_RET        | f1          | 0.571429 |
|  3 | test       | CLS_RET        | accuracy    | 0.858491 |
|  4 | test       | CLS_RET        | mcc         | 0.487051 |
|  5 | test       | CLS_RET        | pr_auc      | 0.692915 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.301522 |
|  1 | test       | RET            | explained_var       |   0.354978 |
|  2 | test       | RET            | spearmanr           |   0.529527 |
|  3 | test       | RET            | mean_squared_error  | 829.376    |
|  4 | test       | RET            | mean_absolute_error |  20.8088   |
|  5 | test       | RET            | pearsonr            |   0.598995 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.767408 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.49892  |
|  2 | test       | CLS_KIT        | f1          | 0.578947 |
|  3 | test       | CLS_KIT        | accuracy    | 0.862069 |
|  4 | test       | CLS_KIT        | mcc         | 0.507968 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.600312 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | r2                  |    0.151493 |
|  1 | test       | KIT            | explained_var       |    0.17317  |
|  2 | test       | KIT            | spearmanr           |    0.444292 |
|  3 | test       | KIT            | mean_squared_error  | 1023.88     |
|  4 | test       | KIT            | mean_absolute_error |   24.3783   |
|  5 | test       | KIT            | pearsonr            |    0.499606 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.354022 |
|  1 | test       | EGFR           | explained_var       |   0.355238 |
|  2 | test       | EGFR           | spearmanr           |   0.25141  |
|  3 | test       | EGFR           | mean_squared_error  | 520.509    |
|  4 | test       | EGFR           | mean_absolute_error |  17.9307   |
|  5 | test       | EGFR           | pearsonr            |   0.600685 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.275748 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.279802 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.455429 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.392674 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.443119 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.534412 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.235277 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.239225 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.445217 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.679443 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.621776 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.490591 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.114944 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.172721 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.622966 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.536024 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.652683 |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.598875 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.578812 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.579422 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.739695 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.208653 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.351389 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.761513 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.463772 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.464246 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.684641 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.302724 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.428863 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.681752 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.357164 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.361407 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.602449 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.249684 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.402313 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.605031 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.502409 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.66588 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.373865 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.634031 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.125874 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.387173 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.587703 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.922609 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.403392 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.273224 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.600701 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.901493 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.372215 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.805302 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.844043 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.800987 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.626099 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6929149100484471,
    "polaris/pkis2-ret-wt-reg-v2": 829.3762125597018,
    "polaris/pkis2-kit-wt-cls-v2": 0.6003117035338268,
    "polaris/pkis2-kit-wt-reg-v2": 1023.8798315894744,
    "polaris/pkis2-egfr-wt-reg-v2": 520.5087059677883,
    "polaris/adme-fang-solu-1": 0.5344118254535447,
    "polaris/adme-fang-rppb-1": 0.4905909961256829,
    "polaris/adme-fang-hppb-1": 0.5988748946627486,
    "polaris/adme-fang-perm-1": 0.7615128189239083,
    "polaris/adme-fang-rclint-1": 0.6817516682557379,
    "polaris/adme-fang-hclint-1": 0.6050310645947233,
    "tdcommons/lipophilicity-astrazeneca": 0.5024090848423185,
    "tdcommons/ppbr-az": 8.665877760612474,
    "tdcommons/clearance-hepatocyte-az": 0.3738645736509408,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6340305227661972,
    "tdcommons/half-life-obach": 0.1258739475572134,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3871731678636915,
    "tdcommons/clearance-microsome-az": 0.5877030024186387,
    "tdcommons/dili": 0.9226086956521738,
    "tdcommons/bioavailability-ma": 0.4033920851346857,
    "tdcommons/vdss-lombardo": 0.27322398363434,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6007007233273056,
    "tdcommons/pgp-broccatelli": 0.9014929352172754,
    "tdcommons/caco2-wang": 0.3722145489149492,
    "tdcommons/herg": 0.8053019145802651,
    "tdcommons/bbb-martins": 0.8440431519699813,
    "tdcommons/ames": 0.8009869000763672,
    "tdcommons/ld50-zhu": 0.626098532203731
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.768011 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.457999 |
|  2 | test       | CLS_RET        | f1          | 0.533333 |
|  3 | test       | CLS_RET        | accuracy    | 0.867925 |
|  4 | test       | CLS_RET        | mcc         | 0.463591 |
|  5 | test       | CLS_RET        | pr_auc      | 0.486337 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.399218 |
|  1 | test       | RET            | explained_var       |   0.416173 |
|  2 | test       | RET            | spearmanr           |   0.634062 |
|  3 | test       | RET            | mean_squared_error  | 713.372    |
|  4 | test       | RET            | mean_absolute_error |  20.3705   |
|  5 | test       | RET            | pearsonr            |   0.65176  |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.803191 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.520925 |
|  2 | test       | CLS_KIT        | f1          | 0.594595 |
|  3 | test       | CLS_KIT        | accuracy    | 0.87069  |
|  4 | test       | CLS_KIT        | mcc         | 0.534453 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.66053  |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.268356 |
|  1 | test       | KIT            | explained_var       |   0.269452 |
|  2 | test       | KIT            | spearmanr           |   0.511173 |
|  3 | test       | KIT            | mean_squared_error  | 882.863    |
|  4 | test       | KIT            | mean_absolute_error |  22.5577   |
|  5 | test       | KIT            | pearsonr            |   0.563699 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.504295 |
|  1 | test       | EGFR           | explained_var       |   0.504297 |
|  2 | test       | EGFR           | spearmanr           |   0.464636 |
|  3 | test       | EGFR           | mean_squared_error  | 399.423    |
|  4 | test       | EGFR           | mean_absolute_error |  15.64     |
|  5 | test       | EGFR           | pearsonr            |   0.710349 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.276556 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.276679 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.487451 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.392236 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.423235 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.55094  |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.197197 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.215503 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.567826 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.713276 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.685198 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.572737 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.198939 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.210224 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.566888 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.485154 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.604827 |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.58492  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.533485 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.533775 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.711765 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.231108 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.370988 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.73067  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.393639 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.394981 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.642506 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.342317 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.470352 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.628666 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.418733 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.424383 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.66825  |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.22577  |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.370417 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.665621 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.535998 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.09007 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.346728 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.724237 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0163686 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.420728 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.544981 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.881739 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.501829 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.407751 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.601153 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.897494 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.356525 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.804418 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.873241 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.798911 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.609052 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.48633698860894087,
    "polaris/pkis2-ret-wt-reg-v2": 713.3717963654312,
    "polaris/pkis2-kit-wt-cls-v2": 0.6605302860322413,
    "polaris/pkis2-kit-wt-reg-v2": 882.8628215113067,
    "polaris/pkis2-egfr-wt-reg-v2": 399.423198468701,
    "polaris/adme-fang-solu-1": 0.5509396335619401,
    "polaris/adme-fang-rppb-1": 0.5727366945675797,
    "polaris/adme-fang-hppb-1": 0.5849201712605034,
    "polaris/adme-fang-perm-1": 0.7306695870742862,
    "polaris/adme-fang-rclint-1": 0.6286663706954321,
    "polaris/adme-fang-hclint-1": 0.6656208511622945,
    "tdcommons/lipophilicity-astrazeneca": 0.5359978542498179,
    "tdcommons/ppbr-az": 9.090067917989275,
    "tdcommons/clearance-hepatocyte-az": 0.3467280997183945,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7242369121938811,
    "tdcommons/half-life-obach": 0.01636855228516125,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4207282002850301,
    "tdcommons/clearance-microsome-az": 0.544981039093573,
    "tdcommons/dili": 0.8817391304347826,
    "tdcommons/bioavailability-ma": 0.5018290655138011,
    "tdcommons/vdss-lombardo": 0.40775064953988954,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6011528028933092,
    "tdcommons/pgp-broccatelli": 0.8974940015995735,
    "tdcommons/caco2-wang": 0.35652457834435775,
    "tdcommons/herg": 0.8044182621502209,
    "tdcommons/bbb-martins": 0.8732410881801125,
    "tdcommons/ames": 0.7989112768998805,
    "tdcommons/ld50-zhu": 0.6090515141474218
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.71844  |
|  1 | test       | CLS_RET        | cohen_kappa | 0        |
|  2 | test       | CLS_RET        | f1          | 0        |
|  3 | test       | CLS_RET        | accuracy    | 0.839623 |
|  4 | test       | CLS_RET        | mcc         | 0        |
|  5 | test       | CLS_RET        | pr_auc      | 0.50881  |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.266834 |
|  1 | test       | RET            | explained_var       |   0.27437  |
|  2 | test       | RET            | spearmanr           |   0.506989 |
|  3 | test       | RET            | mean_squared_error  | 870.565    |
|  4 | test       | RET            | mean_absolute_error |  23.366    |
|  5 | test       | RET            | pearsonr            |   0.536836 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.735977 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.437755 |
|  2 | test       | CLS_KIT        | f1          | 0.536585 |
|  3 | test       | CLS_KIT        | accuracy    | 0.836207 |
|  4 | test       | CLS_KIT        | mcc         | 0.43949  |
|  5 | test       | CLS_KIT        | pr_auc      | 0.563384 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.254005 |
|  1 | test       | KIT            | explained_var       |   0.287478 |
|  2 | test       | KIT            | spearmanr           |   0.500203 |
|  3 | test       | KIT            | mean_squared_error  | 900.181    |
|  4 | test       | KIT            | mean_absolute_error |  22.758    |
|  5 | test       | KIT            | pearsonr            |   0.560796 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.449872 |
|  1 | test       | EGFR           | explained_var       |   0.451331 |
|  2 | test       | EGFR           | spearmanr           |   0.415981 |
|  3 | test       | EGFR           | mean_squared_error  | 443.276    |
|  4 | test       | EGFR           | mean_absolute_error |  15.9841   |
|  5 | test       | EGFR           | pearsonr            |   0.674959 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.304472 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.31251  |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.487405 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.377101 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.403612 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.559141 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.30032  |
|  1 | test       | LOG_RPPB       | explained_var       | 0.363881 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.606957 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.621653 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.637591 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.629524 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.0974331 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.256243  |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.614409  |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.546629  |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.657322  |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.586755  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.39606  |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.456753 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.659367 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.299187 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.45257  |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.676182 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.431407 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.43166  |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.661651 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.320995 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.45194  |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.658692 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.39897  |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.405909 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.640536 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.233446 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.37174  |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.65325  |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.549252 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.84067 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.334694 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.589779 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.043369 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.411475 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.609031 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.875652 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.411041 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.27711 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.613359 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.903692 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.337978 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.798233 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.865287 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.796489 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.61761 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.508809578886136,
    "polaris/pkis2-ret-wt-reg-v2": 870.5653974608298,
    "polaris/pkis2-kit-wt-cls-v2": 0.5633836719832684,
    "polaris/pkis2-kit-wt-reg-v2": 900.1807888478829,
    "polaris/pkis2-egfr-wt-reg-v2": 443.2760872617463,
    "polaris/adme-fang-solu-1": 0.5591412826849863,
    "polaris/adme-fang-rppb-1": 0.629523976939815,
    "polaris/adme-fang-hppb-1": 0.5867547100985387,
    "polaris/adme-fang-perm-1": 0.6761822135828652,
    "polaris/adme-fang-rclint-1": 0.6586920262360325,
    "polaris/adme-fang-hclint-1": 0.6532499129786657,
    "tdcommons/lipophilicity-astrazeneca": 0.5492519997528621,
    "tdcommons/ppbr-az": 8.840673553794359,
    "tdcommons/clearance-hepatocyte-az": 0.33469429406592854,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5897786595958473,
    "tdcommons/half-life-obach": 0.0433689805069963,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4114751723575775,
    "tdcommons/clearance-microsome-az": 0.6090310727903946,
    "tdcommons/dili": 0.8756521739130435,
    "tdcommons/bioavailability-ma": 0.41104090455603587,
    "tdcommons/vdss-lombardo": 0.2771101853087947,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.613358951175407,
    "tdcommons/pgp-broccatelli": 0.9036923487070114,
    "tdcommons/caco2-wang": 0.33797807334386804,
    "tdcommons/herg": 0.7982326951399116,
    "tdcommons/bbb-martins": 0.8652868980612882,
    "tdcommons/ames": 0.796489063815622,
    "tdcommons/ld50-zhu": 0.6176095306515209
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.828817 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.434164 |
|  2 | test       | CLS_RET        | f1          | 0.516129 |
|  3 | test       | CLS_RET        | accuracy    | 0.858491 |
|  4 | test       | CLS_RET        | mcc         | 0.436971 |
|  5 | test       | CLS_RET        | pr_auc      | 0.524019 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.221005 |
|  1 | test       | RET            | explained_var       |   0.241678 |
|  2 | test       | RET            | spearmanr           |   0.512685 |
|  3 | test       | RET            | mean_squared_error  | 924.983    |
|  4 | test       | RET            | mean_absolute_error |  22.5379   |
|  5 | test       | RET            | pearsonr            |   0.491925 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.769342 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.410287 |
|  2 | test       | CLS_KIT        | f1          | 0.484848 |
|  3 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  4 | test       | CLS_KIT        | mcc         | 0.443872 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.61099  |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.224198 |
|  1 | test       | KIT            | explained_var       |   0.237532 |
|  2 | test       | KIT            | spearmanr           |   0.432683 |
|  3 | test       | KIT            | mean_squared_error  | 936.148    |
|  4 | test       | KIT            | mean_absolute_error |  23.8269   |
|  5 | test       | KIT            | pearsonr            |   0.525981 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | EGFR           | r2                  |   0.0434612 |
|  1 | test       | EGFR           | explained_var       |   0.0940173 |
|  2 | test       | EGFR           | spearmanr           |   0.200595  |
|  3 | test       | EGFR           | mean_squared_error  | 770.749     |
|  4 | test       | EGFR           | mean_absolute_error |  23.1582    |
|  5 | test       | EGFR           | pearsonr            |   0.306815  |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.327821 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.339709 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.482285 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.364441 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.394653 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.585331 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.246103 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.2691   |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.686957 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.669824 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.649318 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.637838 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.371489 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.549998 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.752846 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.380651 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.506902 |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.74928  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.481737 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.512348 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.698595 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.256744 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.404241 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.718517 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.427045 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.427069 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.660188 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.323458 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.450376 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.654173 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.388486 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.401867 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.633219 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.237518 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.376188 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.646443 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.499637 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.86031 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.424879 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.632161 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |      Score |
|---:|:-----------|:---------------|:----------|-----------:|
|  0 | test       | Y              | spearmanr | -0.0391494 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.472281 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.593186 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.905652 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.482208 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.371367 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.602396 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.903959 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.317163 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.801031 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.888329 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.805032 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.622407 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5240188168229074,
    "polaris/pkis2-ret-wt-reg-v2": 924.9825643683666,
    "polaris/pkis2-kit-wt-cls-v2": 0.610990011812585,
    "polaris/pkis2-kit-wt-reg-v2": 936.1477002913269,
    "polaris/pkis2-egfr-wt-reg-v2": 770.7487829866209,
    "polaris/adme-fang-solu-1": 0.5853308599721363,
    "polaris/adme-fang-rppb-1": 0.6378382578985033,
    "polaris/adme-fang-hppb-1": 0.7492804283532941,
    "polaris/adme-fang-perm-1": 0.7185165688755576,
    "polaris/adme-fang-rclint-1": 0.6541729140478848,
    "polaris/adme-fang-hclint-1": 0.6464434104146717,
    "tdcommons/lipophilicity-astrazeneca": 0.49963665423506787,
    "tdcommons/ppbr-az": 8.860306795287432,
    "tdcommons/clearance-hepatocyte-az": 0.4248794723044446,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6321613785994613,
    "tdcommons/half-life-obach": -0.039149353651580045,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.47228052548016547,
    "tdcommons/clearance-microsome-az": 0.5931857786216861,
    "tdcommons/dili": 0.9056521739130435,
    "tdcommons/bioavailability-ma": 0.4822081809112072,
    "tdcommons/vdss-lombardo": 0.3713665926732947,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6023960216998192,
    "tdcommons/pgp-broccatelli": 0.9039589442815248,
    "tdcommons/caco2-wang": 0.3171634908140749,
    "tdcommons/herg": 0.8010309278350516,
    "tdcommons/bbb-martins": 0.8883286429018137,
    "tdcommons/ames": 0.8050324071354442,
    "tdcommons/ld50-zhu": 0.6224074998650403
}
```
