# chemeleon2_preview_initial_training_e4s281344 Baseline Results
timestamp: 2026-06-09 14:47:19.312428
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.583333 |
|  1 | test       | CLS_RET        | roc_auc     | 0.919365 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.54033  |
|  3 | test       | CLS_RET        | mcc         | 0.608418 |
|  4 | test       | CLS_RET        | pr_auc      | 0.887192 |
|  5 | test       | CLS_RET        | accuracy    | 0.90566  |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  21.4693   |
|  1 | test       | RET            | spearmanr           |   0.616364 |
|  2 | test       | RET            | r2                  |   0.342548 |
|  3 | test       | RET            | pearsonr            |   0.649382 |
|  4 | test       | RET            | mean_squared_error  | 780.662    |
|  5 | test       | RET            | explained_var       |   0.366271 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.615385 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.791586 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.539195 |
|  3 | test       | CLS_KIT        | mcc         | 0.54567  |
|  4 | test       | CLS_KIT        | pr_auc      | 0.649847 |
|  5 | test       | CLS_KIT        | accuracy    | 0.87069  |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  23.2938   |
|  1 | test       | KIT            | spearmanr           |   0.455989 |
|  2 | test       | KIT            | r2                  |   0.288993 |
|  3 | test       | KIT            | pearsonr            |   0.55876  |
|  4 | test       | KIT            | mean_squared_error  | 857.96     |
|  5 | test       | KIT            | explained_var       |   0.298305 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  16.8198   |
|  1 | test       | EGFR           | spearmanr           |   0.462553 |
|  2 | test       | EGFR           | r2                  |   0.427099 |
|  3 | test       | EGFR           | pearsonr            |   0.654377 |
|  4 | test       | EGFR           | mean_squared_error  | 461.625    |
|  5 | test       | EGFR           | explained_var       |   0.428184 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.418515 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.485587 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.352169 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.600462 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.35124  |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.359311 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.769932  |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.662609  |
|  2 | test       | LOG_RPPB       | r2                  | 0.0800727 |
|  3 | test       | LOG_RPPB       | pearsonr            | 0.645247  |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.817339  |
|  5 | test       | LOG_RPPB       | explained_var       | 0.140058  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.616533 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.617923 |
|  2 | test       | LOG_HPPB       | r2                  | 0.179667 |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.636776 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.496825 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.225771 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.304494 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.814459 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.664007 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.815024 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.166449 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.66405  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.402774 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.744545 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.539967 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.735907 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.259709 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.541188 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.341609 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.732264 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.513458 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.718907 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.188978 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.513896 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.462552 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.65028 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.333106 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.630816 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.237045 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.369868 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.558426 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.902174 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.699368 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.202848 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.701514 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.882231 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.324059 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.812666 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.900016 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.841697 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.548244 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.8871915491704183,
    "polaris/pkis2-ret-wt-reg-v2": 780.6623794651433,
    "polaris/pkis2-kit-wt-cls-v2": 0.6498471849944819,
    "polaris/pkis2-kit-wt-reg-v2": 857.9604658823943,
    "polaris/pkis2-egfr-wt-reg-v2": 461.6253948399814,
    "polaris/adme-fang-solu-1": 0.6004615304784903,
    "polaris/adme-fang-rppb-1": 0.6452470509279817,
    "polaris/adme-fang-hppb-1": 0.6367757323130053,
    "polaris/adme-fang-perm-1": 0.8150244305220798,
    "polaris/adme-fang-rclint-1": 0.7359067072212,
    "polaris/adme-fang-hclint-1": 0.7189074535273141,
    "tdcommons/lipophilicity-astrazeneca": 0.46255227054300757,
    "tdcommons/ppbr-az": 8.650283393655139,
    "tdcommons/clearance-hepatocyte-az": 0.33310560181766635,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6308161554768869,
    "tdcommons/half-life-obach": 0.23704522290835442,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3698677882256821,
    "tdcommons/clearance-microsome-az": 0.5584257524778443,
    "tdcommons/dili": 0.9021739130434783,
    "tdcommons/bioavailability-ma": 0.6993681410043232,
    "tdcommons/vdss-lombardo": 0.20284785549344547,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.7015144665461122,
    "tdcommons/pgp-broccatelli": 0.8822314049586777,
    "tdcommons/caco2-wang": 0.324059296442187,
    "tdcommons/herg": 0.8126656848306333,
    "tdcommons/bbb-martins": 0.9000156347717323,
    "tdcommons/ames": 0.8416965282265172,
    "tdcommons/ld50-zhu": 0.5482444192534048
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.64     |
|  1 | test       | CLS_RET        | roc_auc     | 0.932584 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.598823 |
|  3 | test       | CLS_RET        | mcc         | 0.653736 |
|  4 | test       | CLS_RET        | pr_auc      | 0.876891 |
|  5 | test       | CLS_RET        | accuracy    | 0.915094 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  20.5805   |
|  1 | test       | RET            | spearmanr           |   0.661744 |
|  2 | test       | RET            | r2                  |   0.397745 |
|  3 | test       | RET            | pearsonr            |   0.685693 |
|  4 | test       | RET            | mean_squared_error  | 715.12     |
|  5 | test       | RET            | explained_var       |   0.427574 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.571429 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.80706  |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.476954 |
|  3 | test       | CLS_KIT        | mcc         | 0.477761 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.604633 |
|  5 | test       | CLS_KIT        | accuracy    | 0.844828 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  23.5575   |
|  1 | test       | KIT            | spearmanr           |   0.465158 |
|  2 | test       | KIT            | r2                  |   0.228228 |
|  3 | test       | KIT            | pearsonr            |   0.541545 |
|  4 | test       | KIT            | mean_squared_error  | 931.285    |
|  5 | test       | KIT            | explained_var       |   0.231611 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  16.6566   |
|  1 | test       | EGFR           | spearmanr           |   0.400167 |
|  2 | test       | EGFR           | r2                  |   0.441941 |
|  3 | test       | EGFR           | pearsonr            |   0.667853 |
|  4 | test       | EGFR           | mean_squared_error  | 449.666    |
|  5 | test       | EGFR           | explained_var       |   0.445077 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.427015 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.509035 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.384915 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.622219 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.333486 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.385951 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.462352 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.796522 |
|  2 | test       | LOG_RPPB       | r2                  | 0.552366 |
|  3 | test       | LOG_RPPB       | pearsonr            | 0.806361 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.397714 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.559152 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.570976 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.627244 |
|  2 | test       | LOG_HPPB       | r2                  | 0.29853  |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.671956 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.424837 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.357128 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.299198 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.817699 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.665475 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.81764  |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.165721 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.665839 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.414547 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.733751 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.519448 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.730807 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.271292 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.533837 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.345589 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.711188 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.489265 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.705188 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.198374 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.489625 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.457326 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.59015 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.381372 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.608653 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.196415 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.31532 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.547731 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.895217 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.640173 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.253961 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.636754 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.918688 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.358865 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.812077 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.905703 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.834837 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.585681 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.8768909717232269,
    "polaris/pkis2-ret-wt-reg-v2": 715.1203218001625,
    "polaris/pkis2-kit-wt-cls-v2": 0.604633132189868,
    "polaris/pkis2-kit-wt-reg-v2": 931.2845111146794,
    "polaris/pkis2-egfr-wt-reg-v2": 449.6660593735564,
    "polaris/adme-fang-solu-1": 0.6222185215835123,
    "polaris/adme-fang-rppb-1": 0.8063606014690381,
    "polaris/adme-fang-hppb-1": 0.671955667794289,
    "polaris/adme-fang-perm-1": 0.8176400134493658,
    "polaris/adme-fang-rclint-1": 0.7308065000528484,
    "polaris/adme-fang-hclint-1": 0.7051881137216277,
    "tdcommons/lipophilicity-astrazeneca": 0.4573255560171037,
    "tdcommons/ppbr-az": 8.590153368026925,
    "tdcommons/clearance-hepatocyte-az": 0.3813724975460476,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6086534141994656,
    "tdcommons/half-life-obach": 0.19641507072506945,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3153197728973842,
    "tdcommons/clearance-microsome-az": 0.5477313867842608,
    "tdcommons/dili": 0.8952173913043479,
    "tdcommons/bioavailability-ma": 0.6401729298303958,
    "tdcommons/vdss-lombardo": 0.25396107199722995,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6367540687160941,
    "tdcommons/pgp-broccatelli": 0.9186883497733939,
    "tdcommons/caco2-wang": 0.3588649168766065,
    "tdcommons/herg": 0.8120765832106038,
    "tdcommons/bbb-martins": 0.9057027829893683,
    "tdcommons/ames": 0.83483718106875,
    "tdcommons/ld50-zhu": 0.5856812025265055
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.62069  |
|  1 | test       | CLS_RET        | roc_auc     | 0.88764  |
|  2 | test       | CLS_RET        | cohen_kappa | 0.562641 |
|  3 | test       | CLS_RET        | mcc         | 0.5741   |
|  4 | test       | CLS_RET        | pr_auc      | 0.658722 |
|  5 | test       | CLS_RET        | accuracy    | 0.896226 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  20.5203   |
|  1 | test       | RET            | spearmanr           |   0.596843 |
|  2 | test       | RET            | r2                  |   0.356749 |
|  3 | test       | RET            | pearsonr            |   0.626156 |
|  4 | test       | RET            | mean_squared_error  | 763.8      |
|  5 | test       | RET            | explained_var       |   0.390694 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.577778 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.781915 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.476236 |
|  3 | test       | CLS_KIT        | mcc         | 0.476417 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.561952 |
|  5 | test       | CLS_KIT        | accuracy    | 0.836207 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  23.0745   |
|  1 | test       | KIT            | spearmanr           |   0.501923 |
|  2 | test       | KIT            | r2                  |   0.293366 |
|  3 | test       | KIT            | pearsonr            |   0.572472 |
|  4 | test       | KIT            | mean_squared_error  | 852.684    |
|  5 | test       | KIT            | explained_var       |   0.298631 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  17.0714   |
|  1 | test       | EGFR           | spearmanr           |   0.437562 |
|  2 | test       | EGFR           | r2                  |   0.445981 |
|  3 | test       | EGFR           | pearsonr            |   0.679939 |
|  4 | test       | EGFR           | mean_squared_error  | 446.411    |
|  5 | test       | EGFR           | explained_var       |   0.456619 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.412931 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.509186 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.366358 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.608484 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.343547 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.37014  |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.525954 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.757391 |
|  2 | test       | LOG_RPPB       | r2                  | 0.497847 |
|  3 | test       | LOG_RPPB       | pearsonr            | 0.772756 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.446154 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.50429  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.573118 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.67721  |
|  2 | test       | LOG_HPPB       | r2                  | 0.308039 |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.706125 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.419079 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.405228 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.302802 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.810701 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.659397 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.813738 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.168732 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.660539 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.401197 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.73678  |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.533381 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.730481 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.263427 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.533558 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.348169 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.720948 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.495514 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.708797 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.195947 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.495544 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.46593 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.61882 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.329701 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.660048 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.385799 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.400321 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.577474 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.889565 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.66578 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.24056 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.64071 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.903159 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.335873 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.873932 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.926907 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.823691 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.557558 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6587224350178174,
    "polaris/pkis2-ret-wt-reg-v2": 763.7998497601023,
    "polaris/pkis2-kit-wt-cls-v2": 0.561952048444984,
    "polaris/pkis2-kit-wt-reg-v2": 852.683915106281,
    "polaris/pkis2-egfr-wt-reg-v2": 446.4106854254879,
    "polaris/adme-fang-solu-1": 0.6084842046309481,
    "polaris/adme-fang-rppb-1": 0.772756336473356,
    "polaris/adme-fang-hppb-1": 0.7061247777015098,
    "polaris/adme-fang-perm-1": 0.8137380532004442,
    "polaris/adme-fang-rclint-1": 0.7304811662733989,
    "polaris/adme-fang-hclint-1": 0.7087970189674975,
    "tdcommons/lipophilicity-astrazeneca": 0.46593011664208916,
    "tdcommons/ppbr-az": 8.618820497243265,
    "tdcommons/clearance-hepatocyte-az": 0.32970139036206386,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6600482397961269,
    "tdcommons/half-life-obach": 0.38579880162500085,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4003213832875573,
    "tdcommons/clearance-microsome-az": 0.577473751711023,
    "tdcommons/dili": 0.8895652173913043,
    "tdcommons/bioavailability-ma": 0.6657798470236115,
    "tdcommons/vdss-lombardo": 0.24055978824848223,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6407097649186256,
    "tdcommons/pgp-broccatelli": 0.9031591575579845,
    "tdcommons/caco2-wang": 0.3358733064360567,
    "tdcommons/herg": 0.8739322533136966,
    "tdcommons/bbb-martins": 0.9269074421513446,
    "tdcommons/ames": 0.823691476238031,
    "tdcommons/ld50-zhu": 0.5575580761926261
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.733333 |
|  1 | test       | CLS_RET        | roc_auc     | 0.912756 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.690285 |
|  3 | test       | CLS_RET        | mcc         | 0.698714 |
|  4 | test       | CLS_RET        | pr_auc      | 0.787542 |
|  5 | test       | CLS_RET        | accuracy    | 0.924528 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  21.7888   |
|  1 | test       | RET            | spearmanr           |   0.539678 |
|  2 | test       | RET            | r2                  |   0.351094 |
|  3 | test       | RET            | pearsonr            |   0.601355 |
|  4 | test       | RET            | mean_squared_error  | 770.515    |
|  5 | test       | RET            | explained_var       |   0.361454 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.604651 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.799807 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.514764 |
|  3 | test       | CLS_KIT        | mcc         | 0.514974 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.636539 |
|  5 | test       | CLS_KIT        | accuracy    | 0.853448 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  22.8863   |
|  1 | test       | KIT            | spearmanr           |   0.538735 |
|  2 | test       | KIT            | r2                  |   0.323001 |
|  3 | test       | KIT            | pearsonr            |   0.58211  |
|  4 | test       | KIT            | mean_squared_error  | 816.924    |
|  5 | test       | KIT            | explained_var       |   0.33007  |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  17.6957   |
|  1 | test       | EGFR           | spearmanr           |   0.351446 |
|  2 | test       | EGFR           | r2                  |   0.385561 |
|  3 | test       | EGFR           | pearsonr            |   0.62201  |
|  4 | test       | EGFR           | mean_squared_error  | 495.095    |
|  5 | test       | EGFR           | explained_var       |   0.385589 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.405162 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.523052 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.393704 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.629116 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.328721 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.395772 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.59079  |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.763478 |
|  2 | test       | LOG_RPPB       | r2                  | 0.404378 |
|  3 | test       | LOG_RPPB       | pearsonr            | 0.794406 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.529199 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.409951 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.453481 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.718313 |
|  2 | test       | LOG_HPPB       | r2                  | 0.518126 |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.766528 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.291842 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.566396 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.33183  |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.783787 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.623641 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.789977 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.186445 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.624044 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.406982 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.738432 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.533681 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.73528  |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.263257 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.538843 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.33526  |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.726807 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.51241  |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.72039  |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.189385 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.516218 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.465624 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.61873 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.35583 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.596704 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.128277 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.366237 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.468455 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.907826 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.696375 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.126067 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.629182 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.891696 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.319946 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.844772 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.934705 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.838424 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.539399 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7875417536798767,
    "polaris/pkis2-ret-wt-reg-v2": 770.5145204949961,
    "polaris/pkis2-kit-wt-cls-v2": 0.6365394044154806,
    "polaris/pkis2-kit-wt-reg-v2": 816.9235014368328,
    "polaris/pkis2-egfr-wt-reg-v2": 495.095293994394,
    "polaris/adme-fang-solu-1": 0.6291159681948117,
    "polaris/adme-fang-rppb-1": 0.7944056996099662,
    "polaris/adme-fang-hppb-1": 0.766527861119033,
    "polaris/adme-fang-perm-1": 0.7899769023149505,
    "polaris/adme-fang-rclint-1": 0.7352802250068373,
    "polaris/adme-fang-hclint-1": 0.7203902994793484,
    "tdcommons/lipophilicity-astrazeneca": 0.4656244401931762,
    "tdcommons/ppbr-az": 8.618725418609456,
    "tdcommons/clearance-hepatocyte-az": 0.3558299890963118,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5967043156060654,
    "tdcommons/half-life-obach": 0.12827748779500026,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3662367028058796,
    "tdcommons/clearance-microsome-az": 0.4684547390715376,
    "tdcommons/dili": 0.9078260869565217,
    "tdcommons/bioavailability-ma": 0.6963751247090124,
    "tdcommons/vdss-lombardo": 0.12606678257014037,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6291817359855335,
    "tdcommons/pgp-broccatelli": 0.8916955478539056,
    "tdcommons/caco2-wang": 0.3199464185325539,
    "tdcommons/herg": 0.8447717231222386,
    "tdcommons/bbb-martins": 0.9347052845528456,
    "tdcommons/ames": 0.8384244845209423,
    "tdcommons/ld50-zhu": 0.5393986938886939
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.538462 |
|  1 | test       | CLS_RET        | roc_auc     | 0.904164 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.480816 |
|  3 | test       | CLS_RET        | mcc         | 0.512494 |
|  4 | test       | CLS_RET        | pr_auc      | 0.772379 |
|  5 | test       | CLS_RET        | accuracy    | 0.886792 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  21.4735   |
|  1 | test       | RET            | spearmanr           |   0.538822 |
|  2 | test       | RET            | r2                  |   0.357974 |
|  3 | test       | RET            | pearsonr            |   0.611105 |
|  4 | test       | RET            | mean_squared_error  | 762.345    |
|  5 | test       | RET            | explained_var       |   0.370805 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.604651 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.801741 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.514764 |
|  3 | test       | CLS_KIT        | mcc         | 0.514974 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.600979 |
|  5 | test       | CLS_KIT        | accuracy    | 0.853448 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  23.3708   |
|  1 | test       | KIT            | spearmanr           |   0.424999 |
|  2 | test       | KIT            | r2                  |   0.235089 |
|  3 | test       | KIT            | pearsonr            |   0.519857 |
|  4 | test       | KIT            | mean_squared_error  | 923.006    |
|  5 | test       | KIT            | explained_var       |   0.248474 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  17.4536   |
|  1 | test       | EGFR           | spearmanr           |   0.445117 |
|  2 | test       | EGFR           | r2                  |   0.426986 |
|  3 | test       | EGFR           | pearsonr            |   0.654071 |
|  4 | test       | EGFR           | mean_squared_error  | 461.717    |
|  5 | test       | EGFR           | explained_var       |   0.427623 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.411197 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.515292 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.404438 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.636149 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.322901 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.404682 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.765168 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.751304 |
|  2 | test       | LOG_RPPB       | r2                  | 0.108071 |
|  3 | test       | LOG_RPPB       | pearsonr            | 0.795822 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.792463 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.200869 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.678041 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.700283 |
|  2 | test       | LOG_HPPB       | r2                  | 0.046623 |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.694811 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.577402 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.201149 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.321679 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.801312 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.641842 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.801982 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.177429 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.64248  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.406276 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.744284 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.537383 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.733143 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.261167 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.537469 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.336693 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.726071 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.507918 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.716178 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.19113  |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.507929 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.456373 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.85122 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.278514 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.600578 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0945527 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.369053 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.574678 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.882609 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.630861 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.245581 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.634494 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.913156 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.31018 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.825626 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.920302 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.840551 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.568095 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7723789611105218,
    "polaris/pkis2-ret-wt-reg-v2": 762.3448633574353,
    "polaris/pkis2-kit-wt-cls-v2": 0.6009790741276074,
    "polaris/pkis2-kit-wt-reg-v2": 923.0061636319913,
    "polaris/pkis2-egfr-wt-reg-v2": 461.71650282597835,
    "polaris/adme-fang-solu-1": 0.6361489999906025,
    "polaris/adme-fang-rppb-1": 0.7958216230521081,
    "polaris/adme-fang-hppb-1": 0.6948109666383326,
    "polaris/adme-fang-perm-1": 0.8019822148564407,
    "polaris/adme-fang-rclint-1": 0.7331427099252694,
    "polaris/adme-fang-hclint-1": 0.7161779711759745,
    "tdcommons/lipophilicity-astrazeneca": 0.4563732829775129,
    "tdcommons/ppbr-az": 8.851223124058814,
    "tdcommons/clearance-hepatocyte-az": 0.27851391081069676,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6005784851983315,
    "tdcommons/half-life-obach": 0.09455271910096276,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.36905251720294313,
    "tdcommons/clearance-microsome-az": 0.5746783711685904,
    "tdcommons/dili": 0.8826086956521739,
    "tdcommons/bioavailability-ma": 0.6308613235783173,
    "tdcommons/vdss-lombardo": 0.24558088001963269,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.634493670886076,
    "tdcommons/pgp-broccatelli": 0.9131564916022394,
    "tdcommons/caco2-wang": 0.3101795071214613,
    "tdcommons/herg": 0.8256259204712814,
    "tdcommons/bbb-martins": 0.9203017510944341,
    "tdcommons/ames": 0.8405510192093051,
    "tdcommons/ld50-zhu": 0.568094899236914
}
```
