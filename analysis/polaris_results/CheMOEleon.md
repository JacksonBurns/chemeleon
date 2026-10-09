# CheMOEleon Results
timestamp: 2026-10-09 16:08:01.596889
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.760491 |
|  1 | test       | CLS_RET        | roc_auc     | 0.920026 |
|  2 | test       | CLS_RET        | pr_auc      | 0.825005 |
|  3 | test       | CLS_RET        | mcc         | 0.760936 |
|  4 | test       | CLS_RET        | accuracy    | 0.933962 |
|  5 | test       | CLS_RET        | f1          | 0.8      |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.310553 |
|  1 | test       | RET            | mean_squared_error  | 818.653    |
|  2 | test       | RET            | mean_absolute_error |  22.4349   |
|  3 | test       | RET            | explained_var       |   0.323471 |
|  4 | test       | RET            | spearmanr           |   0.627759 |
|  5 | test       | RET            | pearsonr            |   0.577747 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.648678 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.845261 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.765616 |
|  3 | test       | CLS_KIT        | mcc         | 0.665524 |
|  4 | test       | CLS_KIT        | accuracy    | 0.905172 |
|  5 | test       | CLS_KIT        | f1          | 0.702703 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.381017 |
|  1 | test       | KIT            | mean_squared_error  | 746.916    |
|  2 | test       | KIT            | mean_absolute_error |  21.1898   |
|  3 | test       | KIT            | explained_var       |   0.392506 |
|  4 | test       | KIT            | spearmanr           |   0.560305 |
|  5 | test       | KIT            | pearsonr            |   0.62874  |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.452154 |
|  1 | test       | EGFR           | mean_squared_error  | 441.437    |
|  2 | test       | EGFR           | mean_absolute_error |  16.5175   |
|  3 | test       | EGFR           | explained_var       |   0.462578 |
|  4 | test       | EGFR           | spearmanr           |   0.373    |
|  5 | test       | EGFR           | pearsonr            |   0.683228 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.384265 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.333838 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.38271  |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.395504 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.523536 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.630166 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.0833928 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.814389  |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.692539  |
|  3 | test       | LOG_RPPB       | explained_var       | 0.104795  |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.483478  |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.331074  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.389849 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.369531 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.50076  |
|  3 | test       | LOG_HPPB       | explained_var       | 0.409985 |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.683627 |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.670983 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.592864 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.201692 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.338497 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.592945 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.767532 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.771136 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.472793 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.297631 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.431634 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.47604  |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.70288  |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.691413 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.451103 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.213197 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.360026 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.45135  |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.683872 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.686132 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.458656 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.51458 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.421215 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.592272 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.260358 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.39637 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.603061 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.895217 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.568673 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.347535 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.563178 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.919621 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.408872 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.882916 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.868824 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.851955 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.555907 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.8250051669678926,
    "polaris/pkis2-ret-wt-reg-v2": 818.6527766177521,
    "polaris/pkis2-kit-wt-cls-v2": 0.7656164572300683,
    "polaris/pkis2-kit-wt-reg-v2": 746.9164955674472,
    "polaris/pkis2-egfr-wt-reg-v2": 441.4368221252618,
    "polaris/adme-fang-solu-1": 0.6301660226450432,
    "polaris/adme-fang-rppb-1": 0.33107402082881326,
    "polaris/adme-fang-hppb-1": 0.6709826631412233,
    "polaris/adme-fang-perm-1": 0.7711359645509737,
    "polaris/adme-fang-rclint-1": 0.6914127870634714,
    "polaris/adme-fang-hclint-1": 0.6861320229220331,
    "tdcommons/lipophilicity-astrazeneca": 0.4586558046568008,
    "tdcommons/ppbr-az": 8.514577651458904,
    "tdcommons/clearance-hepatocyte-az": 0.4212151702879444,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5922723690622845,
    "tdcommons/half-life-obach": 0.26035778776330465,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.39637012326761073,
    "tdcommons/clearance-microsome-az": 0.6030606984265566,
    "tdcommons/dili": 0.8952173913043479,
    "tdcommons/bioavailability-ma": 0.5686730961090788,
    "tdcommons/vdss-lombardo": 0.3475350893579801,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5631781193490054,
    "tdcommons/pgp-broccatelli": 0.9196214342841909,
    "tdcommons/caco2-wang": 0.4088724476768074,
    "tdcommons/herg": 0.8829160530191458,
    "tdcommons/bbb-martins": 0.8688242651657286,
    "tdcommons/ames": 0.8519551978695491,
    "tdcommons/ld50-zhu": 0.5559066247030267
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0        |
|  1 | test       | CLS_RET        | roc_auc     | 0.88698  |
|  2 | test       | CLS_RET        | pr_auc      | 0.648434 |
|  3 | test       | CLS_RET        | mcc         | 0        |
|  4 | test       | CLS_RET        | accuracy    | 0.839623 |
|  5 | test       | CLS_RET        | f1          | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.28176  |
|  1 | test       | RET            | mean_squared_error  | 852.842    |
|  2 | test       | RET            | mean_absolute_error |  21.261    |
|  3 | test       | RET            | explained_var       |   0.376492 |
|  4 | test       | RET            | spearmanr           |   0.629774 |
|  5 | test       | RET            | pearsonr            |   0.626961 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.503667 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.871373 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.754569 |
|  3 | test       | CLS_KIT        | mcc         | 0.556543 |
|  4 | test       | CLS_KIT        | accuracy    | 0.87931  |
|  5 | test       | CLS_KIT        | f1          | 0.5625   |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.370723 |
|  1 | test       | KIT            | mean_squared_error  | 759.338    |
|  2 | test       | KIT            | mean_absolute_error |  21.1589   |
|  3 | test       | KIT            | explained_var       |   0.405731 |
|  4 | test       | KIT            | spearmanr           |   0.576893 |
|  5 | test       | KIT            | pearsonr            |   0.642063 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.31697  |
|  1 | test       | EGFR           | mean_squared_error  | 550.364    |
|  2 | test       | EGFR           | mean_absolute_error |  17.7056   |
|  3 | test       | EGFR           | explained_var       |   0.355736 |
|  4 | test       | EGFR           | spearmanr           |   0.297874 |
|  5 | test       | EGFR           | pearsonr            |   0.603123 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.38312  |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.334459 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.386102 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.391444 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.521363 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.62844  |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.333287 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.592362 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.611206 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.353437 |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.71913  |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.653389 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.428064 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.346387 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.492343 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.465736 |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.667736 |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.684142 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.626466 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.185046 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.317906 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.626822 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.798848 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.792101 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.44833  |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.311442 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.448728 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.448367 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.674651 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.66964  |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.457128 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.210857 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.35461  |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.480489 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.690877 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.693887 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.466526 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.03034 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.373097 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.645881 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0260602 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.421037 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.634088 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.913478 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.56435 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.506897 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.557075 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.917222 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.371689 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.851546 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.879612 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.839122 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.571103 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6484339293416372,
    "polaris/pkis2-ret-wt-reg-v2": 852.8421658090385,
    "polaris/pkis2-kit-wt-cls-v2": 0.7545686846155328,
    "polaris/pkis2-kit-wt-reg-v2": 759.3381054265013,
    "polaris/pkis2-egfr-wt-reg-v2": 550.3638880632458,
    "polaris/adme-fang-solu-1": 0.6284400999166021,
    "polaris/adme-fang-rppb-1": 0.6533891204878061,
    "polaris/adme-fang-hppb-1": 0.6841416485416973,
    "polaris/adme-fang-perm-1": 0.7921006581429383,
    "polaris/adme-fang-rclint-1": 0.6696397301161521,
    "polaris/adme-fang-hclint-1": 0.6938866988776365,
    "tdcommons/lipophilicity-astrazeneca": 0.4665257900158564,
    "tdcommons/ppbr-az": 8.03033659633029,
    "tdcommons/clearance-hepatocyte-az": 0.3730968229692201,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6458805281126265,
    "tdcommons/half-life-obach": 0.02606023296263962,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4210365278005052,
    "tdcommons/clearance-microsome-az": 0.6340884820776409,
    "tdcommons/dili": 0.9134782608695653,
    "tdcommons/bioavailability-ma": 0.5643498503491852,
    "tdcommons/vdss-lombardo": 0.5068968860976512,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5570750452079566,
    "tdcommons/pgp-broccatelli": 0.9172220741135697,
    "tdcommons/caco2-wang": 0.37168851337900694,
    "tdcommons/herg": 0.8515463917525773,
    "tdcommons/bbb-martins": 0.8796122576610381,
    "tdcommons/ames": 0.8391215806066302,
    "tdcommons/ld50-zhu": 0.5711028936790032
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.448395 |
|  1 | test       | CLS_RET        | roc_auc     | 0.86649  |
|  2 | test       | CLS_RET        | pr_auc      | 0.600874 |
|  3 | test       | CLS_RET        | mcc         | 0.504899 |
|  4 | test       | CLS_RET        | accuracy    | 0.886792 |
|  5 | test       | CLS_RET        | f1          | 0.5      |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.454049 |
|  1 | test       | RET            | mean_squared_error  | 648.265    |
|  2 | test       | RET            | mean_absolute_error |  19.0393   |
|  3 | test       | RET            | explained_var       |   0.471655 |
|  4 | test       | RET            | spearmanr           |   0.633844 |
|  5 | test       | RET            | pearsonr            |   0.686919 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.628937 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.862669 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.767219 |
|  3 | test       | CLS_KIT        | mcc         | 0.629193 |
|  4 | test       | CLS_KIT        | accuracy    | 0.887931 |
|  5 | test       | CLS_KIT        | f1          | 0.697674 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.367162 |
|  1 | test       | KIT            | mean_squared_error  | 763.636    |
|  2 | test       | KIT            | mean_absolute_error |  20.7126   |
|  3 | test       | KIT            | explained_var       |   0.407497 |
|  4 | test       | KIT            | spearmanr           |   0.606924 |
|  5 | test       | KIT            | pearsonr            |   0.640395 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.467414 |
|  1 | test       | EGFR           | mean_squared_error  | 429.141    |
|  2 | test       | EGFR           | mean_absolute_error |  16.4577   |
|  3 | test       | EGFR           | explained_var       |   0.468367 |
|  4 | test       | EGFR           | spearmanr           |   0.42588  |
|  5 | test       | EGFR           | pearsonr            |   0.684767 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.369596 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.341791 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.400324 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.372316 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.523016 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.614291 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.506108 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.438814 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.494865 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.506413 |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.756522 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.755929 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.0321275 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.586181  |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.686941  |
|  3 | test       | LOG_HPPB       | explained_var       | 0.175152  |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.688059  |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.634676  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.608798 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.193799 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.331536 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.612674 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.785374 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.783015 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.434008 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.319527 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.447779 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.434078 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.679777 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.671896 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.412778 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.228083 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.365441 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.416135 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.665227 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.673422 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.484575 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  8.1375 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.393763 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.705786 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.292041 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.384247 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.55837 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.92913 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.481543 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.52619 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.54939 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.910757 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.436438 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.874669 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.881625 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.837212 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.594617 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6008735187527757,
    "polaris/pkis2-ret-wt-reg-v2": 648.2649392167101,
    "polaris/pkis2-kit-wt-cls-v2": 0.7672187713600971,
    "polaris/pkis2-kit-wt-reg-v2": 763.635764723823,
    "polaris/pkis2-egfr-wt-reg-v2": 429.14072093776366,
    "polaris/adme-fang-solu-1": 0.6142912195485162,
    "polaris/adme-fang-rppb-1": 0.7559286446072808,
    "polaris/adme-fang-hppb-1": 0.6346759600664215,
    "polaris/adme-fang-perm-1": 0.783014712970941,
    "polaris/adme-fang-rclint-1": 0.6718964352470246,
    "polaris/adme-fang-hclint-1": 0.6734224302771716,
    "tdcommons/lipophilicity-astrazeneca": 0.4845745185386567,
    "tdcommons/ppbr-az": 8.137500957018148,
    "tdcommons/clearance-hepatocyte-az": 0.39376265947952516,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7057856192418668,
    "tdcommons/half-life-obach": 0.29204086097264575,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3842472270252323,
    "tdcommons/clearance-microsome-az": 0.5583698200867914,
    "tdcommons/dili": 0.9291304347826087,
    "tdcommons/bioavailability-ma": 0.48154306617891585,
    "tdcommons/vdss-lombardo": 0.5261900715230784,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5493896925858951,
    "tdcommons/pgp-broccatelli": 0.9107571314316183,
    "tdcommons/caco2-wang": 0.4364379271855616,
    "tdcommons/herg": 0.8746686303387334,
    "tdcommons/bbb-martins": 0.881625234521576,
    "tdcommons/ames": 0.837212398911277,
    "tdcommons/ld50-zhu": 0.5946168224505062
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.215541 |
|  1 | test       | CLS_RET        | roc_auc     | 0.912095 |
|  2 | test       | CLS_RET        | pr_auc      | 0.669554 |
|  3 | test       | CLS_RET        | mcc         | 0.266557 |
|  4 | test       | CLS_RET        | accuracy    | 0.849057 |
|  5 | test       | CLS_RET        | f1          | 0.272727 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.378635 |
|  1 | test       | RET            | mean_squared_error  | 737.812    |
|  2 | test       | RET            | mean_absolute_error |  20.6339   |
|  3 | test       | RET            | explained_var       |   0.386158 |
|  4 | test       | RET            | spearmanr           |   0.58162  |
|  5 | test       | RET            | pearsonr            |   0.626397 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.322802 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.886364 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.827737 |
|  3 | test       | CLS_KIT        | mcc         | 0.438709 |
|  4 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  5 | test       | CLS_KIT        | f1          | 0.37037  |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.349116 |
|  1 | test       | KIT            | mean_squared_error  | 785.411    |
|  2 | test       | KIT            | mean_absolute_error |  20.9929   |
|  3 | test       | KIT            | explained_var       |   0.376895 |
|  4 | test       | KIT            | spearmanr           |   0.564722 |
|  5 | test       | KIT            | pearsonr            |   0.630011 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.400682 |
|  1 | test       | EGFR           | mean_squared_error  | 482.911    |
|  2 | test       | EGFR           | mean_absolute_error |  16.9483   |
|  3 | test       | EGFR           | explained_var       |   0.400861 |
|  4 | test       | EGFR           | spearmanr           |   0.355694 |
|  5 | test       | EGFR           | pearsonr            |   0.640435 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.338711 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.358537 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.409644 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.339631 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.506476 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.592222 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.32197  |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.602418 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.611504 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.331628 |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.711304 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.645421 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.297647 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.425372 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.526736 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.459693 |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.633051 |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.706082 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.597393 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.199448 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.334335 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.600474 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.78877  |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.783264 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.457407 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.306317 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.441137 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.458068 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.684217 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.683476 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.473218 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.204607 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.344646 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.481188 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.697564 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.705605 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.474554 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.35622 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.338915 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.629064 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.26413 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.386239 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.600621 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.923043 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.539741 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.521425 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.572898 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.901959 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.521287 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.849779 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.834897 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.856811 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.546278 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6695539279428904,
    "polaris/pkis2-ret-wt-reg-v2": 737.8122708701437,
    "polaris/pkis2-kit-wt-cls-v2": 0.8277372745295695,
    "polaris/pkis2-kit-wt-reg-v2": 785.4108868251415,
    "polaris/pkis2-egfr-wt-reg-v2": 482.9112736998251,
    "polaris/adme-fang-solu-1": 0.5922217576244436,
    "polaris/adme-fang-rppb-1": 0.6454212538436732,
    "polaris/adme-fang-hppb-1": 0.706082220847428,
    "polaris/adme-fang-perm-1": 0.7832637421442287,
    "polaris/adme-fang-rclint-1": 0.6834762843771359,
    "polaris/adme-fang-hclint-1": 0.7056052010868422,
    "tdcommons/lipophilicity-astrazeneca": 0.4745541068542571,
    "tdcommons/ppbr-az": 8.356220116248497,
    "tdcommons/clearance-hepatocyte-az": 0.33891548472447436,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6290635842196026,
    "tdcommons/half-life-obach": 0.264130442966324,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.38623860949692257,
    "tdcommons/clearance-microsome-az": 0.6006205024742796,
    "tdcommons/dili": 0.9230434782608696,
    "tdcommons/bioavailability-ma": 0.5397406052544064,
    "tdcommons/vdss-lombardo": 0.5214249436934643,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5728978300180831,
    "tdcommons/pgp-broccatelli": 0.9019594774726739,
    "tdcommons/caco2-wang": 0.5212868335186633,
    "tdcommons/herg": 0.8497790868924889,
    "tdcommons/bbb-martins": 0.8348968105065665,
    "tdcommons/ames": 0.8568113728484991,
    "tdcommons/ld50-zhu": 0.5462784283577348
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.655641 |
|  1 | test       | CLS_RET        | roc_auc     | 0.906808 |
|  2 | test       | CLS_RET        | pr_auc      | 0.783076 |
|  3 | test       | CLS_RET        | mcc         | 0.663823 |
|  4 | test       | CLS_RET        | accuracy    | 0.896226 |
|  5 | test       | CLS_RET        | f1          | 0.717949 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.416828 |
|  1 | test       | RET            | mean_squared_error  | 692.461    |
|  2 | test       | RET            | mean_absolute_error |  19.6628   |
|  3 | test       | RET            | explained_var       |   0.458158 |
|  4 | test       | RET            | spearmanr           |   0.585422 |
|  5 | test       | RET            | pearsonr            |   0.677148 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0        |
|  1 | test       | CLS_KIT        | roc_auc     | 0.882979 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.779988 |
|  3 | test       | CLS_KIT        | mcc         | 0        |
|  4 | test       | CLS_KIT        | accuracy    | 0.810345 |
|  5 | test       | CLS_KIT        | f1          | 0        |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.376542 |
|  1 | test       | KIT            | mean_squared_error  | 752.317    |
|  2 | test       | KIT            | mean_absolute_error |  20.5602   |
|  3 | test       | KIT            | explained_var       |   0.402716 |
|  4 | test       | KIT            | spearmanr           |   0.590337 |
|  5 | test       | KIT            | pearsonr            |   0.634652 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.46339  |
|  1 | test       | EGFR           | mean_squared_error  | 432.383    |
|  2 | test       | EGFR           | mean_absolute_error |  15.7147   |
|  3 | test       | EGFR           | explained_var       |   0.467352 |
|  4 | test       | EGFR           | spearmanr           |   0.446736 |
|  5 | test       | EGFR           | pearsonr            |   0.693491 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.370349 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.341384 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.394632 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.380343 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.51123  |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.617358 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.434834 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.502139 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.5653   |
|  3 | test       | LOG_RPPB       | explained_var       | 0.472138 |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.801739 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.730626 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.23751  |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.461793 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.58406  |
|  3 | test       | LOG_HPPB       | explained_var       | 0.435924 |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.66957  |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.660895 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.60735  |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.194516 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.336939 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.616727 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.790821 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.785393 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.50933  |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.277005 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.417378 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.511855 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.730153 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.715629 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.434731 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.219556 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.356464 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.434783 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.68998  |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.679097 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.467548 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.33884 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.403711 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.621723 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |      Score |
|---:|:-----------|:---------------|:----------|-----------:|
|  0 | test       | Y              | spearmanr | 0.00184759 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.38098 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.597187 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.937391 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.52145 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.490459 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.576741 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.910524 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.392082 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.854934 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.862258 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.837559 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.537324 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7830761730529534,
    "polaris/pkis2-ret-wt-reg-v2": 692.461085012016,
    "polaris/pkis2-kit-wt-cls-v2": 0.7799881085230265,
    "polaris/pkis2-kit-wt-reg-v2": 752.3165357396285,
    "polaris/pkis2-egfr-wt-reg-v2": 432.3833635911736,
    "polaris/adme-fang-solu-1": 0.6173578381942707,
    "polaris/adme-fang-rppb-1": 0.7306262092242156,
    "polaris/adme-fang-hppb-1": 0.6608946187575298,
    "polaris/adme-fang-perm-1": 0.7853925622747961,
    "polaris/adme-fang-rclint-1": 0.7156291625203525,
    "polaris/adme-fang-hclint-1": 0.6790973447297639,
    "tdcommons/lipophilicity-astrazeneca": 0.46754783652509957,
    "tdcommons/ppbr-az": 9.338842505658034,
    "tdcommons/clearance-hepatocyte-az": 0.40371139120554883,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6217228676123143,
    "tdcommons/half-life-obach": 0.0018475947839580245,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.38097955425737706,
    "tdcommons/clearance-microsome-az": 0.5971868035111764,
    "tdcommons/dili": 0.9373913043478261,
    "tdcommons/bioavailability-ma": 0.5214499501163951,
    "tdcommons/vdss-lombardo": 0.49045879976889756,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.576740506329114,
    "tdcommons/pgp-broccatelli": 0.9105238603039191,
    "tdcommons/caco2-wang": 0.3920820418407063,
    "tdcommons/herg": 0.8549337260677466,
    "tdcommons/bbb-martins": 0.8622576610381488,
    "tdcommons/ames": 0.8375589888190487,
    "tdcommons/ld50-zhu": 0.5373236608711728
}
```
