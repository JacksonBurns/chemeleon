# chemeleon2_preview_initial_training_e4s281344 Baseline Results
timestamp: 2026-06-26 02:21:24.057459
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.684211 |
|  1 | test       | CLS_RET        | accuracy    | 0.886792 |
|  2 | test       | CLS_RET        | pr_auc      | 0.600584 |
|  3 | test       | CLS_RET        | roc_auc     | 0.865829 |
|  4 | test       | CLS_RET        | cohen_kappa | 0.616174 |
|  5 | test       | CLS_RET        | mcc         | 0.62128  |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.548836 |
|  1 | test       | RET            | r2                  |   0.350709 |
|  2 | test       | RET            | mean_squared_error  | 770.972    |
|  3 | test       | RET            | mean_absolute_error |  20.9362   |
|  4 | test       | RET            | pearsonr            |   0.59927  |
|  5 | test       | RET            | explained_var       |   0.359113 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.585366 |
|  1 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.559372 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.766441 |
|  4 | test       | CLS_KIT        | cohen_kappa | 0.496939 |
|  5 | test       | CLS_KIT        | mcc         | 0.498909 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.474423 |
|  1 | test       | KIT            | r2                  |   0.307485 |
|  2 | test       | KIT            | mean_squared_error  | 835.647    |
|  3 | test       | KIT            | mean_absolute_error |  22.0086   |
|  4 | test       | KIT            | pearsonr            |   0.577584 |
|  5 | test       | KIT            | explained_var       |   0.319005 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.453903 |
|  1 | test       | EGFR           | r2                  |   0.513393 |
|  2 | test       | EGFR           | mean_squared_error  | 392.093    |
|  3 | test       | EGFR           | mean_absolute_error |  15.8835   |
|  4 | test       | EGFR           | pearsonr            |   0.720288 |
|  5 | test       | EGFR           | explained_var       |   0.518815 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.56411  |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.431969 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.307974 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.374209 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.660354 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.432222 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.672174 |
|  1 | test       | LOG_RPPB       | r2                  | 0.350973 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.576649 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.541998 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.603917 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.36203  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.587058 |
|  1 | test       | LOG_HPPB       | r2                  | 0.397392 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.364963 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.523047 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.637302 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.402195 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.726109 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.570902 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.212572 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.363247 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.770656 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.593814 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.702497 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.46497  |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.302048 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.427919 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.70417  |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.474898 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.719453 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.485974 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.199653 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.329869 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.719781 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.500005 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.450003 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.70182 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.36305 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.673282 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.292683 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.355836 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.597964 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.877391 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.47589 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.546153 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.595954 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  |  0.8765 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.381457 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.843004 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.876759 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.83884 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.611669 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6005839536230175,
    "polaris/pkis2-ret-wt-reg-v2": 770.9718272271832,
    "polaris/pkis2-kit-wt-cls-v2": 0.5593719199630013,
    "polaris/pkis2-kit-wt-reg-v2": 835.6470004758332,
    "polaris/pkis2-egfr-wt-reg-v2": 392.09276300370334,
    "polaris/adme-fang-solu-1": 0.6603544060544029,
    "polaris/adme-fang-rppb-1": 0.6039165780770772,
    "polaris/adme-fang-hppb-1": 0.6373018108268648,
    "polaris/adme-fang-perm-1": 0.7706562072590151,
    "polaris/adme-fang-rclint-1": 0.704170260499177,
    "polaris/adme-fang-hclint-1": 0.7197808137633659,
    "tdcommons/lipophilicity-astrazeneca": 0.45000344382581253,
    "tdcommons/ppbr-az": 8.701819678564192,
    "tdcommons/clearance-hepatocyte-az": 0.36304980618569643,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6732824530865542,
    "tdcommons/half-life-obach": 0.29268304757104807,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.35583600845411023,
    "tdcommons/clearance-microsome-az": 0.5979643086472002,
    "tdcommons/dili": 0.877391304347826,
    "tdcommons/bioavailability-ma": 0.4758895909544396,
    "tdcommons/vdss-lombardo": 0.546152814463371,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5959538878842676,
    "tdcommons/pgp-broccatelli": 0.8764996001066384,
    "tdcommons/caco2-wang": 0.38145720509006376,
    "tdcommons/herg": 0.8430044182621502,
    "tdcommons/bbb-martins": 0.8767589118198874,
    "tdcommons/ames": 0.8388396091562396,
    "tdcommons/ld50-zhu": 0.6116694474510637
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0        |
|  1 | test       | CLS_RET        | accuracy    | 0.839623 |
|  2 | test       | CLS_RET        | pr_auc      | 0.655721 |
|  3 | test       | CLS_RET        | roc_auc     | 0.848645 |
|  4 | test       | CLS_RET        | cohen_kappa | 0        |
|  5 | test       | CLS_RET        | mcc         | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.560019 |
|  1 | test       | RET            | r2                  |   0.334967 |
|  2 | test       | RET            | mean_squared_error  | 789.664    |
|  3 | test       | RET            | mean_absolute_error |  21.284    |
|  4 | test       | RET            | pearsonr            |   0.60356  |
|  5 | test       | RET            | explained_var       |   0.351069 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.6      |
|  1 | test       | CLS_KIT        | accuracy    | 0.862069 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.726139 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.852031 |
|  4 | test       | CLS_KIT        | cohen_kappa | 0.517672 |
|  5 | test       | CLS_KIT        | mcc         | 0.521477 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.517356 |
|  1 | test       | KIT            | r2                  |   0.241699 |
|  2 | test       | KIT            | mean_squared_error  | 915.03     |
|  3 | test       | KIT            | mean_absolute_error |  23.1001   |
|  4 | test       | KIT            | pearsonr            |   0.574587 |
|  5 | test       | KIT            | explained_var       |   0.265308 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.451233 |
|  1 | test       | EGFR           | r2                  |   0.447432 |
|  2 | test       | EGFR           | mean_squared_error  | 445.242    |
|  3 | test       | EGFR           | mean_absolute_error |  15.3999   |
|  4 | test       | EGFR           | pearsonr            |   0.687473 |
|  5 | test       | EGFR           | explained_var       |   0.452672 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.548764 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.393937 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.328594 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.407507 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.64456  |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.40831  |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.748696 |
|  1 | test       | LOG_RPPB       | r2                  | 0.509808 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.435527 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.558713 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.762795 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.541046 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.719994 |
|  1 | test       | LOG_HPPB       | r2                  | 0.299187 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.424439 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.549518 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.705578 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.306462 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.71732  |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.453882 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.270543 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.425458 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.722722 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.513098 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.702355 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.49152  |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.287059 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.423168 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.701336 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.491808 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.661672 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.399331 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.233306 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.365218 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.663958 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.401862 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.467095 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.16633 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.414134 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.751344 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.391701 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.371178 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.56013 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.895652 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.567343 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.603264 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.595276 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.865236 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.332677 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.836524 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.899937 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.82955 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.575801 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6557207355591662,
    "polaris/pkis2-ret-wt-reg-v2": 789.663581726408,
    "polaris/pkis2-kit-wt-cls-v2": 0.7261393906831952,
    "polaris/pkis2-kit-wt-reg-v2": 915.0295642388107,
    "polaris/pkis2-egfr-wt-reg-v2": 445.24175470715977,
    "polaris/adme-fang-solu-1": 0.6445602201702599,
    "polaris/adme-fang-rppb-1": 0.7627953567003457,
    "polaris/adme-fang-hppb-1": 0.7055775596199503,
    "polaris/adme-fang-perm-1": 0.7227218773879098,
    "polaris/adme-fang-rclint-1": 0.7013361620771144,
    "polaris/adme-fang-hclint-1": 0.6639581919811087,
    "tdcommons/lipophilicity-astrazeneca": 0.4670949719633375,
    "tdcommons/ppbr-az": 8.166331725146136,
    "tdcommons/clearance-hepatocyte-az": 0.4141341853185528,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7513442580234008,
    "tdcommons/half-life-obach": 0.39170107000969895,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.37117761046770104,
    "tdcommons/clearance-microsome-az": 0.5601299780725083,
    "tdcommons/dili": 0.8956521739130435,
    "tdcommons/bioavailability-ma": 0.5673428666444962,
    "tdcommons/vdss-lombardo": 0.6032640430944892,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5952757685352622,
    "tdcommons/pgp-broccatelli": 0.8652359370834444,
    "tdcommons/caco2-wang": 0.3326772583892488,
    "tdcommons/herg": 0.8365243004418262,
    "tdcommons/bbb-martins": 0.8999374609130706,
    "tdcommons/ames": 0.8295502163739255,
    "tdcommons/ld50-zhu": 0.5758013735953138
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.666667 |
|  1 | test       | CLS_RET        | accuracy    | 0.90566  |
|  2 | test       | CLS_RET        | pr_auc      | 0.689273 |
|  3 | test       | CLS_RET        | roc_auc     | 0.873761 |
|  4 | test       | CLS_RET        | cohen_kappa | 0.612856 |
|  5 | test       | CLS_RET        | mcc         | 0.620339 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.578557 |
|  1 | test       | RET            | r2                  |   0.458386 |
|  2 | test       | RET            | mean_squared_error  | 643.115    |
|  3 | test       | RET            | mean_absolute_error |  17.7781   |
|  4 | test       | RET            | pearsonr            |   0.695756 |
|  5 | test       | RET            | explained_var       |   0.475051 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.622222 |
|  1 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.648699 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.819632 |
|  4 | test       | CLS_KIT        | cohen_kappa | 0.531369 |
|  5 | test       | CLS_KIT        | mcc         | 0.531571 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.540858 |
|  1 | test       | KIT            | r2                  |   0.264134 |
|  2 | test       | KIT            | mean_squared_error  | 887.958    |
|  3 | test       | KIT            | mean_absolute_error |  22.0662   |
|  4 | test       | KIT            | pearsonr            |   0.56951  |
|  5 | test       | KIT            | explained_var       |   0.29966  |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.445721 |
|  1 | test       | EGFR           | r2                  |   0.476364 |
|  2 | test       | EGFR           | mean_squared_error  | 421.929    |
|  3 | test       | EGFR           | mean_absolute_error |  15.7308   |
|  4 | test       | EGFR           | pearsonr            |   0.69514  |
|  5 | test       | EGFR           | explained_var       |   0.47645  |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.579115 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.378604 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.336908 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.382125 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.626919 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.37971  |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.745217 |
|  1 | test       | LOG_RPPB       | r2                  | 0.494486 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.44914  |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.513047 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.71712  |
|  5 | test       | LOG_RPPB       | explained_var       | 0.494739 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.697685 |
|  1 | test       | LOG_HPPB       | r2                  | 0.166566 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.50476  |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.655637 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.67718  |
|  5 | test       | LOG_HPPB       | explained_var       | 0.293606 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.756128 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.568643 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.213691 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.349128 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.762646 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.569221 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.720145 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.502104 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.281084 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.41917  |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.722954 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.517169 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.70132  |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.469515 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.206046 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.343885 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.699987 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.481995 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.474064 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.36779 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.383182 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.748181 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0180393 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.40085 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.628581 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.917826 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.651147 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.567294 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.609516 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.917422 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.456202 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.798675 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.881215 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.840263 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.579979 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6892728524393223,
    "polaris/pkis2-ret-wt-reg-v2": 643.1154096019501,
    "polaris/pkis2-kit-wt-cls-v2": 0.6486992587102159,
    "polaris/pkis2-kit-wt-reg-v2": 887.9581499473848,
    "polaris/pkis2-egfr-wt-reg-v2": 421.9293270440611,
    "polaris/adme-fang-solu-1": 0.6269190863167808,
    "polaris/adme-fang-rppb-1": 0.7171200992590923,
    "polaris/adme-fang-hppb-1": 0.6771799476197486,
    "polaris/adme-fang-perm-1": 0.7626460070440536,
    "polaris/adme-fang-rclint-1": 0.7229540565746533,
    "polaris/adme-fang-hclint-1": 0.699987022939068,
    "tdcommons/lipophilicity-astrazeneca": 0.4740640115227018,
    "tdcommons/ppbr-az": 8.367788063008371,
    "tdcommons/clearance-hepatocyte-az": 0.38318248317220366,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7481810861187151,
    "tdcommons/half-life-obach": 0.01803933248750372,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4008502625018289,
    "tdcommons/clearance-microsome-az": 0.6285809065159389,
    "tdcommons/dili": 0.9178260869565217,
    "tdcommons/bioavailability-ma": 0.6511473229132024,
    "tdcommons/vdss-lombardo": 0.5672941884502688,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6095162748643762,
    "tdcommons/pgp-broccatelli": 0.9174220207944548,
    "tdcommons/caco2-wang": 0.4562015910795442,
    "tdcommons/herg": 0.7986745213549338,
    "tdcommons/bbb-martins": 0.8812148217636022,
    "tdcommons/ames": 0.8402631733536978,
    "tdcommons/ld50-zhu": 0.5799791640699797
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.551724 |
|  1 | test       | CLS_RET        | accuracy    | 0.877358 |
|  2 | test       | CLS_RET        | pr_auc      | 0.55549  |
|  3 | test       | CLS_RET        | roc_auc     | 0.854594 |
|  4 | test       | CLS_RET        | cohen_kappa | 0.483121 |
|  5 | test       | CLS_RET        | mcc         | 0.49296  |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.541981 |
|  1 | test       | RET            | r2                  |   0.431203 |
|  2 | test       | RET            | mean_squared_error  | 675.392    |
|  3 | test       | RET            | mean_absolute_error |  19.2652   |
|  4 | test       | RET            | pearsonr            |   0.664748 |
|  5 | test       | RET            | explained_var       |   0.431612 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.604651 |
|  1 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.742092 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.823501 |
|  4 | test       | CLS_KIT        | cohen_kappa | 0.514764 |
|  5 | test       | CLS_KIT        | mcc         | 0.514974 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.554172 |
|  1 | test       | KIT            | r2                  |   0.314176 |
|  2 | test       | KIT            | mean_squared_error  | 827.573    |
|  3 | test       | KIT            | mean_absolute_error |  22.4066   |
|  4 | test       | KIT            | pearsonr            |   0.598262 |
|  5 | test       | KIT            | explained_var       |   0.31431  |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.325597 |
|  1 | test       | EGFR           | r2                  |   0.446476 |
|  2 | test       | EGFR           | mean_squared_error  | 446.012    |
|  3 | test       | EGFR           | mean_absolute_error |  16.9716   |
|  4 | test       | EGFR           | pearsonr            |   0.680563 |
|  5 | test       | EGFR           | explained_var       |   0.456507 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.562027 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.407811 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.321072 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.411894 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.644734 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.414707 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.732174 |
|  1 | test       | LOG_RPPB       | r2                  | 0.50158  |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.442837 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.545623 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.740972 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.521237 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.590267 |
|  1 | test       | LOG_HPPB       | r2                  | 0.274735 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.439249 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.566232 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.60197  |
|  5 | test       | LOG_HPPB       | explained_var       | 0.351681 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.70176  |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.532924 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.231386 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.363051 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.734509 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.53919  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.704829 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.504418 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.279777 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.419662 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.710347 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.504418 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.682649 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.436286 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.218952 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.354123 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.680652 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.436289 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.443826 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.24802 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.349115 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.685318 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.231887 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.378419 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.584593 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.880435 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.527103 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.537955 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.635511 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.912823 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.574601 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.82106 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.879143 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.83862 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.632574 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5554900154704735,
    "polaris/pkis2-ret-wt-reg-v2": 675.391957431974,
    "polaris/pkis2-kit-wt-cls-v2": 0.7420915314947598,
    "polaris/pkis2-kit-wt-reg-v2": 827.5730971420785,
    "polaris/pkis2-egfr-wt-reg-v2": 446.011910401777,
    "polaris/adme-fang-solu-1": 0.6447339466354627,
    "polaris/adme-fang-rppb-1": 0.7409724854967226,
    "polaris/adme-fang-hppb-1": 0.6019699212099203,
    "polaris/adme-fang-perm-1": 0.7345092975157144,
    "polaris/adme-fang-rclint-1": 0.7103467113952897,
    "polaris/adme-fang-hclint-1": 0.680652477711241,
    "tdcommons/lipophilicity-astrazeneca": 0.443825892329216,
    "tdcommons/ppbr-az": 8.248020800213482,
    "tdcommons/clearance-hepatocyte-az": 0.3491150676188105,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6853176772634624,
    "tdcommons/half-life-obach": 0.23188660450824772,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3784187928342235,
    "tdcommons/clearance-microsome-az": 0.5845926045477642,
    "tdcommons/dili": 0.8804347826086956,
    "tdcommons/bioavailability-ma": 0.5271034253408713,
    "tdcommons/vdss-lombardo": 0.5379547735412219,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6355108499095841,
    "tdcommons/pgp-broccatelli": 0.9128232471340977,
    "tdcommons/caco2-wang": 0.5746010849020486,
    "tdcommons/herg": 0.821060382916053,
    "tdcommons/bbb-martins": 0.8791432145090682,
    "tdcommons/ames": 0.8386202980281579,
    "tdcommons/ld50-zhu": 0.6325739142252725
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.611111 |
|  1 | test       | CLS_RET        | accuracy    | 0.867925 |
|  2 | test       | CLS_RET        | pr_auc      | 0.6728   |
|  3 | test       | CLS_RET        | roc_auc     | 0.855254 |
|  4 | test       | CLS_RET        | cohen_kappa | 0.531861 |
|  5 | test       | CLS_RET        | mcc         | 0.533055 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.543996 |
|  1 | test       | RET            | r2                  |   0.305923 |
|  2 | test       | RET            | mean_squared_error  | 824.151    |
|  3 | test       | RET            | mean_absolute_error |  22.6402   |
|  4 | test       | RET            | pearsonr            |   0.55381  |
|  5 | test       | RET            | explained_var       |   0.30598  |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.648649 |
|  1 | test       | CLS_KIT        | accuracy    | 0.887931 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.679881 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.840909 |
|  4 | test       | CLS_KIT        | cohen_kappa | 0.584802 |
|  5 | test       | CLS_KIT        | mcc         | 0.599989 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.474954 |
|  1 | test       | KIT            | r2                  |   0.326555 |
|  2 | test       | KIT            | mean_squared_error  | 812.636    |
|  3 | test       | KIT            | mean_absolute_error |  21.6235   |
|  4 | test       | KIT            | pearsonr            |   0.593317 |
|  5 | test       | KIT            | explained_var       |   0.343251 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.26526  |
|  1 | test       | EGFR           | r2                  |   0.371235 |
|  2 | test       | EGFR           | mean_squared_error  | 506.639    |
|  3 | test       | EGFR           | mean_absolute_error |  16.4573   |
|  4 | test       | EGFR           | pearsonr            |   0.638313 |
|  5 | test       | EGFR           | explained_var       |   0.402426 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.554512 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.400657 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.324951 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.370752 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.65495  |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.418211 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.854783 |
|  1 | test       | LOG_RPPB       | r2                  | 0.450409 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.488302 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.617567 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.860505 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.564008 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.612575 |
|  1 | test       | LOG_HPPB       | r2                  | 0.412093 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.356059 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.468914 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.674923 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.455319 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.741024 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.574503 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.210788 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.337461 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.759735 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.575151 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.726039 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.51216  |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.275407 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.415495 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.725791 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.521794 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.687469 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.45905  |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.21011  |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.342544 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.688635 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.459104 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.429592 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.34574 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.368576 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.696741 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.428115 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.383502 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.599795 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.932174 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.60592 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.369172 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.639354 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.910157 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.386999 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.798969 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.890635 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.825877 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.621458 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6728004102047498,
    "polaris/pkis2-ret-wt-reg-v2": 824.1508634181097,
    "polaris/pkis2-kit-wt-cls-v2": 0.6798805732235997,
    "polaris/pkis2-kit-wt-reg-v2": 812.6358235083588,
    "polaris/pkis2-egfr-wt-reg-v2": 506.638767505938,
    "polaris/adme-fang-solu-1": 0.6549502039226416,
    "polaris/adme-fang-rppb-1": 0.8605048670927772,
    "polaris/adme-fang-hppb-1": 0.6749231244307963,
    "polaris/adme-fang-perm-1": 0.7597354858683751,
    "polaris/adme-fang-rclint-1": 0.7257912717157364,
    "polaris/adme-fang-hclint-1": 0.6886351833838206,
    "tdcommons/lipophilicity-astrazeneca": 0.4295915387301218,
    "tdcommons/ppbr-az": 8.345737721233334,
    "tdcommons/clearance-hepatocyte-az": 0.3685759149216569,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6967405916434192,
    "tdcommons/half-life-obach": 0.4281153264158524,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3835019708635302,
    "tdcommons/clearance-microsome-az": 0.5997948053429801,
    "tdcommons/dili": 0.9321739130434783,
    "tdcommons/bioavailability-ma": 0.6059195211173928,
    "tdcommons/vdss-lombardo": 0.369171912356991,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.639353526220615,
    "tdcommons/pgp-broccatelli": 0.9101572913889628,
    "tdcommons/caco2-wang": 0.3869989150885949,
    "tdcommons/herg": 0.7989690721649485,
    "tdcommons/bbb-martins": 0.8906347717323327,
    "tdcommons/ames": 0.8258767549785585,
    "tdcommons/ld50-zhu": 0.621457745180401
}
```
