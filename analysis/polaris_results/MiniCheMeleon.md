# ChemProp Baseline Results
timestamp: 2026-09-12 21:30:01.323179
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.356461 |
|  1 | test       | CLS_RET        | f1          | 0.416667 |
|  2 | test       | CLS_RET        | roc_auc     | 0.837409 |
|  3 | test       | CLS_RET        | mcc         | 0.40138  |
|  4 | test       | CLS_RET        | accuracy    | 0.867925 |
|  5 | test       | CLS_RET        | pr_auc      | 0.587922 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  22.6752   |
|  1 | test       | RET            | explained_var       |   0.305241 |
|  2 | test       | RET            | mean_squared_error  | 848.752    |
|  3 | test       | RET            | spearmanr           |   0.49164  |
|  4 | test       | RET            | pearsonr            |   0.556058 |
|  5 | test       | RET            | r2                  |   0.285204 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.349533 |
|  1 | test       | CLS_KIT        | f1          | 0.478261 |
|  2 | test       | CLS_KIT        | roc_auc     | 0.808511 |
|  3 | test       | CLS_KIT        | mcc         | 0.350047 |
|  4 | test       | CLS_KIT        | accuracy    | 0.793103 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.553749 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  22.9849   |
|  1 | test       | KIT            | explained_var       |   0.27773  |
|  2 | test       | KIT            | mean_squared_error  | 928.596    |
|  3 | test       | KIT            | spearmanr           |   0.528376 |
|  4 | test       | KIT            | pearsonr            |   0.537488 |
|  5 | test       | KIT            | r2                  |   0.230457 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  17.0979   |
|  1 | test       | EGFR           | explained_var       |   0.414181 |
|  2 | test       | EGFR           | mean_squared_error  | 475.979    |
|  3 | test       | EGFR           | spearmanr           |   0.319752 |
|  4 | test       | EGFR           | pearsonr            |   0.644911 |
|  5 | test       | EGFR           | r2                  |   0.409286 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.391799 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.37107  |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.344287 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.486679 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.609686 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.364993 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.728005  |
|  1 | test       | LOG_RPPB       | explained_var       | 0.12438   |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.804315  |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.44      |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.360545  |
|  5 | test       | LOG_RPPB       | r2                  | 0.0947311 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.466346 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.62487  |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.290476 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.778822 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.800926 |
|  5 | test       | LOG_HPPB       | r2                  | 0.520381 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.323572 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.58982  |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.204731 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.7548   |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.768074 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.586729 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.441453 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.461711 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.304009 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.682698 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.679703 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.461497 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.346777 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.472397 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.205321 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.716615 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.698888 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.471381 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.484193 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.81293 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.386453 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.534761 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.315724 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.428414 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.568951 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.914783 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.547389 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.257017 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.600023 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.915089 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.292434 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.883063 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.896087 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.824017 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.54826 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5879216162311376,
    "polaris/pkis2-ret-wt-reg-v2": 848.7518485331932,
    "polaris/pkis2-kit-wt-cls-v2": 0.5537492491788334,
    "polaris/pkis2-kit-wt-reg-v2": 928.5957339477199,
    "polaris/pkis2-egfr-wt-reg-v2": 475.979112739967,
    "polaris/adme-fang-solu-1": 0.6096860219869692,
    "polaris/adme-fang-rppb-1": 0.36054538586174345,
    "polaris/adme-fang-hppb-1": 0.8009255357865874,
    "polaris/adme-fang-perm-1": 0.7680737734457017,
    "polaris/adme-fang-rclint-1": 0.6797033554990869,
    "polaris/adme-fang-hclint-1": 0.6988877327571038,
    "tdcommons/lipophilicity-astrazeneca": 0.4841928087983812,
    "tdcommons/ppbr-az": 7.8129277060411475,
    "tdcommons/clearance-hepatocyte-az": 0.3864529189758436,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5347611822407122,
    "tdcommons/half-life-obach": 0.3157236849890042,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4284138793159131,
    "tdcommons/clearance-microsome-az": 0.5689513898327736,
    "tdcommons/dili": 0.9147826086956522,
    "tdcommons/bioavailability-ma": 0.5473894246757566,
    "tdcommons/vdss-lombardo": 0.25701651400585673,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6000226039783002,
    "tdcommons/pgp-broccatelli": 0.915089309517462,
    "tdcommons/caco2-wang": 0.29243413787117434,
    "tdcommons/herg": 0.8830633284241531,
    "tdcommons/bbb-martins": 0.8960873983739837,
    "tdcommons/ames": 0.8240165266600091,
    "tdcommons/ld50-zhu": 0.5482603346401363
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.567347 |
|  1 | test       | CLS_RET        | f1          | 0.615385 |
|  2 | test       | CLS_RET        | roc_auc     | 0.818903 |
|  3 | test       | CLS_RET        | mcc         | 0.604725 |
|  4 | test       | CLS_RET        | accuracy    | 0.90566  |
|  5 | test       | CLS_RET        | pr_auc      | 0.657096 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  23.3988   |
|  1 | test       | RET            | explained_var       |   0.276168 |
|  2 | test       | RET            | mean_squared_error  | 893.561    |
|  3 | test       | RET            | spearmanr           |   0.462303 |
|  4 | test       | RET            | pearsonr            |   0.540266 |
|  5 | test       | RET            | r2                  |   0.247468 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.436285 |
|  1 | test       | CLS_KIT        | f1          | 0.526316 |
|  2 | test       | CLS_KIT        | roc_auc     | 0.799807 |
|  3 | test       | CLS_KIT        | mcc         | 0.444197 |
|  4 | test       | CLS_KIT        | accuracy    | 0.844828 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.572973 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  22.3445   |
|  1 | test       | KIT            | explained_var       |   0.328548 |
|  2 | test       | KIT            | mean_squared_error  | 851.094    |
|  3 | test       | KIT            | spearmanr           |   0.583099 |
|  4 | test       | KIT            | pearsonr            |   0.578288 |
|  5 | test       | KIT            | r2                  |   0.294684 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  17.6564   |
|  1 | test       | EGFR           | explained_var       |   0.384761 |
|  2 | test       | EGFR           | mean_squared_error  | 501.075    |
|  3 | test       | EGFR           | spearmanr           |   0.239609 |
|  4 | test       | EGFR           | pearsonr            |   0.620326 |
|  5 | test       | EGFR           | r2                  |   0.37814  |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.404752 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.35019  |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.352694 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.503249 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.593443 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.349487 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.592677 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.311243 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.612396 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.646087 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.57152  |
|  5 | test       | LOG_RPPB       | r2                  | 0.310738 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.594413 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.272811 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.457447 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.708381 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.660914 |
|  5 | test       | LOG_HPPB       | r2                  | 0.244686 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.332756 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.589028 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.206017 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.751725 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.769282 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.584134 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.420607 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.48718  |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.29043  |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.706572 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.70398  |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.485549 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.351458 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.456139 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.211437 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.697764 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.692249 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.455635 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.481534 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.08608 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.446243 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.659194 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0016549 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.377431 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.635779 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.922174 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.432657 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.505237 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.597084 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.904159 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.336237 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.856112 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.912426 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.813605 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.605021 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.657096052738922,
    "polaris/pkis2-ret-wt-reg-v2": 893.5607893929142,
    "polaris/pkis2-kit-wt-cls-v2": 0.5729728194970835,
    "polaris/pkis2-kit-wt-reg-v2": 851.093628775115,
    "polaris/pkis2-egfr-wt-reg-v2": 501.07503112820655,
    "polaris/adme-fang-solu-1": 0.5934432306323822,
    "polaris/adme-fang-rppb-1": 0.5715198338256453,
    "polaris/adme-fang-hppb-1": 0.660914126745697,
    "polaris/adme-fang-perm-1": 0.7692823145054373,
    "polaris/adme-fang-rclint-1": 0.7039797220353476,
    "polaris/adme-fang-hclint-1": 0.6922492441899678,
    "tdcommons/lipophilicity-astrazeneca": 0.4815339542286737,
    "tdcommons/ppbr-az": 8.086077640649458,
    "tdcommons/clearance-hepatocyte-az": 0.4462428161420205,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6591938265683416,
    "tdcommons/half-life-obach": 0.0016549042952588152,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.37743113318433896,
    "tdcommons/clearance-microsome-az": 0.6357786060086038,
    "tdcommons/dili": 0.9221739130434782,
    "tdcommons/bioavailability-ma": 0.4326571333555039,
    "tdcommons/vdss-lombardo": 0.5052367681444508,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5970840867992767,
    "tdcommons/pgp-broccatelli": 0.9041588909624102,
    "tdcommons/caco2-wang": 0.33623745804590927,
    "tdcommons/herg": 0.8561119293078056,
    "tdcommons/bbb-martins": 0.9124257348342715,
    "tdcommons/ames": 0.8136051224813488,
    "tdcommons/ld50-zhu": 0.6050211293958682
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.394286 |
|  1 | test       | CLS_RET        | f1          | 0.461538 |
|  2 | test       | CLS_RET        | roc_auc     | 0.797753 |
|  3 | test       | CLS_RET        | mcc         | 0.420262 |
|  4 | test       | CLS_RET        | accuracy    | 0.867925 |
|  5 | test       | CLS_RET        | pr_auc      | 0.593606 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  22.2152   |
|  1 | test       | RET            | explained_var       |   0.353473 |
|  2 | test       | RET            | mean_squared_error  | 770.726    |
|  3 | test       | RET            | spearmanr           |   0.521139 |
|  4 | test       | RET            | pearsonr            |   0.598631 |
|  5 | test       | RET            | r2                  |   0.350916 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.436285 |
|  1 | test       | CLS_KIT        | f1          | 0.526316 |
|  2 | test       | CLS_KIT        | roc_auc     | 0.82205  |
|  3 | test       | CLS_KIT        | mcc         | 0.444197 |
|  4 | test       | CLS_KIT        | accuracy    | 0.844828 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.557473 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  22.7073   |
|  1 | test       | KIT            | explained_var       |   0.281938 |
|  2 | test       | KIT            | mean_squared_error  | 881.239    |
|  3 | test       | KIT            | spearmanr           |   0.543217 |
|  4 | test       | KIT            | pearsonr            |   0.547253 |
|  5 | test       | KIT            | r2                  |   0.269702 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  16.8743   |
|  1 | test       | EGFR           | explained_var       |   0.429162 |
|  2 | test       | EGFR           | mean_squared_error  | 460.818    |
|  3 | test       | EGFR           | spearmanr           |   0.273654 |
|  4 | test       | EGFR           | pearsonr            |   0.666004 |
|  5 | test       | EGFR           | r2                  |   0.428101 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.398564 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.332594 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.363569 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.49883  |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.57935  |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.32943  |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.583728 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.263988 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.654244 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.638261 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.519005 |
|  5 | test       | LOG_RPPB       | r2                  | 0.263638 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.686598   |
|  1 | test       | LOG_HPPB       | explained_var       | 0.0929224  |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.601919   |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.694629   |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.671955   |
|  5 | test       | LOG_HPPB       | r2                  | 0.00614147 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.321485 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.599448 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.198858 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.771957 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.775575 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.598586 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.430394 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.484711 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.292162 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.696833 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.696401 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.482481 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.41273  |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.334577 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.259492 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.574787 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.580487 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.331911 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.467947 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.98752 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.379429 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.604225 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.203298 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.396129 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.581868 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.922609 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.543066 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.375707 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.559109 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.910357 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.319113 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.866716 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.901149 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.844718 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.627841 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.593606035475155,
    "polaris/pkis2-ret-wt-reg-v2": 770.7256166407669,
    "polaris/pkis2-kit-wt-cls-v2": 0.5574731595109661,
    "polaris/pkis2-kit-wt-reg-v2": 881.2385786197012,
    "polaris/pkis2-egfr-wt-reg-v2": 460.8184563569982,
    "polaris/adme-fang-solu-1": 0.5793504455667515,
    "polaris/adme-fang-rppb-1": 0.5190053978798808,
    "polaris/adme-fang-hppb-1": 0.6719549649248788,
    "polaris/adme-fang-perm-1": 0.7755746942680591,
    "polaris/adme-fang-rclint-1": 0.6964014501426101,
    "polaris/adme-fang-hclint-1": 0.580487441342125,
    "tdcommons/lipophilicity-astrazeneca": 0.4679473296063287,
    "tdcommons/ppbr-az": 7.987520286273444,
    "tdcommons/clearance-hepatocyte-az": 0.3794293849528696,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6042250094692814,
    "tdcommons/half-life-obach": 0.20329834622567058,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3961287584770313,
    "tdcommons/clearance-microsome-az": 0.5818684815364049,
    "tdcommons/dili": 0.922608695652174,
    "tdcommons/bioavailability-ma": 0.5430661789158631,
    "tdcommons/vdss-lombardo": 0.37570737762456374,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5591094032549729,
    "tdcommons/pgp-broccatelli": 0.910357238069848,
    "tdcommons/caco2-wang": 0.31911269558487787,
    "tdcommons/herg": 0.8667157584683357,
    "tdcommons/bbb-martins": 0.9011491557223265,
    "tdcommons/ames": 0.8447179306428557,
    "tdcommons/ld50-zhu": 0.6278410139341961
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.591365 |
|  1 | test       | CLS_RET        | f1          | 0.642857 |
|  2 | test       | CLS_RET        | roc_auc     | 0.840053 |
|  3 | test       | CLS_RET        | mcc         | 0.609983 |
|  4 | test       | CLS_RET        | accuracy    | 0.90566  |
|  5 | test       | CLS_RET        | pr_auc      | 0.649847 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  22.8765   |
|  1 | test       | RET            | explained_var       |   0.317085 |
|  2 | test       | RET            | mean_squared_error  | 821.945    |
|  3 | test       | RET            | spearmanr           |   0.429549 |
|  4 | test       | RET            | pearsonr            |   0.563226 |
|  5 | test       | RET            | r2                  |   0.30778  |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.45625  |
|  1 | test       | CLS_KIT        | f1          | 0.516129 |
|  2 | test       | CLS_KIT        | roc_auc     | 0.851547 |
|  3 | test       | CLS_KIT        | mcc         | 0.51729  |
|  4 | test       | CLS_KIT        | accuracy    | 0.87069  |
|  5 | test       | CLS_KIT        | pr_auc      | 0.719934 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  22.3439   |
|  1 | test       | KIT            | explained_var       |   0.322556 |
|  2 | test       | KIT            | mean_squared_error  | 874.317    |
|  3 | test       | KIT            | spearmanr           |   0.552667 |
|  4 | test       | KIT            | pearsonr            |   0.576803 |
|  5 | test       | KIT            | r2                  |   0.275438 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  18.8522   |
|  1 | test       | EGFR           | explained_var       |   0.314945 |
|  2 | test       | EGFR           | mean_squared_error  | 552.002    |
|  3 | test       | EGFR           | spearmanr           |   0.18787  |
|  4 | test       | EGFR           | pearsonr            |   0.567085 |
|  5 | test       | EGFR           | r2                  |   0.314938 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.392723 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.348048 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.355402 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.511361 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.591327 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.344493 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.625372 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.216596 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.69979  |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.58087  |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.465428 |
|  5 | test       | LOG_RPPB       | r2                  | 0.212376 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.479458 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.611801 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.322084 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.789824 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.785304 |
|  5 | test       | LOG_HPPB       | r2                  | 0.468191 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.33686  |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.575081 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.211695 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.751024 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.758349 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.572673 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.415025 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.523262 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.269712 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.727024 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.723408 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.522247 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.341544 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.467349 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.207095 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.703195 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.693233 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.466813 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.503028 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.03803 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.367847 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.534531 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0846893 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.376354 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.581237 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.910435 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.574659 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.399794 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.607369 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.913823 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.30841 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.855965 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.899038 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.84162 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.612009 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6498472605825547,
    "polaris/pkis2-ret-wt-reg-v2": 821.9450866421943,
    "polaris/pkis2-kit-wt-cls-v2": 0.7199342934282282,
    "polaris/pkis2-kit-wt-reg-v2": 874.3174610700343,
    "polaris/pkis2-egfr-wt-reg-v2": 552.0016043250585,
    "polaris/adme-fang-solu-1": 0.5913267855527102,
    "polaris/adme-fang-rppb-1": 0.4654276367635416,
    "polaris/adme-fang-hppb-1": 0.7853040136097318,
    "polaris/adme-fang-perm-1": 0.7583491135466943,
    "polaris/adme-fang-rclint-1": 0.7234078484325919,
    "polaris/adme-fang-hclint-1": 0.6932333828307421,
    "tdcommons/lipophilicity-astrazeneca": 0.5030278062139238,
    "tdcommons/ppbr-az": 8.038025731067965,
    "tdcommons/clearance-hepatocyte-az": 0.3678467689017376,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5345306033316856,
    "tdcommons/half-life-obach": 0.08468925130220445,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3763536824916023,
    "tdcommons/clearance-microsome-az": 0.5812366219524217,
    "tdcommons/dili": 0.9104347826086956,
    "tdcommons/bioavailability-ma": 0.5746591286997007,
    "tdcommons/vdss-lombardo": 0.3997939357801636,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.607368896925859,
    "tdcommons/pgp-broccatelli": 0.913822980538523,
    "tdcommons/caco2-wang": 0.3084104545906487,
    "tdcommons/herg": 0.8559646539027982,
    "tdcommons/bbb-martins": 0.8990384615384615,
    "tdcommons/ames": 0.8416201609587028,
    "tdcommons/ld50-zhu": 0.612008856421072
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.660498 |
|  1 | test       | CLS_RET        | f1          | 0.709677 |
|  2 | test       | CLS_RET        | roc_auc     | 0.842036 |
|  3 | test       | CLS_RET        | mcc         | 0.664769 |
|  4 | test       | CLS_RET        | accuracy    | 0.915094 |
|  5 | test       | CLS_RET        | pr_auc      | 0.754161 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  23.7048   |
|  1 | test       | RET            | explained_var       |   0.241614 |
|  2 | test       | RET            | mean_squared_error  | 936.055    |
|  3 | test       | RET            | spearmanr           |   0.494495 |
|  4 | test       | RET            | pearsonr            |   0.491615 |
|  5 | test       | RET            | r2                  |   0.21168  |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.434633 |
|  1 | test       | CLS_KIT        | f1          | 0.514286 |
|  2 | test       | CLS_KIT        | roc_auc     | 0.837524 |
|  3 | test       | CLS_KIT        | mcc         | 0.455516 |
|  4 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.585324 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  22.4571   |
|  1 | test       | KIT            | explained_var       |   0.319231 |
|  2 | test       | KIT            | mean_squared_error  | 885.98     |
|  3 | test       | KIT            | spearmanr           |   0.532505 |
|  4 | test       | KIT            | pearsonr            |   0.566671 |
|  5 | test       | KIT            | r2                  |   0.265773 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  17.5885   |
|  1 | test       | EGFR           | explained_var       |   0.347659 |
|  2 | test       | EGFR           | mean_squared_error  | 532.958    |
|  3 | test       | EGFR           | spearmanr           |   0.291637 |
|  4 | test       | EGFR           | pearsonr            |   0.594357 |
|  5 | test       | EGFR           | r2                  |   0.338571 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.391161 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.378434 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.342328 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.510585 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.6152   |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.368607 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.591642 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.278584 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.642167 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.646087 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.52845  |
|  5 | test       | LOG_RPPB       | r2                  | 0.277231 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.546686 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.559008 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.423668 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.788754 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.747716 |
|  5 | test       | LOG_HPPB       | r2                  | 0.300461 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.316044 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.603149 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.196751 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.761684 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.778949 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.602839 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.406045 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.535787 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.263232 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.739395 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.7323   |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.533726 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.350777 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.463081 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.2092   |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.694886 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.688495 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.461393 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.466123 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.23842 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.387905 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.571996 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.09112 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.420126 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.585415 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.936957 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.417359 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.409459 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.670208 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.912957 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.306212 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.864507 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.886335 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.830324 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.640766 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7541610510468642,
    "polaris/pkis2-ret-wt-reg-v2": 936.0550464614716,
    "polaris/pkis2-kit-wt-cls-v2": 0.585324413766155,
    "polaris/pkis2-kit-wt-reg-v2": 885.9800075890632,
    "polaris/pkis2-egfr-wt-reg-v2": 532.9582679218188,
    "polaris/adme-fang-solu-1": 0.615200150383932,
    "polaris/adme-fang-rppb-1": 0.5284504492891114,
    "polaris/adme-fang-hppb-1": 0.7477164947942737,
    "polaris/adme-fang-perm-1": 0.7789487187895126,
    "polaris/adme-fang-rclint-1": 0.7323002060377831,
    "polaris/adme-fang-hclint-1": 0.6884948412853092,
    "tdcommons/lipophilicity-astrazeneca": 0.46612278363250553,
    "tdcommons/ppbr-az": 8.238415664099625,
    "tdcommons/clearance-hepatocyte-az": 0.3879054608443347,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5719963606986653,
    "tdcommons/half-life-obach": 0.09111996004817935,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4201261105477827,
    "tdcommons/clearance-microsome-az": 0.5854153480127536,
    "tdcommons/dili": 0.9369565217391305,
    "tdcommons/bioavailability-ma": 0.41735949451280346,
    "tdcommons/vdss-lombardo": 0.4094591599579166,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6702079566003617,
    "tdcommons/pgp-broccatelli": 0.9129565449213544,
    "tdcommons/caco2-wang": 0.3062124525835981,
    "tdcommons/herg": 0.8645066273932254,
    "tdcommons/bbb-martins": 0.8863352095059412,
    "tdcommons/ames": 0.8303236797274277,
    "tdcommons/ld50-zhu": 0.6407657446777385
}
```
