# Descriptor MLP Results
timestamp: 2025-04-29 19:55:28.772641
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.826173 |
|  1 | test       | CLS_RET        | mcc         | 0.337956 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.288272 |
|  3 | test       | CLS_RET        | accuracy    | 0.858491 |
|  4 | test       | CLS_RET        | pr_auc      | 0.583787 |
|  5 | test       | CLS_RET        | f1          | 0.347826 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.31513  |
|  1 | test       | RET            | pearsonr            |   0.562467 |
|  2 | test       | RET            | spearmanr           |   0.561634 |
|  3 | test       | RET            | r2                  |   0.284373 |
|  4 | test       | RET            | mean_absolute_error |  21.6698   |
|  5 | test       | RET            | mean_squared_error  | 849.739    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.73646  |
|  1 | test       | CLS_KIT        | mcc         | 0.125343 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.12311  |
|  3 | test       | CLS_KIT        | accuracy    | 0.758621 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.463547 |
|  5 | test       | CLS_KIT        | f1          | 0.263158 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | explained_var       |    0.0720287 |
|  1 | test       | KIT            | pearsonr            |    0.410593  |
|  2 | test       | KIT            | spearmanr           |    0.373243  |
|  3 | test       | KIT            | r2                  |    0.0507501 |
|  4 | test       | KIT            | mean_absolute_error |   26.0292    |
|  5 | test       | KIT            | mean_squared_error  | 1145.44      |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.372144 |
|  1 | test       | EGFR           | pearsonr            |   0.611265 |
|  2 | test       | EGFR           | spearmanr           |   0.297116 |
|  3 | test       | EGFR           | r2                  |   0.363622 |
|  4 | test       | EGFR           | mean_absolute_error |  17.7236   |
|  5 | test       | EGFR           | mean_squared_error  | 512.774    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.301551 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.550657 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.455269 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.301198 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.428314 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.378875 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.617876 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.799091 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.853913 |
|  3 | test       | LOG_RPPB       | r2                  | 0.61787  |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.382973 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.339516 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.742873 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.862109 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.856444 |
|  3 | test       | LOG_HPPB       | r2                  | 0.706281 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.351604 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.177888 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.575653 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.761191 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.750716 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.573673 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.347145 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.211199 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.473406 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.694148 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.693424 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.473405 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.423465 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.297286 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.432525 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.67003  |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.686838 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.432444 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.354858 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.220444 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.523739 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.92061 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.340134 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.68135 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.199985 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.367879 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.585569 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.914783 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.73861 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.484471 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.622401 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.930285 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.28552 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.855817 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.904745 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.835564 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.637599 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.583787278866965,
    "polaris/pkis2-ret-wt-reg-v2": 849.7391966328676,
    "polaris/pkis2-kit-wt-cls-v2": 0.4635468824097374,
    "polaris/pkis2-kit-wt-reg-v2": 1145.4447145646427,
    "polaris/pkis2-egfr-wt-reg-v2": 512.7735942141533,
    "polaris/adme-fang-solu-1": 0.550656623449636,
    "polaris/adme-fang-rppb-1": 0.799091282446034,
    "polaris/adme-fang-hppb-1": 0.8621094070782683,
    "polaris/adme-fang-perm-1": 0.7611905699095767,
    "polaris/adme-fang-rclint-1": 0.6941477634892514,
    "polaris/adme-fang-hclint-1": 0.6700295807589963,
    "tdcommons/lipophilicity-astrazeneca": 0.5237386020649047,
    "tdcommons/ppbr-az": 7.920605986566152,
    "tdcommons/clearance-hepatocyte-az": 0.3401344634504715,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6813499328216184,
    "tdcommons/half-life-obach": 0.19998536676393175,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.36787911226242753,
    "tdcommons/clearance-microsome-az": 0.5855687789077708,
    "tdcommons/dili": 0.9147826086956522,
    "tdcommons/bioavailability-ma": 0.7386099102095112,
    "tdcommons/vdss-lombardo": 0.4844707259899688,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6224005424954792,
    "tdcommons/pgp-broccatelli": 0.9302852572647294,
    "tdcommons/caco2-wang": 0.285519777326345,
    "tdcommons/herg": 0.8558173784977908,
    "tdcommons/bbb-martins": 0.9047451532207629,
    "tdcommons/ames": 0.8355636491805205,
    "tdcommons/ld50-zhu": 0.6375986027027177
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.803701 |
|  1 | test       | CLS_RET        | mcc         | 0.318193 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.239234 |
|  3 | test       | CLS_RET        | accuracy    | 0.858491 |
|  4 | test       | CLS_RET        | pr_auc      | 0.598693 |
|  5 | test       | CLS_RET        | f1          | 0.285714 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.362264 |
|  1 | test       | RET            | pearsonr            |   0.60695  |
|  2 | test       | RET            | spearmanr           |   0.618536 |
|  3 | test       | RET            | r2                  |   0.334455 |
|  4 | test       | RET            | mean_absolute_error |  20.3379   |
|  5 | test       | RET            | mean_squared_error  | 790.272    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.73646  |
|  1 | test       | CLS_KIT        | mcc         | 0.157071 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.155925 |
|  3 | test       | CLS_KIT        | accuracy    | 0.758621 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.401656 |
|  5 | test       | CLS_KIT        | f1          | 0.3      |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | explained_var       |   -0.02259   |
|  1 | test       | KIT            | pearsonr            |    0.408166  |
|  2 | test       | KIT            | spearmanr           |    0.383832  |
|  3 | test       | KIT            | r2                  |   -0.0249935 |
|  4 | test       | KIT            | mean_absolute_error |   27.4104    |
|  5 | test       | KIT            | mean_squared_error  | 1236.84      |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.421577 |
|  1 | test       | EGFR           | pearsonr            |   0.64929  |
|  2 | test       | EGFR           | spearmanr           |   0.351436 |
|  3 | test       | EGFR           | r2                  |   0.403765 |
|  4 | test       | EGFR           | mean_absolute_error |  17.2646   |
|  5 | test       | EGFR           | mean_squared_error  | 480.427    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.307245 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.554722 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.460832 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.306979 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.431076 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.375741 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.597463 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.825776 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.870435 |
|  3 | test       | LOG_RPPB       | r2                  | 0.597463 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.418016 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.357647 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.447238 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.706964 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.71159  |
|  3 | test       | LOG_HPPB       | r2                  | 0.395119 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.554196 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.36634  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.580807 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.762235 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.753588 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.580059 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.334838 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.208036 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.47641  |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.697756 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.694762 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.47327  |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.425398 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.297362 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.413362 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.653199 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.673063 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.41322  |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.364285 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.227911 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.525861 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  8.3492 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.326215 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.68365 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.405353 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.364274 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.504296 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.917391 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.67875 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.529161 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.612003 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.926553 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.279241 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.836082 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.913813 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.837344 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.640618 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5986925408594252,
    "polaris/pkis2-ret-wt-reg-v2": 790.2715387272021,
    "polaris/pkis2-kit-wt-cls-v2": 0.4016563009328646,
    "polaris/pkis2-kit-wt-reg-v2": 1236.843242515718,
    "polaris/pkis2-egfr-wt-reg-v2": 480.4274819696209,
    "polaris/adme-fang-solu-1": 0.5547223178805921,
    "polaris/adme-fang-rppb-1": 0.8257755328524117,
    "polaris/adme-fang-hppb-1": 0.7069636273381914,
    "polaris/adme-fang-perm-1": 0.7622354697517713,
    "polaris/adme-fang-rclint-1": 0.6977559301860555,
    "polaris/adme-fang-hclint-1": 0.6531993287408178,
    "tdcommons/lipophilicity-astrazeneca": 0.5258606402476629,
    "tdcommons/ppbr-az": 8.349202275148231,
    "tdcommons/clearance-hepatocyte-az": 0.32621548681937346,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6836495356367281,
    "tdcommons/half-life-obach": 0.4053525393243037,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3642743028601435,
    "tdcommons/clearance-microsome-az": 0.5042956222528998,
    "tdcommons/dili": 0.9173913043478261,
    "tdcommons/bioavailability-ma": 0.6787495843032924,
    "tdcommons/vdss-lombardo": 0.5291606058950776,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.612002712477396,
    "tdcommons/pgp-broccatelli": 0.9265529192215409,
    "tdcommons/caco2-wang": 0.27924119444595186,
    "tdcommons/herg": 0.8360824742268042,
    "tdcommons/bbb-martins": 0.9138133208255159,
    "tdcommons/ames": 0.8373435939611116,
    "tdcommons/ld50-zhu": 0.6406175544142562
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.818242 |
|  1 | test       | CLS_RET        | mcc         | 0.318193 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.239234 |
|  3 | test       | CLS_RET        | accuracy    | 0.858491 |
|  4 | test       | CLS_RET        | pr_auc      | 0.565166 |
|  5 | test       | CLS_RET        | f1          | 0.285714 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.328588 |
|  1 | test       | RET            | pearsonr            |   0.588922 |
|  2 | test       | RET            | spearmanr           |   0.587482 |
|  3 | test       | RET            | r2                  |   0.310595 |
|  4 | test       | RET            | mean_absolute_error |  20.9166   |
|  5 | test       | RET            | mean_squared_error  | 818.603    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.72824  |
|  1 | test       | CLS_KIT        | mcc         | 0.14124  |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.137665 |
|  3 | test       | CLS_KIT        | accuracy    | 0.767241 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.462432 |
|  5 | test       | CLS_KIT        | f1          | 0.27027  |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | explained_var       |    0.0781099 |
|  1 | test       | KIT            | pearsonr            |    0.436629  |
|  2 | test       | KIT            | spearmanr           |    0.402143  |
|  3 | test       | KIT            | r2                  |    0.0605353 |
|  4 | test       | KIT            | mean_absolute_error |   25.8101    |
|  5 | test       | KIT            | mean_squared_error  | 1133.64      |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.380133 |
|  1 | test       | EGFR           | pearsonr            |   0.621579 |
|  2 | test       | EGFR           | spearmanr           |   0.313822 |
|  3 | test       | EGFR           | r2                  |   0.375622 |
|  4 | test       | EGFR           | mean_absolute_error |  17.6523   |
|  5 | test       | EGFR           | mean_squared_error  | 503.104    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.290516 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.539822 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.45422  |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.280557 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.417085 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.390067 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.651016 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.843704 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.909565 |
|  3 | test       | LOG_RPPB       | r2                  | 0.649996 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.376736 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.310973 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.406408 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.678964 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.695087 |
|  3 | test       | LOG_HPPB       | r2                  | 0.364304 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.569088 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.385002 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.554054 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.744742 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.741989 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.553898 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.348182 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.220996 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.481086 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.696928 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.695861 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.480362 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.42076  |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.293358 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.407115 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.650568 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.670734 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.404757 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.360506 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.231198 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.534883 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.95995 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.309715 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.682343 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.268992 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.361159 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.567585 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.899565 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.653808 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.562974 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.617428 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.931352 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.27683 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.826951 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.913227 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.844816 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.64877 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5651659427954137,
    "polaris/pkis2-ret-wt-reg-v2": 818.6026982463095,
    "polaris/pkis2-kit-wt-cls-v2": 0.46243151046648356,
    "polaris/pkis2-kit-wt-reg-v2": 1133.637049529324,
    "polaris/pkis2-egfr-wt-reg-v2": 503.1044670735728,
    "polaris/adme-fang-solu-1": 0.5398216156493096,
    "polaris/adme-fang-rppb-1": 0.8437042182928427,
    "polaris/adme-fang-hppb-1": 0.6789642723709503,
    "polaris/adme-fang-perm-1": 0.7447424958161752,
    "polaris/adme-fang-rclint-1": 0.6969279947323915,
    "polaris/adme-fang-hclint-1": 0.6505682350138622,
    "tdcommons/lipophilicity-astrazeneca": 0.5348833077975682,
    "tdcommons/ppbr-az": 7.959950614205842,
    "tdcommons/clearance-hepatocyte-az": 0.30971518797918834,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.682342920635078,
    "tdcommons/half-life-obach": 0.26899150752662543,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3611590748095259,
    "tdcommons/clearance-microsome-az": 0.5675847090689867,
    "tdcommons/dili": 0.8995652173913044,
    "tdcommons/bioavailability-ma": 0.6538077818423678,
    "tdcommons/vdss-lombardo": 0.5629743264458372,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6174276672694394,
    "tdcommons/pgp-broccatelli": 0.9313516395627832,
    "tdcommons/caco2-wang": 0.276830007764108,
    "tdcommons/herg": 0.8269513991163476,
    "tdcommons/bbb-martins": 0.9132270168855533,
    "tdcommons/ames": 0.8448158373964637,
    "tdcommons/ld50-zhu": 0.6487698026555155
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.808328 |
|  1 | test       | CLS_RET        | mcc         | 0        |
|  2 | test       | CLS_RET        | cohen_kappa | 0        |
|  3 | test       | CLS_RET        | accuracy    | 0.839623 |
|  4 | test       | CLS_RET        | pr_auc      | 0.503079 |
|  5 | test       | CLS_RET        | f1          | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.347928 |
|  1 | test       | RET            | pearsonr            |   0.592533 |
|  2 | test       | RET            | spearmanr           |   0.573363 |
|  3 | test       | RET            | r2                  |   0.341778 |
|  4 | test       | RET            | mean_absolute_error |  21.2796   |
|  5 | test       | RET            | mean_squared_error  | 781.576    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.760638 |
|  1 | test       | CLS_KIT        | mcc         | 0.14124  |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.137665 |
|  3 | test       | CLS_KIT        | accuracy    | 0.767241 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.457913 |
|  5 | test       | CLS_KIT        | f1          | 0.27027  |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | explained_var       |    0.127195  |
|  1 | test       | KIT            | pearsonr            |    0.467384  |
|  2 | test       | KIT            | spearmanr           |    0.446065  |
|  3 | test       | KIT            | r2                  |    0.0882886 |
|  4 | test       | KIT            | mean_absolute_error |   25.066     |
|  5 | test       | KIT            | mean_squared_error  | 1100.15      |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.395641 |
|  1 | test       | EGFR           | pearsonr            |   0.630356 |
|  2 | test       | EGFR           | spearmanr           |   0.360918 |
|  3 | test       | EGFR           | r2                  |   0.392087 |
|  4 | test       | EGFR           | mean_absolute_error |  17.2679   |
|  5 | test       | EGFR           | mean_squared_error  | 489.837    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.299651 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.549271 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.450363 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.298821 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.419945 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.380164 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.692355 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.856777 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.886087 |
|  3 | test       | LOG_RPPB       | r2                  | 0.689001 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.385542 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.276317 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.691345 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.831954 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.79945  |
|  3 | test       | LOG_HPPB       | r2                  | 0.578784 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.420393 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.255105 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.588747 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.767415 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.757813 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.587764 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.332893 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.204218 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.467813 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.689023 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.684551 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.466793 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.434746 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.301018 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.442912 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.674769 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.693052 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.441284 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.348721 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.217011 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.536041 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.12882 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.316208 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.624186 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.33991 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.310883 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.578252 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.897391 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.66445 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.488466 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.615393 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.928686 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.268253 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.852283 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.919833 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.848231 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.663481 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5030791216896694,
    "polaris/pkis2-ret-wt-reg-v2": 781.5764824027711,
    "polaris/pkis2-kit-wt-cls-v2": 0.4579132533408113,
    "polaris/pkis2-kit-wt-reg-v2": 1100.1476406182283,
    "polaris/pkis2-egfr-wt-reg-v2": 489.8367758584126,
    "polaris/adme-fang-solu-1": 0.5492714228617276,
    "polaris/adme-fang-rppb-1": 0.8567772637466231,
    "polaris/adme-fang-hppb-1": 0.831954179286244,
    "polaris/adme-fang-perm-1": 0.7674153956264205,
    "polaris/adme-fang-rclint-1": 0.6890228764852633,
    "polaris/adme-fang-hclint-1": 0.6747686731461147,
    "tdcommons/lipophilicity-astrazeneca": 0.5360407103243329,
    "tdcommons/ppbr-az": 8.12882345673863,
    "tdcommons/clearance-hepatocyte-az": 0.31620818999478767,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6241860435957456,
    "tdcommons/half-life-obach": 0.3399098784023528,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.31088349227393086,
    "tdcommons/clearance-microsome-az": 0.5782520984853011,
    "tdcommons/dili": 0.8973913043478261,
    "tdcommons/bioavailability-ma": 0.6644496175590289,
    "tdcommons/vdss-lombardo": 0.4884662407972304,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6153933092224231,
    "tdcommons/pgp-broccatelli": 0.9286856838176486,
    "tdcommons/caco2-wang": 0.2682531115227333,
    "tdcommons/herg": 0.8522827687776141,
    "tdcommons/bbb-martins": 0.919832707942464,
    "tdcommons/ames": 0.8482308249623058,
    "tdcommons/ld50-zhu": 0.6634805215118057
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.8308   |
|  1 | test       | CLS_RET        | mcc         | 0.449209 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.383169 |
|  3 | test       | CLS_RET        | accuracy    | 0.877358 |
|  4 | test       | CLS_RET        | pr_auc      | 0.626366 |
|  5 | test       | CLS_RET        | f1          | 0.434783 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.367965 |
|  1 | test       | RET            | pearsonr            |   0.608806 |
|  2 | test       | RET            | spearmanr           |   0.602224 |
|  3 | test       | RET            | r2                  |   0.336011 |
|  4 | test       | RET            | mean_absolute_error |  20.6659   |
|  5 | test       | RET            | mean_squared_error  | 788.424    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.745648 |
|  1 | test       | CLS_KIT        | mcc         | 0.270692 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.23875  |
|  3 | test       | CLS_KIT        | accuracy    | 0.818966 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.421778 |
|  5 | test       | CLS_KIT        | f1          | 0.322581 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | explained_var       |    0.0762908 |
|  1 | test       | KIT            | pearsonr            |    0.430206  |
|  2 | test       | KIT            | spearmanr           |    0.401208  |
|  3 | test       | KIT            | r2                  |    0.0743765 |
|  4 | test       | KIT            | mean_absolute_error |   25.9631    |
|  5 | test       | KIT            | mean_squared_error  | 1116.94      |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.286425 |
|  1 | test       | EGFR           | pearsonr            |   0.539983 |
|  2 | test       | EGFR           | spearmanr           |   0.312779 |
|  3 | test       | EGFR           | r2                  |   0.269703 |
|  4 | test       | EGFR           | mean_absolute_error |  18.8786   |
|  5 | test       | EGFR           | mean_squared_error  | 588.451    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.29339  |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.541694 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.439496 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.279993 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.424243 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.390372 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.754097 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.887573 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.914783 |
|  3 | test       | LOG_RPPB       | r2                  | 0.73657  |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.34754  |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.234053 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.661784 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.81884  |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.822676 |
|  3 | test       | LOG_HPPB       | r2                  | 0.555225 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.437097 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.269373 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.562465 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.750475 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.747463 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.557841 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.343685 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.219042 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.490029 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.705845 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.703291 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.489657 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.42391  |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.288111 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.44514  |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.688728 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.701421 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.445063 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.343149 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.215543 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.53322 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.21143 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.334799 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.612719 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.257625 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.393351 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.535503 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.90087 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.65281 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.409242 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.621044 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.940149 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.27812 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.839617 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.922217 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.843163 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.628426 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6263661693979863,
    "polaris/pkis2-ret-wt-reg-v2": 788.423912067469,
    "polaris/pkis2-kit-wt-cls-v2": 0.42177771545361714,
    "polaris/pkis2-kit-wt-reg-v2": 1116.935156297913,
    "polaris/pkis2-egfr-wt-reg-v2": 588.4505098261964,
    "polaris/adme-fang-solu-1": 0.5416939259814229,
    "polaris/adme-fang-rppb-1": 0.887573358802433,
    "polaris/adme-fang-hppb-1": 0.818840336877212,
    "polaris/adme-fang-perm-1": 0.7504747556668985,
    "polaris/adme-fang-rclint-1": 0.7058447125095365,
    "polaris/adme-fang-hclint-1": 0.6887277069740707,
    "tdcommons/lipophilicity-astrazeneca": 0.5332204139402935,
    "tdcommons/ppbr-az": 8.211428839558991,
    "tdcommons/clearance-hepatocyte-az": 0.334798750724707,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6127189345489502,
    "tdcommons/half-life-obach": 0.2576254458853787,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.393350993995929,
    "tdcommons/clearance-microsome-az": 0.5355030055099153,
    "tdcommons/dili": 0.9008695652173914,
    "tdcommons/bioavailability-ma": 0.6528101097439307,
    "tdcommons/vdss-lombardo": 0.4092421376712,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6210443037974683,
    "tdcommons/pgp-broccatelli": 0.9401492935217275,
    "tdcommons/caco2-wang": 0.2781202534620516,
    "tdcommons/herg": 0.8396170839469809,
    "tdcommons/bbb-martins": 0.9222170106316449,
    "tdcommons/ames": 0.8431631713955627,
    "tdcommons/ld50-zhu": 0.6284261819984013
}
```
