# ChemProp Baseline Results
timestamp: 2026-09-16 13:39:36.887381
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.877358 |
|  1 | test       | CLS_RET        | mcc         | 0.453107 |
|  2 | test       | CLS_RET        | f1          | 0.380952 |
|  3 | test       | CLS_RET        | roc_auc     | 0.856576 |
|  4 | test       | CLS_RET        | pr_auc      | 0.642657 |
|  5 | test       | CLS_RET        | cohen_kappa | 0.34067  |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.311632 |
|  1 | test       | RET            | pearsonr            |   0.558914 |
|  2 | test       | RET            | mean_squared_error  | 849.053    |
|  3 | test       | RET            | spearmanr           |   0.5496   |
|  4 | test       | RET            | mean_absolute_error |  21.855    |
|  5 | test       | RET            | r2                  |   0.284951 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  1 | test       | CLS_KIT        | mcc         | 0.435091 |
|  2 | test       | CLS_KIT        | f1          | 0.451613 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.827853 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.600484 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.38375  |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.318693 |
|  1 | test       | KIT            | pearsonr            |   0.572771 |
|  2 | test       | KIT            | mean_squared_error  | 893.371    |
|  3 | test       | KIT            | spearmanr           |   0.515267 |
|  4 | test       | KIT            | mean_absolute_error |  22.0142   |
|  5 | test       | KIT            | r2                  |   0.259648 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.454607 |
|  1 | test       | EGFR           | pearsonr            |   0.674348 |
|  2 | test       | EGFR           | mean_squared_error  | 440.576    |
|  3 | test       | EGFR           | spearmanr           |   0.391038 |
|  4 | test       | EGFR           | mean_absolute_error |  16.5071   |
|  5 | test       | EGFR           | r2                  |   0.453223 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.407026 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.640019 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.324623 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.542313 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.381218 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.401261 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.168761  |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.414549  |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.808964  |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.494783  |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.716732  |
|  5 | test       | LOG_RPPB       | r2                  | 0.0894991 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.330256 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.602494 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.413567 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.578195 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.541981 |
|  5 | test       | LOG_HPPB       | r2                  | 0.317139 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.610332 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.781284 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.195452 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.790057 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.336519 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.60546  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.497831 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.706203 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.288887 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.712788 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.42546  |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.488281 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.467448 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.698987 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.20685  |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.706212 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.35331  |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.467444 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.445594 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  7.7637 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.396162 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.665824 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.244917 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.417447 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.605186 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.918696 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.569671 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.562561 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.571768 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.918488 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.373653 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.849779 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.858544 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.838401 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.586801 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6426572957717763,
    "polaris/pkis2-ret-wt-reg-v2": 849.0530698521792,
    "polaris/pkis2-kit-wt-cls-v2": 0.6004836555381771,
    "polaris/pkis2-kit-wt-reg-v2": 893.3710615815303,
    "polaris/pkis2-egfr-wt-reg-v2": 440.5758689880552,
    "polaris/adme-fang-solu-1": 0.6400193543667096,
    "polaris/adme-fang-rppb-1": 0.4145490491869022,
    "polaris/adme-fang-hppb-1": 0.6024942202653071,
    "polaris/adme-fang-perm-1": 0.7812837305931727,
    "polaris/adme-fang-rclint-1": 0.7062028712524958,
    "polaris/adme-fang-hclint-1": 0.6989874014075668,
    "tdcommons/lipophilicity-astrazeneca": 0.4455941903307324,
    "tdcommons/ppbr-az": 7.7637004908252925,
    "tdcommons/clearance-hepatocyte-az": 0.3961616864519215,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6658237198704868,
    "tdcommons/half-life-obach": 0.24491729897754796,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4174469605142508,
    "tdcommons/clearance-microsome-az": 0.6051858267378684,
    "tdcommons/dili": 0.918695652173913,
    "tdcommons/bioavailability-ma": 0.5696707682075157,
    "tdcommons/vdss-lombardo": 0.5625609048954062,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5717676311030742,
    "tdcommons/pgp-broccatelli": 0.9184884030925087,
    "tdcommons/caco2-wang": 0.37365340510113065,
    "tdcommons/herg": 0.8497790868924889,
    "tdcommons/bbb-martins": 0.8585444027517198,
    "tdcommons/ames": 0.8384009869000764,
    "tdcommons/ld50-zhu": 0.5868010731833875
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.839623 |
|  1 | test       | CLS_RET        | mcc         | 0        |
|  2 | test       | CLS_RET        | f1          | 0        |
|  3 | test       | CLS_RET        | roc_auc     | 0.816259 |
|  4 | test       | CLS_RET        | pr_auc      | 0.586799 |
|  5 | test       | CLS_RET        | cohen_kappa | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.414206 |
|  1 | test       | RET            | pearsonr            |   0.653407 |
|  2 | test       | RET            | mean_squared_error  | 799.39     |
|  3 | test       | RET            | spearmanr           |   0.595542 |
|  4 | test       | RET            | mean_absolute_error |  20.7404   |
|  5 | test       | RET            | r2                  |   0.326775 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  1 | test       | CLS_KIT        | mcc         | 0.531571 |
|  2 | test       | CLS_KIT        | f1          | 0.622222 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.812863 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.647871 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.531369 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.288042 |
|  1 | test       | KIT            | pearsonr            |   0.582519 |
|  2 | test       | KIT            | mean_squared_error  | 879.41     |
|  3 | test       | KIT            | spearmanr           |   0.530677 |
|  4 | test       | KIT            | mean_absolute_error |  22.4112   |
|  5 | test       | KIT            | r2                  |   0.271218 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.394602 |
|  1 | test       | EGFR           | pearsonr            |   0.633351 |
|  2 | test       | EGFR           | mean_squared_error  | 498.304    |
|  3 | test       | EGFR           | spearmanr           |   0.279231 |
|  4 | test       | EGFR           | mean_absolute_error |  16.9102   |
|  5 | test       | EGFR           | r2                  |   0.381579 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.385002 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.632645 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.333443 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.541746 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.386273 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.384993 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.269736 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.519625 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.650421 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.665217 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.554073 |
|  5 | test       | LOG_RPPB       | r2                  | 0.267942 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.395336 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.634619 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.36717  |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.623271 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.488171 |
|  5 | test       | LOG_HPPB       | r2                  | 0.393747 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.595398 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.773696 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.204187 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.77325  |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.343815 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.587828 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.511617 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.715278 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.281447 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.723036 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.423705 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.501461 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.44286  |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.68236  |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.216912 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.693282 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.359759 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.441538 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.454409 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.50136 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.41307 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.705717 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.163867 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.416455 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.581184 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.925217 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.505155 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.516555 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.559109 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.896561 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.312954 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.82268 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.894778 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.843455 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.594967 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5867989435337546,
    "polaris/pkis2-ret-wt-reg-v2": 799.3904621515268,
    "polaris/pkis2-kit-wt-cls-v2": 0.6478710289211332,
    "polaris/pkis2-kit-wt-reg-v2": 879.4100811337046,
    "polaris/pkis2-egfr-wt-reg-v2": 498.30408472254993,
    "polaris/adme-fang-solu-1": 0.6326447734704839,
    "polaris/adme-fang-rppb-1": 0.5196253248409931,
    "polaris/adme-fang-hppb-1": 0.6346185484023408,
    "polaris/adme-fang-perm-1": 0.7736963692501686,
    "polaris/adme-fang-rclint-1": 0.7152777596127174,
    "polaris/adme-fang-hclint-1": 0.6823596861511351,
    "tdcommons/lipophilicity-astrazeneca": 0.4544085133189247,
    "tdcommons/ppbr-az": 7.501364053579478,
    "tdcommons/clearance-hepatocyte-az": 0.4130697723001206,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7057168639728413,
    "tdcommons/half-life-obach": 0.16386743287002348,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4164547276775561,
    "tdcommons/clearance-microsome-az": 0.581184233401406,
    "tdcommons/dili": 0.9252173913043479,
    "tdcommons/bioavailability-ma": 0.5051546391752577,
    "tdcommons/vdss-lombardo": 0.5165551709816185,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5591094032549728,
    "tdcommons/pgp-broccatelli": 0.8965609170887763,
    "tdcommons/caco2-wang": 0.3129537760689537,
    "tdcommons/herg": 0.822680412371134,
    "tdcommons/bbb-martins": 0.8947779862414009,
    "tdcommons/ames": 0.8434549335213143,
    "tdcommons/ld50-zhu": 0.5949671279619446
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.867925 |
|  1 | test       | CLS_RET        | mcc         | 0.387824 |
|  2 | test       | CLS_RET        | f1          | 0.363636 |
|  3 | test       | CLS_RET        | roc_auc     | 0.857237 |
|  4 | test       | CLS_RET        | pr_auc      | 0.636575 |
|  5 | test       | CLS_RET        | cohen_kappa | 0.313599 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.279527 |
|  1 | test       | RET            | pearsonr            |   0.533306 |
|  2 | test       | RET            | mean_squared_error  | 859.595    |
|  3 | test       | RET            | spearmanr           |   0.534722 |
|  4 | test       | RET            | mean_absolute_error |  22.493    |
|  5 | test       | RET            | r2                  |   0.276072 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.827586 |
|  1 | test       | CLS_KIT        | mcc         | 0.321498 |
|  2 | test       | CLS_KIT        | f1          | 0.375    |
|  3 | test       | CLS_KIT        | roc_auc     | 0.808511 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.587766 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.290954 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.322409 |
|  1 | test       | KIT            | pearsonr            |   0.595865 |
|  2 | test       | KIT            | mean_squared_error  | 857.061    |
|  3 | test       | KIT            | spearmanr           |   0.534344 |
|  4 | test       | KIT            | mean_absolute_error |  21.8966   |
|  5 | test       | KIT            | r2                  |   0.289739 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.437289 |
|  1 | test       | EGFR           | pearsonr            |   0.661873 |
|  2 | test       | EGFR           | mean_squared_error  | 453.419    |
|  3 | test       | EGFR           | spearmanr           |   0.291027 |
|  4 | test       | EGFR           | mean_absolute_error |  16.6743   |
|  5 | test       | EGFR           | r2                  |   0.437283 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.406    |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.637374 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.327957 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.51676  |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.385684 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.395112 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.337104 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.580789 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.590556 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.666957 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.506247 |
|  5 | test       | LOG_RPPB       | r2                  | 0.33532  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | LOG_HPPB       | explained_var       |  0.0906801  |
|  1 | test       | LOG_HPPB       | pearsonr            |  0.671123   |
|  2 | test       | LOG_HPPB       | mean_squared_error  |  0.610806   |
|  3 | test       | LOG_HPPB       | spearmanr           |  0.676293   |
|  4 | test       | LOG_HPPB       | mean_absolute_error |  0.69426    |
|  5 | test       | LOG_HPPB       | r2                  | -0.00853216 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.599186 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.774493 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.199011 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.784    |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.342616 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.598277 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.493539 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.703389 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.287708 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.708297 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.431557 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.490371 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.453535 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.697756 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.214451 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.707177 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.359777 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.447875 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.445457 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.69787 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.398029 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.692144 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0675633 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.424075 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.624166 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.924783 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.454938 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.473564 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.611551 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.918022 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.323094 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.81458 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.902283 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.842552 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.583426 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6365752729029,
    "polaris/pkis2-ret-wt-reg-v2": 859.5954308492272,
    "polaris/pkis2-kit-wt-cls-v2": 0.5877661405317551,
    "polaris/pkis2-kit-wt-reg-v2": 857.0606570851212,
    "polaris/pkis2-egfr-wt-reg-v2": 453.4193730999389,
    "polaris/adme-fang-solu-1": 0.637373827546844,
    "polaris/adme-fang-rppb-1": 0.5807889014785247,
    "polaris/adme-fang-hppb-1": 0.6711227696608865,
    "polaris/adme-fang-perm-1": 0.7744932323149158,
    "polaris/adme-fang-rclint-1": 0.7033892720819905,
    "polaris/adme-fang-hclint-1": 0.697756113189267,
    "tdcommons/lipophilicity-astrazeneca": 0.44545669123672305,
    "tdcommons/ppbr-az": 7.697867514622232,
    "tdcommons/clearance-hepatocyte-az": 0.3980288519016042,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6921441686694793,
    "tdcommons/half-life-obach": 0.06756334904949929,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4240746669581145,
    "tdcommons/clearance-microsome-az": 0.6241659552124907,
    "tdcommons/dili": 0.9247826086956522,
    "tdcommons/bioavailability-ma": 0.4549384768872631,
    "tdcommons/vdss-lombardo": 0.473563772808027,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6115506329113924,
    "tdcommons/pgp-broccatelli": 0.9180218608371101,
    "tdcommons/caco2-wang": 0.32309417550917413,
    "tdcommons/herg": 0.814580265095729,
    "tdcommons/bbb-martins": 0.9022826766729206,
    "tdcommons/ames": 0.8425522332530498,
    "tdcommons/ld50-zhu": 0.5834256771407689
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.877358 |
|  1 | test       | CLS_RET        | mcc         | 0.459084 |
|  2 | test       | CLS_RET        | f1          | 0.48     |
|  3 | test       | CLS_RET        | roc_auc     | 0.835426 |
|  4 | test       | CLS_RET        | pr_auc      | 0.625595 |
|  5 | test       | CLS_RET        | cohen_kappa | 0.420521 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.385798 |
|  1 | test       | RET            | pearsonr            |   0.621328 |
|  2 | test       | RET            | mean_squared_error  | 729.802    |
|  3 | test       | RET            | spearmanr           |   0.589452 |
|  4 | test       | RET            | mean_absolute_error |  21.3134   |
|  5 | test       | RET            | r2                  |   0.385381 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  1 | test       | CLS_KIT        | mcc         | 0.468918 |
|  2 | test       | CLS_KIT        | f1          | 0.540541 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.823017 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.644339 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.457048 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.351166 |
|  1 | test       | KIT            | pearsonr            |   0.609931 |
|  2 | test       | KIT            | mean_squared_error  | 813.031    |
|  3 | test       | KIT            | spearmanr           |   0.541247 |
|  4 | test       | KIT            | mean_absolute_error |  21.2161   |
|  5 | test       | KIT            | r2                  |   0.326227 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.399875 |
|  1 | test       | EGFR           | pearsonr            |   0.635476 |
|  2 | test       | EGFR           | mean_squared_error  | 503.937    |
|  3 | test       | EGFR           | spearmanr           |   0.310109 |
|  4 | test       | EGFR           | mean_absolute_error |  18.5174   |
|  5 | test       | EGFR           | r2                  |   0.374588 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.39324  |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.62709  |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.333039 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.559476 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.378949 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.385739 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.244043 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.494448 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.674532 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.683478 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.592549 |
|  5 | test       | LOG_RPPB       | r2                  | 0.240803 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.37199  |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.673924 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.393345 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.64558  |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.489469 |
|  5 | test       | LOG_HPPB       | r2                  | 0.350529 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.568345 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.763884 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.214277 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.772038 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.360324 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.567459 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.517065 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.720261 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.272797 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.725342 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.419794 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.516784 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.470904 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.700774 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.214043 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.722711 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.351894 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.448924 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.443725 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.88206 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.433703 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.617585 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.199195 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.376455 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.608637 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.918696 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.482541 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.448394 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.59019 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.903759 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.347801 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.825037 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.90154 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.840402 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.561842 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6255948485030051,
    "polaris/pkis2-ret-wt-reg-v2": 729.8018388811814,
    "polaris/pkis2-kit-wt-cls-v2": 0.6443386249590073,
    "polaris/pkis2-kit-wt-reg-v2": 813.0309841262914,
    "polaris/pkis2-egfr-wt-reg-v2": 503.9370303263191,
    "polaris/adme-fang-solu-1": 0.6270895853747629,
    "polaris/adme-fang-rppb-1": 0.4944483824895757,
    "polaris/adme-fang-hppb-1": 0.6739242759866819,
    "polaris/adme-fang-perm-1": 0.7638838212337935,
    "polaris/adme-fang-rclint-1": 0.7202613334592175,
    "polaris/adme-fang-hclint-1": 0.7007737925939004,
    "tdcommons/lipophilicity-astrazeneca": 0.4437253016687575,
    "tdcommons/ppbr-az": 7.882058114749587,
    "tdcommons/clearance-hepatocyte-az": 0.43370262512183566,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6175845506169894,
    "tdcommons/half-life-obach": 0.1991951084008923,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.37645480914079976,
    "tdcommons/clearance-microsome-az": 0.6086370891695884,
    "tdcommons/dili": 0.918695652173913,
    "tdcommons/bioavailability-ma": 0.48254073827735283,
    "tdcommons/vdss-lombardo": 0.4483937515465038,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5901898734177216,
    "tdcommons/pgp-broccatelli": 0.9037589976006397,
    "tdcommons/caco2-wang": 0.3478011164013873,
    "tdcommons/herg": 0.8250368188512519,
    "tdcommons/bbb-martins": 0.9015400250156348,
    "tdcommons/ames": 0.840402200943821,
    "tdcommons/ld50-zhu": 0.5618417036743061
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.858491 |
|  1 | test       | CLS_RET        | mcc         | 0.317299 |
|  2 | test       | CLS_RET        | f1          | 0.210526 |
|  3 | test       | CLS_RET        | roc_auc     | 0.817581 |
|  4 | test       | CLS_RET        | pr_auc      | 0.713188 |
|  5 | test       | CLS_RET        | cohen_kappa | 0.182939 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.2927   |
|  1 | test       | RET            | pearsonr            |   0.54116  |
|  2 | test       | RET            | mean_squared_error  | 854.083    |
|  3 | test       | RET            | spearmanr           |   0.502054 |
|  4 | test       | RET            | mean_absolute_error |  22.8261   |
|  5 | test       | RET            | r2                  |   0.280715 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.862069 |
|  1 | test       | CLS_KIT        | mcc         | 0.475801 |
|  2 | test       | CLS_KIT        | f1          | 0.466667 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.854932 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.687118 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.40665  |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.332641 |
|  1 | test       | KIT            | pearsonr            |   0.586174 |
|  2 | test       | KIT            | mean_squared_error  | 847.448    |
|  3 | test       | KIT            | spearmanr           |   0.51778  |
|  4 | test       | KIT            | mean_absolute_error |  21.1532   |
|  5 | test       | KIT            | r2                  |   0.297705 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.442045 |
|  1 | test       | EGFR           | pearsonr            |   0.672037 |
|  2 | test       | EGFR           | mean_squared_error  | 452.62     |
|  3 | test       | EGFR           | spearmanr           |   0.355172 |
|  4 | test       | EGFR           | mean_absolute_error |  16.4054   |
|  5 | test       | EGFR           | r2                  |   0.438276 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.418559 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.655309 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.326274 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.531203 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.374998 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.398217 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.211122 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.51646  |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.719622 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.638261 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.679802 |
|  5 | test       | LOG_RPPB       | r2                  | 0.190054 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.483925 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.695919 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.516584 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.721216 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.63035  |
|  5 | test       | LOG_HPPB       | r2                  | 0.147042 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.571405 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.765897 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.212357 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.777377 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.336679 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.571336 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.524114 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.723974 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.268692 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.735666 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.414158 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.524054 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.46925  |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.694166 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.206715 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.705848 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.354527 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.467792 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.452859 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.63005 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.370687 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.650287 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.13313 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.446504 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.601941 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.927391 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.49019 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.376193 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.55278 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.918555 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.319981 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.839028 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.889384 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.839317 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.556273 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7131882234756786,
    "polaris/pkis2-ret-wt-reg-v2": 854.0825005789593,
    "polaris/pkis2-kit-wt-cls-v2": 0.6871179811132668,
    "polaris/pkis2-kit-wt-reg-v2": 847.4480744659508,
    "polaris/pkis2-egfr-wt-reg-v2": 452.6198174783641,
    "polaris/adme-fang-solu-1": 0.6553091790934225,
    "polaris/adme-fang-rppb-1": 0.516459877006685,
    "polaris/adme-fang-hppb-1": 0.6959185352213773,
    "polaris/adme-fang-perm-1": 0.7658970554352469,
    "polaris/adme-fang-rclint-1": 0.7239735955944371,
    "polaris/adme-fang-hclint-1": 0.6941662521949008,
    "tdcommons/lipophilicity-astrazeneca": 0.45285874856653674,
    "tdcommons/ppbr-az": 7.6300466231071455,
    "tdcommons/clearance-hepatocyte-az": 0.37068749591853384,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6502873939121387,
    "tdcommons/half-life-obach": 0.13313048487840115,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4465042124715072,
    "tdcommons/clearance-microsome-az": 0.601940904638516,
    "tdcommons/dili": 0.927391304347826,
    "tdcommons/bioavailability-ma": 0.490189557698703,
    "tdcommons/vdss-lombardo": 0.376193170839052,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5527802893309222,
    "tdcommons/pgp-broccatelli": 0.9185550519861372,
    "tdcommons/caco2-wang": 0.31998121350785136,
    "tdcommons/herg": 0.8390279823269514,
    "tdcommons/bbb-martins": 0.889383989993746,
    "tdcommons/ames": 0.8393173941138459,
    "tdcommons/ld50-zhu": 0.556273441999949
}
```
