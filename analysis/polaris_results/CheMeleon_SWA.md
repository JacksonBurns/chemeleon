# ChemProp Baseline Results
timestamp: 2025-08-15 05:26:43.637923
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.562641 |
|  1 | test       | CLS_RET        | accuracy    | 0.896226 |
|  2 | test       | CLS_RET        | f1          | 0.62069  |
|  3 | test       | CLS_RET        | pr_auc      | 0.634111 |
|  4 | test       | CLS_RET        | mcc         | 0.5741   |
|  5 | test       | CLS_RET        | roc_auc     | 0.85195  |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.685013 |
|  1 | test       | RET            | r2                  |   0.415704 |
|  2 | test       | RET            | explained_var       |   0.46833  |
|  3 | test       | RET            | spearmanr           |   0.641924 |
|  4 | test       | RET            | mean_absolute_error |  19.2021   |
|  5 | test       | RET            | mean_squared_error  | 693.796    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.432763 |
|  1 | test       | CLS_KIT        | accuracy    | 0.862069 |
|  2 | test       | CLS_KIT        | f1          | 0.5      |
|  3 | test       | CLS_KIT        | pr_auc      | 0.633802 |
|  4 | test       | CLS_KIT        | mcc         | 0.478195 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.798839 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.615544 |
|  1 | test       | KIT            | r2                  |   0.327287 |
|  2 | test       | KIT            | explained_var       |   0.361932 |
|  3 | test       | KIT            | spearmanr           |   0.534937 |
|  4 | test       | KIT            | mean_absolute_error |  21.6519   |
|  5 | test       | KIT            | mean_squared_error  | 811.752    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.650891 |
|  1 | test       | EGFR           | r2                  |   0.417732 |
|  2 | test       | EGFR           | explained_var       |   0.419773 |
|  3 | test       | EGFR           | spearmanr           |   0.429753 |
|  4 | test       | EGFR           | mean_absolute_error |  16.381    |
|  5 | test       | EGFR           | mean_squared_error  | 469.173    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.659784 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.431285 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.435314 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.583831 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.366894 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.308345 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.722677 |
|  1 | test       | LOG_RPPB       | r2                  | 0.46248  |
|  2 | test       | LOG_RPPB       | explained_var       | 0.465141 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.781739 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.515782 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.477577 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.759054 |
|  1 | test       | LOG_HPPB       | r2                  | 0.532053 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.572507 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.74108  |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.447589 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.283407 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.806992 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.650724 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.651005 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.804354 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.302234 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.173029 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.748713 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.56047  |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.560562 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.757277 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.393178 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.248134 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.71951  |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.512546 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.513741 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.719746 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.34057  |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.189332 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.461202 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.89633 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.387242 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.680128 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.236822 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.458304 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.592427 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.892609 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.706186 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.577933 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.625565 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.926586 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.360926 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.856701 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.85958 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.843445 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.514876 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6341113279302366,
    "polaris/pkis2-ret-wt-reg-v2": 693.7956012249894,
    "polaris/pkis2-kit-wt-cls-v2": 0.6338024145708188,
    "polaris/pkis2-kit-wt-reg-v2": 811.7524108531081,
    "polaris/pkis2-egfr-wt-reg-v2": 469.1729246165813,
    "polaris/adme-fang-solu-1": 0.6597835875924976,
    "polaris/adme-fang-rppb-1": 0.7226768935917747,
    "polaris/adme-fang-hppb-1": 0.7590537966110936,
    "polaris/adme-fang-perm-1": 0.8069918143745921,
    "polaris/adme-fang-rclint-1": 0.7487127724994438,
    "polaris/adme-fang-hclint-1": 0.7195102036301272,
    "tdcommons/lipophilicity-astrazeneca": 0.46120182211626143,
    "tdcommons/ppbr-az": 7.896334788914444,
    "tdcommons/clearance-hepatocyte-az": 0.3872415960621836,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6801282262262497,
    "tdcommons/half-life-obach": 0.2368220486371441,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4583037251266191,
    "tdcommons/clearance-microsome-az": 0.592427188600926,
    "tdcommons/dili": 0.8926086956521739,
    "tdcommons/bioavailability-ma": 0.7061855670103092,
    "tdcommons/vdss-lombardo": 0.5779327739339528,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6255650994575045,
    "tdcommons/pgp-broccatelli": 0.9265862436683551,
    "tdcommons/caco2-wang": 0.3609257811733037,
    "tdcommons/herg": 0.856701030927835,
    "tdcommons/bbb-martins": 0.8595802063789868,
    "tdcommons/ames": 0.8434451428459534,
    "tdcommons/ld50-zhu": 0.5148764702296225
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.239234 |
|  1 | test       | CLS_RET        | accuracy    | 0.858491 |
|  2 | test       | CLS_RET        | f1          | 0.285714 |
|  3 | test       | CLS_RET        | pr_auc      | 0.705067 |
|  4 | test       | CLS_RET        | mcc         | 0.318193 |
|  5 | test       | CLS_RET        | roc_auc     | 0.869134 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.710685 |
|  1 | test       | RET            | r2                  |   0.454652 |
|  2 | test       | RET            | explained_var       |   0.503967 |
|  3 | test       | RET            | spearmanr           |   0.642142 |
|  4 | test       | RET            | mean_absolute_error |  18.457    |
|  5 | test       | RET            | mean_squared_error  | 647.55     |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.501147 |
|  1 | test       | CLS_KIT        | accuracy    | 0.87069  |
|  2 | test       | CLS_KIT        | f1          | 0.571429 |
|  3 | test       | CLS_KIT        | pr_auc      | 0.634404 |
|  4 | test       | CLS_KIT        | mcc         | 0.525226 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.817215 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.587481 |
|  1 | test       | KIT            | r2                  |   0.280853 |
|  2 | test       | KIT            | explained_var       |   0.296524 |
|  3 | test       | KIT            | spearmanr           |   0.550216 |
|  4 | test       | KIT            | mean_absolute_error |  21.8152   |
|  5 | test       | KIT            | mean_squared_error  | 867.784    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.685263 |
|  1 | test       | EGFR           | r2                  |   0.453525 |
|  2 | test       | EGFR           | explained_var       |   0.465737 |
|  3 | test       | EGFR           | spearmanr           |   0.358424 |
|  4 | test       | EGFR           | mean_absolute_error |  16.047    |
|  5 | test       | EGFR           | mean_squared_error  | 440.333    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.660092 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.430847 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.435692 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.575169 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.368233 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.308583 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.846653 |
|  1 | test       | LOG_RPPB       | r2                  | 0.646956 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.650925 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.826087 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.423661 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.313673 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.755945 |
|  1 | test       | LOG_HPPB       | r2                  | 0.500325 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.569379 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.714187 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.455504 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.302623 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.814239 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.662901 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.662903 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.807465 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.29364  |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.166996 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.739134 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.545217 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.545431 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.740707 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.403607 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.256745 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.715485 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.504582 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.505485 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.712569 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.341373 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.192425 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.453473 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.05149 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.407338 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.697359 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.308233 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.487739 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.603332 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.890435 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.627037 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.57129 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.62986 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.931552 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.292102 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.813991 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.892765 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.84121 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.53366 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7050667101298542,
    "polaris/pkis2-ret-wt-reg-v2": 647.5495097692209,
    "polaris/pkis2-kit-wt-cls-v2": 0.6344037579955639,
    "polaris/pkis2-kit-wt-reg-v2": 867.7835583858657,
    "polaris/pkis2-egfr-wt-reg-v2": 440.3325856594353,
    "polaris/adme-fang-solu-1": 0.660092056439872,
    "polaris/adme-fang-rppb-1": 0.8466525398944388,
    "polaris/adme-fang-hppb-1": 0.7559446167518616,
    "polaris/adme-fang-perm-1": 0.8142386045583238,
    "polaris/adme-fang-rclint-1": 0.7391336056794626,
    "polaris/adme-fang-hclint-1": 0.7154854907825532,
    "tdcommons/lipophilicity-astrazeneca": 0.453472554348764,
    "tdcommons/ppbr-az": 8.05148557304696,
    "tdcommons/clearance-hepatocyte-az": 0.40733762841824683,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6973590236635019,
    "tdcommons/half-life-obach": 0.30823293729829015,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4877390961035911,
    "tdcommons/clearance-microsome-az": 0.6033320356052535,
    "tdcommons/dili": 0.8904347826086956,
    "tdcommons/bioavailability-ma": 0.6270369138676422,
    "tdcommons/vdss-lombardo": 0.571290443910618,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6298598553345389,
    "tdcommons/pgp-broccatelli": 0.9315515862436683,
    "tdcommons/caco2-wang": 0.2921018510457134,
    "tdcommons/herg": 0.8139911634756996,
    "tdcommons/bbb-martins": 0.892765009380863,
    "tdcommons/ames": 0.8412099316610859,
    "tdcommons/ld50-zhu": 0.5336601469248977
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.690285 |
|  1 | test       | CLS_RET        | accuracy    | 0.924528 |
|  2 | test       | CLS_RET        | f1          | 0.733333 |
|  3 | test       | CLS_RET        | pr_auc      | 0.724153 |
|  4 | test       | CLS_RET        | mcc         | 0.698714 |
|  5 | test       | CLS_RET        | roc_auc     | 0.886319 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.668532 |
|  1 | test       | RET            | r2                  |   0.331927 |
|  2 | test       | RET            | explained_var       |   0.446099 |
|  3 | test       | RET            | spearmanr           |   0.601166 |
|  4 | test       | RET            | mean_absolute_error |  20.3925   |
|  5 | test       | RET            | mean_squared_error  | 793.273    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.432763 |
|  1 | test       | CLS_KIT        | accuracy    | 0.862069 |
|  2 | test       | CLS_KIT        | f1          | 0.5      |
|  3 | test       | CLS_KIT        | pr_auc      | 0.612101 |
|  4 | test       | CLS_KIT        | mcc         | 0.478195 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.779981 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.581836 |
|  1 | test       | KIT            | r2                  |   0.293553 |
|  2 | test       | KIT            | explained_var       |   0.29741  |
|  3 | test       | KIT            | spearmanr           |   0.529985 |
|  4 | test       | KIT            | mean_absolute_error |  22.2447   |
|  5 | test       | KIT            | mean_squared_error  | 852.458    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.688085 |
|  1 | test       | EGFR           | r2                  |   0.4641   |
|  2 | test       | EGFR           | explained_var       |   0.469575 |
|  3 | test       | EGFR           | spearmanr           |   0.41259  |
|  4 | test       | EGFR           | mean_absolute_error |  16.1263   |
|  5 | test       | EGFR           | mean_squared_error  | 431.811    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.632886 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.394325 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.400531 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.549597 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.385053 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.328384 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.818179 |
|  1 | test       | LOG_RPPB       | r2                  | 0.612347 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.612675 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.817391 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.454379 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.344423 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.770331 |
|  1 | test       | LOG_HPPB       | r2                  | 0.559481 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.593402 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.786004 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.43558  |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.266795 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.798216 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.637111 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.637146 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.796442 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.307746 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.179773 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.753831 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.568038 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.568102 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.75549  |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.390596 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.243861 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.708358 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.491325 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.492531 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.713577 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.347434 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.197574 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.447742 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  7.9322 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.416473 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.716806 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.29807 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.498198 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.616628 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.891739 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.594613 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.49325 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.627147 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.925786 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.351496 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.82268 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.887684 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.842401 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.519462 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7241531952046574,
    "polaris/pkis2-ret-wt-reg-v2": 793.2732310836742,
    "polaris/pkis2-kit-wt-cls-v2": 0.6121010638714043,
    "polaris/pkis2-kit-wt-reg-v2": 852.4579072084682,
    "polaris/pkis2-egfr-wt-reg-v2": 431.81101689459746,
    "polaris/adme-fang-solu-1": 0.6328857600415566,
    "polaris/adme-fang-rppb-1": 0.8181788780609068,
    "polaris/adme-fang-hppb-1": 0.7703312696836375,
    "polaris/adme-fang-perm-1": 0.7982156844876829,
    "polaris/adme-fang-rclint-1": 0.7538310511436654,
    "polaris/adme-fang-hclint-1": 0.7083580778622305,
    "tdcommons/lipophilicity-astrazeneca": 0.4477421360697065,
    "tdcommons/ppbr-az": 7.932198153036865,
    "tdcommons/clearance-hepatocyte-az": 0.41647332960337796,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7168055662782511,
    "tdcommons/half-life-obach": 0.2980702175377635,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4981980027917556,
    "tdcommons/clearance-microsome-az": 0.6166280522392354,
    "tdcommons/dili": 0.8917391304347826,
    "tdcommons/bioavailability-ma": 0.5946125706684402,
    "tdcommons/vdss-lombardo": 0.4932498414209982,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6271473779385172,
    "tdcommons/pgp-broccatelli": 0.9257864569448148,
    "tdcommons/caco2-wang": 0.35149638340142225,
    "tdcommons/herg": 0.822680412371134,
    "tdcommons/bbb-martins": 0.887683708567855,
    "tdcommons/ames": 0.8424014568524937,
    "tdcommons/ld50-zhu": 0.5194622815910308
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.478066 |
|  1 | test       | CLS_RET        | accuracy    | 0.896226 |
|  2 | test       | CLS_RET        | f1          | 0.521739 |
|  3 | test       | CLS_RET        | pr_auc      | 0.749196 |
|  4 | test       | CLS_RET        | mcc         | 0.560462 |
|  5 | test       | CLS_RET        | roc_auc     | 0.900859 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.664491 |
|  1 | test       | RET            | r2                  |   0.394962 |
|  2 | test       | RET            | explained_var       |   0.440969 |
|  3 | test       | RET            | spearmanr           |   0.568964 |
|  4 | test       | RET            | mean_absolute_error |  20.2665   |
|  5 | test       | RET            | mean_squared_error  | 718.425    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.600636 |
|  1 | test       | CLS_KIT        | accuracy    | 0.887931 |
|  2 | test       | CLS_KIT        | f1          | 0.666667 |
|  3 | test       | CLS_KIT        | pr_auc      | 0.654462 |
|  4 | test       | CLS_KIT        | mcc         | 0.607849 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.810928 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.610404 |
|  1 | test       | KIT            | r2                  |   0.313406 |
|  2 | test       | KIT            | explained_var       |   0.344516 |
|  3 | test       | KIT            | spearmanr           |   0.559351 |
|  4 | test       | KIT            | mean_absolute_error |  21.1417   |
|  5 | test       | KIT            | mean_squared_error  | 828.502    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.643284 |
|  1 | test       | EGFR           | r2                  |   0.376646 |
|  2 | test       | EGFR           | explained_var       |   0.378497 |
|  3 | test       | EGFR           | spearmanr           |   0.337272 |
|  4 | test       | EGFR           | mean_absolute_error |  17.4076   |
|  5 | test       | EGFR           | mean_squared_error  | 502.279    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.634871 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.39986  |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.402043 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.548367 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.380776 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.325383 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.802475 |
|  1 | test       | LOG_RPPB       | r2                  | 0.574409 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.579061 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.791304 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.464552 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.37813  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.741712 |
|  1 | test       | LOG_HPPB       | r2                  | 0.513082 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.550116 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.728398 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.465757 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.294896 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.82525  |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.680927 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.680932 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.815181 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.287363 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.158066 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.749669 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.560912 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.561885 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.754274 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.39599  |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.247884 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.725067 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.519956 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.521345 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.725252 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.332826 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.186454 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.46408 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.78782 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.375534 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.68354 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.285518 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.46432 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.583282 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.916522 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.661457 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.572678 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.61901 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.904459 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.355001 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.827099 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.902224 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.833991 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.519938 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7491961808058119,
    "polaris/pkis2-ret-wt-reg-v2": 718.4248551855669,
    "polaris/pkis2-kit-wt-cls-v2": 0.6544615912120338,
    "polaris/pkis2-kit-wt-reg-v2": 828.5022876851499,
    "polaris/pkis2-egfr-wt-reg-v2": 502.27861499221683,
    "polaris/adme-fang-solu-1": 0.6348710090790719,
    "polaris/adme-fang-rppb-1": 0.8024753490371945,
    "polaris/adme-fang-hppb-1": 0.7417119129221962,
    "polaris/adme-fang-perm-1": 0.825249855432036,
    "polaris/adme-fang-rclint-1": 0.7496690598905695,
    "polaris/adme-fang-hclint-1": 0.7250665286185378,
    "tdcommons/lipophilicity-astrazeneca": 0.46408012812478194,
    "tdcommons/ppbr-az": 7.787816880828367,
    "tdcommons/clearance-hepatocyte-az": 0.37553389489562644,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6835397147475519,
    "tdcommons/half-life-obach": 0.28551794289630733,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.46431984693432277,
    "tdcommons/clearance-microsome-az": 0.58328234243116,
    "tdcommons/dili": 0.9165217391304348,
    "tdcommons/bioavailability-ma": 0.661456601263718,
    "tdcommons/vdss-lombardo": 0.5726780905536104,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6190099457504521,
    "tdcommons/pgp-broccatelli": 0.9044588109837376,
    "tdcommons/caco2-wang": 0.35500067269910884,
    "tdcommons/herg": 0.8270986745213549,
    "tdcommons/bbb-martins": 0.9022240462789243,
    "tdcommons/ames": 0.8339912667175782,
    "tdcommons/ld50-zhu": 0.5199379995201534
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.6322   |
|  1 | test       | CLS_RET        | accuracy    | 0.90566  |
|  2 | test       | CLS_RET        | f1          | 0.6875   |
|  3 | test       | CLS_RET        | pr_auc      | 0.695823 |
|  4 | test       | CLS_RET        | mcc         | 0.633917 |
|  5 | test       | CLS_RET        | roc_auc     | 0.85922  |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.660752 |
|  1 | test       | RET            | r2                  |   0.400435 |
|  2 | test       | RET            | explained_var       |   0.433519 |
|  3 | test       | RET            | spearmanr           |   0.57023  |
|  4 | test       | RET            | mean_absolute_error |  19.8405   |
|  5 | test       | RET            | mean_squared_error  | 711.927    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.496939 |
|  1 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  2 | test       | CLS_KIT        | f1          | 0.585366 |
|  3 | test       | CLS_KIT        | pr_auc      | 0.701706 |
|  4 | test       | CLS_KIT        | mcc         | 0.498909 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.825919 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.573129 |
|  1 | test       | KIT            | r2                  |   0.274641 |
|  2 | test       | KIT            | explained_var       |   0.285501 |
|  3 | test       | KIT            | spearmanr           |   0.528019 |
|  4 | test       | KIT            | mean_absolute_error |  22.0258   |
|  5 | test       | KIT            | mean_squared_error  | 875.279    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.671069 |
|  1 | test       | EGFR           | r2                  |   0.445629 |
|  2 | test       | EGFR           | explained_var       |   0.448339 |
|  3 | test       | EGFR           | spearmanr           |   0.438427 |
|  4 | test       | EGFR           | mean_absolute_error |  16.2558   |
|  5 | test       | EGFR           | mean_squared_error  | 446.695    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.679864 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.456531 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.461427 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.582196 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.363587 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.294657 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.857894 |
|  1 | test       | LOG_RPPB       | r2                  | 0.647602 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.64828  |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.846087 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.439108 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.313099 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.737766 |
|  1 | test       | LOG_HPPB       | r2                  | 0.510457 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.514309 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.691726 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.475142 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.296486 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.800158 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.64006  |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.640138 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.799147 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.304996 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.178311 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.753452 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.567528 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.567649 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.758811 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.392253 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.244149 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.721286 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.513675 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.51403  |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.725173 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.334342 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.188893 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.44559 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.33833 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.348437 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.694558 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.355359 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.433866 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.618648 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.913913 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.663618 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.592697 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.626243 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.914656 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.411261 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.813549 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.886452 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.845265 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.522746 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6958234385303663,
    "polaris/pkis2-ret-wt-reg-v2": 711.9267126753602,
    "polaris/pkis2-kit-wt-cls-v2": 0.7017063612356143,
    "polaris/pkis2-kit-wt-reg-v2": 875.2789819314522,
    "polaris/pkis2-egfr-wt-reg-v2": 446.69503326029525,
    "polaris/adme-fang-solu-1": 0.6798639008245517,
    "polaris/adme-fang-rppb-1": 0.8578937746844575,
    "polaris/adme-fang-hppb-1": 0.7377658033661463,
    "polaris/adme-fang-perm-1": 0.8001577560258798,
    "polaris/adme-fang-rclint-1": 0.7534517168211309,
    "polaris/adme-fang-hclint-1": 0.7212864006810396,
    "tdcommons/lipophilicity-astrazeneca": 0.44559007608322876,
    "tdcommons/ppbr-az": 8.338327228907822,
    "tdcommons/clearance-hepatocyte-az": 0.3484370059992109,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.694558275871964,
    "tdcommons/half-life-obach": 0.35535886114677934,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.43386616972794123,
    "tdcommons/clearance-microsome-az": 0.6186482468705138,
    "tdcommons/dili": 0.9139130434782609,
    "tdcommons/bioavailability-ma": 0.6636182241436648,
    "tdcommons/vdss-lombardo": 0.5926970928010359,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.62624321880651,
    "tdcommons/pgp-broccatelli": 0.9146560917088776,
    "tdcommons/caco2-wang": 0.4112611667928843,
    "tdcommons/herg": 0.8135493372606775,
    "tdcommons/bbb-martins": 0.8864524702939337,
    "tdcommons/ames": 0.8452652293955238,
    "tdcommons/ld50-zhu": 0.5227458254778016
}
```
