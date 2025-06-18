# MLP on PCA-reduced Descriptors (Pretrained PCA) Results
timestamp: 2025-06-17 20:44:12.017390
GPU: True (CUDA_VISIBLE_DEVICES=0)
Using pretrained PCA from prefitted_pca_model.pt with 142 components

## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.839623 |
|  1 | test       | CLS_RET        | pr_auc      | 0.608801 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.137799 |
|  3 | test       | CLS_RET        | mcc         | 0.183279 |
|  4 | test       | CLS_RET        | roc_auc     | 0.848645 |
|  5 | test       | CLS_RET        | f1          | 0.190476 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.553959 |
|  1 | test       | RET            | explained_var       |   0.305759 |
|  2 | test       | RET            | mean_absolute_error |  22.7242   |
|  3 | test       | RET            | mean_squared_error  | 845.65     |
|  4 | test       | RET            | pearsonr            |   0.554029 |
|  5 | test       | RET            | r2                  |   0.287817 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.818966 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.511869 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.301606 |
|  3 | test       | CLS_KIT        | mcc         | 0.316097 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.753385 |
|  5 | test       | CLS_KIT        | f1          | 0.4      |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | spearmanr           |    0.396837 |
|  1 | test       | KIT            | explained_var       |    0.134344 |
|  2 | test       | KIT            | mean_absolute_error |   26.1995   |
|  3 | test       | KIT            | mean_squared_error  | 1047.95     |
|  4 | test       | KIT            | pearsonr            |    0.423627 |
|  5 | test       | KIT            | r2                  |    0.131545 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.268072 |
|  1 | test       | EGFR           | explained_var       |   0.305604 |
|  2 | test       | EGFR           | mean_absolute_error |  18.7135   |
|  3 | test       | EGFR           | mean_squared_error  | 564.325    |
|  4 | test       | EGFR           | pearsonr            |   0.553135 |
|  5 | test       | EGFR           | r2                  |   0.299643 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.452193 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.298603 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.435311 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.381847 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.548212 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.295718 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.683478 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.385007 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.591761 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.546579 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.632551 |
|  5 | test       | LOG_RPPB       | r2                  | 0.384817 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.842998 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.704837 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.416956 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.233164 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.850104 |
|  5 | test       | LOG_HPPB       | r2                  | 0.615012 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.75469  |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.546337 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.362471 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.224792 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.740044 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.546235 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.649276 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.420101 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.454723 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.327388 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.650083 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.420084 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.657322 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.395821 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.379955 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.234713 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.639396 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.395708 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.583561 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.83713 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.354375 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.68663 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.267587 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.362079 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.518029 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.912174 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.71134 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.385276 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.599118 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.916822 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.309019 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.850221 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.890869 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.840367 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.613471 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.608801441077923,
    "polaris/pkis2-ret-wt-reg-v2": 845.6501515444747,
    "polaris/pkis2-kit-wt-cls-v2": 0.5118685400325798,
    "polaris/pkis2-kit-wt-reg-v2": 1047.9513780075754,
    "polaris/pkis2-egfr-wt-reg-v2": 564.325496076601,
    "polaris/adme-fang-solu-1": 0.5482115220558281,
    "polaris/adme-fang-rppb-1": 0.6325511820294444,
    "polaris/adme-fang-hppb-1": 0.8501040002764186,
    "polaris/adme-fang-perm-1": 0.7400438610475429,
    "polaris/adme-fang-rclint-1": 0.6500828266113278,
    "polaris/adme-fang-hclint-1": 0.6393959833868882,
    "tdcommons/lipophilicity-astrazeneca": 0.5835609596400034,
    "tdcommons/ppbr-az": 8.837133180894664,
    "tdcommons/clearance-hepatocyte-az": 0.35437533640574315,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6866297221757234,
    "tdcommons/half-life-obach": 0.2675866037701108,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3620786821584192,
    "tdcommons/clearance-microsome-az": 0.5180285297653121,
    "tdcommons/dili": 0.9121739130434783,
    "tdcommons/bioavailability-ma": 0.7113402061855669,
    "tdcommons/vdss-lombardo": 0.3852759665777344,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.599118444846293,
    "tdcommons/pgp-broccatelli": 0.9168221807517994,
    "tdcommons/caco2-wang": 0.3090187029796727,
    "tdcommons/herg": 0.850220913107511,
    "tdcommons/bbb-martins": 0.8908692933083177,
    "tdcommons/ames": 0.8403669545125222,
    "tdcommons/ld50-zhu": 0.6134714406398056
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.867925 |
|  1 | test       | CLS_RET        | pr_auc      | 0.661301 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.264618 |
|  3 | test       | CLS_RET        | mcc         | 0.390492 |
|  4 | test       | CLS_RET        | roc_auc     | 0.881031 |
|  5 | test       | CLS_RET        | f1          | 0.3      |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.600938 |
|  1 | test       | RET            | explained_var       |   0.373306 |
|  2 | test       | RET            | mean_absolute_error |  21.1442   |
|  3 | test       | RET            | mean_squared_error  | 767.802    |
|  4 | test       | RET            | pearsonr            |   0.611195 |
|  5 | test       | RET            | r2                  |   0.353378 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.818966 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.493587 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.329295 |
|  3 | test       | CLS_KIT        | mcc         | 0.337847 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.779497 |
|  5 | test       | CLS_KIT        | f1          | 0.432432 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | spearmanr           |    0.416272 |
|  1 | test       | KIT            | explained_var       |    0.135574 |
|  2 | test       | KIT            | mean_absolute_error |   25.6097   |
|  3 | test       | KIT            | mean_squared_error  | 1052.76     |
|  4 | test       | KIT            | pearsonr            |    0.441145 |
|  5 | test       | KIT            | r2                  |    0.12756  |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.320607 |
|  1 | test       | EGFR           | explained_var       |   0.364991 |
|  2 | test       | EGFR           | mean_absolute_error |  18.057    |
|  3 | test       | EGFR           | mean_squared_error  | 512.811    |
|  4 | test       | EGFR           | pearsonr            |   0.60449  |
|  5 | test       | EGFR           | r2                  |   0.363576 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.469414 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.323948 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.434052 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.367146 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.569336 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.322833 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.825217 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.54045  |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.482343 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.409156 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.779614 |
|  5 | test       | LOG_RPPB       | r2                  | 0.539489 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.740469 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.569051 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.523761 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.341182 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.764215 |
|  5 | test       | LOG_HPPB       | r2                  | 0.436658 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.724346 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.516991 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.374621 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.239414 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.719717 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.516718 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.640014 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.41627  |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.451519 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.329817 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.645821 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.41578  |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.642501 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.379049 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.38933  |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.241373 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.619099 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.378562 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.563041 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.76137 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.389669 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.668457 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.13164 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.404274 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.481746 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.886957 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.612238 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.473965 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.580583 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.902226 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.291873 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.846981 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.902498 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.844362 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.641711 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6613014305435518,
    "polaris/pkis2-ret-wt-reg-v2": 767.8017197506773,
    "polaris/pkis2-kit-wt-cls-v2": 0.4935867818505116,
    "polaris/pkis2-kit-wt-reg-v2": 1052.759775846175,
    "polaris/pkis2-egfr-wt-reg-v2": 512.8106936653771,
    "polaris/adme-fang-solu-1": 0.5693364849278093,
    "polaris/adme-fang-rppb-1": 0.7796140843816683,
    "polaris/adme-fang-hppb-1": 0.7642145111997527,
    "polaris/adme-fang-perm-1": 0.7197173301019035,
    "polaris/adme-fang-rclint-1": 0.6458205625183164,
    "polaris/adme-fang-hclint-1": 0.6190990623552705,
    "tdcommons/lipophilicity-astrazeneca": 0.5630414800700687,
    "tdcommons/ppbr-az": 8.761373043435631,
    "tdcommons/clearance-hepatocyte-az": 0.38966947971285065,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6684565637769329,
    "tdcommons/half-life-obach": 0.13164021370612608,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.40427435222079916,
    "tdcommons/clearance-microsome-az": 0.48174565750337833,
    "tdcommons/dili": 0.8869565217391304,
    "tdcommons/bioavailability-ma": 0.6122381110741603,
    "tdcommons/vdss-lombardo": 0.4739653515728488,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5805831826401446,
    "tdcommons/pgp-broccatelli": 0.9022260730471874,
    "tdcommons/caco2-wang": 0.29187343638288904,
    "tdcommons/herg": 0.846980854197349,
    "tdcommons/bbb-martins": 0.9024976547842402,
    "tdcommons/ames": 0.8443615500597232,
    "tdcommons/ld50-zhu": 0.6417113598531896
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.849057 |
|  1 | test       | CLS_RET        | pr_auc      | 0.624919 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.215541 |
|  3 | test       | CLS_RET        | mcc         | 0.266557 |
|  4 | test       | CLS_RET        | roc_auc     | 0.857898 |
|  5 | test       | CLS_RET        | f1          | 0.272727 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.568205 |
|  1 | test       | RET            | explained_var       |   0.296487 |
|  2 | test       | RET            | mean_absolute_error |  22.7164   |
|  3 | test       | RET            | mean_squared_error  | 892.371    |
|  4 | test       | RET            | pearsonr            |   0.545654 |
|  5 | test       | RET            | r2                  |   0.24847  |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.818966 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.507128 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.271531 |
|  3 | test       | CLS_KIT        | mcc         | 0.293758 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.758704 |
|  5 | test       | CLS_KIT        | f1          | 0.363636 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.46597  |
|  1 | test       | KIT            | explained_var       |   0.21452  |
|  2 | test       | KIT            | mean_absolute_error |  24.7321   |
|  3 | test       | KIT            | mean_squared_error  | 950.195    |
|  4 | test       | KIT            | pearsonr            |   0.480107 |
|  5 | test       | KIT            | r2                  |   0.212557 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.26967  |
|  1 | test       | EGFR           | explained_var       |   0.302529 |
|  2 | test       | EGFR           | mean_absolute_error |  18.8205   |
|  3 | test       | EGFR           | mean_squared_error  | 566.966    |
|  4 | test       | EGFR           | pearsonr            |   0.550496 |
|  5 | test       | EGFR           | r2                  |   0.296366 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.450553 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.265486 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.445724 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.402213 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.518558 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.258153 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.872174 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.607488 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.456767 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.348838 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.825405 |
|  5 | test       | LOG_RPPB       | r2                  | 0.607378 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.724119 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.520672 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.554547 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.373664 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.741609 |
|  5 | test       | LOG_HPPB       | r2                  | 0.383025 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.723093 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.517689 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.375007 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.238971 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.719541 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.517614 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.665661 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.431038 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.443067 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.32121  |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.660116 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.431027 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.650769 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.396543 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.381932 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.234504 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.631418 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.396246 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.577229 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.66081 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.389238 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.675913 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |      Score |
|---:|:-----------|:---------------|:----------|-----------:|
|  0 | test       | Y              | spearmanr | -0.0138551 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.311042 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.522274 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.876087 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.504157 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.403886 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.619236 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.917155 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.292881 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.834315 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.910217 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.851524 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  0.6409 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6249187006503948,
    "polaris/pkis2-ret-wt-reg-v2": 892.3709839157024,
    "polaris/pkis2-kit-wt-cls-v2": 0.5071278574087444,
    "polaris/pkis2-kit-wt-reg-v2": 950.1952647225992,
    "polaris/pkis2-egfr-wt-reg-v2": 566.966073234605,
    "polaris/adme-fang-solu-1": 0.5185579335716157,
    "polaris/adme-fang-rppb-1": 0.8254047078509478,
    "polaris/adme-fang-hppb-1": 0.7416090737652536,
    "polaris/adme-fang-perm-1": 0.7195413340654004,
    "polaris/adme-fang-rclint-1": 0.6601160808019203,
    "polaris/adme-fang-hclint-1": 0.631417743591459,
    "tdcommons/lipophilicity-astrazeneca": 0.5772293676081157,
    "tdcommons/ppbr-az": 8.66080521148518,
    "tdcommons/clearance-hepatocyte-az": 0.38923782536277735,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6759125288427181,
    "tdcommons/half-life-obach": -0.013855131577918888,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3110419172874421,
    "tdcommons/clearance-microsome-az": 0.5222740109981031,
    "tdcommons/dili": 0.8760869565217391,
    "tdcommons/bioavailability-ma": 0.5041569670768208,
    "tdcommons/vdss-lombardo": 0.4038858283277115,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6192359855334538,
    "tdcommons/pgp-broccatelli": 0.9171554252199413,
    "tdcommons/caco2-wang": 0.2928806125490966,
    "tdcommons/herg": 0.8343151693667158,
    "tdcommons/bbb-martins": 0.9102173233270795,
    "tdcommons/ames": 0.8515244081536744,
    "tdcommons/ld50-zhu": 0.6408995713039083
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.849057 |
|  1 | test       | CLS_RET        | pr_auc      | 0.458012 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.094984 |
|  3 | test       | CLS_RET        | mcc         | 0.223293 |
|  4 | test       | CLS_RET        | roc_auc     | 0.790482 |
|  5 | test       | CLS_RET        | f1          | 0.111111 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.53499  |
|  1 | test       | RET            | explained_var       |   0.286297 |
|  2 | test       | RET            | mean_absolute_error |  22.4866   |
|  3 | test       | RET            | mean_squared_error  | 865.675    |
|  4 | test       | RET            | pearsonr            |   0.535583 |
|  5 | test       | RET            | r2                  |   0.270952 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.801724 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.517977 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.235092 |
|  3 | test       | CLS_KIT        | mcc         | 0.246387 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.773694 |
|  5 | test       | CLS_KIT        | f1          | 0.342857 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.47587  |
|  1 | test       | KIT            | explained_var       |   0.231458 |
|  2 | test       | KIT            | mean_absolute_error |  24.234    |
|  3 | test       | KIT            | mean_squared_error  | 942.314    |
|  4 | test       | KIT            | pearsonr            |   0.501147 |
|  5 | test       | KIT            | r2                  |   0.219088 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.245232 |
|  1 | test       | EGFR           | explained_var       |   0.267548 |
|  2 | test       | EGFR           | mean_absolute_error |  19.6335   |
|  3 | test       | EGFR           | mean_squared_error  | 591.261    |
|  4 | test       | EGFR           | pearsonr            |   0.517465 |
|  5 | test       | EGFR           | r2                  |   0.266215 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.435997 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.296788 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.439194 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.381848 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.546152 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.295715 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.776522 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.511895 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.511441 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.442901 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.739944 |
|  5 | test       | LOG_RPPB       | r2                  | 0.501509 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.808771 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.66143  |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.409736 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.249523 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.822709 |
|  5 | test       | LOG_HPPB       | r2                  | 0.588    |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.733525 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.52215  |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.374409 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.236742 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.72261  |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.522113 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.677055 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.45951  |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.442323 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.30513  |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.678136 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.45951  |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.635948 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.372437 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.391094 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.245538 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.611033 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.367838 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.588548 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.68617 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.322263 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.567931 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.256296 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.338782 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.470859 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.886087 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.657133 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.478566 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.614263 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.914023 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.315882 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.846392 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.916667 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.85034 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.65425 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.4580115743121924,
    "polaris/pkis2-ret-wt-reg-v2": 865.6752603314901,
    "polaris/pkis2-kit-wt-cls-v2": 0.517976676831864,
    "polaris/pkis2-kit-wt-reg-v2": 942.3139942849077,
    "polaris/pkis2-egfr-wt-reg-v2": 591.2607360700024,
    "polaris/adme-fang-solu-1": 0.5461524081838374,
    "polaris/adme-fang-rppb-1": 0.7399443672990513,
    "polaris/adme-fang-hppb-1": 0.8227094381357859,
    "polaris/adme-fang-perm-1": 0.7226098352222453,
    "polaris/adme-fang-rclint-1": 0.6781355452436838,
    "polaris/adme-fang-hclint-1": 0.61103280885482,
    "tdcommons/lipophilicity-astrazeneca": 0.588548049739429,
    "tdcommons/ppbr-az": 8.68616824919508,
    "tdcommons/clearance-hepatocyte-az": 0.32226349620784583,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5679313553508274,
    "tdcommons/half-life-obach": 0.25629615326853755,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.33878215540375944,
    "tdcommons/clearance-microsome-az": 0.47085897787485237,
    "tdcommons/dili": 0.8860869565217391,
    "tdcommons/bioavailability-ma": 0.6571333555038243,
    "tdcommons/vdss-lombardo": 0.4785664825080439,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6142631103074142,
    "tdcommons/pgp-broccatelli": 0.9140229272194083,
    "tdcommons/caco2-wang": 0.3158816555181818,
    "tdcommons/herg": 0.8463917525773196,
    "tdcommons/bbb-martins": 0.9166666666666667,
    "tdcommons/ames": 0.8503397364350193,
    "tdcommons/ld50-zhu": 0.6542495073833389
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.858491 |
|  1 | test       | CLS_RET        | pr_auc      | 0.632699 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.288272 |
|  3 | test       | CLS_RET        | mcc         | 0.337956 |
|  4 | test       | CLS_RET        | roc_auc     | 0.849306 |
|  5 | test       | CLS_RET        | f1          | 0.347826 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.588257 |
|  1 | test       | RET            | explained_var       |   0.343496 |
|  2 | test       | RET            | mean_absolute_error |  21.8168   |
|  3 | test       | RET            | mean_squared_error  | 798.397    |
|  4 | test       | RET            | pearsonr            |   0.587225 |
|  5 | test       | RET            | r2                  |   0.327612 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.784483 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.439107 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.201542 |
|  3 | test       | CLS_KIT        | mcc         | 0.206776 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.757253 |
|  5 | test       | CLS_KIT        | f1          | 0.324324 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | spearmanr           |    0.416711 |
|  1 | test       | KIT            | explained_var       |    0.146952 |
|  2 | test       | KIT            | mean_absolute_error |   25.9589   |
|  3 | test       | KIT            | mean_squared_error  | 1042.82     |
|  4 | test       | KIT            | pearsonr            |    0.432615 |
|  5 | test       | KIT            | r2                  |    0.135797 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.299501 |
|  1 | test       | EGFR           | explained_var       |   0.273796 |
|  2 | test       | EGFR           | mean_absolute_error |  18.9074   |
|  3 | test       | EGFR           | mean_squared_error  | 586.289    |
|  4 | test       | EGFR           | pearsonr            |   0.528815 |
|  5 | test       | EGFR           | r2                  |   0.272386 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.445731 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.288177 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.441684 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.391269 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.538329 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.278339 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.850435 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.702317 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.396621 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.268513 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.874904 |
|  5 | test       | LOG_RPPB       | r2                  | 0.697785 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.784017 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.62243  |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.442394 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.264639 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.795646 |
|  5 | test       | LOG_HPPB       | r2                  | 0.563041 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.723086 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.518221 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.382375 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.239059 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.719888 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.517435 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.662933 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.436133 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.443854 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.319144 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.661129 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.434686 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.660092 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.396488 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.384731 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.23463  |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.6376   |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.395922 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.573688 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.80404 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.347427 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.626791 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |      Score |
|---:|:-----------|:---------------|:----------|-----------:|
|  0 | test       | Y              | spearmanr | -0.0427996 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.435626 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.526408 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.886957 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.566345 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.380917 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.605674 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.922487 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.301831 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.826657 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.916979 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.850831 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.641724 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6326987724850635,
    "polaris/pkis2-ret-wt-reg-v2": 798.3967005653739,
    "polaris/pkis2-kit-wt-cls-v2": 0.4391066281222707,
    "polaris/pkis2-kit-wt-reg-v2": 1042.8200264960271,
    "polaris/pkis2-egfr-wt-reg-v2": 586.2885029862828,
    "polaris/adme-fang-solu-1": 0.5383286682166071,
    "polaris/adme-fang-rppb-1": 0.8749038861928807,
    "polaris/adme-fang-hppb-1": 0.7956455237371255,
    "polaris/adme-fang-perm-1": 0.7198877867521483,
    "polaris/adme-fang-rclint-1": 0.6611286206986366,
    "polaris/adme-fang-hclint-1": 0.6375998672056499,
    "tdcommons/lipophilicity-astrazeneca": 0.5736876527581896,
    "tdcommons/ppbr-az": 8.804038585737906,
    "tdcommons/clearance-hepatocyte-az": 0.3474267756878841,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6267912214040464,
    "tdcommons/half-life-obach": -0.042799563658750414,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4356258656087307,
    "tdcommons/clearance-microsome-az": 0.5264081427967142,
    "tdcommons/dili": 0.8869565217391304,
    "tdcommons/bioavailability-ma": 0.5663451945460591,
    "tdcommons/vdss-lombardo": 0.3809170825090856,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6056735985533455,
    "tdcommons/pgp-broccatelli": 0.9224873367102107,
    "tdcommons/caco2-wang": 0.30183069004999535,
    "tdcommons/herg": 0.8266568483063328,
    "tdcommons/bbb-martins": 0.9169793621013131,
    "tdcommons/ames": 0.8508312283381309,
    "tdcommons/ld50-zhu": 0.6417235806030254
}
```
