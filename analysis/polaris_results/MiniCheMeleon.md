# ChemProp Baseline Results
timestamp: 2026-09-14 15:36:37.143141
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.858491 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.288272 |
|  2 | test       | CLS_RET        | f1          | 0.347826 |
|  3 | test       | CLS_RET        | roc_auc     | 0.872439 |
|  4 | test       | CLS_RET        | pr_auc      | 0.654254 |
|  5 | test       | CLS_RET        | mcc         | 0.337956 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.247297 |
|  1 | test       | RET            | mean_absolute_error |  23.7374   |
|  2 | test       | RET            | r2                  |   0.236119 |
|  3 | test       | RET            | mean_squared_error  | 907.036    |
|  4 | test       | RET            | pearsonr            |   0.500899 |
|  5 | test       | RET            | spearmanr           |   0.502124 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.827586 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.22252  |
|  2 | test       | CLS_KIT        | f1          | 0.285714 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.845261 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.630068 |
|  5 | test       | CLS_KIT        | mcc         | 0.284178 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.380054 |
|  1 | test       | KIT            | mean_absolute_error |  20.8344   |
|  2 | test       | KIT            | r2                  |   0.359407 |
|  3 | test       | KIT            | mean_squared_error  | 772.993    |
|  4 | test       | KIT            | pearsonr            |   0.625747 |
|  5 | test       | KIT            | spearmanr           |   0.563626 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.414104 |
|  1 | test       | EGFR           | mean_absolute_error |  16.8591   |
|  2 | test       | EGFR           | r2                  |   0.413382 |
|  3 | test       | EGFR           | mean_squared_error  | 472.678    |
|  4 | test       | EGFR           | pearsonr            |   0.644084 |
|  5 | test       | EGFR           | spearmanr           |   0.330845 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.396594 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.391912 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.392699 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.329265 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.630429 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.520263 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.328295 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.530954 |
|  2 | test       | LOG_RPPB       | r2                  | 0.327266 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.597712 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.576176 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.657391 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.3476   |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.529697 |
|  2 | test       | LOG_HPPB       | r2                  | 0.305847 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.420406 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.667989 |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.668653 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.611818 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.326315 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.609337 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.193532 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.782361 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.79209  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.507746 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.424751 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.493555 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.28591  |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.715484 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.725121 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.455049 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.358242 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.455047 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.211665 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.693363 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.701853 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.452989 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.16276 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.434609 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.552229 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.291717 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.398963 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.624319 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.905652 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.515464 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.566013 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.573124 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.916356 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.318565 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.85729 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.883873 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.844246 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.530698 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6542536536332592,
    "polaris/pkis2-ret-wt-reg-v2": 907.0360884366381,
    "polaris/pkis2-kit-wt-cls-v2": 0.6300680727079923,
    "polaris/pkis2-kit-wt-reg-v2": 772.993149290519,
    "polaris/pkis2-egfr-wt-reg-v2": 472.67847781128006,
    "polaris/adme-fang-solu-1": 0.6304293704981224,
    "polaris/adme-fang-rppb-1": 0.5761759846515828,
    "polaris/adme-fang-hppb-1": 0.6679892274050949,
    "polaris/adme-fang-perm-1": 0.7823609087094935,
    "polaris/adme-fang-rclint-1": 0.7154844094368781,
    "polaris/adme-fang-hclint-1": 0.6933631006340434,
    "tdcommons/lipophilicity-astrazeneca": 0.4529891844306673,
    "tdcommons/ppbr-az": 8.162759434080721,
    "tdcommons/clearance-hepatocyte-az": 0.4346091640675435,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5522287485444232,
    "tdcommons/half-life-obach": 0.29171682169719204,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.39896277573235545,
    "tdcommons/clearance-microsome-az": 0.624318887117569,
    "tdcommons/dili": 0.9056521739130434,
    "tdcommons/bioavailability-ma": 0.5154639175257731,
    "tdcommons/vdss-lombardo": 0.5660132954802323,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.573123869801085,
    "tdcommons/pgp-broccatelli": 0.916355638496401,
    "tdcommons/caco2-wang": 0.31856524820167637,
    "tdcommons/herg": 0.8572901325478645,
    "tdcommons/bbb-martins": 0.8838727329580988,
    "tdcommons/ames": 0.8442460200904659,
    "tdcommons/ld50-zhu": 0.5306984867830237
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.839623 |
|  1 | test       | CLS_RET        | cohen_kappa | 0        |
|  2 | test       | CLS_RET        | f1          | 0        |
|  3 | test       | CLS_RET        | roc_auc     | 0.785856 |
|  4 | test       | CLS_RET        | pr_auc      | 0.495969 |
|  5 | test       | CLS_RET        | mcc         | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.383766 |
|  1 | test       | RET            | mean_absolute_error |  21.4595   |
|  2 | test       | RET            | r2                  |   0.368895 |
|  3 | test       | RET            | mean_squared_error  | 749.378    |
|  4 | test       | RET            | pearsonr            |   0.628333 |
|  5 | test       | RET            | spearmanr           |   0.615741 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.836207 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.368119 |
|  2 | test       | CLS_KIT        | f1          | 0.457143 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.827853 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.65221  |
|  5 | test       | CLS_KIT        | mcc         | 0.385806 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.308637 |
|  1 | test       | KIT            | mean_absolute_error |  21.6413   |
|  2 | test       | KIT            | r2                  |   0.2949   |
|  3 | test       | KIT            | mean_squared_error  | 850.833    |
|  4 | test       | KIT            | pearsonr            |   0.591899 |
|  5 | test       | KIT            | spearmanr           |   0.568458 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.400966 |
|  1 | test       | EGFR           | mean_absolute_error |  16.8287   |
|  2 | test       | EGFR           | r2                  |   0.381388 |
|  3 | test       | EGFR           | mean_squared_error  | 498.458    |
|  4 | test       | EGFR           | pearsonr            |   0.637753 |
|  5 | test       | EGFR           | spearmanr           |   0.319236 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.402533 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.419603 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.394305 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.328395 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.636501 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.548309 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.506465 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.492679 |
|  2 | test       | LOG_RPPB       | r2                  | 0.506251 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.438687 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.721598 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.768696 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.425209 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.555817 |
|  2 | test       | LOG_HPPB       | r2                  | 0.256976 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.450004 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.664292 |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.674612 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.627545 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.321005 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.627527 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.18452  |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.793579 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.797834 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.512489 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.424216 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.508799 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.277304 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.716043 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.726161 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.461356 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.363541 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.455277 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.211576 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.689017 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.699438 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.442658 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.39371 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.395943 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.743528 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.198378 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.43083 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.617324 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.927391 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.467243 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.562002 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.586686 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.929286 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.350153 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.842857 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.894035 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.824218 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.581079 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.4959690375930785,
    "polaris/pkis2-ret-wt-reg-v2": 749.3776224045953,
    "polaris/pkis2-kit-wt-cls-v2": 0.6522101618873388,
    "polaris/pkis2-kit-wt-reg-v2": 850.8327053675309,
    "polaris/pkis2-egfr-wt-reg-v2": 498.45836096167943,
    "polaris/adme-fang-solu-1": 0.6365014487884583,
    "polaris/adme-fang-rppb-1": 0.7215976814633236,
    "polaris/adme-fang-hppb-1": 0.6642921277811368,
    "polaris/adme-fang-perm-1": 0.7935794318285769,
    "polaris/adme-fang-rclint-1": 0.7160427992889494,
    "polaris/adme-fang-hclint-1": 0.6890165173590018,
    "tdcommons/lipophilicity-astrazeneca": 0.44265769668987814,
    "tdcommons/ppbr-az": 8.393712850444432,
    "tdcommons/clearance-hepatocyte-az": 0.39594292623534966,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7435275062266357,
    "tdcommons/half-life-obach": 0.19837802027861381,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.430830129898371,
    "tdcommons/clearance-microsome-az": 0.6173241570091421,
    "tdcommons/dili": 0.9273913043478261,
    "tdcommons/bioavailability-ma": 0.4672430994346525,
    "tdcommons/vdss-lombardo": 0.5620019275405866,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5866862567811936,
    "tdcommons/pgp-broccatelli": 0.9292855238603039,
    "tdcommons/caco2-wang": 0.3501533667297363,
    "tdcommons/herg": 0.8428571428571429,
    "tdcommons/bbb-martins": 0.8940353345841151,
    "tdcommons/ames": 0.8242182145724412,
    "tdcommons/ld50-zhu": 0.5810786921206927
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.877358 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.453608 |
|  2 | test       | CLS_RET        | f1          | 0.518519 |
|  3 | test       | CLS_RET        | roc_auc     | 0.844679 |
|  4 | test       | CLS_RET        | pr_auc      | 0.63602  |
|  5 | test       | CLS_RET        | mcc         | 0.474614 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.395084 |
|  1 | test       | RET            | mean_absolute_error |  20.3788   |
|  2 | test       | RET            | r2                  |   0.373619 |
|  3 | test       | RET            | mean_squared_error  | 743.768    |
|  4 | test       | RET            | pearsonr            |   0.635059 |
|  5 | test       | RET            | spearmanr           |   0.576623 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.844828 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.332481 |
|  2 | test       | CLS_KIT        | f1          | 0.4      |
|  3 | test       | CLS_KIT        | roc_auc     | 0.84381  |
|  4 | test       | CLS_KIT        | pr_auc      | 0.651346 |
|  5 | test       | CLS_KIT        | mcc         | 0.389019 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.341407 |
|  1 | test       | KIT            | mean_absolute_error |  21.9573   |
|  2 | test       | KIT            | r2                  |   0.337914 |
|  3 | test       | KIT            | mean_squared_error  | 798.929    |
|  4 | test       | KIT            | pearsonr            |   0.595502 |
|  5 | test       | KIT            | spearmanr           |   0.534167 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.446298 |
|  1 | test       | EGFR           | mean_absolute_error |  16.4874   |
|  2 | test       | EGFR           | r2                  |   0.443824 |
|  3 | test       | EGFR           | mean_squared_error  | 448.149    |
|  4 | test       | EGFR           | pearsonr            |   0.670535 |
|  5 | test       | EGFR           | spearmanr           |   0.446847 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.366916 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.396904 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.36532  |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.34411  |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.617937 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.510926 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.54667  |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.428722 |
|  2 | test       | LOG_RPPB       | r2                  | 0.53767  |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.410772 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.769199 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.790435 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.122972  |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.685562  |
|  2 | test       | LOG_HPPB       | r2                  | 0.0271126 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.589218  |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.649981  |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.673084  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.599261 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.339574 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.59379  |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.201233 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.779365 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.796275 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.501988 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.423585 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.500566 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.281952 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.708521 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.708333 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.480772 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.353019 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.478261 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.202649 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.699238 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.704951 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.443978 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.74382 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.36156 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.676349 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0975152 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.373924 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.625995 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.906522 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.451613 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.581212 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.577645 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.917689 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.333837 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.850074 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.903182 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.836688 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.550446 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6360199312946145,
    "polaris/pkis2-ret-wt-reg-v2": 743.7680012543683,
    "polaris/pkis2-kit-wt-cls-v2": 0.6513455586119767,
    "polaris/pkis2-kit-wt-reg-v2": 798.9289340420196,
    "polaris/pkis2-egfr-wt-reg-v2": 448.1488455407627,
    "polaris/adme-fang-solu-1": 0.6179374050632648,
    "polaris/adme-fang-rppb-1": 0.7691989146462169,
    "polaris/adme-fang-hppb-1": 0.6499811699811321,
    "polaris/adme-fang-perm-1": 0.779365217068966,
    "polaris/adme-fang-rclint-1": 0.7085213949673453,
    "polaris/adme-fang-hclint-1": 0.6992377065590448,
    "tdcommons/lipophilicity-astrazeneca": 0.4439784519445329,
    "tdcommons/ppbr-az": 7.743821088487218,
    "tdcommons/clearance-hepatocyte-az": 0.36155983293355287,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6763492831984566,
    "tdcommons/half-life-obach": 0.09751519902314694,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.37392417319219545,
    "tdcommons/clearance-microsome-az": 0.6259952029110873,
    "tdcommons/dili": 0.9065217391304348,
    "tdcommons/bioavailability-ma": 0.45161290322580644,
    "tdcommons/vdss-lombardo": 0.5812117920555936,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5776446654611211,
    "tdcommons/pgp-broccatelli": 0.9176886163689683,
    "tdcommons/caco2-wang": 0.3338366170969534,
    "tdcommons/herg": 0.8500736377025038,
    "tdcommons/bbb-martins": 0.9031816760475295,
    "tdcommons/ames": 0.8366876187119386,
    "tdcommons/ld50-zhu": 0.5504462091532386
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.858491 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.182939 |
|  2 | test       | CLS_RET        | f1          | 0.210526 |
|  3 | test       | CLS_RET        | roc_auc     | 0.888962 |
|  4 | test       | CLS_RET        | pr_auc      | 0.763933 |
|  5 | test       | CLS_RET        | mcc         | 0.317299 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.437186 |
|  1 | test       | RET            | mean_absolute_error |  20.4916   |
|  2 | test       | RET            | r2                  |   0.436909 |
|  3 | test       | RET            | mean_squared_error  | 668.617    |
|  4 | test       | RET            | pearsonr            |   0.661209 |
|  5 | test       | RET            | spearmanr           |   0.58078  |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.87931  |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.52459  |
|  2 | test       | CLS_KIT        | f1          | 0.588235 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.852031 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.716179 |
|  5 | test       | CLS_KIT        | mcc         | 0.557732 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.353888 |
|  1 | test       | KIT            | mean_absolute_error |  21.5564   |
|  2 | test       | KIT            | r2                  |   0.319602 |
|  3 | test       | KIT            | mean_squared_error  | 821.025    |
|  4 | test       | KIT            | pearsonr            |   0.602301 |
|  5 | test       | KIT            | spearmanr           |   0.561452 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.391102 |
|  1 | test       | EGFR           | mean_absolute_error |  17.1569   |
|  2 | test       | EGFR           | r2                  |   0.388456 |
|  3 | test       | EGFR           | mean_squared_error  | 492.763    |
|  4 | test       | EGFR           | pearsonr            |   0.62615  |
|  5 | test       | EGFR           | spearmanr           |   0.318814 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.353717 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.392209 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.334767 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.360675 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.594743 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.52615  |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.250299 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.681513 |
|  2 | test       | LOG_RPPB       | r2                  | 0.215427 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.697079 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.54261  |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.64087  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.444736 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.49989  |
|  2 | test       | LOG_HPPB       | r2                  | 0.357312 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.389237 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.696068 |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.648483 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.61264  |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.341579 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.605081 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.19564  |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.782778 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.804782 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.515868 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.417163 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.515174 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.273706 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.721558 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.727718 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.505319 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.346949 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.505233 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.192172 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.719987 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.728273 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.447477 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.39472 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.436333 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.625768 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.162875 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.396448 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.62404 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.906957 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.552045 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.487288 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.631329 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.911424 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.353924 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.865979 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.893996 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.839862 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.599977 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7639328318740084,
    "polaris/pkis2-ret-wt-reg-v2": 668.6169901466196,
    "polaris/pkis2-kit-wt-cls-v2": 0.7161794044708276,
    "polaris/pkis2-kit-wt-reg-v2": 821.0248176055244,
    "polaris/pkis2-egfr-wt-reg-v2": 492.7631237888853,
    "polaris/adme-fang-solu-1": 0.5947428026177881,
    "polaris/adme-fang-rppb-1": 0.5426103861586902,
    "polaris/adme-fang-hppb-1": 0.6960681855213934,
    "polaris/adme-fang-perm-1": 0.7827784562143681,
    "polaris/adme-fang-rclint-1": 0.7215582437017292,
    "polaris/adme-fang-hclint-1": 0.7199866705603281,
    "tdcommons/lipophilicity-astrazeneca": 0.44747663489409856,
    "tdcommons/ppbr-az": 7.3947175958459415,
    "tdcommons/clearance-hepatocyte-az": 0.43633296611544065,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6257680659888534,
    "tdcommons/half-life-obach": 0.16287493159835903,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3964479074341395,
    "tdcommons/clearance-microsome-az": 0.6240401667933101,
    "tdcommons/dili": 0.9069565217391304,
    "tdcommons/bioavailability-ma": 0.5520452278017959,
    "tdcommons/vdss-lombardo": 0.4872877695309941,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6313291139240506,
    "tdcommons/pgp-broccatelli": 0.9114236203679019,
    "tdcommons/caco2-wang": 0.35392350732556016,
    "tdcommons/herg": 0.865979381443299,
    "tdcommons/bbb-martins": 0.8939962476547842,
    "tdcommons/ames": 0.8398617556639058,
    "tdcommons/ld50-zhu": 0.5999766730713748
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.877358 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.509609 |
|  2 | test       | CLS_RET        | f1          | 0.580645 |
|  3 | test       | CLS_RET        | roc_auc     | 0.846001 |
|  4 | test       | CLS_RET        | pr_auc      | 0.630741 |
|  5 | test       | CLS_RET        | mcc         | 0.512903 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.36316  |
|  1 | test       | RET            | mean_absolute_error |  21.6864   |
|  2 | test       | RET            | r2                  |   0.333743 |
|  3 | test       | RET            | mean_squared_error  | 791.116    |
|  4 | test       | RET            | pearsonr            |   0.602725 |
|  5 | test       | RET            | spearmanr           |   0.586055 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.887931 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.567661 |
|  2 | test       | CLS_KIT        | f1          | 0.628571 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.883946 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.710276 |
|  5 | test       | CLS_KIT        | mcc         | 0.594935 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.332209 |
|  1 | test       | KIT            | mean_absolute_error |  21.8184   |
|  2 | test       | KIT            | r2                  |   0.266306 |
|  3 | test       | KIT            | mean_squared_error  | 885.337    |
|  4 | test       | KIT            | pearsonr            |   0.588761 |
|  5 | test       | KIT            | spearmanr           |   0.50008  |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.368464 |
|  1 | test       | EGFR           | mean_absolute_error |  17.5627   |
|  2 | test       | EGFR           | r2                  |   0.360459 |
|  3 | test       | EGFR           | mean_squared_error  | 515.322    |
|  4 | test       | EGFR           | pearsonr            |   0.607216 |
|  5 | test       | EGFR           | spearmanr           |   0.418146 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.389941 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.387549 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.375879 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.338385 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.624515 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.541111 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.48615  |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.474851 |
|  2 | test       | LOG_RPPB       | r2                  | 0.486019 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.456663 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.734261 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.804348 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.40851  |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.53795  |
|  2 | test       | LOG_HPPB       | r2                  | 0.360875 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.387079 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.64022  |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.676751 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.592948 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.339965 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.592312 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.201966 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.77166  |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.778201 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.502798 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.425544 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.499822 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.282372 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.714519 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.718885 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.458761 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.355358 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.455843 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.211356 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.681038 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.681043 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.433554 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.80462 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.417315 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.657027 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.156968 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.438502 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.618316 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.922174 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.511806 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.487584 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.650882 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.917489 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.325783 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.829013 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.902654 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.84286 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.554471 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6307410255719698,
    "polaris/pkis2-ret-wt-reg-v2": 791.1164241478227,
    "polaris/pkis2-kit-wt-cls-v2": 0.7102762635433089,
    "polaris/pkis2-kit-wt-reg-v2": 885.3373248939089,
    "polaris/pkis2-egfr-wt-reg-v2": 515.3221628839755,
    "polaris/adme-fang-solu-1": 0.624514853110473,
    "polaris/adme-fang-rppb-1": 0.7342609636259282,
    "polaris/adme-fang-hppb-1": 0.6402202581571836,
    "polaris/adme-fang-perm-1": 0.7716595243000447,
    "polaris/adme-fang-rclint-1": 0.7145185906016944,
    "polaris/adme-fang-hclint-1": 0.6810383121490247,
    "tdcommons/lipophilicity-astrazeneca": 0.43355431265490396,
    "tdcommons/ppbr-az": 7.804617922651533,
    "tdcommons/clearance-hepatocyte-az": 0.4173154964480448,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.657027177977552,
    "tdcommons/half-life-obach": 0.1569675064277368,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4385021050765278,
    "tdcommons/clearance-microsome-az": 0.61831607512123,
    "tdcommons/dili": 0.9221739130434782,
    "tdcommons/bioavailability-ma": 0.5118057864981709,
    "tdcommons/vdss-lombardo": 0.48758420009168735,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6508815551537072,
    "tdcommons/pgp-broccatelli": 0.9174886696880831,
    "tdcommons/caco2-wang": 0.3257828086717543,
    "tdcommons/herg": 0.8290132547864507,
    "tdcommons/bbb-martins": 0.9026540025015637,
    "tdcommons/ames": 0.8428596604593785,
    "tdcommons/ld50-zhu": 0.5544710675002112
}
```
