# chemeleon2_preview_initial_training_e4s281344 Baseline Results
timestamp: 2026-06-12 10:46:05.831190
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.65078  |
|  1 | test       | CLS_RET        | mcc         | 0.512903 |
|  2 | test       | CLS_RET        | f1          | 0.580645 |
|  3 | test       | CLS_RET        | accuracy    | 0.877358 |
|  4 | test       | CLS_RET        | cohen_kappa | 0.509609 |
|  5 | test       | CLS_RET        | roc_auc     | 0.839392 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.300659 |
|  1 | test       | RET            | mean_squared_error  | 830.402    |
|  2 | test       | RET            | spearmanr           |   0.556115 |
|  3 | test       | RET            | explained_var       |   0.345712 |
|  4 | test       | RET            | pearsonr            |   0.590998 |
|  5 | test       | RET            | mean_absolute_error |  21.3382   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.541568 |
|  1 | test       | CLS_KIT        | mcc         | 0.403382 |
|  2 | test       | CLS_KIT        | f1          | 0.486486 |
|  3 | test       | CLS_KIT        | accuracy    | 0.836207 |
|  4 | test       | CLS_KIT        | cohen_kappa | 0.393172 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.79207  |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.290726 |
|  1 | test       | KIT            | mean_squared_error  | 855.869    |
|  2 | test       | KIT            | spearmanr           |   0.524236 |
|  3 | test       | KIT            | explained_var       |   0.293508 |
|  4 | test       | KIT            | pearsonr            |   0.573291 |
|  5 | test       | KIT            | mean_absolute_error |  22.7832   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.47757  |
|  1 | test       | EGFR           | mean_squared_error  | 420.958    |
|  2 | test       | EGFR           | spearmanr           |   0.459668 |
|  3 | test       | EGFR           | explained_var       |   0.480829 |
|  4 | test       | EGFR           | pearsonr            |   0.695326 |
|  5 | test       | EGFR           | mean_absolute_error |  15.5949   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.37749  |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.337512 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.498602 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.383866 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.620543 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.388614 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.349036 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.57837  |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.705217 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.383639 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.629495 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.576207 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.514009 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.294335 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.665903 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.533684 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.730618 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.437844 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.626052 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.185251 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.790814 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.637941 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.802766 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.311738 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.533473 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.263375 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.725848 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.533475 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.730403 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.405063 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.456827 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.210974 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.688092 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.456907 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.693206 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.348416 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.43952 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  8.1851 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.428721 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.653788 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.454731 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.415454 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.594356 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.931304 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.663785 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.180798 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.644326 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.917622 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.298525 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.877909 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.895306 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.832384 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.582963 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6507799248208456,
    "polaris/pkis2-ret-wt-reg-v2": 830.4015852228187,
    "polaris/pkis2-kit-wt-cls-v2": 0.5415681474512847,
    "polaris/pkis2-kit-wt-reg-v2": 855.86931328345,
    "polaris/pkis2-egfr-wt-reg-v2": 420.9575868577108,
    "polaris/adme-fang-solu-1": 0.6205431820876988,
    "polaris/adme-fang-rppb-1": 0.6294953201324299,
    "polaris/adme-fang-hppb-1": 0.7306178761739521,
    "polaris/adme-fang-perm-1": 0.8027659056132663,
    "polaris/adme-fang-rclint-1": 0.7304032918461084,
    "polaris/adme-fang-hclint-1": 0.6932059552282236,
    "tdcommons/lipophilicity-astrazeneca": 0.43951973768075314,
    "tdcommons/ppbr-az": 8.185099540260056,
    "tdcommons/clearance-hepatocyte-az": 0.42872105010630734,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6537877251790848,
    "tdcommons/half-life-obach": 0.45473104770666184,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.41545437348313285,
    "tdcommons/clearance-microsome-az": 0.5943556800107747,
    "tdcommons/dili": 0.931304347826087,
    "tdcommons/bioavailability-ma": 0.6637845028267376,
    "tdcommons/vdss-lombardo": 0.18079758984745156,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6443264014466545,
    "tdcommons/pgp-broccatelli": 0.91762196747534,
    "tdcommons/caco2-wang": 0.29852455123887955,
    "tdcommons/herg": 0.8779086892488954,
    "tdcommons/bbb-martins": 0.8953056597873671,
    "tdcommons/ames": 0.832383637823337,
    "tdcommons/ld50-zhu": 0.5829632510177498
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.651484 |
|  1 | test       | CLS_RET        | mcc         | 0.49296  |
|  2 | test       | CLS_RET        | f1          | 0.551724 |
|  3 | test       | CLS_RET        | accuracy    | 0.877358 |
|  4 | test       | CLS_RET        | cohen_kappa | 0.483121 |
|  5 | test       | CLS_RET        | roc_auc     | 0.814276 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.396986 |
|  1 | test       | RET            | mean_squared_error  | 716.022    |
|  2 | test       | RET            | spearmanr           |   0.630604 |
|  3 | test       | RET            | explained_var       |   0.416799 |
|  4 | test       | RET            | pearsonr            |   0.650934 |
|  5 | test       | RET            | mean_absolute_error |  20.8016   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.589313 |
|  1 | test       | CLS_KIT        | mcc         | 0.421263 |
|  2 | test       | CLS_KIT        | f1          | 0.533333 |
|  3 | test       | CLS_KIT        | accuracy    | 0.818966 |
|  4 | test       | CLS_KIT        | cohen_kappa | 0.421103 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.837524 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.238923 |
|  1 | test       | KIT            | mean_squared_error  | 918.38     |
|  2 | test       | KIT            | spearmanr           |   0.530681 |
|  3 | test       | KIT            | explained_var       |   0.275052 |
|  4 | test       | KIT            | pearsonr            |   0.570419 |
|  5 | test       | KIT            | mean_absolute_error |  23.5705   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.41199  |
|  1 | test       | EGFR           | mean_squared_error  | 473.8      |
|  2 | test       | EGFR           | spearmanr           |   0.323933 |
|  3 | test       | EGFR           | explained_var       |   0.428176 |
|  4 | test       | EGFR           | pearsonr            |   0.655259 |
|  5 | test       | EGFR           | mean_absolute_error |  16.5107   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.419463 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.314755 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.553023 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.425981 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.658802 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.385722 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.555851 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.394618 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.817391 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.565875 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.78436  |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.497774 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.225071 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.469327 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.574223 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.340351 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.614036 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.61318  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.641928 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.177386 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.785732 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.642217 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.802061 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.3034   |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.520078 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.270937 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.724049 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.520755 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.721703 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.413105 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.461789 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.209046 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.701688 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.462554 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.706725 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.350768 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.459306 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.79303 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.416398 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.72836 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.361761 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.383335 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.611765 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.907391 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.621217 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.602707 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.635963 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.929819 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.293436 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.840648 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.907227 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.838597 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.585767 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6514841004443939,
    "polaris/pkis2-ret-wt-reg-v2": 716.0217014123848,
    "polaris/pkis2-kit-wt-cls-v2": 0.5893132323732129,
    "polaris/pkis2-kit-wt-reg-v2": 918.3799279581896,
    "polaris/pkis2-egfr-wt-reg-v2": 473.79963938218344,
    "polaris/adme-fang-solu-1": 0.6588015109142873,
    "polaris/adme-fang-rppb-1": 0.7843604373764532,
    "polaris/adme-fang-hppb-1": 0.6140357213456975,
    "polaris/adme-fang-perm-1": 0.8020610694312701,
    "polaris/adme-fang-rclint-1": 0.721702943698824,
    "polaris/adme-fang-hclint-1": 0.7067253081383913,
    "tdcommons/lipophilicity-astrazeneca": 0.459305862392698,
    "tdcommons/ppbr-az": 7.793029982237569,
    "tdcommons/clearance-hepatocyte-az": 0.4163976815929054,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.728360339226209,
    "tdcommons/half-life-obach": 0.36176139390706824,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3833348611065765,
    "tdcommons/clearance-microsome-az": 0.6117645294472209,
    "tdcommons/dili": 0.9073913043478261,
    "tdcommons/bioavailability-ma": 0.6212171599600932,
    "tdcommons/vdss-lombardo": 0.6027073947435451,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6359629294755877,
    "tdcommons/pgp-broccatelli": 0.9298187150093309,
    "tdcommons/caco2-wang": 0.29343638432774805,
    "tdcommons/herg": 0.8406480117820324,
    "tdcommons/bbb-martins": 0.9072271732332708,
    "tdcommons/ames": 0.838596800407292,
    "tdcommons/ld50-zhu": 0.585766638830647
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.531796 |
|  1 | test       | CLS_RET        | mcc         | 0.297861 |
|  2 | test       | CLS_RET        | f1          | 0.333333 |
|  3 | test       | CLS_RET        | accuracy    | 0.849057 |
|  4 | test       | CLS_RET        | cohen_kappa | 0.264527 |
|  5 | test       | CLS_RET        | roc_auc     | 0.836087 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.376887 |
|  1 | test       | RET            | mean_squared_error  | 739.888    |
|  2 | test       | RET            | spearmanr           |   0.614749 |
|  3 | test       | RET            | explained_var       |   0.403812 |
|  4 | test       | RET            | pearsonr            |   0.63715  |
|  5 | test       | RET            | mean_absolute_error |  20.0355   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.562073 |
|  1 | test       | CLS_KIT        | mcc         | 0.478195 |
|  2 | test       | CLS_KIT        | f1          | 0.5      |
|  3 | test       | CLS_KIT        | accuracy    | 0.862069 |
|  4 | test       | CLS_KIT        | cohen_kappa | 0.432763 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.774178 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.259297 |
|  1 | test       | KIT            | mean_squared_error  | 893.795    |
|  2 | test       | KIT            | spearmanr           |   0.508187 |
|  3 | test       | KIT            | explained_var       |   0.274435 |
|  4 | test       | KIT            | pearsonr            |   0.570379 |
|  5 | test       | KIT            | mean_absolute_error |  23.276    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.491912 |
|  1 | test       | EGFR           | mean_squared_error  | 409.401    |
|  2 | test       | EGFR           | spearmanr           |   0.480617 |
|  3 | test       | EGFR           | explained_var       |   0.494916 |
|  4 | test       | EGFR           | pearsonr            |   0.710966 |
|  5 | test       | EGFR           | mean_absolute_error |  15.7345   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.370882 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.341094 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.501708 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.381613 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.618179 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.387208 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.563631 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.387706 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.78087  |
|  3 | test       | LOG_RPPB       | explained_var       | 0.563883 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.782693 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.507298 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.516904 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.292582 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.76614  |
|  3 | test       | LOG_HPPB       | explained_var       | 0.586719 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.766566 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.454384 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.614849 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.190801 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.784562 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.617181 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.785668 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.327226 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.563098 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.24665  |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.75476  |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.566178 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.752517 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.394981 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.480999 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.201585 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.698876 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.481702 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.702976 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.347043 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.464494 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.35424 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.371062 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.728077 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.325293 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.42875 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.590321 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.922609 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.569006 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.448354 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.62986 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.91289 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.295533 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.833137 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.89599 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.845439 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.581586 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5317955302555479,
    "polaris/pkis2-ret-wt-reg-v2": 739.8878368417667,
    "polaris/pkis2-kit-wt-cls-v2": 0.5620728409495317,
    "polaris/pkis2-kit-wt-reg-v2": 893.7948956807234,
    "polaris/pkis2-egfr-wt-reg-v2": 409.4009412443527,
    "polaris/adme-fang-solu-1": 0.6181793642088835,
    "polaris/adme-fang-rppb-1": 0.7826928566908683,
    "polaris/adme-fang-hppb-1": 0.7665655791173519,
    "polaris/adme-fang-perm-1": 0.7856675968097767,
    "polaris/adme-fang-rclint-1": 0.7525167775945321,
    "polaris/adme-fang-hclint-1": 0.7029763515765678,
    "tdcommons/lipophilicity-astrazeneca": 0.4644937653200967,
    "tdcommons/ppbr-az": 8.354242927128173,
    "tdcommons/clearance-hepatocyte-az": 0.37106205038962603,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.728076605232402,
    "tdcommons/half-life-obach": 0.3252925673044625,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4287498487733732,
    "tdcommons/clearance-microsome-az": 0.5903208496129748,
    "tdcommons/dili": 0.922608695652174,
    "tdcommons/bioavailability-ma": 0.5690056534752245,
    "tdcommons/vdss-lombardo": 0.44835415381453486,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6298598553345389,
    "tdcommons/pgp-broccatelli": 0.912889896027726,
    "tdcommons/caco2-wang": 0.29553342854154824,
    "tdcommons/herg": 0.8331369661266569,
    "tdcommons/bbb-martins": 0.8959896810506567,
    "tdcommons/ames": 0.8454385243494096,
    "tdcommons/ld50-zhu": 0.5815855884293903
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.689498 |
|  1 | test       | CLS_RET        | mcc         | 0.486398 |
|  2 | test       | CLS_RET        | f1          | 0.5625   |
|  3 | test       | CLS_RET        | accuracy    | 0.867925 |
|  4 | test       | CLS_RET        | cohen_kappa | 0.48508  |
|  5 | test       | CLS_RET        | roc_auc     | 0.869795 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.37475  |
|  1 | test       | RET            | mean_squared_error  | 742.425    |
|  2 | test       | RET            | spearmanr           |   0.577084 |
|  3 | test       | RET            | explained_var       |   0.381144 |
|  4 | test       | RET            | pearsonr            |   0.617523 |
|  5 | test       | RET            | mean_absolute_error |  21.1132   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.738858 |
|  1 | test       | CLS_KIT        | mcc         | 0.551257 |
|  2 | test       | CLS_KIT        | f1          | 0.636364 |
|  3 | test       | CLS_KIT        | accuracy    | 0.862069 |
|  4 | test       | CLS_KIT        | cohen_kappa | 0.551257 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.848646 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.313553 |
|  1 | test       | KIT            | mean_squared_error  | 828.324    |
|  2 | test       | KIT            | spearmanr           |   0.555134 |
|  3 | test       | KIT            | explained_var       |   0.326423 |
|  4 | test       | KIT            | pearsonr            |   0.603197 |
|  5 | test       | KIT            | mean_absolute_error |  22.5206   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.480524 |
|  1 | test       | EGFR           | mean_squared_error  | 418.578    |
|  2 | test       | EGFR           | spearmanr           |   0.490197 |
|  3 | test       | EGFR           | explained_var       |   0.501422 |
|  4 | test       | EGFR           | pearsonr            |   0.709831 |
|  5 | test       | EGFR           | mean_absolute_error |  15.6567   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.401077 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.324723 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.53095  |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.406039 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.637827 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.411814 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.49215  |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.451215 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.79913  |
|  3 | test       | LOG_RPPB       | explained_var       | 0.524366 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.762752 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.576955 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.454525 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.330361 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.677363 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.521937 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.724298 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.494443 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.649806 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.173484 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.797605 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.650833 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.806777 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.305696 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.576236 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.239233 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.759054 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.577462 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.76065  |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.391928 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.460486 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.209553 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.703012 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.492709 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.712862 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.348432 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.446173 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.35506 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.391182 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.61147 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.373703 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.371968 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.611824 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.941739 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.552378 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.639845 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.646248 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.915689 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  0.2951 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.854934 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.885319 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.853438 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.618456 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6894980884026581,
    "polaris/pkis2-ret-wt-reg-v2": 742.4248327443617,
    "polaris/pkis2-kit-wt-cls-v2": 0.7388576192505107,
    "polaris/pkis2-kit-wt-reg-v2": 828.3242153950174,
    "polaris/pkis2-egfr-wt-reg-v2": 418.5777062499909,
    "polaris/adme-fang-solu-1": 0.6378274766000998,
    "polaris/adme-fang-rppb-1": 0.762751539256182,
    "polaris/adme-fang-hppb-1": 0.7242983744202429,
    "polaris/adme-fang-perm-1": 0.8067773777004515,
    "polaris/adme-fang-rclint-1": 0.7606502629583313,
    "polaris/adme-fang-hclint-1": 0.7128622288438181,
    "tdcommons/lipophilicity-astrazeneca": 0.4461734881741659,
    "tdcommons/ppbr-az": 8.355059460962394,
    "tdcommons/clearance-hepatocyte-az": 0.3911824468459985,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6114698956134894,
    "tdcommons/half-life-obach": 0.3737030321525443,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3719677024864005,
    "tdcommons/clearance-microsome-az": 0.6118241808966581,
    "tdcommons/dili": 0.9417391304347826,
    "tdcommons/bioavailability-ma": 0.5523777851679414,
    "tdcommons/vdss-lombardo": 0.6398454739263952,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.64624773960217,
    "tdcommons/pgp-broccatelli": 0.9156891495601174,
    "tdcommons/caco2-wang": 0.29510014974757615,
    "tdcommons/herg": 0.8549337260677468,
    "tdcommons/bbb-martins": 0.8853189493433397,
    "tdcommons/ames": 0.8534375061191721,
    "tdcommons/ld50-zhu": 0.6184558550475898
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.552033 |
|  1 | test       | CLS_RET        | mcc         | 0.385217 |
|  2 | test       | CLS_RET        | f1          | 0.466667 |
|  3 | test       | CLS_RET        | accuracy    | 0.849057 |
|  4 | test       | CLS_RET        | cohen_kappa | 0.38057  |
|  5 | test       | CLS_RET        | roc_auc     | 0.812954 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.282872 |
|  1 | test       | RET            | mean_squared_error  | 851.522    |
|  2 | test       | RET            | spearmanr           |   0.546811 |
|  3 | test       | RET            | explained_var       |   0.282972 |
|  4 | test       | RET            | pearsonr            |   0.532999 |
|  5 | test       | RET            | mean_absolute_error |  23.6488   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.654236 |
|  1 | test       | CLS_KIT        | mcc         | 0.512904 |
|  2 | test       | CLS_KIT        | f1          | 0.608696 |
|  3 | test       | CLS_KIT        | accuracy    | 0.844828 |
|  4 | test       | CLS_KIT        | cohen_kappa | 0.51215  |
|  5 | test       | CLS_KIT        | roc_auc     | 0.845261 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.257868 |
|  1 | test       | KIT            | mean_squared_error  | 895.519    |
|  2 | test       | KIT            | spearmanr           |   0.509095 |
|  3 | test       | KIT            | explained_var       |   0.274381 |
|  4 | test       | KIT            | pearsonr            |   0.575125 |
|  5 | test       | KIT            | mean_absolute_error |  22.5289   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.416031 |
|  1 | test       | EGFR           | mean_squared_error  | 470.544    |
|  2 | test       | EGFR           | spearmanr           |   0.371905 |
|  3 | test       | EGFR           | explained_var       |   0.422552 |
|  4 | test       | EGFR           | pearsonr            |   0.652108 |
|  5 | test       | EGFR           | mean_absolute_error |  17.3855   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.458077 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.293819 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.564541 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.459804 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.678247 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.360201 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.50564  |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.43923  |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.870435 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.603101 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.796519 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.553063 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.370971 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.380964 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.638399 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.447378 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.670525 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.528803 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.635752 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.180446 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.785037 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.635802 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.797759 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.311695 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.546746 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.255881 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.742366 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.54832  |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.740805 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.402621 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.498838 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.194656 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.712967 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.501373 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.714587 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.332885 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.428403 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.00032 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.454582 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.657273 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.22461 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.370363 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.597755 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  |    0.92 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.56568 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.495087 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.651334 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.944548 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.346088 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.826951 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.896244 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.835084 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.583348 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5520332030224049,
    "polaris/pkis2-ret-wt-reg-v2": 851.5218221131362,
    "polaris/pkis2-kit-wt-cls-v2": 0.65423621679967,
    "polaris/pkis2-kit-wt-reg-v2": 895.5192445591555,
    "polaris/pkis2-egfr-wt-reg-v2": 470.54378510809994,
    "polaris/adme-fang-solu-1": 0.6782469093282743,
    "polaris/adme-fang-rppb-1": 0.7965186227542874,
    "polaris/adme-fang-hppb-1": 0.6705249963196281,
    "polaris/adme-fang-perm-1": 0.7977587238580918,
    "polaris/adme-fang-rclint-1": 0.7408045824652938,
    "polaris/adme-fang-hclint-1": 0.71458714725126,
    "tdcommons/lipophilicity-astrazeneca": 0.4284033375410806,
    "tdcommons/ppbr-az": 9.000324882275303,
    "tdcommons/clearance-hepatocyte-az": 0.4545816923833273,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.657273250245752,
    "tdcommons/half-life-obach": 0.22460993371761578,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3703630320771267,
    "tdcommons/clearance-microsome-az": 0.5977545102696873,
    "tdcommons/dili": 0.92,
    "tdcommons/bioavailability-ma": 0.5656800798137678,
    "tdcommons/vdss-lombardo": 0.49508657772791287,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6513336347197106,
    "tdcommons/pgp-broccatelli": 0.9445481205011997,
    "tdcommons/caco2-wang": 0.346088454337051,
    "tdcommons/herg": 0.8269513991163476,
    "tdcommons/bbb-martins": 0.8962437460913071,
    "tdcommons/ames": 0.835083906087842,
    "tdcommons/ld50-zhu": 0.5833479203551968
}
```
