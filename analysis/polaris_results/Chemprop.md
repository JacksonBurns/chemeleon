# Chemprop Baseline Results
timestamp: 2025-04-28 18:01:37.398716
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.473913 |
|  1 | test       | CLS_RET        | mcc         | 0        |
|  2 | test       | CLS_RET        | accuracy    | 0.839623 |
|  3 | test       | CLS_RET        | cohen_kappa | 0        |
|  4 | test       | CLS_RET        | roc_auc     | 0.776603 |
|  5 | test       | CLS_RET        | f1          | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | RET            | mean_absolute_error |   25.9476    |
|  1 | test       | RET            | spearmanr           |    0.385313  |
|  2 | test       | RET            | mean_squared_error  | 1104.54      |
|  3 | test       | RET            | pearsonr            |    0.353268  |
|  4 | test       | RET            | r2                  |    0.0697841 |
|  5 | test       | RET            | explained_var       |    0.0809102 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.440342 |
|  1 | test       | CLS_KIT        | mcc         | 0.124494 |
|  2 | test       | CLS_KIT        | accuracy    | 0.775862 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.117096 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.741779 |
|  5 | test       | CLS_KIT        | f1          | 0.235294 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  23.3881   |
|  1 | test       | KIT            | spearmanr           |   0.488987 |
|  2 | test       | KIT            | mean_squared_error  | 916.982    |
|  3 | test       | KIT            | pearsonr            |   0.538438 |
|  4 | test       | KIT            | r2                  |   0.240081 |
|  5 | test       | KIT            | explained_var       |   0.283958 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | EGFR           | mean_absolute_error |  23.064     |
|  1 | test       | EGFR           | spearmanr           |   0.0741582 |
|  2 | test       | EGFR           | mean_squared_error  | 826.431     |
|  3 | test       | EGFR           | pearsonr            |   0.136811  |
|  4 | test       | EGFR           | r2                  |  -0.0256428 |
|  5 | test       | EGFR           | explained_var       |   0.0135929 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.393985 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.532927 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.341053 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.61109  |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.370957 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.373112 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error |  0.81018   |
|  1 | test       | LOG_RPPB       | spearmanr           |  0.214783  |
|  2 | test       | LOG_RPPB       | mean_squared_error  |  0.91131   |
|  3 | test       | LOG_RPPB       | pearsonr            |  0.17836   |
|  4 | test       | LOG_RPPB       | r2                  | -0.0256933 |
|  5 | test       | LOG_RPPB       | explained_var       |  0.0141742 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.661955  |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.643747  |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.573464  |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.567476  |
|  4 | test       | LOG_HPPB       | r2                  | 0.053125  |
|  5 | test       | LOG_HPPB       | explained_var       | 0.0702842 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.374702 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.719624 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.254573 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.698006 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.486118 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.487187 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.441583 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.682643 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.303499 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.684352 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.462399 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.464323 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.375369 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.662124 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.239506 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.640461 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.383367 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.383476 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.454692 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.09804 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.342526 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.657904 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.302129 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.429798 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.537209 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.906087 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.621882 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.496698 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.516275 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.911024 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.409064 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.709426 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.862375 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.824465 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.590037 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.4739126076126694,
    "polaris/pkis2-ret-wt-reg-v2": 1104.5430837924507,
    "polaris/pkis2-kit-wt-cls-v2": 0.44034151425805956,
    "polaris/pkis2-kit-wt-reg-v2": 916.9820765157901,
    "polaris/pkis2-egfr-wt-reg-v2": 826.4306379771456,
    "polaris/adme-fang-solu-1": 0.6110900500211651,
    "polaris/adme-fang-rppb-1": 0.17836038630728374,
    "polaris/adme-fang-hppb-1": 0.5674755840472965,
    "polaris/adme-fang-perm-1": 0.6980057866897077,
    "polaris/adme-fang-rclint-1": 0.6843521937463056,
    "polaris/adme-fang-hclint-1": 0.6404613320422048,
    "tdcommons/lipophilicity-astrazeneca": 0.45469246210370745,
    "tdcommons/ppbr-az": 8.098037824545436,
    "tdcommons/clearance-hepatocyte-az": 0.342526253427613,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6579043524525793,
    "tdcommons/half-life-obach": 0.30212881354276194,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4297984010324548,
    "tdcommons/clearance-microsome-az": 0.5372087247155588,
    "tdcommons/dili": 0.9060869565217391,
    "tdcommons/bioavailability-ma": 0.6218822746923844,
    "tdcommons/vdss-lombardo": 0.4966977013674516,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5162748643761302,
    "tdcommons/pgp-broccatelli": 0.9110237270061317,
    "tdcommons/caco2-wang": 0.40906376247206483,
    "tdcommons/herg": 0.7094256259204713,
    "tdcommons/bbb-martins": 0.8623749218261412,
    "tdcommons/ames": 0.8244649395915329,
    "tdcommons/ld50-zhu": 0.5900371637105619
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.590026 |
|  1 | test       | CLS_RET        | mcc         | 0.223293 |
|  2 | test       | CLS_RET        | accuracy    | 0.849057 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.094984 |
|  4 | test       | CLS_RET        | roc_auc     | 0.801718 |
|  5 | test       | CLS_RET        | f1          | 0.111111 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  23.978    |
|  1 | test       | RET            | spearmanr           |   0.457853 |
|  2 | test       | RET            | mean_squared_error  | 984.032    |
|  3 | test       | RET            | pearsonr            |   0.458482 |
|  4 | test       | RET            | r2                  |   0.171275 |
|  5 | test       | RET            | explained_var       |   0.193119 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.35849  |
|  1 | test       | CLS_KIT        | mcc         | 0        |
|  2 | test       | CLS_KIT        | accuracy    | 0.810345 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0        |
|  4 | test       | CLS_KIT        | roc_auc     | 0.652805 |
|  5 | test       | CLS_KIT        | f1          | 0        |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  23.0109   |
|  1 | test       | KIT            | spearmanr           |   0.508687 |
|  2 | test       | KIT            | mean_squared_error  | 928.335    |
|  3 | test       | KIT            | pearsonr            |   0.561039 |
|  4 | test       | KIT            | r2                  |   0.230673 |
|  5 | test       | KIT            | explained_var       |   0.307276 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  20.4419   |
|  1 | test       | EGFR           | spearmanr           |   0.222919 |
|  2 | test       | EGFR           | mean_squared_error  | 676.203    |
|  3 | test       | EGFR           | pearsonr            |   0.420055 |
|  4 | test       | EGFR           | r2                  |   0.160797 |
|  5 | test       | EGFR           | explained_var       |   0.160807 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.387249 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.555685 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.338897 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.615016 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.374935 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.378158 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.694049  |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.328696  |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.833985  |
|  3 | test       | LOG_RPPB       | pearsonr            | 0.249703  |
|  4 | test       | LOG_RPPB       | r2                  | 0.0613377 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.062325  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.595651 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.668195 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.478312 |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.580156 |
|  4 | test       | LOG_HPPB       | r2                  | 0.210235 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.216015 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.37514  |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.715919 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.250583 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.703046 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.494172 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.494258 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.419038 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.714781 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.275558 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.71591  |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.511893 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.511999 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.385858 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.646945 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.243022 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.626686 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.374316 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.381197 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.469805 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.93535 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.328099 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.647531 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.301228 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.400143 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.503706 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.906957 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.602927 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.525165 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.563969 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.890496 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.376234 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.695582 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.811288 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.830159 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.609616 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5900259406865028,
    "polaris/pkis2-ret-wt-reg-v2": 984.032039975163,
    "polaris/pkis2-kit-wt-cls-v2": 0.35848963136771334,
    "polaris/pkis2-kit-wt-reg-v2": 928.3345803068048,
    "polaris/pkis2-egfr-wt-reg-v2": 676.2029481412721,
    "polaris/adme-fang-solu-1": 0.6150160215445122,
    "polaris/adme-fang-rppb-1": 0.2497028242807443,
    "polaris/adme-fang-hppb-1": 0.5801561461376035,
    "polaris/adme-fang-perm-1": 0.7030461555877876,
    "polaris/adme-fang-rclint-1": 0.7159101444791578,
    "polaris/adme-fang-hclint-1": 0.626685908928898,
    "tdcommons/lipophilicity-astrazeneca": 0.46980536438737597,
    "tdcommons/ppbr-az": 7.935351177618201,
    "tdcommons/clearance-hepatocyte-az": 0.32809901901089467,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6475307427498239,
    "tdcommons/half-life-obach": 0.3012279481516677,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.40014299004059595,
    "tdcommons/clearance-microsome-az": 0.5037062168989814,
    "tdcommons/dili": 0.9069565217391304,
    "tdcommons/bioavailability-ma": 0.6029265048220818,
    "tdcommons/vdss-lombardo": 0.5251649545976853,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5639692585895117,
    "tdcommons/pgp-broccatelli": 0.8904958677685951,
    "tdcommons/caco2-wang": 0.3762340911022146,
    "tdcommons/herg": 0.6955817378497791,
    "tdcommons/bbb-martins": 0.8112883051907441,
    "tdcommons/ames": 0.8301591963813664,
    "tdcommons/ld50-zhu": 0.6096163785344694
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.434672 |
|  1 | test       | CLS_RET        | mcc         | 0        |
|  2 | test       | CLS_RET        | accuracy    | 0.839623 |
|  3 | test       | CLS_RET        | cohen_kappa | 0        |
|  4 | test       | CLS_RET        | roc_auc     | 0.763384 |
|  5 | test       | CLS_RET        | f1          | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  23.7723   |
|  1 | test       | RET            | spearmanr           |   0.514482 |
|  2 | test       | RET            | mean_squared_error  | 933.622    |
|  3 | test       | RET            | pearsonr            |   0.486956 |
|  4 | test       | RET            | r2                  |   0.213729 |
|  5 | test       | RET            | explained_var       |   0.213742 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.442999 |
|  1 | test       | CLS_KIT        | mcc         | 0.206776 |
|  2 | test       | CLS_KIT        | accuracy    | 0.784483 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.201542 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.764507 |
|  5 | test       | CLS_KIT        | f1          | 0.324324 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  21.5231   |
|  1 | test       | KIT            | spearmanr           |   0.52035  |
|  2 | test       | KIT            | mean_squared_error  | 833.705    |
|  3 | test       | KIT            | pearsonr            |   0.580397 |
|  4 | test       | KIT            | r2                  |   0.309095 |
|  5 | test       | KIT            | explained_var       |   0.330063 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | EGFR           | mean_absolute_error |  21.051     |
|  1 | test       | EGFR           | spearmanr           |   0.149674  |
|  2 | test       | EGFR           | mean_squared_error  | 738.921     |
|  3 | test       | EGFR           | pearsonr            |   0.289439  |
|  4 | test       | EGFR           | r2                  |   0.0829612 |
|  5 | test       | EGFR           | explained_var       |   0.0831333 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.413956 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.500219 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.353773 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.590687 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.347498 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.34778  |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.693547  |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.227826  |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.857109  |
|  3 | test       | LOG_RPPB       | pearsonr            | 0.195226  |
|  4 | test       | LOG_RPPB       | r2                  | 0.0353113 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.03686   |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error |  0.699146   |
|  1 | test       | LOG_HPPB       | spearmanr           |  0.384445   |
|  2 | test       | LOG_HPPB       | mean_squared_error  |  0.638182   |
|  3 | test       | LOG_HPPB       | pearsonr            |  0.330516   |
|  4 | test       | LOG_HPPB       | r2                  | -0.0537342  |
|  5 | test       | LOG_HPPB       | explained_var       |  0.00614101 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.385975 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.722449 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.255263 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.698839 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.484726 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.486407 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.433411 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.698801 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.290935 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.698499 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.484654 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.487236 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.387113 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.645289 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.240075 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.621169 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.381904 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.385663 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.453283 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.93282 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.361993 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.673799 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.256152 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.421027 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.50221 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.917826 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.577985 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.531533 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.568716 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.883364 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.36397 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.694109 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.865111 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.843277 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.562925 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.4346721144698639,
    "polaris/pkis2-ret-wt-reg-v2": 933.6224968353667,
    "polaris/pkis2-kit-wt-cls-v2": 0.44299935722764416,
    "polaris/pkis2-kit-wt-reg-v2": 833.7045091889248,
    "polaris/pkis2-egfr-wt-reg-v2": 738.9209915305378,
    "polaris/adme-fang-solu-1": 0.5906870444756219,
    "polaris/adme-fang-rppb-1": 0.1952264782315199,
    "polaris/adme-fang-hppb-1": 0.3305159659470481,
    "polaris/adme-fang-perm-1": 0.6988393132095868,
    "polaris/adme-fang-rclint-1": 0.6984992260982636,
    "polaris/adme-fang-hclint-1": 0.6211694042828204,
    "tdcommons/lipophilicity-astrazeneca": 0.45328324929873154,
    "tdcommons/ppbr-az": 7.9328169632640435,
    "tdcommons/clearance-hepatocyte-az": 0.36199257785045064,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6737990570367647,
    "tdcommons/half-life-obach": 0.25615162349333587,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.42102733032277095,
    "tdcommons/clearance-microsome-az": 0.5022098185134957,
    "tdcommons/dili": 0.9178260869565218,
    "tdcommons/bioavailability-ma": 0.5779847023611572,
    "tdcommons/vdss-lombardo": 0.5315330320980965,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5687160940325499,
    "tdcommons/pgp-broccatelli": 0.8833644361503599,
    "tdcommons/caco2-wang": 0.36397031237585054,
    "tdcommons/herg": 0.6941089837997054,
    "tdcommons/bbb-martins": 0.8651110068792996,
    "tdcommons/ames": 0.8432767432297481,
    "tdcommons/ld50-zhu": 0.5629254353069001
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.352745 |
|  1 | test       | CLS_RET        | mcc         | 0        |
|  2 | test       | CLS_RET        | accuracy    | 0.839623 |
|  3 | test       | CLS_RET        | cohen_kappa | 0        |
|  4 | test       | CLS_RET        | roc_auc     | 0.749504 |
|  5 | test       | CLS_RET        | f1          | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | RET            | mean_absolute_error |   25.138    |
|  1 | test       | RET            | spearmanr           |    0.445789 |
|  2 | test       | RET            | mean_squared_error  | 1041.4      |
|  3 | test       | RET            | pearsonr            |    0.418974 |
|  4 | test       | RET            | r2                  |    0.122961 |
|  5 | test       | RET            | explained_var       |    0.123271 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.579998 |
|  1 | test       | CLS_KIT        | mcc         | 0.413319 |
|  2 | test       | CLS_KIT        | accuracy    | 0.844828 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.388759 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.841393 |
|  5 | test       | CLS_KIT        | f1          | 0.470588 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  22.7968   |
|  1 | test       | KIT            | spearmanr           |   0.487021 |
|  2 | test       | KIT            | mean_squared_error  | 885.641    |
|  3 | test       | KIT            | pearsonr            |   0.56074  |
|  4 | test       | KIT            | r2                  |   0.266054 |
|  5 | test       | KIT            | explained_var       |   0.307855 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  21.1394   |
|  1 | test       | EGFR           | spearmanr           |   0.217842 |
|  2 | test       | EGFR           | mean_squared_error  | 705.261    |
|  3 | test       | EGFR           | pearsonr            |   0.372648 |
|  4 | test       | EGFR           | r2                  |   0.124735 |
|  5 | test       | EGFR           | explained_var       |   0.126096 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.416941 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.50266  |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.362289 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.576362 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.331791 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.332193 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.705339  |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.297391  |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.857859  |
|  3 | test       | LOG_RPPB       | pearsonr            | 0.216297  |
|  4 | test       | LOG_RPPB       | r2                  | 0.0344668 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.0378185 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.675924  |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.685308  |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.595654  |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.616235  |
|  4 | test       | LOG_HPPB       | r2                  | 0.0164869 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.052028  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.393647 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.687022 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.273044 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.671383 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.448834 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.450277 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.450183 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.663196 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.314011 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.666287 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.443778 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.443855 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.354858 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.689921 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.2209   |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.666293 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.431272 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.434233 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.478257 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.36578 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.378821 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.596624 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.246981 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.384804 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.451901 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  |    0.89 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.584303 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.496613 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.573237 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.871901 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.335726 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.679381 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.89513 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.838801 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.609074 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.35274508950310246,
    "polaris/pkis2-ret-wt-reg-v2": 1041.4011348866725,
    "polaris/pkis2-kit-wt-cls-v2": 0.5799982023356187,
    "polaris/pkis2-kit-wt-reg-v2": 885.6409931489636,
    "polaris/pkis2-egfr-wt-reg-v2": 705.2608432653578,
    "polaris/adme-fang-solu-1": 0.5763622162909174,
    "polaris/adme-fang-rppb-1": 0.21629655310409587,
    "polaris/adme-fang-hppb-1": 0.6162349536407169,
    "polaris/adme-fang-perm-1": 0.6713831330953548,
    "polaris/adme-fang-rclint-1": 0.6662869206991502,
    "polaris/adme-fang-hclint-1": 0.6662928003688151,
    "tdcommons/lipophilicity-astrazeneca": 0.47825674462886086,
    "tdcommons/ppbr-az": 8.365783486681888,
    "tdcommons/clearance-hepatocyte-az": 0.3788209216347244,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5966243026911265,
    "tdcommons/half-life-obach": 0.24698074633759062,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.38480445164187416,
    "tdcommons/clearance-microsome-az": 0.4519009502421633,
    "tdcommons/dili": 0.89,
    "tdcommons/bioavailability-ma": 0.5843032923179249,
    "tdcommons/vdss-lombardo": 0.49661296523173326,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5732368896925859,
    "tdcommons/pgp-broccatelli": 0.871900826446281,
    "tdcommons/caco2-wang": 0.3357260554730762,
    "tdcommons/herg": 0.6793814432989691,
    "tdcommons/bbb-martins": 0.8951297686053784,
    "tdcommons/ames": 0.8388014255223325,
    "tdcommons/ld50-zhu": 0.6090741500957731
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.313821 |
|  1 | test       | CLS_RET        | mcc         | 0        |
|  2 | test       | CLS_RET        | accuracy    | 0.839623 |
|  3 | test       | CLS_RET        | cohen_kappa | 0        |
|  4 | test       | CLS_RET        | roc_auc     | 0.691342 |
|  5 | test       | CLS_RET        | f1          | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | RET            | mean_absolute_error |   25.3052    |
|  1 | test       | RET            | spearmanr           |    0.42762   |
|  2 | test       | RET            | mean_squared_error  | 1092.72      |
|  3 | test       | RET            | pearsonr            |    0.394682  |
|  4 | test       | RET            | r2                  |    0.0797393 |
|  5 | test       | RET            | explained_var       |    0.0806203 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.377296 |
|  1 | test       | CLS_KIT        | mcc         | 0        |
|  2 | test       | CLS_KIT        | accuracy    | 0.810345 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0        |
|  4 | test       | CLS_KIT        | roc_auc     | 0.625725 |
|  5 | test       | CLS_KIT        | f1          | 0        |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |         Score |
|---:|:-----------|:---------------|:--------------------|--------------:|
|  0 | test       | KIT            | mean_absolute_error |   30.0875     |
|  1 | test       | KIT            | spearmanr           |    0.173218   |
|  2 | test       | KIT            | mean_squared_error  | 1204.43       |
|  3 | test       | KIT            | pearsonr            |    0.219806   |
|  4 | test       | KIT            | r2                  |    0.0018654  |
|  5 | test       | KIT            | explained_var       |    0.00444679 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  20.3013   |
|  1 | test       | EGFR           | spearmanr           |   0.264777 |
|  2 | test       | EGFR           | mean_squared_error  | 685.891    |
|  3 | test       | EGFR           | pearsonr            |   0.39485  |
|  4 | test       | EGFR           | r2                  |   0.148774 |
|  5 | test       | EGFR           | explained_var       |   0.150322 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.414397 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.490977 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.359693 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.587288 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.336579 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.339924 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.732679   |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.253913   |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.881484   |
|  3 | test       | LOG_RPPB       | pearsonr            | 0.199265   |
|  4 | test       | LOG_RPPB       | r2                  | 0.00787614 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.0306521  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.618566 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.574528 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.507738 |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.568362 |
|  4 | test       | LOG_HPPB       | r2                  | 0.161649 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.288478 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.356639 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.724138 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.242775 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.714558 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.509934 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.510043 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.434718 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.700064 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.292024 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.695154 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.482725 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.483196 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.361242 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.68468  |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.228399 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.661893 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.411964 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.41902  |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.456331 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.20025 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.350121 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.701544 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.268837 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.425856 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.569913 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.908696 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.596608 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.328499 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.605561 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.879432 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.374442 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.705155 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.885163 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.842468 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.617433 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.31382114883988477,
    "polaris/pkis2-ret-wt-reg-v2": 1092.7222070584412,
    "polaris/pkis2-kit-wt-cls-v2": 0.37729576182960417,
    "polaris/pkis2-kit-wt-reg-v2": 1204.4330977949314,
    "polaris/pkis2-egfr-wt-reg-v2": 685.8908405884886,
    "polaris/adme-fang-solu-1": 0.587287999625133,
    "polaris/adme-fang-rppb-1": 0.19926490691249624,
    "polaris/adme-fang-hppb-1": 0.5683617427244505,
    "polaris/adme-fang-perm-1": 0.7145584468046873,
    "polaris/adme-fang-rclint-1": 0.6951542598912497,
    "polaris/adme-fang-hclint-1": 0.6618933929058317,
    "tdcommons/lipophilicity-astrazeneca": 0.45633100176992863,
    "tdcommons/ppbr-az": 8.200249426062078,
    "tdcommons/clearance-hepatocyte-az": 0.350121412256134,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7015437006935749,
    "tdcommons/half-life-obach": 0.268837190537759,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.425856086082614,
    "tdcommons/clearance-microsome-az": 0.5699130397714653,
    "tdcommons/dili": 0.908695652173913,
    "tdcommons/bioavailability-ma": 0.5966079148653143,
    "tdcommons/vdss-lombardo": 0.3284988857636628,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6055605786618444,
    "tdcommons/pgp-broccatelli": 0.8794321514262863,
    "tdcommons/caco2-wang": 0.3744417314088593,
    "tdcommons/herg": 0.7051546391752577,
    "tdcommons/bbb-martins": 0.8851626016260162,
    "tdcommons/ames": 0.8424680334449471,
    "tdcommons/ld50-zhu": 0.6174325002656094
}
```
