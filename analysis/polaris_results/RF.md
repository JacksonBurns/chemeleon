# Random Forest Baseline Results
timestamp: 2025-10-06 17:06:14.094141
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.887971 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.448395 |
|  2 | test       | CLS_RET        | pr_auc      | 0.693535 |
|  3 | test       | CLS_RET        | f1          | 0.5      |
|  4 | test       | CLS_RET        | mcc         | 0.504899 |
|  5 | test       | CLS_RET        | accuracy    | 0.886792 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  21.2742   |
|  1 | test       | RET            | spearmanr           |   0.621943 |
|  2 | test       | RET            | pearsonr            |   0.665048 |
|  3 | test       | RET            | explained_var       |   0.383184 |
|  4 | test       | RET            | mean_squared_error  | 776.859    |
|  5 | test       | RET            | r2                  |   0.34575  |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.813588 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.456674 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.612015 |
|  3 | test       | CLS_KIT        | f1          | 0.529412 |
|  4 | test       | CLS_KIT        | mcc         | 0.485525 |
|  5 | test       | CLS_KIT        | accuracy    | 0.862069 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  23.1698   |
|  1 | test       | KIT            | spearmanr           |   0.569582 |
|  2 | test       | KIT            | pearsonr            |   0.596252 |
|  3 | test       | KIT            | explained_var       |   0.342902 |
|  4 | test       | KIT            | mean_squared_error  | 803.325    |
|  5 | test       | KIT            | r2                  |   0.334271 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  17.5041   |
|  1 | test       | EGFR           | spearmanr           |   0.366003 |
|  2 | test       | EGFR           | pearsonr            |   0.627311 |
|  3 | test       | EGFR           | explained_var       |   0.359081 |
|  4 | test       | EGFR           | mean_squared_error  | 516.684    |
|  5 | test       | EGFR           | r2                  |   0.358769 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.436677 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.470637 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.578278 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.28328  |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.390701 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.279387 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.600382 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.790435 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.764523 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.378364 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.553144 |
|  5 | test       | LOG_RPPB       | r2                  | 0.377427 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.549565 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.708534 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.717435 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.451602 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.358463 |
|  5 | test       | LOG_HPPB       | r2                  | 0.408125 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.413193 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.701764 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.71761  |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.463924 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.265689 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.46368  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.490553 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.643031 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.645004 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.365557 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.358187 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.365528 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.414382 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.632895 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.634498 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.361161 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.24914  |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.358564 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.712358 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.39545 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.465207 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.69929 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.365739 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.416084 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.58562 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.924783 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.708015 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.497091 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.66354 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.923654 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.315368 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.849632 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.916784 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.850128 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.636944 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6935349142279312,
    "polaris/pkis2-ret-wt-reg-v2": 776.8594695047798,
    "polaris/pkis2-kit-wt-cls-v2": 0.612015426830886,
    "polaris/pkis2-kit-wt-reg-v2": 803.3245029803641,
    "polaris/pkis2-egfr-wt-reg-v2": 516.6841028554263,
    "polaris/adme-fang-solu-1": 0.5782783995626744,
    "polaris/adme-fang-rppb-1": 0.764522821540536,
    "polaris/adme-fang-hppb-1": 0.7174348428164359,
    "polaris/adme-fang-perm-1": 0.7176096501289605,
    "polaris/adme-fang-rclint-1": 0.6450040911565413,
    "polaris/adme-fang-hclint-1": 0.6344981063987123,
    "tdcommons/lipophilicity-astrazeneca": 0.7123576383692365,
    "tdcommons/ppbr-az": 9.395449622314462,
    "tdcommons/clearance-hepatocyte-az": 0.4652065606315913,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.69928994326819,
    "tdcommons/half-life-obach": 0.36573917335957634,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4160837320130524,
    "tdcommons/clearance-microsome-az": 0.585619745981653,
    "tdcommons/dili": 0.9247826086956521,
    "tdcommons/bioavailability-ma": 0.7080146325241103,
    "tdcommons/vdss-lombardo": 0.4970909592681226,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6635397830018083,
    "tdcommons/pgp-broccatelli": 0.923653692348707,
    "tdcommons/caco2-wang": 0.31536758418137095,
    "tdcommons/herg": 0.8496318114874816,
    "tdcommons/bbb-martins": 0.9167839274546592,
    "tdcommons/ames": 0.8501282578472263,
    "tdcommons/ld50-zhu": 0.6369438630511572
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.891276 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.356461 |
|  2 | test       | CLS_RET        | pr_auc      | 0.689136 |
|  3 | test       | CLS_RET        | f1          | 0.416667 |
|  4 | test       | CLS_RET        | mcc         | 0.40138  |
|  5 | test       | CLS_RET        | accuracy    | 0.867925 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  21.2368   |
|  1 | test       | RET            | spearmanr           |   0.631151 |
|  2 | test       | RET            | pearsonr            |   0.65735  |
|  3 | test       | RET            | explained_var       |   0.376829 |
|  4 | test       | RET            | mean_squared_error  | 785.182    |
|  5 | test       | RET            | r2                  |   0.338741 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.826161 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.456674 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.642968 |
|  3 | test       | CLS_KIT        | f1          | 0.529412 |
|  4 | test       | CLS_KIT        | mcc         | 0.485525 |
|  5 | test       | CLS_KIT        | accuracy    | 0.862069 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  23.4694   |
|  1 | test       | KIT            | spearmanr           |   0.555134 |
|  2 | test       | KIT            | pearsonr            |   0.583299 |
|  3 | test       | KIT            | explained_var       |   0.331631 |
|  4 | test       | KIT            | mean_squared_error  | 813.837    |
|  5 | test       | KIT            | r2                  |   0.325559 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  17.3197   |
|  1 | test       | EGFR           | spearmanr           |   0.378752 |
|  2 | test       | EGFR           | pearsonr            |   0.64138  |
|  3 | test       | EGFR           | explained_var       |   0.371868 |
|  4 | test       | EGFR           | mean_squared_error  | 506.142    |
|  5 | test       | EGFR           | r2                  |   0.371852 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.440295 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.461253 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.573995 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.277887 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.393552 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.274128 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.579625 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.78087  |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.78584  |
|  3 | test       | LOG_RPPB       | explained_var       | 0.411627 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.523012 |
|  5 | test       | LOG_RPPB       | r2                  | 0.411343 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.549762 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.688059 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.715459 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.454777 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.358023 |
|  5 | test       | LOG_HPPB       | r2                  | 0.40885  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.412702 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.701423 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.715656 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.46155  |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.266855 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.461325 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.490444 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.652205 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.65063  |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.369112 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.356191 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.369063 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.414211 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.640073 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.637868 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.362794 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.24843  |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.360391 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  0.7144 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.24801 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.444838 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.690338 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.372464 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.398673 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.599694 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.930652 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.707848 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.522593 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.674277 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.919988 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.323878 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.843741 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.905136 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.852873 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.63687 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6891356493523677,
    "polaris/pkis2-ret-wt-reg-v2": 785.1822320018248,
    "polaris/pkis2-kit-wt-cls-v2": 0.6429681106784213,
    "polaris/pkis2-kit-wt-reg-v2": 813.8370637841771,
    "polaris/pkis2-egfr-wt-reg-v2": 506.141624638134,
    "polaris/adme-fang-solu-1": 0.5739950882493573,
    "polaris/adme-fang-rppb-1": 0.7858399000946392,
    "polaris/adme-fang-hppb-1": 0.7154594317822847,
    "polaris/adme-fang-perm-1": 0.7156557706086468,
    "polaris/adme-fang-rclint-1": 0.6506298439480473,
    "polaris/adme-fang-hclint-1": 0.6378675210442596,
    "tdcommons/lipophilicity-astrazeneca": 0.7144003851662888,
    "tdcommons/ppbr-az": 9.24801220295139,
    "tdcommons/clearance-hepatocyte-az": 0.4448378490617916,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6903382240894126,
    "tdcommons/half-life-obach": 0.3724636784526061,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.39867322557194307,
    "tdcommons/clearance-microsome-az": 0.5996940833064102,
    "tdcommons/dili": 0.9306521739130436,
    "tdcommons/bioavailability-ma": 0.7078483538410376,
    "tdcommons/vdss-lombardo": 0.5225934267953982,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6742766726943943,
    "tdcommons/pgp-broccatelli": 0.9199880031991469,
    "tdcommons/caco2-wang": 0.32387756803637885,
    "tdcommons/herg": 0.8437407952871872,
    "tdcommons/bbb-martins": 0.9051360225140711,
    "tdcommons/ames": 0.8528725841508547,
    "tdcommons/ld50-zhu": 0.6368702812342935
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.88764  |
|  1 | test       | CLS_RET        | cohen_kappa | 0.383169 |
|  2 | test       | CLS_RET        | pr_auc      | 0.684744 |
|  3 | test       | CLS_RET        | f1          | 0.434783 |
|  4 | test       | CLS_RET        | mcc         | 0.449209 |
|  5 | test       | CLS_RET        | accuracy    | 0.877358 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  21.4439   |
|  1 | test       | RET            | spearmanr           |   0.628514 |
|  2 | test       | RET            | pearsonr            |   0.650367 |
|  3 | test       | RET            | explained_var       |   0.370276 |
|  4 | test       | RET            | mean_squared_error  | 794.045    |
|  5 | test       | RET            | r2                  |   0.331277 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.824952 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.456674 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.640785 |
|  3 | test       | CLS_KIT        | f1          | 0.529412 |
|  4 | test       | CLS_KIT        | mcc         | 0.485525 |
|  5 | test       | CLS_KIT        | accuracy    | 0.862069 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  23.63     |
|  1 | test       | KIT            | spearmanr           |   0.542517 |
|  2 | test       | KIT            | pearsonr            |   0.568619 |
|  3 | test       | KIT            | explained_var       |   0.315787 |
|  4 | test       | KIT            | mean_squared_error  | 836.905    |
|  5 | test       | KIT            | r2                  |   0.306442 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  17.4331   |
|  1 | test       | EGFR           | spearmanr           |   0.366515 |
|  2 | test       | EGFR           | pearsonr            |   0.63419  |
|  3 | test       | EGFR           | explained_var       |   0.36438  |
|  4 | test       | EGFR           | mean_squared_error  | 512.338    |
|  5 | test       | EGFR           | r2                  |   0.364162 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.440802 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.456598 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.568556 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.275029 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.395088 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.271295 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.581237 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.805217 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.776576 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.413785 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.521235 |
|  5 | test       | LOG_RPPB       | r2                  | 0.413342 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.549706 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.743983 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.729374 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.461866 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.3542   |
|  5 | test       | LOG_HPPB       | r2                  | 0.415163 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.41298  |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.705669 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.719495 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.464847 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.26523  |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.464606 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.491632 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.648501 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.648361 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.366776 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.357534 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.366684 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.41541  |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.637782 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.637145 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.362161 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.248655 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.359814 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.70954 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.27247 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.455788 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.687474 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.39943 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.413276 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.600144 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.932391 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.711839 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.506865 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.677215 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.925387 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.320608 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.851399 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.914321 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.848505 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.634293 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.684744313420784,
    "polaris/pkis2-ret-wt-reg-v2": 794.0454216518871,
    "polaris/pkis2-kit-wt-cls-v2": 0.6407845641854626,
    "polaris/pkis2-kit-wt-reg-v2": 836.9048637697124,
    "polaris/pkis2-egfr-wt-reg-v2": 512.3379446619415,
    "polaris/adme-fang-solu-1": 0.5685562546868163,
    "polaris/adme-fang-rppb-1": 0.7765759930918072,
    "polaris/adme-fang-hppb-1": 0.7293739322671601,
    "polaris/adme-fang-perm-1": 0.7194948807137258,
    "polaris/adme-fang-rclint-1": 0.6483612894977471,
    "polaris/adme-fang-hclint-1": 0.6371448617134728,
    "tdcommons/lipophilicity-astrazeneca": 0.7095404963624338,
    "tdcommons/ppbr-az": 9.272467961524956,
    "tdcommons/clearance-hepatocyte-az": 0.45578778006655485,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6874739394283287,
    "tdcommons/half-life-obach": 0.39942999267405566,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4132760599080295,
    "tdcommons/clearance-microsome-az": 0.6001440257929367,
    "tdcommons/dili": 0.9323913043478261,
    "tdcommons/bioavailability-ma": 0.7118390422347856,
    "tdcommons/vdss-lombardo": 0.5068645312029815,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6772151898734178,
    "tdcommons/pgp-broccatelli": 0.9253865635830445,
    "tdcommons/caco2-wang": 0.320607986736685,
    "tdcommons/herg": 0.8513991163475698,
    "tdcommons/bbb-martins": 0.9143214509068168,
    "tdcommons/ames": 0.8485049638724079,
    "tdcommons/ld50-zhu": 0.6342932411020118
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.899868 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.356461 |
|  2 | test       | CLS_RET        | pr_auc      | 0.726303 |
|  3 | test       | CLS_RET        | f1          | 0.416667 |
|  4 | test       | CLS_RET        | mcc         | 0.40138  |
|  5 | test       | CLS_RET        | accuracy    | 0.867925 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  21.2197   |
|  1 | test       | RET            | spearmanr           |   0.632351 |
|  2 | test       | RET            | pearsonr            |   0.661743 |
|  3 | test       | RET            | explained_var       |   0.380136 |
|  4 | test       | RET            | mean_squared_error  | 784.588    |
|  5 | test       | RET            | r2                  |   0.339241 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.821809 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.456674 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.646622 |
|  3 | test       | CLS_KIT        | f1          | 0.529412 |
|  4 | test       | CLS_KIT        | mcc         | 0.485525 |
|  5 | test       | CLS_KIT        | accuracy    | 0.862069 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  23.3412   |
|  1 | test       | KIT            | spearmanr           |   0.550101 |
|  2 | test       | KIT            | pearsonr            |   0.579565 |
|  3 | test       | KIT            | explained_var       |   0.328568 |
|  4 | test       | KIT            | mean_squared_error  | 818.198    |
|  5 | test       | KIT            | r2                  |   0.321945 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  17.4596   |
|  1 | test       | EGFR           | spearmanr           |   0.366749 |
|  2 | test       | EGFR           | pearsonr            |   0.631889 |
|  3 | test       | EGFR           | explained_var       |   0.362506 |
|  4 | test       | EGFR           | mean_squared_error  | 513.745    |
|  5 | test       | EGFR           | r2                  |   0.362416 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.439675 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.463418 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.572738 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.278786 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.392917 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.275299 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.590395 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.746957 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.75638  |
|  3 | test       | LOG_RPPB       | explained_var       | 0.396565 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.536646 |
|  5 | test       | LOG_RPPB       | r2                  | 0.395996 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.549548 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.675223 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.708935 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.453008 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.356484 |
|  5 | test       | LOG_HPPB       | r2                  | 0.411392 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.414668 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.701528 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.714739 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.457576 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.268889 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.457221 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.490831 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.647302 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.646493 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.36517  |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.358416 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.365123 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.416438 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.630526 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.628797 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.35567  |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.251334 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.352917 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.711878 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  9.3083 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.454964 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.702514 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.372086 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.396789 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.586871 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.922174 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.722481 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.553041 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.668965 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.926153 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.318026 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.85891 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.911976 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.850724 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.634708 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7263028559842695,
    "polaris/pkis2-ret-wt-reg-v2": 784.5883325938678,
    "polaris/pkis2-kit-wt-cls-v2": 0.6466224169932374,
    "polaris/pkis2-kit-wt-reg-v2": 818.1981367667817,
    "polaris/pkis2-egfr-wt-reg-v2": 513.7453826367129,
    "polaris/adme-fang-solu-1": 0.5727381088385395,
    "polaris/adme-fang-rppb-1": 0.7563804106828941,
    "polaris/adme-fang-hppb-1": 0.7089351588149938,
    "polaris/adme-fang-perm-1": 0.7147388191493275,
    "polaris/adme-fang-rclint-1": 0.6464926160286333,
    "polaris/adme-fang-hclint-1": 0.6287967298252345,
    "tdcommons/lipophilicity-astrazeneca": 0.7118781702947845,
    "tdcommons/ppbr-az": 9.308295635517181,
    "tdcommons/clearance-hepatocyte-az": 0.4549640253306689,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7025139499944251,
    "tdcommons/half-life-obach": 0.3720856232152395,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3967890770422068,
    "tdcommons/clearance-microsome-az": 0.5868707224404046,
    "tdcommons/dili": 0.9221739130434782,
    "tdcommons/bioavailability-ma": 0.7224808779514466,
    "tdcommons/vdss-lombardo": 0.553040642806498,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6689647377938517,
    "tdcommons/pgp-broccatelli": 0.9261530258597707,
    "tdcommons/caco2-wang": 0.31802584913170856,
    "tdcommons/herg": 0.8589101620029455,
    "tdcommons/bbb-martins": 0.9119762351469668,
    "tdcommons/ames": 0.8507235309091621,
    "tdcommons/ld50-zhu": 0.6347080493293167
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.899537 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.383169 |
|  2 | test       | CLS_RET        | pr_auc      | 0.70733  |
|  3 | test       | CLS_RET        | f1          | 0.434783 |
|  4 | test       | CLS_RET        | mcc         | 0.449209 |
|  5 | test       | CLS_RET        | accuracy    | 0.877358 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  21.2459   |
|  1 | test       | RET            | spearmanr           |   0.630377 |
|  2 | test       | RET            | pearsonr            |   0.660342 |
|  3 | test       | RET            | explained_var       |   0.377556 |
|  4 | test       | RET            | mean_squared_error  | 793.208    |
|  5 | test       | RET            | r2                  |   0.331982 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.834623 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.456674 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.658718 |
|  3 | test       | CLS_KIT        | f1          | 0.529412 |
|  4 | test       | CLS_KIT        | mcc         | 0.485525 |
|  5 | test       | CLS_KIT        | accuracy    | 0.862069 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  23.5292   |
|  1 | test       | KIT            | spearmanr           |   0.557092 |
|  2 | test       | KIT            | pearsonr            |   0.576576 |
|  3 | test       | KIT            | explained_var       |   0.324576 |
|  4 | test       | KIT            | mean_squared_error  | 824.249    |
|  5 | test       | KIT            | r2                  |   0.31693  |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  17.2865   |
|  1 | test       | EGFR           | spearmanr           |   0.386062 |
|  2 | test       | EGFR           | pearsonr            |   0.64663  |
|  3 | test       | EGFR           | explained_var       |   0.380619 |
|  4 | test       | EGFR           | mean_squared_error  | 499.179    |
|  5 | test       | EGFR           | r2                  |   0.380493 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.43783  |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.471071 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.579024 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.280865 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.391942 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.277098 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.579412 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.76     |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.771112 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.414606 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.520882 |
|  5 | test       | LOG_RPPB       | r2                  | 0.413739 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.543136 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.704255 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.720944 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.46572  |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.353337 |
|  5 | test       | LOG_HPPB       | r2                  | 0.416587 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.413893 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.703269 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.718028 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.462805 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.26625  |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.462547 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.490152 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.648338 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.646474 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.366681 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.357582 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.3666   |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.415237 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.636028 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.632278 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.358013 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.25045  |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.355191 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.714281 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.19034 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr |  0.4533 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.692299 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.339466 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.413615 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.589763 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.934565 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.719654 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.522732 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.665348 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.928486 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.320337 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.855817 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.918074 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.847006 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.635621 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7073304209656397,
    "polaris/pkis2-ret-wt-reg-v2": 793.2084259264572,
    "polaris/pkis2-kit-wt-cls-v2": 0.6587182442484976,
    "polaris/pkis2-kit-wt-reg-v2": 824.2492956362241,
    "polaris/pkis2-egfr-wt-reg-v2": 499.17932114302454,
    "polaris/adme-fang-solu-1": 0.5790237904811822,
    "polaris/adme-fang-rppb-1": 0.7711117650252846,
    "polaris/adme-fang-hppb-1": 0.7209435329105299,
    "polaris/adme-fang-perm-1": 0.7180276436903776,
    "polaris/adme-fang-rclint-1": 0.6464740696107658,
    "polaris/adme-fang-hclint-1": 0.6322776149995339,
    "tdcommons/lipophilicity-astrazeneca": 0.7142814690476189,
    "tdcommons/ppbr-az": 9.190342356726454,
    "tdcommons/clearance-hepatocyte-az": 0.4533001331792948,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6922988396586933,
    "tdcommons/half-life-obach": 0.33946555389562416,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4136149327137728,
    "tdcommons/clearance-microsome-az": 0.5897629663784179,
    "tdcommons/dili": 0.9345652173913043,
    "tdcommons/bioavailability-ma": 0.7196541403392085,
    "tdcommons/vdss-lombardo": 0.5227322249288276,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6653481012658228,
    "tdcommons/pgp-broccatelli": 0.9284857371367635,
    "tdcommons/caco2-wang": 0.32033651009986397,
    "tdcommons/herg": 0.8558173784977908,
    "tdcommons/bbb-martins": 0.9180737961225766,
    "tdcommons/ames": 0.8470060114746716,
    "tdcommons/ld50-zhu": 0.6356208455343109
}
```
