# ChemProp Baseline Results
timestamp: 2025-06-06 15:58:48.216059
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.85195  |
|  1 | test       | CLS_RET        | pr_auc      | 0.6936   |
|  2 | test       | CLS_RET        | cohen_kappa | 0.480816 |
|  3 | test       | CLS_RET        | accuracy    | 0.886792 |
|  4 | test       | CLS_RET        | mcc         | 0.512494 |
|  5 | test       | CLS_RET        | f1          | 0.538462 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | RET            | explained_var       |    0.121549 |
|  1 | test       | RET            | mean_squared_error  | 1061.06     |
|  2 | test       | RET            | r2                  |    0.106406 |
|  3 | test       | RET            | mean_absolute_error |   25.7623   |
|  4 | test       | RET            | spearmanr           |    0.364891 |
|  5 | test       | RET            | pearsonr            |    0.348739 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.748549 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.459354 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.270793 |
|  3 | test       | CLS_KIT        | accuracy    | 0.775862 |
|  4 | test       | CLS_KIT        | mcc         | 0.270793 |
|  5 | test       | CLS_KIT        | f1          | 0.409091 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | explained_var       |   -0.0829691 |
|  1 | test       | KIT            | mean_squared_error  | 1318.78      |
|  2 | test       | KIT            | r2                  |   -0.0928975 |
|  3 | test       | KIT            | mean_absolute_error |   28.448     |
|  4 | test       | KIT            | spearmanr           |    0.333692  |
|  5 | test       | KIT            | pearsonr            |    0.311935  |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.291178 |
|  1 | test       | EGFR           | mean_squared_error  | 574.485    |
|  2 | test       | EGFR           | r2                  |   0.287034 |
|  3 | test       | EGFR           | mean_absolute_error |  18.4371   |
|  4 | test       | EGFR           | spearmanr           |   0.287728 |
|  5 | test       | EGFR           | pearsonr            |   0.539941 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.301903 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.395865 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.269862 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.422787 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.457613 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.549676 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.538876 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.409758 |
|  2 | test       | LOG_RPPB       | r2                  | 0.538811 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.43807  |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.833913 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.739488 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_HPPB       | explained_var       | -0.308317 |
|  1 | test       | LOG_HPPB       | mean_squared_error  |  0.866563 |
|  2 | test       | LOG_HPPB       | r2                  | -0.430826 |
|  3 | test       | LOG_HPPB       | mean_absolute_error |  0.501052 |
|  4 | test       | LOG_HPPB       | spearmanr           |  0.755291 |
|  5 | test       | LOG_HPPB       | pearsonr            |  0.53417  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.504283 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.2476   |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.500194 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.385483 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.732598 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.714147 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.426336 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.325217 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.42393  |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.448936 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.666472 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.655468 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.376438 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.25063  |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.354728 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.400995 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.625289 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.617728 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.81069 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.71338 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.324214 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.685103 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.396429 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.373586 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.551613 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.871739 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.636515 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.255646 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.57708 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.911224 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.309804 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.846097 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.888798 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.823364 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.641013 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6935997849708924,
    "polaris/pkis2-ret-wt-reg-v2": 1061.0579915143398,
    "polaris/pkis2-kit-wt-cls-v2": 0.45935386282196167,
    "polaris/pkis2-kit-wt-reg-v2": 1318.7819673097035,
    "polaris/pkis2-egfr-wt-reg-v2": 574.4852040183036,
    "polaris/adme-fang-solu-1": 0.549676124532078,
    "polaris/adme-fang-rppb-1": 0.7394884317123722,
    "polaris/adme-fang-hppb-1": 0.5341698013257336,
    "polaris/adme-fang-perm-1": 0.7141474549293233,
    "polaris/adme-fang-rclint-1": 0.6554677414177122,
    "polaris/adme-fang-hclint-1": 0.6177278839237181,
    "tdcommons/lipophilicity-astrazeneca": 0.8106903050740559,
    "tdcommons/ppbr-az": 8.71337992059097,
    "tdcommons/clearance-hepatocyte-az": 0.32421352716266344,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.685102670605009,
    "tdcommons/half-life-obach": 0.39642945803013796,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.37358594201433104,
    "tdcommons/clearance-microsome-az": 0.5516131214748567,
    "tdcommons/dili": 0.8717391304347826,
    "tdcommons/bioavailability-ma": 0.6365147988027935,
    "tdcommons/vdss-lombardo": 0.2556463412932418,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5770795660036165,
    "tdcommons/pgp-broccatelli": 0.9112236736870167,
    "tdcommons/caco2-wang": 0.3098037716073676,
    "tdcommons/herg": 0.8460972017673049,
    "tdcommons/bbb-martins": 0.8887976860537836,
    "tdcommons/ames": 0.8233644676809807,
    "tdcommons/ld50-zhu": 0.6410134798509343
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.824851 |
|  1 | test       | CLS_RET        | pr_auc      | 0.620991 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.480816 |
|  3 | test       | CLS_RET        | accuracy    | 0.886792 |
|  4 | test       | CLS_RET        | mcc         | 0.512494 |
|  5 | test       | CLS_RET        | f1          | 0.538462 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.208857 |
|  1 | test       | RET            | mean_squared_error  | 976.611    |
|  2 | test       | RET            | r2                  |   0.177525 |
|  3 | test       | RET            | mean_absolute_error |  24.0737   |
|  4 | test       | RET            | spearmanr           |   0.495189 |
|  5 | test       | RET            | pearsonr            |   0.501089 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.754352 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.402751 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.152809 |
|  3 | test       | CLS_KIT        | accuracy    | 0.775862 |
|  4 | test       | CLS_KIT        | mcc         | 0.158281 |
|  5 | test       | CLS_KIT        | f1          | 0.277778 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |         Score |
|---:|:-----------|:---------------|:--------------------|--------------:|
|  0 | test       | KIT            | explained_var       |    0.0244498  |
|  1 | test       | KIT            | mean_squared_error  | 1201.79       |
|  2 | test       | KIT            | r2                  |    0.00405848 |
|  3 | test       | KIT            | mean_absolute_error |   27.3346     |
|  4 | test       | KIT            | spearmanr           |    0.373247   |
|  5 | test       | KIT            | pearsonr            |    0.36704    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.244054 |
|  1 | test       | EGFR           | mean_squared_error  | 609.997    |
|  2 | test       | EGFR           | r2                  |   0.242962 |
|  3 | test       | EGFR           | mean_absolute_error |  19.668    |
|  4 | test       | EGFR           | spearmanr           |   0.253637 |
|  5 | test       | EGFR           | pearsonr            |   0.526484 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.28114  |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.392094 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.276817 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.426371 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.484433 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.548275 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.567043 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.419176 |
|  2 | test       | LOG_RPPB       | r2                  | 0.528211 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.533507 |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.882609 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.755397 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.283077 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.458582 |
|  2 | test       | LOG_HPPB       | r2                  | 0.242813 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.580488 |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.564749 |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.557496 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.521504 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.238789 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.51798  |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.368181 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.739332 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.741603 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.437274 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.319144 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.434687 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.441787 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.674737 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.669368 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.352314 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.254141 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.345689 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.408449 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.614289 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.601519 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.559253 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.79575 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.322702 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.673248 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.271572 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.334011 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.44897 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.864348 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.663785 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.240923 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.61415 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.922421 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.304572 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.822533 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.912015 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.827063 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.644185 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6209914188243952,
    "polaris/pkis2-ret-wt-reg-v2": 976.6107670692382,
    "polaris/pkis2-kit-wt-cls-v2": 0.4027510884603049,
    "polaris/pkis2-kit-wt-reg-v2": 1201.7867453915042,
    "polaris/pkis2-egfr-wt-reg-v2": 609.9972595111199,
    "polaris/adme-fang-solu-1": 0.5482749490604413,
    "polaris/adme-fang-rppb-1": 0.7553971876506365,
    "polaris/adme-fang-hppb-1": 0.55749558068557,
    "polaris/adme-fang-perm-1": 0.7416034390711089,
    "polaris/adme-fang-rclint-1": 0.6693678801193237,
    "polaris/adme-fang-hclint-1": 0.601518530304327,
    "tdcommons/lipophilicity-astrazeneca": 0.5592534345047814,
    "tdcommons/ppbr-az": 8.79575089647433,
    "tdcommons/clearance-hepatocyte-az": 0.32270183735448016,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6732475855458798,
    "tdcommons/half-life-obach": 0.2715722686205144,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.33401072645980234,
    "tdcommons/clearance-microsome-az": 0.44897007732237565,
    "tdcommons/dili": 0.8643478260869565,
    "tdcommons/bioavailability-ma": 0.6637845028267375,
    "tdcommons/vdss-lombardo": 0.2409227636535467,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6141500904159132,
    "tdcommons/pgp-broccatelli": 0.9224206878165822,
    "tdcommons/caco2-wang": 0.30457236473145555,
    "tdcommons/herg": 0.8225331369661267,
    "tdcommons/bbb-martins": 0.9120153220762977,
    "tdcommons/ames": 0.8270633848322857,
    "tdcommons/ld50-zhu": 0.6441854529948615
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.867151 |
|  1 | test       | CLS_RET        | pr_auc      | 0.669497 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.288272 |
|  3 | test       | CLS_RET        | accuracy    | 0.858491 |
|  4 | test       | CLS_RET        | mcc         | 0.337956 |
|  5 | test       | CLS_RET        | f1          | 0.347826 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.29851  |
|  1 | test       | RET            | mean_squared_error  | 915.716    |
|  2 | test       | RET            | r2                  |   0.228809 |
|  3 | test       | RET            | mean_absolute_error |  22.1157   |
|  4 | test       | RET            | spearmanr           |   0.553832 |
|  5 | test       | RET            | pearsonr            |   0.566998 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.735977 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.434498 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.102064 |
|  3 | test       | CLS_KIT        | accuracy    | 0.767241 |
|  4 | test       | CLS_KIT        | mcc         | 0.106968 |
|  5 | test       | CLS_KIT        | f1          | 0.228571 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | explained_var       |    0.0723429 |
|  1 | test       | KIT            | mean_squared_error  | 1120.08      |
|  2 | test       | KIT            | r2                  |    0.0717715 |
|  3 | test       | KIT            | mean_absolute_error |   25.6442    |
|  4 | test       | KIT            | spearmanr           |    0.428908  |
|  5 | test       | KIT            | pearsonr            |    0.421057  |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.396353 |
|  1 | test       | EGFR           | mean_squared_error  | 486.404    |
|  2 | test       | EGFR           | r2                  |   0.396348 |
|  3 | test       | EGFR           | mean_absolute_error |  17.534    |
|  4 | test       | EGFR           | spearmanr           |   0.424765 |
|  5 | test       | EGFR           | pearsonr            |   0.639658 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.222752 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.422418 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.220887 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.464454 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.377573 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.475012 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.574976 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.383978 |
|  2 | test       | LOG_RPPB       | r2                  | 0.567826 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.504232 |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.810435 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.767539 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | LOG_HPPB       | explained_var       |  0.124892  |
|  1 | test       | LOG_HPPB       | mean_squared_error  |  0.630141  |
|  2 | test       | LOG_HPPB       | r2                  | -0.0404561 |
|  3 | test       | LOG_HPPB       | mean_absolute_error |  0.626145  |
|  4 | test       | LOG_HPPB       | spearmanr           |  0.525327  |
|  5 | test       | LOG_HPPB       | pearsonr            |  0.448794  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.48037  |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.257434 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.480344 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.391852 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.689769 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.695123 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.433145 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.321631 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.430281 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.44263  |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.678252 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.672783 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.382541 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.239967 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.382181 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.388581 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.657886 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.638883 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.54649 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.83737 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.169199 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.635198 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.227537 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.444757 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.467759 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.79913 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.624543 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.21308 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.62387 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.915423 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.347914 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.821355 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.895638 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.830586 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.629077 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6694969398583014,
    "polaris/pkis2-ret-wt-reg-v2": 915.7158695546395,
    "polaris/pkis2-kit-wt-cls-v2": 0.43449805193466096,
    "polaris/pkis2-kit-wt-reg-v2": 1120.0785685908145,
    "polaris/pkis2-egfr-wt-reg-v2": 486.4038365112108,
    "polaris/adme-fang-solu-1": 0.4750116327164369,
    "polaris/adme-fang-rppb-1": 0.767539269765313,
    "polaris/adme-fang-hppb-1": 0.44879393858835087,
    "polaris/adme-fang-perm-1": 0.6951232170521606,
    "polaris/adme-fang-rclint-1": 0.6727825020804665,
    "polaris/adme-fang-hclint-1": 0.638882980200237,
    "tdcommons/lipophilicity-astrazeneca": 0.54648958782355,
    "tdcommons/ppbr-az": 8.837365367527724,
    "tdcommons/clearance-hepatocyte-az": 0.1691991564031998,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6351981231215412,
    "tdcommons/half-life-obach": 0.22753653551695208,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4447574849850863,
    "tdcommons/clearance-microsome-az": 0.46775856912373637,
    "tdcommons/dili": 0.7991304347826087,
    "tdcommons/bioavailability-ma": 0.6245427336215497,
    "tdcommons/vdss-lombardo": 0.2130795120651871,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.623869801084991,
    "tdcommons/pgp-broccatelli": 0.9154225539856039,
    "tdcommons/caco2-wang": 0.3479137407928131,
    "tdcommons/herg": 0.8213549337260678,
    "tdcommons/bbb-martins": 0.8956378986866791,
    "tdcommons/ames": 0.8305860698270968,
    "tdcommons/ld50-zhu": 0.6290770820119546
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.853272 |
|  1 | test       | CLS_RET        | pr_auc      | 0.617485 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.453608 |
|  3 | test       | CLS_RET        | accuracy    | 0.877358 |
|  4 | test       | CLS_RET        | mcc         | 0.474614 |
|  5 | test       | CLS_RET        | f1          | 0.518519 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.273704 |
|  1 | test       | RET            | mean_squared_error  | 919.059    |
|  2 | test       | RET            | r2                  |   0.225994 |
|  3 | test       | RET            | mean_absolute_error |  23.164    |
|  4 | test       | RET            | spearmanr           |   0.473117 |
|  5 | test       | RET            | pearsonr            |   0.535437 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.747099 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.411785 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.141837 |
|  3 | test       | CLS_KIT        | accuracy    | 0.75     |
|  4 | test       | CLS_KIT        | mcc         | 0.142399 |
|  5 | test       | CLS_KIT        | f1          | 0.292683 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | explained_var       |    0.155461 |
|  1 | test       | KIT            | mean_squared_error  | 1035.94     |
|  2 | test       | KIT            | r2                  |    0.141496 |
|  3 | test       | KIT            | mean_absolute_error |   24.4031   |
|  4 | test       | KIT            | spearmanr           |    0.477886 |
|  5 | test       | KIT            | pearsonr            |    0.484731 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.363543 |
|  1 | test       | EGFR           | mean_squared_error  | 519.384    |
|  2 | test       | EGFR           | r2                  |   0.355418 |
|  3 | test       | EGFR           | mean_absolute_error |  17.3975   |
|  4 | test       | EGFR           | spearmanr           |   0.400995 |
|  5 | test       | EGFR           | pearsonr            |   0.627435 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.261412 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.403855 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.255125 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.440487 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.431657 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.513796 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.404455 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.542583 |
|  2 | test       | LOG_RPPB       | r2                  | 0.389315 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.565765 |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.64     |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.654973 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_HPPB       | explained_var       | -1.04477  |
|  1 | test       | LOG_HPPB       | mean_squared_error  |  1.286    |
|  2 | test       | LOG_HPPB       | r2                  | -1.12338  |
|  3 | test       | LOG_HPPB       | mean_absolute_error |  0.49254  |
|  4 | test       | LOG_HPPB       | spearmanr           |  0.795172 |
|  5 | test       | LOG_HPPB       | pearsonr            |  0.450192 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.526955 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.234393 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.526854 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.375294 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.728159 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.731733 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.440324 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.319162 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.434655 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.454289 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.671556 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.66391  |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.388501 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.237967 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.387329 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.380874 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.652689 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.634633 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.564988 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.64284 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.339448 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.660002 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.299211 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.349452 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.541374 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.843478 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.695045 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.421767 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.637658 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.884098 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.300796 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.813697 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.915494 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.844818 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.665703 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.617484693112994,
    "polaris/pkis2-ret-wt-reg-v2": 919.0585887533921,
    "polaris/pkis2-kit-wt-cls-v2": 0.4117846361250371,
    "polaris/pkis2-kit-wt-reg-v2": 1035.9436437241095,
    "polaris/pkis2-egfr-wt-reg-v2": 519.38394184448,
    "polaris/adme-fang-solu-1": 0.5137957148945396,
    "polaris/adme-fang-rppb-1": 0.6549729850967014,
    "polaris/adme-fang-hppb-1": 0.45019181129291064,
    "polaris/adme-fang-perm-1": 0.731733355788732,
    "polaris/adme-fang-rclint-1": 0.6639095939727501,
    "polaris/adme-fang-hclint-1": 0.634632961521157,
    "tdcommons/lipophilicity-astrazeneca": 0.5649879574889228,
    "tdcommons/ppbr-az": 8.642836576676752,
    "tdcommons/clearance-hepatocyte-az": 0.3394482044765796,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6600024463221986,
    "tdcommons/half-life-obach": 0.29921084299001843,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.34945175590091215,
    "tdcommons/clearance-microsome-az": 0.541374097897936,
    "tdcommons/dili": 0.8434782608695652,
    "tdcommons/bioavailability-ma": 0.6950448952444297,
    "tdcommons/vdss-lombardo": 0.42176665087202936,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6376582278481013,
    "tdcommons/pgp-broccatelli": 0.8840975739802719,
    "tdcommons/caco2-wang": 0.3007956081535424,
    "tdcommons/herg": 0.8136966126656848,
    "tdcommons/bbb-martins": 0.9154940587867417,
    "tdcommons/ames": 0.8448177955315358,
    "tdcommons/ld50-zhu": 0.6657028609399704
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.870456 |
|  1 | test       | CLS_RET        | pr_auc      | 0.702815 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.591365 |
|  3 | test       | CLS_RET        | accuracy    | 0.90566  |
|  4 | test       | CLS_RET        | mcc         | 0.609983 |
|  5 | test       | CLS_RET        | f1          | 0.642857 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.355374 |
|  1 | test       | RET            | mean_squared_error  | 796.538    |
|  2 | test       | RET            | r2                  |   0.329177 |
|  3 | test       | RET            | mean_absolute_error |  21.4491   |
|  4 | test       | RET            | spearmanr           |   0.548613 |
|  5 | test       | RET            | pearsonr            |   0.605722 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.742263 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.400032 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.235092 |
|  3 | test       | CLS_KIT        | accuracy    | 0.801724 |
|  4 | test       | CLS_KIT        | mcc         | 0.246387 |
|  5 | test       | CLS_KIT        | f1          | 0.342857 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | explained_var       |    0.0434206 |
|  1 | test       | KIT            | mean_squared_error  | 1162.19      |
|  2 | test       | KIT            | r2                  |    0.0368727 |
|  3 | test       | KIT            | mean_absolute_error |   26.6299    |
|  4 | test       | KIT            | spearmanr           |    0.412063  |
|  5 | test       | KIT            | pearsonr            |    0.399313  |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.380984 |
|  1 | test       | EGFR           | mean_squared_error  | 501.552    |
|  2 | test       | EGFR           | r2                  |   0.377548 |
|  3 | test       | EGFR           | mean_absolute_error |  17.2286   |
|  4 | test       | EGFR           | spearmanr           |   0.429433 |
|  5 | test       | EGFR           | pearsonr            |   0.621473 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.241549 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.413521 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.237297 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.465496 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.388169 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.493429 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.670266 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.293745 |
|  2 | test       | LOG_RPPB       | r2                  | 0.669386 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.42981  |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.866957 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.826823 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.491363 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.383637 |
|  2 | test       | LOG_HPPB       | r2                  | 0.366559 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.460293 |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.708534 |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.7295   |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.498046 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.24922  |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.496924 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.378381 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.739304 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.721659 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.452417 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.309193 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.452314 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.438929 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.68627  |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.680446 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.416441 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.227588 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.414052 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.379238 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.659927 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.648905 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.543408 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.51984 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.337922 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.596242 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.314182 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.372069 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.456214 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.814348 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.598603 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.327473 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.598101 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.917689 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.365374 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.838733 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.927103 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.835673 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.644699 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7028148157793086,
    "polaris/pkis2-ret-wt-reg-v2": 796.538120267991,
    "polaris/pkis2-kit-wt-cls-v2": 0.4000316425506703,
    "polaris/pkis2-kit-wt-reg-v2": 1162.1903185617862,
    "polaris/pkis2-egfr-wt-reg-v2": 501.5523044494447,
    "polaris/adme-fang-solu-1": 0.4934290144749345,
    "polaris/adme-fang-rppb-1": 0.8268232372084902,
    "polaris/adme-fang-hppb-1": 0.7294999696608211,
    "polaris/adme-fang-perm-1": 0.721658844242903,
    "polaris/adme-fang-rclint-1": 0.6804455893117656,
    "polaris/adme-fang-hclint-1": 0.6489051488841986,
    "tdcommons/lipophilicity-astrazeneca": 0.5434082013595671,
    "tdcommons/ppbr-az": 8.519841627144856,
    "tdcommons/clearance-hepatocyte-az": 0.3379219577142582,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5962424127091196,
    "tdcommons/half-life-obach": 0.3141818121341579,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.37206907532660216,
    "tdcommons/clearance-microsome-az": 0.4562140316934191,
    "tdcommons/dili": 0.8143478260869565,
    "tdcommons/bioavailability-ma": 0.5986032590621883,
    "tdcommons/vdss-lombardo": 0.3274729719572365,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5981012658227847,
    "tdcommons/pgp-broccatelli": 0.9176886163689683,
    "tdcommons/caco2-wang": 0.3653739521211394,
    "tdcommons/herg": 0.8387334315169367,
    "tdcommons/bbb-martins": 0.9271028767979987,
    "tdcommons/ames": 0.8356733047445613,
    "tdcommons/ld50-zhu": 0.6446985285562817
}
```
