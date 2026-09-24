# ChemProp Baseline Results
timestamp: 2026-09-23 18:25:40.450265
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.836087 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.313599 |
|  2 | test       | CLS_RET        | mcc         | 0.387824 |
|  3 | test       | CLS_RET        | f1          | 0.363636 |
|  4 | test       | CLS_RET        | pr_auc      | 0.645247 |
|  5 | test       | CLS_RET        | accuracy    | 0.867925 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.445253 |
|  1 | test       | RET            | mean_squared_error  | 962.876    |
|  2 | test       | RET            | pearsonr            |   0.444084 |
|  3 | test       | RET            | r2                  |   0.189093 |
|  4 | test       | RET            | mean_absolute_error |  24.5864   |
|  5 | test       | RET            | explained_var       |   0.192506 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.783366 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.329295 |
|  2 | test       | CLS_KIT        | mcc         | 0.337847 |
|  3 | test       | CLS_KIT        | f1          | 0.432432 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.530154 |
|  5 | test       | CLS_KIT        | accuracy    | 0.818966 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.471526 |
|  1 | test       | KIT            | mean_squared_error  | 908.607    |
|  2 | test       | KIT            | pearsonr            |   0.534514 |
|  3 | test       | KIT            | r2                  |   0.247021 |
|  4 | test       | KIT            | mean_absolute_error |  23.2947   |
|  5 | test       | KIT            | explained_var       |   0.259227 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.330364 |
|  1 | test       | EGFR           | mean_squared_error  | 476.847    |
|  2 | test       | EGFR           | pearsonr            |   0.641713 |
|  3 | test       | EGFR           | r2                  |   0.408209 |
|  4 | test       | EGFR           | mean_absolute_error |  16.7898   |
|  5 | test       | EGFR           | explained_var       |   0.408519 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.534937 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.337246 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.6353   |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.377981 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.382605 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.378034 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | LOG_RPPB       | spearmanr           |  0.405217  |
|  1 | test       | LOG_RPPB       | mean_squared_error  |  0.918236  |
|  2 | test       | LOG_RPPB       | pearsonr            |  0.254261  |
|  3 | test       | LOG_RPPB       | r2                  | -0.0334891 |
|  4 | test       | LOG_RPPB       | mean_absolute_error |  0.671159  |
|  5 | test       | LOG_RPPB       | explained_var       | -0.0216829 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.615326 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.387401 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.628875 |
|  3 | test       | LOG_HPPB       | r2                  | 0.360342 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.521291 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.375757 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.779718 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.198843 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.77548  |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.598616 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.334793 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.600196 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.727191 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.271079 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.722035 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.519825 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.413654 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.520226 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.71667  |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.217026 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.693135 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.441245 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.354481 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.441404 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.451915 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.94491 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.406764 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.661369 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.160702 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.396682 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.520033 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.92087 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.565015 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0533099 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.555041 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.909224 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.33338 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.838733 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.876388 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.82982 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.656664 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6452466996786328,
    "polaris/pkis2-ret-wt-reg-v2": 962.8756642869636,
    "polaris/pkis2-kit-wt-cls-v2": 0.5301538804593855,
    "polaris/pkis2-kit-wt-reg-v2": 908.6073778619044,
    "polaris/pkis2-egfr-wt-reg-v2": 476.846826845793,
    "polaris/adme-fang-solu-1": 0.6353003283016025,
    "polaris/adme-fang-rppb-1": 0.25426072539965733,
    "polaris/adme-fang-hppb-1": 0.6288750988651445,
    "polaris/adme-fang-perm-1": 0.7754797475767975,
    "polaris/adme-fang-rclint-1": 0.7220345360249449,
    "polaris/adme-fang-hclint-1": 0.6931352716613411,
    "tdcommons/lipophilicity-astrazeneca": 0.45191471228145413,
    "tdcommons/ppbr-az": 7.9449110139631856,
    "tdcommons/clearance-hepatocyte-az": 0.40676427613081856,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6613685394939343,
    "tdcommons/half-life-obach": 0.16070152514033448,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3966824004462237,
    "tdcommons/clearance-microsome-az": 0.5200333826663572,
    "tdcommons/dili": 0.9208695652173913,
    "tdcommons/bioavailability-ma": 0.5650149650814765,
    "tdcommons/vdss-lombardo": 0.05330987822160589,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5550406871609403,
    "tdcommons/pgp-broccatelli": 0.9092242068781659,
    "tdcommons/caco2-wang": 0.333379725957749,
    "tdcommons/herg": 0.8387334315169367,
    "tdcommons/bbb-martins": 0.8763875859912444,
    "tdcommons/ames": 0.8298204390138832,
    "tdcommons/ld50-zhu": 0.6566635424261649
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.827495 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.567347 |
|  2 | test       | CLS_RET        | mcc         | 0.604725 |
|  3 | test       | CLS_RET        | f1          | 0.615385 |
|  4 | test       | CLS_RET        | pr_auc      | 0.706061 |
|  5 | test       | CLS_RET        | accuracy    | 0.90566  |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.532449 |
|  1 | test       | RET            | mean_squared_error  | 865.44     |
|  2 | test       | RET            | pearsonr            |   0.561938 |
|  3 | test       | RET            | r2                  |   0.27115  |
|  4 | test       | RET            | mean_absolute_error |  22.4782   |
|  5 | test       | RET            | explained_var       |   0.307738 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.826886 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.477754 |
|  2 | test       | CLS_KIT        | mcc         | 0.483492 |
|  3 | test       | CLS_KIT        | f1          | 0.564103 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.675007 |
|  5 | test       | CLS_KIT        | accuracy    | 0.853448 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.48405  |
|  1 | test       | KIT            | mean_squared_error  | 923.835    |
|  2 | test       | KIT            | pearsonr            |   0.53736  |
|  3 | test       | KIT            | r2                  |   0.234402 |
|  4 | test       | KIT            | mean_absolute_error |  22.9824   |
|  5 | test       | KIT            | explained_var       |   0.241301 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.213667 |
|  1 | test       | EGFR           | mean_squared_error  | 500.071    |
|  2 | test       | EGFR           | pearsonr            |   0.618952 |
|  3 | test       | EGFR           | r2                  |   0.379386 |
|  4 | test       | EGFR           | mean_absolute_error |  17.488    |
|  5 | test       | EGFR           | explained_var       |   0.383023 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.560135 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.312077 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.669281 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.424401 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.373593 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.43733  |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.66087  |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.65192  |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.518486 |
|  3 | test       | LOG_RPPB       | r2                  | 0.266254 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.586963 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.266485 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.583849 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.499292 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.553173 |
|  3 | test       | LOG_HPPB       | r2                  | 0.175594 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.633197 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.24712  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.773364 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.204207 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.772591 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.587787 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.346144 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.596896 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.740534 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.266295 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.730633 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.528301 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.409093 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.529221 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.697766 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.20723  |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.685241 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.466466 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.357562 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.466712 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.470294 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.83562 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.406919 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.708457 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.159401 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.386487 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.613924 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.90087 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.558696 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.532041 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.561596 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.895095 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.321077 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.838292 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.896498 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.840721 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.59944 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7060612329693136,
    "polaris/pkis2-ret-wt-reg-v2": 865.4396364759659,
    "polaris/pkis2-kit-wt-cls-v2": 0.6750072593136464,
    "polaris/pkis2-kit-wt-reg-v2": 923.8347442584758,
    "polaris/pkis2-egfr-wt-reg-v2": 500.0710884118781,
    "polaris/adme-fang-solu-1": 0.6692814681375314,
    "polaris/adme-fang-rppb-1": 0.5184858660032465,
    "polaris/adme-fang-hppb-1": 0.5531731577681069,
    "polaris/adme-fang-perm-1": 0.7725905102601988,
    "polaris/adme-fang-rclint-1": 0.7306332920548985,
    "polaris/adme-fang-hclint-1": 0.6852411080788532,
    "tdcommons/lipophilicity-astrazeneca": 0.4702944407633373,
    "tdcommons/ppbr-az": 7.835619096568318,
    "tdcommons/clearance-hepatocyte-az": 0.40691881572696476,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7084573484667253,
    "tdcommons/half-life-obach": 0.15940130856329693,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.38648659945915453,
    "tdcommons/clearance-microsome-az": 0.6139240825520111,
    "tdcommons/dili": 0.9008695652173913,
    "tdcommons/bioavailability-ma": 0.5586963751247089,
    "tdcommons/vdss-lombardo": 0.532041438612007,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5615958408679927,
    "tdcommons/pgp-broccatelli": 0.8950946414289523,
    "tdcommons/caco2-wang": 0.3210768719018622,
    "tdcommons/herg": 0.8382916053019146,
    "tdcommons/bbb-martins": 0.8964978111319575,
    "tdcommons/ames": 0.8407213769605828,
    "tdcommons/ld50-zhu": 0.5994395608321256
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.864508 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.356461 |
|  2 | test       | CLS_RET        | mcc         | 0.40138  |
|  3 | test       | CLS_RET        | f1          | 0.416667 |
|  4 | test       | CLS_RET        | pr_auc      | 0.659848 |
|  5 | test       | CLS_RET        | accuracy    | 0.867925 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.552253 |
|  1 | test       | RET            | mean_squared_error  | 787.925    |
|  2 | test       | RET            | pearsonr            |   0.582415 |
|  3 | test       | RET            | r2                  |   0.336431 |
|  4 | test       | RET            | mean_absolute_error |  22.4048   |
|  5 | test       | RET            | explained_var       |   0.339057 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.823985 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.517672 |
|  2 | test       | CLS_KIT        | mcc         | 0.521477 |
|  3 | test       | CLS_KIT        | f1          | 0.6      |
|  4 | test       | CLS_KIT        | pr_auc      | 0.653638 |
|  5 | test       | CLS_KIT        | accuracy    | 0.862069 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | spearmanr           |    0.447035 |
|  1 | test       | KIT            | mean_squared_error  | 1006.25     |
|  2 | test       | KIT            | pearsonr            |    0.516904 |
|  3 | test       | KIT            | r2                  |    0.166101 |
|  4 | test       | KIT            | mean_absolute_error |   23.9264   |
|  5 | test       | KIT            | explained_var       |    0.172077 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.290323 |
|  1 | test       | EGFR           | mean_squared_error  | 441.131    |
|  2 | test       | EGFR           | pearsonr            |   0.675565 |
|  3 | test       | EGFR           | r2                  |   0.452534 |
|  4 | test       | EGFR           | mean_absolute_error |  16.4966   |
|  5 | test       | EGFR           | explained_var       |   0.452534 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.493272 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.347371 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.610246 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.359305 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.394595 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.369934 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.61913  |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.60377  |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.569425 |
|  3 | test       | LOG_RPPB       | r2                  | 0.320448 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.522869 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.324106 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.67614  |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.452472 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.67215  |
|  3 | test       | LOG_HPPB       | r2                  | 0.252901 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.602901 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.354576 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.78804  |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.193292 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.788243 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.609821 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.338976 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.621135 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.708936 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.282281 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.709173 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.499983 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.419811 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.500566 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.695327 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.221708 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.687391 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.429191 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.373418 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.433402 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.477989 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.65032 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.39576 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.609128 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.212247 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.386244 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.560742 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.925217 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.528101 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.526146 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.553458 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.916689 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.367471 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.817968 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.901188 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.826333 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.612106 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6598484093113275,
    "polaris/pkis2-ret-wt-reg-v2": 787.9250609603664,
    "polaris/pkis2-kit-wt-cls-v2": 0.6536375313344734,
    "polaris/pkis2-kit-wt-reg-v2": 1006.2530378193493,
    "polaris/pkis2-egfr-wt-reg-v2": 441.13059778181764,
    "polaris/adme-fang-solu-1": 0.6102463032030546,
    "polaris/adme-fang-rppb-1": 0.5694249777644748,
    "polaris/adme-fang-hppb-1": 0.6721495529974643,
    "polaris/adme-fang-perm-1": 0.7882425701472049,
    "polaris/adme-fang-rclint-1": 0.7091732931563107,
    "polaris/adme-fang-hclint-1": 0.687390756583515,
    "tdcommons/lipophilicity-astrazeneca": 0.47798870691231315,
    "tdcommons/ppbr-az": 7.65032104464891,
    "tdcommons/clearance-hepatocyte-az": 0.395760228978629,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.609127764958357,
    "tdcommons/half-life-obach": 0.2122465667361522,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.38624441308773577,
    "tdcommons/clearance-microsome-az": 0.5607423723074699,
    "tdcommons/dili": 0.9252173913043478,
    "tdcommons/bioavailability-ma": 0.5281010974393082,
    "tdcommons/vdss-lombardo": 0.5261456249644441,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5534584086799277,
    "tdcommons/pgp-broccatelli": 0.9166888829645428,
    "tdcommons/caco2-wang": 0.367471475759284,
    "tdcommons/herg": 0.8179675994108984,
    "tdcommons/bbb-martins": 0.9011882426516573,
    "tdcommons/ames": 0.8263330004503711,
    "tdcommons/ld50-zhu": 0.6121058016468611
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.857898 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.509672 |
|  2 | test       | CLS_RET        | mcc         | 0.55641  |
|  3 | test       | CLS_RET        | f1          | 0.56     |
|  4 | test       | CLS_RET        | pr_auc      | 0.685982 |
|  5 | test       | CLS_RET        | accuracy    | 0.896226 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.55449  |
|  1 | test       | RET            | mean_squared_error  | 681.32     |
|  2 | test       | RET            | pearsonr            |   0.65647  |
|  3 | test       | RET            | r2                  |   0.426211 |
|  4 | test       | RET            | mean_absolute_error |  20.6688   |
|  5 | test       | RET            | explained_var       |   0.430217 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.831238 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.388759 |
|  2 | test       | CLS_KIT        | mcc         | 0.413319 |
|  3 | test       | CLS_KIT        | f1          | 0.470588 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.644122 |
|  5 | test       | CLS_KIT        | accuracy    | 0.844828 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.561729 |
|  1 | test       | KIT            | mean_squared_error  | 899.62     |
|  2 | test       | KIT            | pearsonr            |   0.593743 |
|  3 | test       | KIT            | r2                  |   0.254469 |
|  4 | test       | KIT            | mean_absolute_error |  21.7209   |
|  5 | test       | KIT            | explained_var       |   0.346044 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.278888 |
|  1 | test       | EGFR           | mean_squared_error  | 468.347    |
|  2 | test       | EGFR           | pearsonr            |   0.654704 |
|  3 | test       | EGFR           | r2                  |   0.418757 |
|  4 | test       | EGFR           | mean_absolute_error |  17.01     |
|  5 | test       | EGFR           | explained_var       |   0.420566 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.52511  |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.33101  |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.624934 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.389482 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.391665 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.389626 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.586957 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.730948 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.426148 |
|  3 | test       | LOG_RPPB       | r2                  | 0.177307 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.618429 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.178029 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.697227 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.432829 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.705955 |
|  3 | test       | LOG_HPPB       | r2                  | 0.285334 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.49837  |
|  5 | test       | LOG_HPPB       | explained_var       | 0.328306 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.729216 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.234287 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.726122 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.527068 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.372447 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.527229 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.725662 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.272455 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.719806 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.517389 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.413326 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.518039 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.71909  |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.199416 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.710767 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.486584 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.344305 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.486644 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.466599 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.81154 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.380039 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.52855 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.112433 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.395186 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.638168 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.906522 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.47988 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.463197 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.574254 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.902293 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.311551 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.82975 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.886765 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.827954 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.608068 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6859822828328417,
    "polaris/pkis2-ret-wt-reg-v2": 681.3202595216471,
    "polaris/pkis2-kit-wt-cls-v2": 0.6441223793840554,
    "polaris/pkis2-kit-wt-reg-v2": 899.6201750722564,
    "polaris/pkis2-egfr-wt-reg-v2": 468.3471292442095,
    "polaris/adme-fang-solu-1": 0.6249342691797761,
    "polaris/adme-fang-rppb-1": 0.4261479462208255,
    "polaris/adme-fang-hppb-1": 0.7059551242134533,
    "polaris/adme-fang-perm-1": 0.7261223561772816,
    "polaris/adme-fang-rclint-1": 0.7198059081452497,
    "polaris/adme-fang-hclint-1": 0.71076694616588,
    "tdcommons/lipophilicity-astrazeneca": 0.4665991413820358,
    "tdcommons/ppbr-az": 7.811540451732218,
    "tdcommons/clearance-hepatocyte-az": 0.3800392198071974,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5285503058871255,
    "tdcommons/half-life-obach": 0.11243349049159264,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.39518566769134017,
    "tdcommons/clearance-microsome-az": 0.6381675745596274,
    "tdcommons/dili": 0.9065217391304348,
    "tdcommons/bioavailability-ma": 0.47988027934818756,
    "tdcommons/vdss-lombardo": 0.46319654263735754,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.574254068716094,
    "tdcommons/pgp-broccatelli": 0.9022927219408158,
    "tdcommons/caco2-wang": 0.31155110712957707,
    "tdcommons/herg": 0.8297496318114875,
    "tdcommons/bbb-martins": 0.8867651657285803,
    "tdcommons/ames": 0.8279543362901174,
    "tdcommons/ld50-zhu": 0.6080675273244855
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.795109 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.483121 |
|  2 | test       | CLS_RET        | mcc         | 0.49296  |
|  3 | test       | CLS_RET        | f1          | 0.551724 |
|  4 | test       | CLS_RET        | pr_auc      | 0.647247 |
|  5 | test       | CLS_RET        | accuracy    | 0.877358 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.499826 |
|  1 | test       | RET            | mean_squared_error  | 929.452    |
|  2 | test       | RET            | pearsonr            |   0.51869  |
|  3 | test       | RET            | r2                  |   0.217241 |
|  4 | test       | RET            | mean_absolute_error |  23.272    |
|  5 | test       | RET            | explained_var       |   0.268097 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.807544 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.432763 |
|  2 | test       | CLS_KIT        | mcc         | 0.478195 |
|  3 | test       | CLS_KIT        | f1          | 0.5      |
|  4 | test       | CLS_KIT        | pr_auc      | 0.633042 |
|  5 | test       | CLS_KIT        | accuracy    | 0.862069 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.499507 |
|  1 | test       | KIT            | mean_squared_error  | 888.091    |
|  2 | test       | KIT            | pearsonr            |   0.561212 |
|  3 | test       | KIT            | r2                  |   0.264024 |
|  4 | test       | KIT            | mean_absolute_error |  21.9952   |
|  5 | test       | KIT            | explained_var       |   0.286495 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.317787 |
|  1 | test       | EGFR           | mean_squared_error  | 515.254    |
|  2 | test       | EGFR           | pearsonr            |   0.623329 |
|  3 | test       | EGFR           | r2                  |   0.360543 |
|  4 | test       | EGFR           | mean_absolute_error |  18.3179   |
|  5 | test       | EGFR           | explained_var       |   0.371382 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.512262 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.335186 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.629886 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.38178  |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.389269 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.396755 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.615652 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.738769 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.479564 |
|  3 | test       | LOG_RPPB       | r2                  | 0.168504 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.690433 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.226736 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.679349 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.402602 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.66205  |
|  3 | test       | LOG_HPPB       | r2                  | 0.335244 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.536028 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.431606 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.773837 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.192415 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.783852 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.611591 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.32964  |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.614263 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.725453 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.273274 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.723225 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.515937 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.412323 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.516171 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.718547 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.209391 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.698006 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.460902 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.347553 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.465775 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.443325 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.21657 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.370596 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.679846 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.109489 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.447991 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.645709 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.912174 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.511806 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0123307 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.643422 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.91129 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.34995 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.823711 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.901579 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.832519 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.613876 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6472465799237322,
    "polaris/pkis2-ret-wt-reg-v2": 929.4524172680177,
    "polaris/pkis2-kit-wt-cls-v2": 0.6330420954056205,
    "polaris/pkis2-kit-wt-reg-v2": 888.0910129646481,
    "polaris/pkis2-egfr-wt-reg-v2": 515.2544853355547,
    "polaris/adme-fang-solu-1": 0.6298856279925125,
    "polaris/adme-fang-rppb-1": 0.4795640121759921,
    "polaris/adme-fang-hppb-1": 0.6620499788432251,
    "polaris/adme-fang-perm-1": 0.7838518416112019,
    "polaris/adme-fang-rclint-1": 0.7232246697311424,
    "polaris/adme-fang-hclint-1": 0.6980060257048671,
    "tdcommons/lipophilicity-astrazeneca": 0.44332472691081815,
    "tdcommons/ppbr-az": 8.216566660544954,
    "tdcommons/clearance-hepatocyte-az": 0.3705963412757768,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6798463263424821,
    "tdcommons/half-life-obach": 0.1094885888508036,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.44799126521025034,
    "tdcommons/clearance-microsome-az": 0.6457086560825476,
    "tdcommons/dili": 0.9121739130434783,
    "tdcommons/bioavailability-ma": 0.5118057864981709,
    "tdcommons/vdss-lombardo": 0.01233067741304109,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6434222423146474,
    "tdcommons/pgp-broccatelli": 0.9112903225806451,
    "tdcommons/caco2-wang": 0.3499495337669625,
    "tdcommons/herg": 0.8237113402061855,
    "tdcommons/bbb-martins": 0.9015791119449656,
    "tdcommons/ames": 0.8325187491433159,
    "tdcommons/ld50-zhu": 0.6138759198479143
}
```
