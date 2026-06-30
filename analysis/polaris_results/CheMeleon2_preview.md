# chemeleon2_preview_initial_training_e4s281344 Baseline Results
timestamp: 2026-06-29 22:03:51.571331
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0        |
|  1 | test       | CLS_RET        | roc_auc     | 0.584931 |
|  2 | test       | CLS_RET        | f1          | 0        |
|  3 | test       | CLS_RET        | pr_auc      | 0.19004  |
|  4 | test       | CLS_RET        | mcc         | 0        |
|  5 | test       | CLS_RET        | accuracy    | 0.839623 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | RET            | pearsonr            |    0.486224 |
|  1 | test       | RET            | mean_absolute_error |   25.9163   |
|  2 | test       | RET            | mean_squared_error  | 1050.72     |
|  3 | test       | RET            | explained_var       |    0.128244 |
|  4 | test       | RET            | r2                  |    0.115108 |
|  5 | test       | RET            | spearmanr           |    0.421748 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |     Score |
|---:|:-----------|:---------------|:------------|----------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.0670241 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.571083  |
|  2 | test       | CLS_KIT        | f1          | 0.142857  |
|  3 | test       | CLS_KIT        | pr_auc      | 0.307127  |
|  4 | test       | CLS_KIT        | mcc         | 0.0855959 |
|  5 | test       | CLS_KIT        | accuracy    | 0.793103  |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | pearsonr            |    0.403382 |
|  1 | test       | KIT            | mean_absolute_error |   25.8498   |
|  2 | test       | KIT            | mean_squared_error  | 1073.63     |
|  3 | test       | KIT            | explained_var       |    0.147994 |
|  4 | test       | KIT            | r2                  |    0.110268 |
|  5 | test       | KIT            | spearmanr           |    0.411574 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | EGFR           | pearsonr            |   0.311926   |
|  1 | test       | EGFR           | mean_absolute_error |  22.5258     |
|  2 | test       | EGFR           | mean_squared_error  | 808.093      |
|  3 | test       | EGFR           | explained_var       |   0.0251762  |
|  4 | test       | EGFR           | r2                  |  -0.00288429 |
|  5 | test       | EGFR           | spearmanr           |   0.192787   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.479966 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.472714 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.422247 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.221262 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.221203 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.407169 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | LOG_RPPB       | pearsonr            |  0.584816  |
|  1 | test       | LOG_RPPB       | mean_absolute_error |  0.843345  |
|  2 | test       | LOG_RPPB       | mean_squared_error  |  0.92771   |
|  3 | test       | LOG_RPPB       | explained_var       |  0.11041   |
|  4 | test       | LOG_RPPB       | r2                  | -0.0441521 |
|  5 | test       | LOG_RPPB       | spearmanr           |  0.641739  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | LOG_HPPB       | pearsonr            | -0.0962342 |
|  1 | test       | LOG_HPPB       | mean_absolute_error |  0.668834  |
|  2 | test       | LOG_HPPB       | mean_squared_error  |  0.706216  |
|  3 | test       | LOG_HPPB       | explained_var       | -0.0443857 |
|  4 | test       | LOG_HPPB       | r2                  | -0.166068  |
|  5 | test       | LOG_HPPB       | spearmanr           | -0.109405  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.715897 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.409675 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.254826 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.494519 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.485609 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.721145 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.636236 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.470254 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.342662 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.40203  |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.393028 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.631743 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.607636 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.391677 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.249593 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.357751 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.357398 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.62368  |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.497084 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 10.2956 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.225983 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.464627 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.349254 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.329176 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.44153 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.823913 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.441969 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.371608 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.562274 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.847374 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.35518 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.729602 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.752462 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.746844 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.676982 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.19003981882146437,
    "polaris/pkis2-ret-wt-reg-v2": 1050.7249244367615,
    "polaris/pkis2-kit-wt-cls-v2": 0.3071273301208526,
    "polaris/pkis2-kit-wt-reg-v2": 1073.6256206938272,
    "polaris/pkis2-egfr-wt-reg-v2": 808.0925457746791,
    "polaris/adme-fang-solu-1": 0.47996611232005776,
    "polaris/adme-fang-rppb-1": 0.5848160074282585,
    "polaris/adme-fang-hppb-1": -0.09623415722437788,
    "polaris/adme-fang-perm-1": 0.7158968690024866,
    "polaris/adme-fang-rclint-1": 0.6362358257027488,
    "polaris/adme-fang-hclint-1": 0.6076356220364832,
    "tdcommons/lipophilicity-astrazeneca": 0.49708355607305255,
    "tdcommons/ppbr-az": 10.295600950346863,
    "tdcommons/clearance-hepatocyte-az": 0.22598321286198617,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.4646265798022476,
    "tdcommons/half-life-obach": 0.34925431959720005,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3291762515865465,
    "tdcommons/clearance-microsome-az": 0.4415302095451408,
    "tdcommons/dili": 0.8239130434782609,
    "tdcommons/bioavailability-ma": 0.4419687396075823,
    "tdcommons/vdss-lombardo": 0.3716081562303986,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5622739602169982,
    "tdcommons/pgp-broccatelli": 0.8473740335910424,
    "tdcommons/caco2-wang": 0.3551795947467176,
    "tdcommons/herg": 0.7296023564064802,
    "tdcommons/bbb-martins": 0.7524624765478424,
    "tdcommons/ames": 0.7468444653312185,
    "tdcommons/ld50-zhu": 0.676982051343492
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0        |
|  1 | test       | CLS_RET        | roc_auc     | 0.673496 |
|  2 | test       | CLS_RET        | f1          | 0        |
|  3 | test       | CLS_RET        | pr_auc      | 0.305445 |
|  4 | test       | CLS_RET        | mcc         | 0        |
|  5 | test       | CLS_RET        | accuracy    | 0.839623 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | RET            | pearsonr            |    0.501477 |
|  1 | test       | RET            | mean_absolute_error |   25.8283   |
|  2 | test       | RET            | mean_squared_error  | 1063.76     |
|  3 | test       | RET            | explained_var       |    0.124471 |
|  4 | test       | RET            | r2                  |    0.10413  |
|  5 | test       | RET            | spearmanr           |    0.377522 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0        |
|  1 | test       | CLS_KIT        | roc_auc     | 0.5      |
|  2 | test       | CLS_KIT        | f1          | 0        |
|  3 | test       | CLS_KIT        | pr_auc      | 0.237327 |
|  4 | test       | CLS_KIT        | mcc         | 0        |
|  5 | test       | CLS_KIT        | accuracy    | 0.810345 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | pearsonr            |    0.420352 |
|  1 | test       | KIT            | mean_absolute_error |   25.8701   |
|  2 | test       | KIT            | mean_squared_error  | 1033.6      |
|  3 | test       | KIT            | explained_var       |    0.14363  |
|  4 | test       | KIT            | r2                  |    0.143435 |
|  5 | test       | KIT            | spearmanr           |    0.385975 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | EGFR           | pearsonr            |   0.339951  |
|  1 | test       | EGFR           | mean_absolute_error |  21.3297    |
|  2 | test       | EGFR           | mean_squared_error  | 787.267     |
|  3 | test       | EGFR           | explained_var       |   0.0254604 |
|  4 | test       | EGFR           | r2                  |   0.0229611 |
|  5 | test       | EGFR           | spearmanr           |   0.214498  |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.446876 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.500932 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.437452 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.199657 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.19316  |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.382229 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | LOG_RPPB       | pearsonr            |  0.160786   |
|  1 | test       | LOG_RPPB       | mean_absolute_error |  0.776182   |
|  2 | test       | LOG_RPPB       | mean_squared_error  |  0.914092   |
|  3 | test       | LOG_RPPB       | explained_var       |  0.00630411 |
|  4 | test       | LOG_RPPB       | r2                  | -0.0288245  |
|  5 | test       | LOG_RPPB       | spearmanr           |  0.255652   |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | LOG_HPPB       | pearsonr            |  0.00950011  |
|  1 | test       | LOG_HPPB       | mean_absolute_error |  0.676461    |
|  2 | test       | LOG_HPPB       | mean_squared_error  |  0.61118     |
|  3 | test       | LOG_HPPB       | explained_var       | -0.000554065 |
|  4 | test       | LOG_HPPB       | r2                  | -0.00914977  |
|  5 | test       | LOG_HPPB       | spearmanr           |  0.0155856   |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.657938 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.458374 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.305191 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.41445  |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.38394  |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.656706 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.32916  |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.592665 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.50532  |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.108292 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.104904 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.337156 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.451686 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.474762 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.317146 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.203931 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.183475 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.469725 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.774904 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 10.1499 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.184987 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.460253 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0228236 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.348902 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.429201 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  |     0.9 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.328567 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.44249 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.553006 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.861237 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.413421 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.736082 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.80093 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.789021 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.671723 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.3054445680555327,
    "polaris/pkis2-ret-wt-reg-v2": 1063.7607642749906,
    "polaris/pkis2-kit-wt-cls-v2": 0.23732671862629312,
    "polaris/pkis2-kit-wt-reg-v2": 1033.6033153278763,
    "polaris/pkis2-egfr-wt-reg-v2": 787.2671771309249,
    "polaris/adme-fang-solu-1": 0.4468762452324803,
    "polaris/adme-fang-rppb-1": 0.16078552642287314,
    "polaris/adme-fang-hppb-1": 0.00950011457315536,
    "polaris/adme-fang-perm-1": 0.6579380019657679,
    "polaris/adme-fang-rclint-1": 0.3291598407067508,
    "polaris/adme-fang-hclint-1": 0.4516859917892739,
    "tdcommons/lipophilicity-astrazeneca": 0.7749038232735225,
    "tdcommons/ppbr-az": 10.149871672219156,
    "tdcommons/clearance-hepatocyte-az": 0.1849868396803344,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.4602526652871035,
    "tdcommons/half-life-obach": 0.0228235883708082,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.348901895062302,
    "tdcommons/clearance-microsome-az": 0.42920138773787436,
    "tdcommons/dili": 0.9,
    "tdcommons/bioavailability-ma": 0.3285666777519122,
    "tdcommons/vdss-lombardo": 0.4424899537315322,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.553006329113924,
    "tdcommons/pgp-broccatelli": 0.8612370034657425,
    "tdcommons/caco2-wang": 0.4134210071528509,
    "tdcommons/herg": 0.7360824742268042,
    "tdcommons/bbb-martins": 0.8009302689180737,
    "tdcommons/ames": 0.7890207366504142,
    "tdcommons/ld50-zhu": 0.6717226974838318
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.331371 |
|  1 | test       | CLS_RET        | roc_auc     | 0.736286 |
|  2 | test       | CLS_RET        | f1          | 0.4      |
|  3 | test       | CLS_RET        | pr_auc      | 0.481887 |
|  4 | test       | CLS_RET        | mcc         | 0.361758 |
|  5 | test       | CLS_RET        | accuracy    | 0.858491 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | RET            | pearsonr            |    0.46641  |
|  1 | test       | RET            | mean_absolute_error |   25.4665   |
|  2 | test       | RET            | mean_squared_error  | 1055.49     |
|  3 | test       | RET            | explained_var       |    0.139281 |
|  4 | test       | RET            | r2                  |    0.111096 |
|  5 | test       | RET            | spearmanr           |    0.373493 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0        |
|  1 | test       | CLS_KIT        | roc_auc     | 0.394101 |
|  2 | test       | CLS_KIT        | f1          | 0        |
|  3 | test       | CLS_KIT        | pr_auc      | 0.224267 |
|  4 | test       | CLS_KIT        | mcc         | 0        |
|  5 | test       | CLS_KIT        | accuracy    | 0.810345 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | pearsonr            |    0.409496  |
|  1 | test       | KIT            | mean_absolute_error |   25.613     |
|  2 | test       | KIT            | mean_squared_error  | 1121.95      |
|  3 | test       | KIT            | explained_var       |    0.0918926 |
|  4 | test       | KIT            | r2                  |    0.0702204 |
|  5 | test       | KIT            | spearmanr           |    0.327074  |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | EGFR           | pearsonr            |   0.260906   |
|  1 | test       | EGFR           | mean_absolute_error |  21.1158     |
|  2 | test       | EGFR           | mean_squared_error  | 799.767      |
|  3 | test       | EGFR           | explained_var       |   0.00751584 |
|  4 | test       | EGFR           | r2                  |   0.00744868 |
|  5 | test       | EGFR           | spearmanr           |   0.0759408  |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.568982 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.424034 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.367872 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.322998 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.321493 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.460777 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.20353   |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.791681  |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.865857  |
|  3 | test       | LOG_RPPB       | explained_var       | 0.0328664 |
|  4 | test       | LOG_RPPB       | r2                  | 0.0254642 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.135652  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | LOG_HPPB       | pearsonr            |  0.302556  |
|  1 | test       | LOG_HPPB       | mean_absolute_error |  0.7116    |
|  2 | test       | LOG_HPPB       | mean_squared_error  |  0.638215  |
|  3 | test       | LOG_HPPB       | explained_var       |  0.0390085 |
|  4 | test       | LOG_HPPB       | r2                  | -0.0537888 |
|  5 | test       | LOG_HPPB       | spearmanr           |  0.246772  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.583452 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.497861 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.346956 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.325575 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.299634 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.59594  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.379668 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.592193 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.499888 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.115621 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.114526 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.371978 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.332985  |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.518864  |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.364305  |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.0882076 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.0620595 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.389992  |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.915877 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.31236 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.304813 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.603515 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0540874 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.346365 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.352384 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.855217 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.493183 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.400128 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.613359 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.775193 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.426752 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.751841 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.781739 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.794474 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.715712 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.48188668875880264,
    "polaris/pkis2-ret-wt-reg-v2": 1055.4891348899216,
    "polaris/pkis2-kit-wt-cls-v2": 0.22426687251972716,
    "polaris/pkis2-kit-wt-reg-v2": 1121.9502420567253,
    "polaris/pkis2-egfr-wt-reg-v2": 799.7665619880621,
    "polaris/adme-fang-solu-1": 0.5689824617190873,
    "polaris/adme-fang-rppb-1": 0.20352964451259964,
    "polaris/adme-fang-hppb-1": 0.30255581257378666,
    "polaris/adme-fang-perm-1": 0.5834515769301071,
    "polaris/adme-fang-rclint-1": 0.379667691611215,
    "polaris/adme-fang-hclint-1": 0.33298533336293235,
    "tdcommons/lipophilicity-astrazeneca": 0.9158765983070646,
    "tdcommons/ppbr-az": 9.312360240137854,
    "tdcommons/clearance-hepatocyte-az": 0.30481285149127285,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6035154936707907,
    "tdcommons/half-life-obach": 0.05408744318277355,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.34636545428429466,
    "tdcommons/clearance-microsome-az": 0.35238364030264435,
    "tdcommons/dili": 0.8552173913043478,
    "tdcommons/bioavailability-ma": 0.493182573994014,
    "tdcommons/vdss-lombardo": 0.40012793477340963,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.613358951175407,
    "tdcommons/pgp-broccatelli": 0.7751932817915224,
    "tdcommons/caco2-wang": 0.42675150515995236,
    "tdcommons/herg": 0.751840942562592,
    "tdcommons/bbb-martins": 0.7817385866166354,
    "tdcommons/ames": 0.7944741428263722,
    "tdcommons/ld50-zhu": 0.7157120719556073
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0        |
|  1 | test       | CLS_RET        | roc_auc     | 0.437541 |
|  2 | test       | CLS_RET        | f1          | 0        |
|  3 | test       | CLS_RET        | pr_auc      | 0.142795 |
|  4 | test       | CLS_RET        | mcc         | 0        |
|  5 | test       | CLS_RET        | accuracy    | 0.839623 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | RET            | pearsonr            |    0.342134  |
|  1 | test       | RET            | mean_absolute_error |   28.2862    |
|  2 | test       | RET            | mean_squared_error  | 1208.38      |
|  3 | test       | RET            | explained_var       |    0.0061766 |
|  4 | test       | RET            | r2                  |   -0.0176676 |
|  5 | test       | RET            | spearmanr           |    0.361024  |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0        |
|  1 | test       | CLS_KIT        | roc_auc     | 0.44971  |
|  2 | test       | CLS_KIT        | f1          | 0        |
|  3 | test       | CLS_KIT        | pr_auc      | 0.197189 |
|  4 | test       | CLS_KIT        | mcc         | 0        |
|  5 | test       | CLS_KIT        | accuracy    | 0.810345 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | pearsonr            |    0.335685  |
|  1 | test       | KIT            | mean_absolute_error |   26.1299    |
|  2 | test       | KIT            | mean_squared_error  | 1184.55      |
|  3 | test       | KIT            | explained_var       |    0.0477982 |
|  4 | test       | KIT            | r2                  |    0.0183457 |
|  5 | test       | KIT            | spearmanr           |    0.32647   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | EGFR           | pearsonr            |   0.407237   |
|  1 | test       | EGFR           | mean_absolute_error |  23.1528     |
|  2 | test       | EGFR           | mean_squared_error  | 811.871      |
|  3 | test       | EGFR           | explained_var       |   0.0454391  |
|  4 | test       | EGFR           | r2                  |  -0.00757299 |
|  5 | test       | EGFR           | spearmanr           |   0.208853   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.44091  |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.463112 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.446754 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.186394 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.176003 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.386571 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | LOG_RPPB       | pearsonr            | -0.0973165 |
|  1 | test       | LOG_RPPB       | mean_absolute_error |  0.803202  |
|  2 | test       | LOG_RPPB       | mean_squared_error  |  0.920714  |
|  3 | test       | LOG_RPPB       | explained_var       | -0.021013  |
|  4 | test       | LOG_RPPB       | r2                  | -0.0362781 |
|  5 | test       | LOG_RPPB       | spearmanr           |  0.149565  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.478367  |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.679256  |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.569283  |
|  3 | test       | LOG_HPPB       | explained_var       | 0.193413  |
|  4 | test       | LOG_HPPB       | r2                  | 0.0600283 |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.543968  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.650136 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.433447 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.290598 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.416853 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.413399 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.645414 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.382652 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.592869 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.491205 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.133938 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.129908 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.397282 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.352106  |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.515507  |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.371919  |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.0497678 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.0424568 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.357063  |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.488975 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.27878 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.27941 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.480433 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | -0.109971 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.33878 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.499508 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.814348 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.49152 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.31337 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.559109 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.852839 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.395053 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.757585 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.731082 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.806481 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.746168 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.14279513325548496,
    "polaris/pkis2-ret-wt-reg-v2": 1208.3837154545035,
    "polaris/pkis2-kit-wt-cls-v2": 0.1971886937310069,
    "polaris/pkis2-kit-wt-reg-v2": 1184.5466232002368,
    "polaris/pkis2-egfr-wt-reg-v2": 811.870551425573,
    "polaris/adme-fang-solu-1": 0.44091048892519646,
    "polaris/adme-fang-rppb-1": -0.09731651799226385,
    "polaris/adme-fang-hppb-1": 0.47836714390398116,
    "polaris/adme-fang-perm-1": 0.6501362745584492,
    "polaris/adme-fang-rclint-1": 0.38265241227392516,
    "polaris/adme-fang-hclint-1": 0.35210596786144227,
    "tdcommons/lipophilicity-astrazeneca": 0.4889753866876875,
    "tdcommons/ppbr-az": 9.278778958943322,
    "tdcommons/clearance-hepatocyte-az": 0.27941008913205434,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.4804331662839836,
    "tdcommons/half-life-obach": -0.10997125631905943,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.33878037648500586,
    "tdcommons/clearance-microsome-az": 0.49950774819003596,
    "tdcommons/dili": 0.8143478260869565,
    "tdcommons/bioavailability-ma": 0.4915197871632857,
    "tdcommons/vdss-lombardo": 0.31336981184763224,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5591094032549728,
    "tdcommons/pgp-broccatelli": 0.8528392428685684,
    "tdcommons/caco2-wang": 0.3950529656727215,
    "tdcommons/herg": 0.7575846833578792,
    "tdcommons/bbb-martins": 0.7310819262038775,
    "tdcommons/ames": 0.8064814270888405,
    "tdcommons/ld50-zhu": 0.7461679618277957
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0        |
|  1 | test       | CLS_RET        | roc_auc     | 0.66887  |
|  2 | test       | CLS_RET        | f1          | 0        |
|  3 | test       | CLS_RET        | pr_auc      | 0.340893 |
|  4 | test       | CLS_RET        | mcc         | 0        |
|  5 | test       | CLS_RET        | accuracy    | 0.839623 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | RET            | pearsonr            |    0.469003  |
|  1 | test       | RET            | mean_absolute_error |   25.8281    |
|  2 | test       | RET            | mean_squared_error  | 1070.47      |
|  3 | test       | RET            | explained_var       |    0.121832  |
|  4 | test       | RET            | r2                  |    0.0984769 |
|  5 | test       | RET            | spearmanr           |    0.34737   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0        |
|  1 | test       | CLS_KIT        | roc_auc     | 0.384913 |
|  2 | test       | CLS_KIT        | f1          | 0        |
|  3 | test       | CLS_KIT        | pr_auc      | 0.176527 |
|  4 | test       | CLS_KIT        | mcc         | 0        |
|  5 | test       | CLS_KIT        | accuracy    | 0.810345 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | pearsonr            |    0.361936 |
|  1 | test       | KIT            | mean_absolute_error |   27.8255   |
|  2 | test       | KIT            | mean_squared_error  | 1060.9      |
|  3 | test       | KIT            | explained_var       |    0.125766 |
|  4 | test       | KIT            | r2                  |    0.120813 |
|  5 | test       | KIT            | spearmanr           |    0.414552 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | EGFR           | pearsonr            |  -0.157825   |
|  1 | test       | EGFR           | mean_absolute_error |  21.3502     |
|  2 | test       | EGFR           | mean_squared_error  | 808.539      |
|  3 | test       | EGFR           | explained_var       |  -0.00320978 |
|  4 | test       | EGFR           | r2                  |  -0.00343794 |
|  5 | test       | EGFR           | spearmanr           |  -0.117019   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.521765 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.434376 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.411214 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.261327 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.241552 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.453731 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.413338   |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.808055   |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.887047   |
|  3 | test       | LOG_RPPB       | explained_var       | 0.0455403  |
|  4 | test       | LOG_RPPB       | r2                  | 0.00161455 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.478261   |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | LOG_HPPB       | pearsonr            |  0.256763  |
|  1 | test       | LOG_HPPB       | mean_absolute_error |  0.71039   |
|  2 | test       | LOG_HPPB       | mean_squared_error  |  0.647782  |
|  3 | test       | LOG_HPPB       | explained_var       |  0.0650871 |
|  4 | test       | LOG_HPPB       | r2                  | -0.0695845 |
|  5 | test       | LOG_HPPB       | spearmanr           |  0.299488  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.646693 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.434672 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.294065 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.408338 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.406401 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.657771 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.347026 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.606276 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.52391  |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.118841 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.071975 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.349568 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.576194 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.405809 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.263362 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.329868 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.321949 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.59711  |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.717405 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.95853 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |      Score |
|---:|:-----------|:---------------|:----------|-----------:|
|  0 | test       | Y              | spearmanr | -0.0768579 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.561864 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.221766 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.373103 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.485101 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.866522 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.476222 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.222277 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.590529 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.885897 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.548554 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.768483 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.68621 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.804958 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.800003 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.3408926628636999,
    "polaris/pkis2-ret-wt-reg-v2": 1070.4730709667128,
    "polaris/pkis2-kit-wt-cls-v2": 0.17652696698372772,
    "polaris/pkis2-kit-wt-reg-v2": 1060.9013125862955,
    "polaris/pkis2-egfr-wt-reg-v2": 808.5386563558529,
    "polaris/adme-fang-solu-1": 0.5217652910648082,
    "polaris/adme-fang-rppb-1": 0.41333794805416896,
    "polaris/adme-fang-hppb-1": 0.25676283861050975,
    "polaris/adme-fang-perm-1": 0.6466931263206354,
    "polaris/adme-fang-rclint-1": 0.3470262430787507,
    "polaris/adme-fang-hclint-1": 0.576194100448613,
    "tdcommons/lipophilicity-astrazeneca": 0.7174050531160262,
    "tdcommons/ppbr-az": 8.958530648765496,
    "tdcommons/clearance-hepatocyte-az": -0.07685793764953341,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5618635947206514,
    "tdcommons/half-life-obach": 0.22176571228543787,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3731034782573632,
    "tdcommons/clearance-microsome-az": 0.4851009113720875,
    "tdcommons/dili": 0.8665217391304348,
    "tdcommons/bioavailability-ma": 0.4762221483205853,
    "tdcommons/vdss-lombardo": 0.22227744188180687,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5905289330922242,
    "tdcommons/pgp-broccatelli": 0.8858970941082378,
    "tdcommons/caco2-wang": 0.5485535642071401,
    "tdcommons/herg": 0.7684830633284242,
    "tdcommons/bbb-martins": 0.6862101313320825,
    "tdcommons/ames": 0.8049579980027023,
    "tdcommons/ld50-zhu": 0.800002995616851
}
```
