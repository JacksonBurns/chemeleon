# `molclr` Results
timestamp: 2025-05-28 21:32:51.628831

## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |     Score |
|---:|:-----------|:---------------|:------------|----------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.709187  |
|  1 | test       | CLS_RET        | f1          | 0.105263  |
|  2 | test       | CLS_RET        | mcc         | 0.128346  |
|  3 | test       | CLS_RET        | cohen_kappa | 0.0739979 |
|  4 | test       | CLS_RET        | pr_auc      | 0.421467  |
|  5 | test       | CLS_RET        | accuracy    | 0.839623  |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | RET            | r2                  |    0.0810802 |
|  1 | test       | RET            | pearsonr            |    0.325474  |
|  2 | test       | RET            | spearmanr           |    0.2748    |
|  3 | test       | RET            | mean_squared_error  | 1091.13      |
|  4 | test       | RET            | explained_var       |    0.0834155 |
|  5 | test       | RET            | mean_absolute_error |   27.2925    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |     Score |
|---:|:-----------|:---------------|:------------|----------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.634913  |
|  1 | test       | CLS_KIT        | f1          | 0.142857  |
|  2 | test       | CLS_KIT        | mcc         | 0.0855959 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.0670241 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.310838  |
|  5 | test       | CLS_KIT        | accuracy    | 0.793103  |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | r2                  |    0.0382789 |
|  1 | test       | KIT            | pearsonr            |    0.288397  |
|  2 | test       | KIT            | spearmanr           |    0.293491  |
|  3 | test       | KIT            | mean_squared_error  | 1160.49      |
|  4 | test       | KIT            | explained_var       |    0.0395892 |
|  5 | test       | KIT            | mean_absolute_error |   28.9311    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | EGFR           | r2                  |   0.0206498 |
|  1 | test       | EGFR           | pearsonr            |   0.245762  |
|  2 | test       | EGFR           | spearmanr           |   0.165568  |
|  3 | test       | EGFR           | mean_squared_error  | 789.13      |
|  4 | test       | EGFR           | explained_var       |   0.0471197 |
|  5 | test       | EGFR           | mean_absolute_error |  22.4768    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.242637 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.509338 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.437081 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.410626 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.255347 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.441025 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | LOG_RPPB       | r2                  | -0.00288903 |
|  1 | test       | LOG_RPPB       | pearsonr            |  0.130701   |
|  2 | test       | LOG_RPPB       | spearmanr           |  0.196522   |
|  3 | test       | LOG_RPPB       | mean_squared_error  |  0.891049   |
|  4 | test       | LOG_RPPB       | explained_var       |  0.0151753  |
|  5 | test       | LOG_RPPB       | mean_absolute_error |  0.790488   |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.0380529 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.408492  |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.447093  |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.582592  |
|  4 | test       | LOG_HPPB       | explained_var       | 0.0786462 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.669835  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.190698 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.440602 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.481968 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.400922 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.192022 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.525427 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.271002 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.527354 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.51917  |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.411551 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.272338 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.525624 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.256539 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.50876  |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.530579 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.288768 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.256778 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.438845 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  0.7426 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.37007 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.263962 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.675546 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0319822 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.407837 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.417893 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.909565 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.564682 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.342331 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.596519 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.833178 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.439163 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.687923 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.857489 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.800451 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.683465 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.4214669177585326,
    "polaris/pkis2-ret-wt-reg-v2": 1091.1300382213092,
    "polaris/pkis2-kit-wt-cls-v2": 0.31083779600688505,
    "polaris/pkis2-kit-wt-reg-v2": 1160.4935168151192,
    "polaris/pkis2-egfr-wt-reg-v2": 789.1295186562164,
    "polaris/adme-fang-solu-1": 0.5093380743158173,
    "polaris/adme-fang-rppb-1": 0.1307011598356586,
    "polaris/adme-fang-hppb-1": 0.4084919244545512,
    "polaris/adme-fang-perm-1": 0.44060168745722184,
    "polaris/adme-fang-rclint-1": 0.5273544108629985,
    "polaris/adme-fang-hclint-1": 0.508760360325342,
    "tdcommons/lipophilicity-astrazeneca": 0.7425999800988605,
    "tdcommons/ppbr-az": 9.370072479248046,
    "tdcommons/clearance-hepatocyte-az": 0.26396164776163283,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6755463256455024,
    "tdcommons/half-life-obach": 0.03198221454912485,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4078373143772182,
    "tdcommons/clearance-microsome-az": 0.4178928256590399,
    "tdcommons/dili": 0.9095652173913042,
    "tdcommons/bioavailability-ma": 0.564682407715331,
    "tdcommons/vdss-lombardo": 0.34233121144414513,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5965189873417721,
    "tdcommons/pgp-broccatelli": 0.8331778192482004,
    "tdcommons/caco2-wang": 0.4391630202899305,
    "tdcommons/herg": 0.6879234167893962,
    "tdcommons/bbb-martins": 0.8574890556597873,
    "tdcommons/ames": 0.8004513501341323,
    "tdcommons/ld50-zhu": 0.6834652028935526
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.695968 |
|  1 | test       | CLS_RET        | f1          | 0        |
|  2 | test       | CLS_RET        | mcc         | 0        |
|  3 | test       | CLS_RET        | cohen_kappa | 0        |
|  4 | test       | CLS_RET        | pr_auc      | 0.563766 |
|  5 | test       | CLS_RET        | accuracy    | 0.839623 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |         Score |
|---:|:-----------|:---------------|:--------------------|--------------:|
|  0 | test       | RET            | r2                  |    0.00158541 |
|  1 | test       | RET            | pearsonr            |    0.225923   |
|  2 | test       | RET            | spearmanr           |    0.175282   |
|  3 | test       | RET            | mean_squared_error  | 1185.52       |
|  4 | test       | RET            | explained_var       |    0.0487861  |
|  5 | test       | RET            | mean_absolute_error |   26.6664     |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.602031 |
|  1 | test       | CLS_KIT        | f1          | 0.153846 |
|  2 | test       | CLS_KIT        | mcc         | 0.149606 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.101408 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.285536 |
|  5 | test       | CLS_KIT        | accuracy    | 0.810345 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | r2                  |    0.0441523 |
|  1 | test       | KIT            | pearsonr            |    0.284968  |
|  2 | test       | KIT            | spearmanr           |    0.29426   |
|  3 | test       | KIT            | mean_squared_error  | 1153.41      |
|  4 | test       | KIT            | explained_var       |    0.07242   |
|  5 | test       | KIT            | mean_absolute_error |   27.8649    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | EGFR           | r2                  |   0.028237  |
|  1 | test       | EGFR           | pearsonr            |   0.178206  |
|  2 | test       | EGFR           | spearmanr           |   0.111004  |
|  3 | test       | EGFR           | mean_squared_error  | 783.016     |
|  4 | test       | EGFR           | explained_var       |   0.0282487 |
|  5 | test       | EGFR           | mean_absolute_error |  21.0891    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.252363 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.503364 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.434773 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.405353 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.252563 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.460165 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | LOG_RPPB       | r2                  | -0.00194996 |
|  1 | test       | LOG_RPPB       | pearsonr            |  0.145415   |
|  2 | test       | LOG_RPPB       | spearmanr           |  0.145217   |
|  3 | test       | LOG_RPPB       | mean_squared_error  |  0.890214   |
|  4 | test       | LOG_RPPB       | explained_var       |  0.0112793  |
|  5 | test       | LOG_RPPB       | mean_absolute_error |  0.792805   |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.116412 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.446313 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.498739 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.535135 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.129605 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.63874  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.183184 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.444542 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.473833 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.404644 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.197399 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.53267  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.291984 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.541365 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.536608 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.399706 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.292085 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.517308 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.263734 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.516144 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.535957 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.285973 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.266398 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.431785 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.748055 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.57622 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.281292 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.663941 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0346871 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.329839 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.40398 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.911304 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.59694 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.517555 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.568038 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.856372 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.45319 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.63461 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.855808 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.805115 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.712687 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5637662896043414,
    "polaris/pkis2-ret-wt-reg-v2": 1185.5225576093517,
    "polaris/pkis2-kit-wt-cls-v2": 0.28553583188016546,
    "polaris/pkis2-kit-wt-reg-v2": 1153.4061330915565,
    "polaris/pkis2-egfr-wt-reg-v2": 783.0160259074714,
    "polaris/adme-fang-solu-1": 0.503364119361664,
    "polaris/adme-fang-rppb-1": 0.14541521780824362,
    "polaris/adme-fang-hppb-1": 0.44631339435491985,
    "polaris/adme-fang-perm-1": 0.4445423035118629,
    "polaris/adme-fang-rclint-1": 0.5413646355667361,
    "polaris/adme-fang-hclint-1": 0.5161444226079548,
    "tdcommons/lipophilicity-astrazeneca": 0.7480546207655043,
    "tdcommons/ppbr-az": 9.576218310852596,
    "tdcommons/clearance-hepatocyte-az": 0.28129221338590055,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6639412865528457,
    "tdcommons/half-life-obach": 0.03468713549745503,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3298385700473394,
    "tdcommons/clearance-microsome-az": 0.40398041105685306,
    "tdcommons/dili": 0.9113043478260869,
    "tdcommons/bioavailability-ma": 0.5969404722314599,
    "tdcommons/vdss-lombardo": 0.5175547121023981,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5680379746835443,
    "tdcommons/pgp-broccatelli": 0.8563716342308718,
    "tdcommons/caco2-wang": 0.4531897103954609,
    "tdcommons/herg": 0.6346097201767306,
    "tdcommons/bbb-martins": 0.8558083176985617,
    "tdcommons/ames": 0.8051146488084748,
    "tdcommons/ld50-zhu": 0.7126868291643217
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.714475 |
|  1 | test       | CLS_RET        | f1          | 0.111111 |
|  2 | test       | CLS_RET        | mcc         | 0.223293 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.094984 |
|  4 | test       | CLS_RET        | pr_auc      | 0.533218 |
|  5 | test       | CLS_RET        | accuracy    | 0.849057 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | RET            | r2                  |   -0.0194946 |
|  1 | test       | RET            | pearsonr            |    0.153981  |
|  2 | test       | RET            | spearmanr           |    0.118856  |
|  3 | test       | RET            | mean_squared_error  | 1210.55      |
|  4 | test       | RET            | explained_var       |    0.0236847 |
|  5 | test       | RET            | mean_absolute_error |   27.0891    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |     Score |
|---:|:-----------|:---------------|:------------|----------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.676015  |
|  1 | test       | CLS_KIT        | f1          | 0.216216  |
|  2 | test       | CLS_KIT        | mcc         | 0.0757048 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.0737885 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.313954  |
|  5 | test       | CLS_KIT        | accuracy    | 0.75      |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | r2                  |    0.124744 |
|  1 | test       | KIT            | pearsonr            |    0.369603 |
|  2 | test       | KIT            | spearmanr           |    0.374232 |
|  3 | test       | KIT            | mean_squared_error  | 1056.16     |
|  4 | test       | KIT            | explained_var       |    0.132697 |
|  5 | test       | KIT            | mean_absolute_error |   27.1453   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | EGFR           | r2                  |   0.0284306 |
|  1 | test       | EGFR           | pearsonr            |   0.176959  |
|  2 | test       | EGFR           | spearmanr           |   0.106549  |
|  3 | test       | EGFR           | mean_squared_error  | 782.86      |
|  4 | test       | EGFR           | explained_var       |   0.0286582 |
|  5 | test       | EGFR           | mean_absolute_error |  20.9748    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.25471  |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.5112   |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.448362 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.40408  |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.255208 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.454345 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | LOG_RPPB       | r2                  | -0.0337471  |
|  1 | test       | LOG_RPPB       | pearsonr            |  0.071823   |
|  2 | test       | LOG_RPPB       | spearmanr           |  0.0617391  |
|  3 | test       | LOG_RPPB       | mean_squared_error  |  0.918466   |
|  4 | test       | LOG_RPPB       | explained_var       |  0.00341682 |
|  5 | test       | LOG_RPPB       | mean_absolute_error |  0.818538   |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.101246 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.40592  |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.415616 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.54432  |
|  4 | test       | LOG_HPPB       | explained_var       | 0.141526 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.641277 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.1777   |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.429389 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.463713 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.407362 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.184258 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.531425 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.276347 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.533526 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.527618 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.408534 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.284014 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.517399 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.254679 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.506981 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.519464 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.28949  |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.254954 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.441694 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.734231 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 10.2744 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.236296 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.654026 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.112487 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.418065 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.393798 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.914783 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.607582 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.492636 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.608951 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.851506 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.435869 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.67025 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.86214 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.801339 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.700899 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5332184807858262,
    "polaris/pkis2-ret-wt-reg-v2": 1210.5531032890285,
    "polaris/pkis2-kit-wt-cls-v2": 0.3139538394937052,
    "polaris/pkis2-kit-wt-reg-v2": 1056.157104345953,
    "polaris/pkis2-egfr-wt-reg-v2": 782.8599931035476,
    "polaris/adme-fang-solu-1": 0.5112003310229661,
    "polaris/adme-fang-rppb-1": 0.07182298055130634,
    "polaris/adme-fang-hppb-1": 0.405919739637839,
    "polaris/adme-fang-perm-1": 0.42938893337062467,
    "polaris/adme-fang-rclint-1": 0.5335263702785654,
    "polaris/adme-fang-hclint-1": 0.5069808801415129,
    "tdcommons/lipophilicity-astrazeneca": 0.7342312727598915,
    "tdcommons/ppbr-az": 10.274352580771676,
    "tdcommons/clearance-hepatocyte-az": 0.23629560406643527,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6540261402400225,
    "tdcommons/half-life-obach": 0.1124870127130534,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4180653314368723,
    "tdcommons/clearance-microsome-az": 0.39379763024385145,
    "tdcommons/dili": 0.9147826086956522,
    "tdcommons/bioavailability-ma": 0.6075823079481211,
    "tdcommons/vdss-lombardo": 0.4926359030752743,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6089511754068716,
    "tdcommons/pgp-broccatelli": 0.851506264996001,
    "tdcommons/caco2-wang": 0.4358692079098545,
    "tdcommons/herg": 0.6702503681885125,
    "tdcommons/bbb-martins": 0.8621404002501564,
    "tdcommons/ames": 0.8013393643893554,
    "tdcommons/ld50-zhu": 0.700898935225723
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.804362 |
|  1 | test       | CLS_RET        | f1          | 0.3      |
|  2 | test       | CLS_RET        | mcc         | 0.390492 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.264618 |
|  4 | test       | CLS_RET        | pr_auc      | 0.567539 |
|  5 | test       | CLS_RET        | accuracy    | 0.867925 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | RET            | r2                  |    0.0259525 |
|  1 | test       | RET            | pearsonr            |    0.351958  |
|  2 | test       | RET            | spearmanr           |    0.316646  |
|  3 | test       | RET            | mean_squared_error  | 1156.59      |
|  4 | test       | RET            | explained_var       |    0.0807052 |
|  5 | test       | RET            | mean_absolute_error |   26.2066    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |     Score |
|---:|:-----------|:---------------|:------------|----------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.665861  |
|  1 | test       | CLS_KIT        | f1          | 0.0833333 |
|  2 | test       | CLS_KIT        | mcc         | 0.104855  |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.0534125 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.318532  |
|  5 | test       | CLS_KIT        | accuracy    | 0.810345  |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | r2                  |    0.0170361 |
|  1 | test       | KIT            | pearsonr            |    0.30923   |
|  2 | test       | KIT            | spearmanr           |    0.328886  |
|  3 | test       | KIT            | mean_squared_error  | 1186.13      |
|  4 | test       | KIT            | explained_var       |    0.0910245 |
|  5 | test       | KIT            | mean_absolute_error |   27.5159    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | EGFR           | r2                  |   0.0175034 |
|  1 | test       | EGFR           | pearsonr            |   0.156593  |
|  2 | test       | EGFR           | spearmanr           |   0.0593581 |
|  3 | test       | EGFR           | mean_squared_error  | 791.665     |
|  4 | test       | EGFR           | explained_var       |   0.0231652 |
|  5 | test       | EGFR           | mean_absolute_error |  20.7451    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.240455 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.507106 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.44118  |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.411809 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.254706 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.435172 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | LOG_RPPB       | r2                  | -0.116089    |
|  1 | test       | LOG_RPPB       | pearsonr            | -0.031506    |
|  2 | test       | LOG_RPPB       | spearmanr           |  0.18087     |
|  3 | test       | LOG_RPPB       | mean_squared_error  |  0.991625    |
|  4 | test       | LOG_RPPB       | explained_var       | -0.000490544 |
|  5 | test       | LOG_RPPB       | mean_absolute_error |  0.863065    |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | LOG_HPPB       | r2                  | -0.0195484 |
|  1 | test       | LOG_HPPB       | pearsonr            |  0.466761  |
|  2 | test       | LOG_HPPB       | spearmanr           |  0.480862  |
|  3 | test       | LOG_HPPB       | mean_squared_error  |  0.617478  |
|  4 | test       | LOG_HPPB       | explained_var       |  0.0987883 |
|  5 | test       | LOG_HPPB       | mean_absolute_error |  0.699136  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.197407 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.447266 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.483175 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.397599 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.197851 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.52113  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.292696 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.544346 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.541581 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.399304 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.292704 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.516233 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.246645 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.501102 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.519673 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.292611 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.249148 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.440946 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.760858 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.67181 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.282126 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.62991 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0346749 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.406756 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.430658 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  |    0.91 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.568341 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.49754 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.607821 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.842642 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.440318 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.686451 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.850141 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.798583 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.700396 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5675393108049313,
    "polaris/pkis2-ret-wt-reg-v2": 1156.5889172439931,
    "polaris/pkis2-kit-wt-cls-v2": 0.31853197776453296,
    "polaris/pkis2-kit-wt-reg-v2": 1186.1269147000364,
    "polaris/pkis2-egfr-wt-reg-v2": 791.6648216096902,
    "polaris/adme-fang-solu-1": 0.5071055620109537,
    "polaris/adme-fang-rppb-1": -0.03150601159945554,
    "polaris/adme-fang-hppb-1": 0.4667612273198292,
    "polaris/adme-fang-perm-1": 0.4472655587647629,
    "polaris/adme-fang-rclint-1": 0.544346251541416,
    "polaris/adme-fang-hclint-1": 0.5011019287392592,
    "tdcommons/lipophilicity-astrazeneca": 0.7608577149482,
    "tdcommons/ppbr-az": 9.671809811395908,
    "tdcommons/clearance-hepatocyte-az": 0.2821261656534393,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6299095276028865,
    "tdcommons/half-life-obach": 0.034674940182088346,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4067556255591499,
    "tdcommons/clearance-microsome-az": 0.4306576606337852,
    "tdcommons/dili": 0.91,
    "tdcommons/bioavailability-ma": 0.5683405387429331,
    "tdcommons/vdss-lombardo": 0.49753958394658565,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6078209764918625,
    "tdcommons/pgp-broccatelli": 0.8426419621434285,
    "tdcommons/caco2-wang": 0.4403181163049719,
    "tdcommons/herg": 0.6864506627393225,
    "tdcommons/bbb-martins": 0.850140712945591,
    "tdcommons/ames": 0.7985832892752942,
    "tdcommons/ld50-zhu": 0.7003956752442863
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.740251 |
|  1 | test       | CLS_RET        | f1          | 0.111111 |
|  2 | test       | CLS_RET        | mcc         | 0.223293 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.094984 |
|  4 | test       | CLS_RET        | pr_auc      | 0.543074 |
|  5 | test       | CLS_RET        | accuracy    | 0.849057 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | RET            | r2                  |    0.011853  |
|  1 | test       | RET            | pearsonr            |    0.307564  |
|  2 | test       | RET            | spearmanr           |    0.242076  |
|  3 | test       | RET            | mean_squared_error  | 1173.33      |
|  4 | test       | RET            | explained_var       |    0.0876512 |
|  5 | test       | RET            | mean_absolute_error |   26.053     |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.680368 |
|  1 | test       | CLS_KIT        | f1          | 0.153846 |
|  2 | test       | CLS_KIT        | mcc         | 0.149606 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.101408 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.348544 |
|  5 | test       | CLS_KIT        | accuracy    | 0.810345 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | r2                  |    0.0329747 |
|  1 | test       | KIT            | pearsonr            |    0.27361   |
|  2 | test       | KIT            | spearmanr           |    0.279135  |
|  3 | test       | KIT            | mean_squared_error  | 1166.89      |
|  4 | test       | KIT            | explained_var       |    0.0560313 |
|  5 | test       | KIT            | mean_absolute_error |   28.1321    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | EGFR           | r2                  |   0.0216648 |
|  1 | test       | EGFR           | pearsonr            |   0.163776  |
|  2 | test       | EGFR           | spearmanr           |   0.0869877 |
|  3 | test       | EGFR           | mean_squared_error  | 788.312     |
|  4 | test       | EGFR           | explained_var       |   0.0244827 |
|  5 | test       | EGFR           | mean_absolute_error |  20.7566    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.237528 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.49338  |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.439556 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.413396 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.241515 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.448504 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | LOG_RPPB       | r2                  | -0.0146072  |
|  1 | test       | LOG_RPPB       | pearsonr            |  0.0612817  |
|  2 | test       | LOG_RPPB       | spearmanr           |  0.143478   |
|  3 | test       | LOG_RPPB       | mean_squared_error  |  0.90146    |
|  4 | test       | LOG_RPPB       | explained_var       |  0.00332131 |
|  5 | test       | LOG_RPPB       | mean_absolute_error |  0.804767   |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.073516 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.326495 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.410268 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.561115 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.076983 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.647118 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.171756 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.422526 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.457505 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.410306 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.173946 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.516872 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.313448 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.564887 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.558758 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.387588 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.31383  |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.506174 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.25853  |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.510994 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.527298 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.287994 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.258684 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.441366 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.747703 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.46058 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.282068 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.668789 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0169234 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.416583 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.359129 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.902609 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.658464 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.417944 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.603526 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.851573 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.447805 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.674963 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.843183 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.794572 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.681415 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5430743025549936,
    "polaris/pkis2-ret-wt-reg-v2": 1173.3307860301802,
    "polaris/pkis2-kit-wt-cls-v2": 0.34854393007458623,
    "polaris/pkis2-kit-wt-reg-v2": 1166.893968716977,
    "polaris/pkis2-egfr-wt-reg-v2": 788.3116821244234,
    "polaris/adme-fang-solu-1": 0.4933802513643362,
    "polaris/adme-fang-rppb-1": 0.06128169147140541,
    "polaris/adme-fang-hppb-1": 0.32649503427363447,
    "polaris/adme-fang-perm-1": 0.422525873344049,
    "polaris/adme-fang-rclint-1": 0.5648865915044958,
    "polaris/adme-fang-hclint-1": 0.5109938338633327,
    "tdcommons/lipophilicity-astrazeneca": 0.7477032194705237,
    "tdcommons/ppbr-az": 9.460583823106798,
    "tdcommons/clearance-hepatocyte-az": 0.2820682552682827,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6687892091399383,
    "tdcommons/half-life-obach": 0.016923439134345304,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4165828382448885,
    "tdcommons/clearance-microsome-az": 0.3591287952118593,
    "tdcommons/dili": 0.9026086956521739,
    "tdcommons/bioavailability-ma": 0.6584635849684071,
    "tdcommons/vdss-lombardo": 0.41794446407637437,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6035262206148282,
    "tdcommons/pgp-broccatelli": 0.8515729138896293,
    "tdcommons/caco2-wang": 0.4478050710810399,
    "tdcommons/herg": 0.6749631811487482,
    "tdcommons/bbb-martins": 0.8431832395247029,
    "tdcommons/ames": 0.79457204957998,
    "tdcommons/ld50-zhu": 0.6814152598981121
}
```
