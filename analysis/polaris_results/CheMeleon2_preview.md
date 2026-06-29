# chemeleon2_preview_initial_training_e4s281344 Baseline Results
timestamp: 2026-06-28 01:24:46.656904
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.867925 |
|  1 | test       | CLS_RET        | f1          | 0.416667 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.356461 |
|  3 | test       | CLS_RET        | mcc         | 0.40138  |
|  4 | test       | CLS_RET        | roc_auc     | 0.820886 |
|  5 | test       | CLS_RET        | pr_auc      | 0.58232  |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  25.052    |
|  1 | test       | RET            | spearmanr           |   0.392082 |
|  2 | test       | RET            | explained_var       |   0.180837 |
|  3 | test       | RET            | pearsonr            |   0.427521 |
|  4 | test       | RET            | r2                  |   0.170224 |
|  5 | test       | RET            | mean_squared_error  | 985.28     |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.836207 |
|  1 | test       | CLS_KIT        | f1          | 0.512821 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.416314 |
|  3 | test       | CLS_KIT        | mcc         | 0.421313 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.814797 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.518589 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  24.0983   |
|  1 | test       | KIT            | spearmanr           |   0.445796 |
|  2 | test       | KIT            | explained_var       |   0.250478 |
|  3 | test       | KIT            | pearsonr            |   0.506377 |
|  4 | test       | KIT            | r2                  |   0.23613  |
|  5 | test       | KIT            | mean_squared_error  | 921.749    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  18.3886   |
|  1 | test       | EGFR           | spearmanr           |   0.252364 |
|  2 | test       | EGFR           | explained_var       |   0.325535 |
|  3 | test       | EGFR           | pearsonr            |   0.577301 |
|  4 | test       | EGFR           | r2                  |   0.318658 |
|  5 | test       | EGFR           | mean_squared_error  | 549.004    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.373139 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.519352 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.38995  |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.62481  |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.361153 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.346369 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error |  0.832483  |
|  1 | test       | LOG_RPPB       | spearmanr           |  0.554783  |
|  2 | test       | LOG_RPPB       | explained_var       |  0.0738642 |
|  3 | test       | LOG_RPPB       | pearsonr            |  0.569463  |
|  4 | test       | LOG_RPPB       | r2                  | -0.0286842 |
|  5 | test       | LOG_RPPB       | mean_squared_error  |  0.913967  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.649774  |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.286653  |
|  2 | test       | LOG_HPPB       | explained_var       | 0.0319354 |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.213967  |
|  4 | test       | LOG_HPPB       | r2                  | 0.0297933 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.587595  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.375199 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.709054 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.541633 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.736744 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.528434 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.23361  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.425205 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.714553 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.500366 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.71128  |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.500357 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.28207  |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.470261 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.485459 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.204271 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.479078 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.203614 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.309324 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.470811 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  8.6564 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.320787 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.704986 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.189402 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.34851 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.586191 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.833478 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.514466 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.521649 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.543287 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.883031 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.334567 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.765096 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.885358 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.821737 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.576314 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5823196109757977,
    "polaris/pkis2-ret-wt-reg-v2": 985.2802668191489,
    "polaris/pkis2-kit-wt-cls-v2": 0.5185888339404114,
    "polaris/pkis2-kit-wt-reg-v2": 921.7494240774763,
    "polaris/pkis2-egfr-wt-reg-v2": 549.0035323347402,
    "polaris/adme-fang-solu-1": 0.62480971092464,
    "polaris/adme-fang-rppb-1": 0.5694625605948572,
    "polaris/adme-fang-hppb-1": 0.21396744202230372,
    "polaris/adme-fang-perm-1": 0.7367441548268829,
    "polaris/adme-fang-rclint-1": 0.7112803158756853,
    "polaris/adme-fang-hclint-1": 0.4790784701122567,
    "tdcommons/lipophilicity-astrazeneca": 0.47081084458033245,
    "tdcommons/ppbr-az": 8.656400595786106,
    "tdcommons/clearance-hepatocyte-az": 0.32078730954976503,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7049862581760934,
    "tdcommons/half-life-obach": 0.18940224627865934,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3485098305314943,
    "tdcommons/clearance-microsome-az": 0.5861908586548478,
    "tdcommons/dili": 0.8334782608695652,
    "tdcommons/bioavailability-ma": 0.5144662454273362,
    "tdcommons/vdss-lombardo": 0.5216492559743972,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5432866184448463,
    "tdcommons/pgp-broccatelli": 0.8830311916822181,
    "tdcommons/caco2-wang": 0.3345674591912574,
    "tdcommons/herg": 0.7650957290132547,
    "tdcommons/bbb-martins": 0.8853580362726705,
    "tdcommons/ames": 0.821737257436018,
    "tdcommons/ld50-zhu": 0.5763135693431385
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.877358 |
|  1 | test       | CLS_RET        | f1          | 0.606061 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.533514 |
|  3 | test       | CLS_RET        | mcc         | 0.533858 |
|  4 | test       | CLS_RET        | roc_auc     | 0.837409 |
|  5 | test       | CLS_RET        | pr_auc      | 0.682133 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  19.8417   |
|  1 | test       | RET            | spearmanr           |   0.66757  |
|  2 | test       | RET            | explained_var       |   0.468094 |
|  3 | test       | RET            | pearsonr            |   0.704432 |
|  4 | test       | RET            | r2                  |   0.450234 |
|  5 | test       | RET            | mean_squared_error  | 652.795    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  1 | test       | CLS_KIT        | f1          | 0.540541 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.457048 |
|  3 | test       | CLS_KIT        | mcc         | 0.468918 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.800774 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.647994 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  21.9207   |
|  1 | test       | KIT            | spearmanr           |   0.515506 |
|  2 | test       | KIT            | explained_var       |   0.313224 |
|  3 | test       | KIT            | pearsonr            |   0.572251 |
|  4 | test       | KIT            | r2                  |   0.312316 |
|  5 | test       | KIT            | mean_squared_error  | 829.818    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | EGFR           | mean_absolute_error |  21.1084    |
|  1 | test       | EGFR           | spearmanr           |   0.0882894 |
|  2 | test       | EGFR           | explained_var       |   0.051465  |
|  3 | test       | EGFR           | pearsonr            |   0.33267   |
|  4 | test       | EGFR           | r2                  |   0.0499638 |
|  5 | test       | EGFR           | mean_squared_error  | 765.509     |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.381076 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.546043 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.394599 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.633238 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.393103 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.329047 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error |  0.81342   |
|  1 | test       | LOG_RPPB       | spearmanr           |  0.498261  |
|  2 | test       | LOG_RPPB       | explained_var       |  0.0509338 |
|  3 | test       | LOG_RPPB       | pearsonr            |  0.480318  |
|  4 | test       | LOG_RPPB       | r2                  | -0.0015365 |
|  5 | test       | LOG_RPPB       | mean_squared_error  |  0.889847  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.676691  |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.517534  |
|  2 | test       | LOG_HPPB       | explained_var       | 0.130551  |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.36193   |
|  4 | test       | LOG_HPPB       | r2                  | 0.0455946 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.578025  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.353536 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.72128  |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.55285  |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.744628 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.552614 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.221632 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.425923 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.711917 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.484139 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.709173 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.482162 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.292342 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.374655 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.650298 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.411241 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.657639 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.389563 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.2371   |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.464868 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.38653 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.379066 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.584425 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.169587 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.367959 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.58621 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.895652 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.534752 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.482737 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.621383 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.878966 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.326405 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.816348 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.878928 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.76462 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.615454 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6821332266019259,
    "polaris/pkis2-ret-wt-reg-v2": 652.7952891378242,
    "polaris/pkis2-kit-wt-cls-v2": 0.6479936067454919,
    "polaris/pkis2-kit-wt-reg-v2": 829.817841967738,
    "polaris/pkis2-egfr-wt-reg-v2": 765.5092163383484,
    "polaris/adme-fang-solu-1": 0.6332383443302706,
    "polaris/adme-fang-rppb-1": 0.48031752757629675,
    "polaris/adme-fang-hppb-1": 0.36193034298567167,
    "polaris/adme-fang-perm-1": 0.7446282213385044,
    "polaris/adme-fang-rclint-1": 0.7091732517842194,
    "polaris/adme-fang-hclint-1": 0.6576393666572433,
    "tdcommons/lipophilicity-astrazeneca": 0.4648681200061526,
    "tdcommons/ppbr-az": 8.386529773855464,
    "tdcommons/clearance-hepatocyte-az": 0.37906587649218376,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5844249805204265,
    "tdcommons/half-life-obach": 0.16958724954615112,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3679591251930433,
    "tdcommons/clearance-microsome-az": 0.5862095644538309,
    "tdcommons/dili": 0.8956521739130435,
    "tdcommons/bioavailability-ma": 0.5347522447622215,
    "tdcommons/vdss-lombardo": 0.482737443310048,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.621383363471971,
    "tdcommons/pgp-broccatelli": 0.8789656091708878,
    "tdcommons/caco2-wang": 0.326404557035375,
    "tdcommons/herg": 0.8163475699558174,
    "tdcommons/bbb-martins": 0.8789282363977486,
    "tdcommons/ames": 0.7646204155162624,
    "tdcommons/ld50-zhu": 0.6154536238110275
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.867925 |
|  1 | test       | CLS_RET        | f1          | 0.533333 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.457999 |
|  3 | test       | CLS_RET        | mcc         | 0.463591 |
|  4 | test       | CLS_RET        | roc_auc     | 0.855915 |
|  5 | test       | CLS_RET        | pr_auc      | 0.645994 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  19.7543   |
|  1 | test       | RET            | spearmanr           |   0.627192 |
|  2 | test       | RET            | explained_var       |   0.495479 |
|  3 | test       | RET            | pearsonr            |   0.704201 |
|  4 | test       | RET            | r2                  |   0.487862 |
|  5 | test       | RET            | mean_squared_error  | 608.115    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  1 | test       | CLS_KIT        | f1          | 0.540541 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.457048 |
|  3 | test       | CLS_KIT        | mcc         | 0.468918 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.789168 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.546446 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  22.5978   |
|  1 | test       | KIT            | spearmanr           |   0.473673 |
|  2 | test       | KIT            | explained_var       |   0.283183 |
|  3 | test       | KIT            | pearsonr            |   0.541162 |
|  4 | test       | KIT            | r2                  |   0.276462 |
|  5 | test       | KIT            | mean_squared_error  | 873.082    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  18.6959   |
|  1 | test       | EGFR           | spearmanr           |   0.229629 |
|  2 | test       | EGFR           | explained_var       |   0.322416 |
|  3 | test       | EGFR           | pearsonr            |   0.578612 |
|  4 | test       | EGFR           | r2                  |   0.322414 |
|  5 | test       | EGFR           | mean_squared_error  | 545.977    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.434418 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.472814 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.329174 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.573778 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.32559  |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.365651 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error |  0.815495  |
|  1 | test       | LOG_RPPB       | spearmanr           | -0.381739  |
|  2 | test       | LOG_RPPB       | explained_var       | -0.0211354 |
|  3 | test       | LOG_RPPB       | pearsonr            | -0.224194  |
|  4 | test       | LOG_RPPB       | r2                  | -0.0360997 |
|  5 | test       | LOG_RPPB       | mean_squared_error  |  0.920556  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error |  0.678766  |
|  1 | test       | LOG_HPPB       | spearmanr           |  0.0968752 |
|  2 | test       | LOG_HPPB       | explained_var       |  0.0102395 |
|  3 | test       | LOG_HPPB       | pearsonr            |  0.101977  |
|  4 | test       | LOG_HPPB       | r2                  | -0.0211843 |
|  5 | test       | LOG_HPPB       | mean_squared_error  |  0.618469  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.366417 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.743484 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.554663 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.746796 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.535723 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.229999 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.465838 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.642532 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.405899 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.638502 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.405222 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.335778 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.367727 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.659111 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.420577 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.659532 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.420111 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.225235 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.846263 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.73142 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.425396 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.636241 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.319157 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.384868 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.573657 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.90913 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.549052 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.439369 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.621722 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.848974 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.357737 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.803682 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.884342 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.838746 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.572325 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.64599421329456,
    "polaris/pkis2-ret-wt-reg-v2": 608.1147219043308,
    "polaris/pkis2-kit-wt-cls-v2": 0.5464460299348118,
    "polaris/pkis2-kit-wt-reg-v2": 873.0819008646446,
    "polaris/pkis2-egfr-wt-reg-v2": 545.9771288949414,
    "polaris/adme-fang-solu-1": 0.5737781119268607,
    "polaris/adme-fang-rppb-1": -0.22419446438294446,
    "polaris/adme-fang-hppb-1": 0.10197720783940593,
    "polaris/adme-fang-perm-1": 0.7467958010418747,
    "polaris/adme-fang-rclint-1": 0.638501919897101,
    "polaris/adme-fang-hclint-1": 0.6595324758642214,
    "tdcommons/lipophilicity-astrazeneca": 0.8462634111188706,
    "tdcommons/ppbr-az": 9.731423991686118,
    "tdcommons/clearance-hepatocyte-az": 0.42539611554160844,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6362411716079854,
    "tdcommons/half-life-obach": 0.31915667045089735,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.38486773834071275,
    "tdcommons/clearance-microsome-az": 0.5736572299973025,
    "tdcommons/dili": 0.9091304347826087,
    "tdcommons/bioavailability-ma": 0.5490522115064849,
    "tdcommons/vdss-lombardo": 0.4393689018898167,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6217224231464739,
    "tdcommons/pgp-broccatelli": 0.8489736070381232,
    "tdcommons/caco2-wang": 0.3577373555636396,
    "tdcommons/herg": 0.8036818851251841,
    "tdcommons/bbb-martins": 0.8843417761100688,
    "tdcommons/ames": 0.8387456186727761,
    "tdcommons/ld50-zhu": 0.5723249164879403
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.839623 |
|  1 | test       | CLS_RET        | f1          | 0        |
|  2 | test       | CLS_RET        | cohen_kappa | 0        |
|  3 | test       | CLS_RET        | mcc         | 0        |
|  4 | test       | CLS_RET        | roc_auc     | 0.679445 |
|  5 | test       | CLS_RET        | pr_auc      | 0.511413 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  19.6389   |
|  1 | test       | RET            | spearmanr           |   0.587649 |
|  2 | test       | RET            | explained_var       |   0.414224 |
|  3 | test       | RET            | pearsonr            |   0.662982 |
|  4 | test       | RET            | r2                  |   0.414222 |
|  5 | test       | RET            | mean_squared_error  | 695.556    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.87931  |
|  1 | test       | CLS_KIT        | f1          | 0.611111 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.54382  |
|  3 | test       | CLS_KIT        | mcc         | 0.563295 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.82205  |
|  5 | test       | CLS_KIT        | pr_auc      | 0.683027 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  21.767    |
|  1 | test       | KIT            | spearmanr           |   0.505421 |
|  2 | test       | KIT            | explained_var       |   0.352388 |
|  3 | test       | KIT            | pearsonr            |   0.597053 |
|  4 | test       | KIT            | r2                  |   0.243836 |
|  5 | test       | KIT            | mean_squared_error  | 912.451    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  17.9142   |
|  1 | test       | EGFR           | spearmanr           |   0.354259 |
|  2 | test       | EGFR           | explained_var       |   0.365982 |
|  3 | test       | EGFR           | pearsonr            |   0.626052 |
|  4 | test       | EGFR           | r2                  |   0.354509 |
|  5 | test       | EGFR           | mean_squared_error  | 520.116    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.397857 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.506044 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.359843 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.601531 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.359367 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.347338 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error |  0.828149  |
|  1 | test       | LOG_RPPB       | spearmanr           |  0.366087  |
|  2 | test       | LOG_RPPB       | explained_var       |  0.0361089 |
|  3 | test       | LOG_RPPB       | pearsonr            |  0.215466  |
|  4 | test       | LOG_RPPB       | r2                  | -0.0494243 |
|  5 | test       | LOG_RPPB       | mean_squared_error  |  0.932395  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error |  0.734977  |
|  1 | test       | LOG_HPPB       | spearmanr           |  0.490794  |
|  2 | test       | LOG_HPPB       | explained_var       |  0.0954495 |
|  3 | test       | LOG_HPPB       | pearsonr            |  0.424233  |
|  4 | test       | LOG_HPPB       | r2                  | -0.132151  |
|  5 | test       | LOG_HPPB       | mean_squared_error  |  0.685674  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.353056 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.740505 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.56041  |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.749487 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.55588  |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.220014 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.453133 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.66889  |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.444053 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.666444 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.443327 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.314266 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.351283 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.673651 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.467867 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.688743 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.46341  |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.208417 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.461447 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 10.6022 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.359952 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.545559 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.192216 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.372521 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.547676 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.918261 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.527769 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.486854 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.501921 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.873234 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.498156 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.812371 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.877384 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.821827 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.580016 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5114128761686896,
    "polaris/pkis2-ret-wt-reg-v2": 695.5557760762615,
    "polaris/pkis2-kit-wt-cls-v2": 0.6830269972272776,
    "polaris/pkis2-kit-wt-reg-v2": 912.4510125469826,
    "polaris/pkis2-egfr-wt-reg-v2": 520.1161044592025,
    "polaris/adme-fang-solu-1": 0.6015313080474349,
    "polaris/adme-fang-rppb-1": 0.21546585462828294,
    "polaris/adme-fang-hppb-1": 0.42423275820870326,
    "polaris/adme-fang-perm-1": 0.7494866987628422,
    "polaris/adme-fang-rclint-1": 0.6664439504564054,
    "polaris/adme-fang-hclint-1": 0.6887427431247544,
    "tdcommons/lipophilicity-astrazeneca": 0.46144679630370367,
    "tdcommons/ppbr-az": 10.60220434526638,
    "tdcommons/clearance-hepatocyte-az": 0.3599521043906917,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5455587029116641,
    "tdcommons/half-life-obach": 0.19221646315196617,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3725210043146578,
    "tdcommons/clearance-microsome-az": 0.5476763006121849,
    "tdcommons/dili": 0.9182608695652174,
    "tdcommons/bioavailability-ma": 0.5277685400731627,
    "tdcommons/vdss-lombardo": 0.48685422075594204,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5019213381555154,
    "tdcommons/pgp-broccatelli": 0.8732338043188483,
    "tdcommons/caco2-wang": 0.4981555710355654,
    "tdcommons/herg": 0.8123711340206186,
    "tdcommons/bbb-martins": 0.8773843026891808,
    "tdcommons/ames": 0.8218273316493372,
    "tdcommons/ld50-zhu": 0.5800157176025503
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.886792 |
|  1 | test       | CLS_RET        | f1          | 0.6      |
|  2 | test       | CLS_RET        | cohen_kappa | 0.535427 |
|  3 | test       | CLS_RET        | mcc         | 0.541965 |
|  4 | test       | CLS_RET        | roc_auc     | 0.865829 |
|  5 | test       | CLS_RET        | pr_auc      | 0.658084 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  23.9506   |
|  1 | test       | RET            | spearmanr           |   0.531568 |
|  2 | test       | RET            | explained_var       |   0.269668 |
|  3 | test       | RET            | pearsonr            |   0.522768 |
|  4 | test       | RET            | r2                  |   0.26606  |
|  5 | test       | RET            | mean_squared_error  | 871.484    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.827586 |
|  1 | test       | CLS_KIT        | f1          | 0.444444 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.348315 |
|  3 | test       | CLS_KIT        | mcc         | 0.360788 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.796905 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.498192 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  21.8759   |
|  1 | test       | KIT            | spearmanr           |   0.494285 |
|  2 | test       | KIT            | explained_var       |   0.29311  |
|  3 | test       | KIT            | pearsonr            |   0.55879  |
|  4 | test       | KIT            | r2                  |   0.264192 |
|  5 | test       | KIT            | mean_squared_error  | 887.888    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  18.6485   |
|  1 | test       | EGFR           | spearmanr           |   0.201791 |
|  2 | test       | EGFR           | explained_var       |   0.283003 |
|  3 | test       | EGFR           | pearsonr            |   0.564073 |
|  4 | test       | EGFR           | r2                  |   0.281475 |
|  5 | test       | EGFR           | mean_squared_error  | 578.964    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.408085 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.499536 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.336839 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.597941 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.331163 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.362629 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.740414  |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.393043  |
|  2 | test       | LOG_RPPB       | explained_var       | 0.036455  |
|  3 | test       | LOG_RPPB       | pearsonr            | 0.221679  |
|  4 | test       | LOG_RPPB       | r2                  | 0.0114667 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.878294  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error |  0.688923  |
|  1 | test       | LOG_HPPB       | spearmanr           |  0.301475  |
|  2 | test       | LOG_HPPB       | explained_var       |  0.0413782 |
|  3 | test       | LOG_HPPB       | pearsonr            |  0.20547   |
|  4 | test       | LOG_HPPB       | r2                  | -0.0111851 |
|  5 | test       | LOG_HPPB       | mean_squared_error  |  0.612413  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.342688 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.736511 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.560185 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.751099 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.559952 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.217997 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.437404 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.697599 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.469477 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.695094 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.462924 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.303203 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.361503 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.665926 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.421664 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.671167 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.421142 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.224834 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.478563 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.58852 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.352616 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.526904 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |      Score |
|---:|:-----------|:---------------|:----------|-----------:|
|  0 | test       | Y              | spearmanr | -0.0884565 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.371465 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.556051 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.913043 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.512803 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.50898 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.520683 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.834577 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.337329 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.765096 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.889032 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.795647 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.628996 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6580838895153623,
    "polaris/pkis2-ret-wt-reg-v2": 871.4842736696947,
    "polaris/pkis2-kit-wt-cls-v2": 0.49819230855807856,
    "polaris/pkis2-kit-wt-reg-v2": 887.8877394372416,
    "polaris/pkis2-egfr-wt-reg-v2": 578.9644650228657,
    "polaris/adme-fang-solu-1": 0.5979405986314399,
    "polaris/adme-fang-rppb-1": 0.2216792986103354,
    "polaris/adme-fang-hppb-1": 0.20547004039098304,
    "polaris/adme-fang-perm-1": 0.751098772448377,
    "polaris/adme-fang-rclint-1": 0.6950942557779576,
    "polaris/adme-fang-hclint-1": 0.6711673856097788,
    "tdcommons/lipophilicity-astrazeneca": 0.4785630736294247,
    "tdcommons/ppbr-az": 8.58851861233788,
    "tdcommons/clearance-hepatocyte-az": 0.3526164364715666,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.526904243442628,
    "tdcommons/half-life-obach": -0.08845649667645372,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3714652615539903,
    "tdcommons/clearance-microsome-az": 0.5560513664409397,
    "tdcommons/dili": 0.9130434782608695,
    "tdcommons/bioavailability-ma": 0.5128034585966079,
    "tdcommons/vdss-lombardo": 0.5089798961613662,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5206826401446655,
    "tdcommons/pgp-broccatelli": 0.8345774460143962,
    "tdcommons/caco2-wang": 0.337328966424242,
    "tdcommons/herg": 0.7650957290132547,
    "tdcommons/bbb-martins": 0.8890322076297686,
    "tdcommons/ames": 0.7956470657345944,
    "tdcommons/ld50-zhu": 0.628996488511159
}
```
