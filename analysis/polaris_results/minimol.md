# `minimol` MLP Results
timestamp: 2025-05-01 19:02:13.287783

## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.915094 |
|  1 | test       | CLS_RET        | f1          | 0.666667 |
|  2 | test       | CLS_RET        | roc_auc     | 0.942498 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.621729 |
|  4 | test       | CLS_RET        | pr_auc      | 0.851023 |
|  5 | test       | CLS_RET        | mcc         | 0.65052  |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.736403 |
|  1 | test       | RET            | explained_var       |   0.532611 |
|  2 | test       | RET            | r2                  |   0.512238 |
|  3 | test       | RET            | mean_absolute_error |  18.2639   |
|  4 | test       | RET            | spearmanr           |   0.663328 |
|  5 | test       | RET            | mean_squared_error  | 579.171    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  1 | test       | CLS_KIT        | f1          | 0.413793 |
|  2 | test       | CLS_KIT        | roc_auc     | 0.794004 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.354712 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.593392 |
|  5 | test       | CLS_KIT        | mcc         | 0.431481 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.486813 |
|  1 | test       | KIT            | explained_var       |   0.191486 |
|  2 | test       | KIT            | r2                  |   0.185729 |
|  3 | test       | KIT            | mean_absolute_error |  24.9348   |
|  4 | test       | KIT            | spearmanr           |   0.423964 |
|  5 | test       | KIT            | mean_squared_error  | 982.568    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.561161 |
|  1 | test       | EGFR           | explained_var       |   0.314778 |
|  2 | test       | EGFR           | r2                  |   0.253099 |
|  3 | test       | EGFR           | mean_absolute_error |  20.0308   |
|  4 | test       | EGFR           | spearmanr           |   0.385967 |
|  5 | test       | EGFR           | mean_squared_error  | 601.829    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.681049 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.463822 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.461654 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.38461  |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.555673 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.29188  |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | LOG_RPPB       | pearsonr            |  0.146509  |
|  1 | test       | LOG_RPPB       | explained_var       |  0.0199137 |
|  2 | test       | LOG_RPPB       | r2                  | -0.0463204 |
|  3 | test       | LOG_RPPB       | mean_absolute_error |  0.835573  |
|  4 | test       | LOG_RPPB       | spearmanr           |  0.163478  |
|  5 | test       | LOG_RPPB       | mean_squared_error  |  0.929637  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_HPPB       | pearsonr            | -0.284429 |
|  1 | test       | LOG_HPPB       | explained_var       | -0.187037 |
|  2 | test       | LOG_HPPB       | r2                  | -0.245089 |
|  3 | test       | LOG_HPPB       | mean_absolute_error |  0.771848 |
|  4 | test       | LOG_HPPB       | spearmanr           | -0.261135 |
|  5 | test       | LOG_HPPB       | mean_squared_error  |  0.754074 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.789688 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.623597 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.615096 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.317457 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.802601 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.190679 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.742477 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.550711 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.536625 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.403608 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.74331  |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.261595 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.742397 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.551031 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.538207 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.330452 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.731341 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.179365 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.48741 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.65137 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.405727 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.667431 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.16968 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.453468 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.618951 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.933913 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.675757 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0657942 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.647152 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.943415 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.286195 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.838439 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.901892 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.858724 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.616083 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.851023194874565,
    "polaris/pkis2-ret-wt-reg-v2": 579.1713339566504,
    "polaris/pkis2-kit-wt-cls-v2": 0.5933923698653115,
    "polaris/pkis2-kit-wt-reg-v2": 982.5682494487107,
    "polaris/pkis2-egfr-wt-reg-v2": 601.8292073748356,
    "polaris/adme-fang-solu-1": 0.6810489080559204,
    "polaris/adme-fang-rppb-1": 0.14650902666632298,
    "polaris/adme-fang-hppb-1": -0.28442860431476874,
    "polaris/adme-fang-perm-1": 0.7896882268056373,
    "polaris/adme-fang-rclint-1": 0.7424773748221534,
    "polaris/adme-fang-hclint-1": 0.7423974866309099,
    "tdcommons/lipophilicity-astrazeneca": 0.48741030835537685,
    "tdcommons/ppbr-az": 9.651369125011357,
    "tdcommons/clearance-hepatocyte-az": 0.40572717828312754,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6674310271234267,
    "tdcommons/half-life-obach": 0.16967972726127842,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.45346837212824403,
    "tdcommons/clearance-microsome-az": 0.6189513928863113,
    "tdcommons/dili": 0.9339130434782608,
    "tdcommons/bioavailability-ma": 0.6757565680079815,
    "tdcommons/vdss-lombardo": 0.06579416276993329,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6471518987341773,
    "tdcommons/pgp-broccatelli": 0.9434150893095175,
    "tdcommons/caco2-wang": 0.2861945715467851,
    "tdcommons/herg": 0.838438880706922,
    "tdcommons/bbb-martins": 0.9018918073796124,
    "tdcommons/ames": 0.8587244708139967,
    "tdcommons/ld50-zhu": 0.6160829477819925
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.924528 |
|  1 | test       | CLS_RET        | f1          | 0.692308 |
|  2 | test       | CLS_RET        | roc_auc     | 0.923992 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.653878 |
|  4 | test       | CLS_RET        | pr_auc      | 0.865513 |
|  5 | test       | CLS_RET        | mcc         | 0.696957 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.709759 |
|  1 | test       | RET            | explained_var       |   0.489969 |
|  2 | test       | RET            | r2                  |   0.432204 |
|  3 | test       | RET            | mean_absolute_error |  19.3357   |
|  4 | test       | RET            | spearmanr           |   0.64767  |
|  5 | test       | RET            | mean_squared_error  | 674.204    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.818966 |
|  1 | test       | CLS_KIT        | f1          | 0.461538 |
|  2 | test       | CLS_KIT        | roc_auc     | 0.794971 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.354873 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.516539 |
|  5 | test       | CLS_KIT        | mcc         | 0.359135 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.491586 |
|  1 | test       | KIT            | explained_var       |   0.20002  |
|  2 | test       | KIT            | r2                  |   0.20002  |
|  3 | test       | KIT            | mean_absolute_error |  24.5059   |
|  4 | test       | KIT            | spearmanr           |   0.484766 |
|  5 | test       | KIT            | mean_squared_error  | 965.323    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.578794 |
|  1 | test       | EGFR           | explained_var       |   0.331162 |
|  2 | test       | EGFR           | r2                  |   0.331081 |
|  3 | test       | EGFR           | mean_absolute_error |  17.2224   |
|  4 | test       | EGFR           | spearmanr           |   0.37397  |
|  5 | test       | EGFR           | mean_squared_error  | 538.993    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.690968 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.477413 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.472893 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.392066 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.578137 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.285786 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.637209 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.382578 |
|  2 | test       | LOG_RPPB       | r2                  | 0.377221 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.576236 |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.729565 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.553328 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.443867  |
|  1 | test       | LOG_HPPB       | explained_var       | 0.171974  |
|  2 | test       | LOG_HPPB       | r2                  | 0.0521256 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.65709   |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.405837  |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.574069  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.802734 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.643286 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.632755 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.320816 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.798463 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.18193  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.698908 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.488192 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.48789  |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.430166 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.694712 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.289108 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.71801  |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.515281 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.515278 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.340564 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.709088 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.188271 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.470574 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.08145 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.437722 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.676996 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.21161 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.474058 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.600147 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.958261 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.588627 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | -0.14298 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.679476 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.941949 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.314793 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.826951 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.917566 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.849094 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.597166 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.8655134081200655,
    "polaris/pkis2-ret-wt-reg-v2": 674.2035546893727,
    "polaris/pkis2-kit-wt-cls-v2": 0.5165394448009356,
    "polaris/pkis2-kit-wt-reg-v2": 965.3234660062498,
    "polaris/pkis2-egfr-wt-reg-v2": 538.993475796184,
    "polaris/adme-fang-solu-1": 0.6909682575136458,
    "polaris/adme-fang-rppb-1": 0.637209052775691,
    "polaris/adme-fang-hppb-1": 0.44386682988491316,
    "polaris/adme-fang-perm-1": 0.8027336946541437,
    "polaris/adme-fang-rclint-1": 0.6989082042777915,
    "polaris/adme-fang-hclint-1": 0.7180099420274828,
    "tdcommons/lipophilicity-astrazeneca": 0.4705743048020771,
    "tdcommons/ppbr-az": 9.081451995249086,
    "tdcommons/clearance-hepatocyte-az": 0.4377218100910761,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6769959008712423,
    "tdcommons/half-life-obach": 0.2116097116843012,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.47405761625596876,
    "tdcommons/clearance-microsome-az": 0.6001469835875571,
    "tdcommons/dili": 0.9582608695652174,
    "tdcommons/bioavailability-ma": 0.5886265380778185,
    "tdcommons/vdss-lombardo": -0.14297990054141865,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6794755877034357,
    "tdcommons/pgp-broccatelli": 0.9419488136496933,
    "tdcommons/caco2-wang": 0.3147927756907704,
    "tdcommons/herg": 0.8269513991163475,
    "tdcommons/bbb-martins": 0.9175656660412757,
    "tdcommons/ames": 0.8490943625291273,
    "tdcommons/ld50-zhu": 0.5971656458458494
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.90566  |
|  1 | test       | CLS_RET        | f1          | 0.615385 |
|  2 | test       | CLS_RET        | roc_auc     | 0.919365 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.567347 |
|  4 | test       | CLS_RET        | pr_auc      | 0.793604 |
|  5 | test       | CLS_RET        | mcc         | 0.604725 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.760698 |
|  1 | test       | RET            | explained_var       |   0.57399  |
|  2 | test       | RET            | r2                  |   0.561037 |
|  3 | test       | RET            | mean_absolute_error |  17.1611   |
|  4 | test       | RET            | spearmanr           |   0.684484 |
|  5 | test       | RET            | mean_squared_error  | 521.227    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.818966 |
|  1 | test       | CLS_KIT        | f1          | 0.322581 |
|  2 | test       | CLS_KIT        | roc_auc     | 0.797872 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.23875  |
|  4 | test       | CLS_KIT        | pr_auc      | 0.569506 |
|  5 | test       | CLS_KIT        | mcc         | 0.270692 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.484891 |
|  1 | test       | KIT            | explained_var       |   0.215393 |
|  2 | test       | KIT            | r2                  |   0.21396  |
|  3 | test       | KIT            | mean_absolute_error |  24.9398   |
|  4 | test       | KIT            | spearmanr           |   0.467913 |
|  5 | test       | KIT            | mean_squared_error  | 948.501    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.565043 |
|  1 | test       | EGFR           | explained_var       |   0.318892 |
|  2 | test       | EGFR           | r2                  |   0.313394 |
|  3 | test       | EGFR           | mean_absolute_error |  18.7419   |
|  4 | test       | EGFR           | spearmanr           |   0.387835 |
|  5 | test       | EGFR           | mean_squared_error  | 553.246    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.700224 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.488335 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.480508 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.376034 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.590849 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.281658 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.65709  |
|  1 | test       | LOG_RPPB       | explained_var       | 0.208124 |
|  2 | test       | LOG_RPPB       | r2                  | 0.166422 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.714835 |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.576522 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.740619 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.679189 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.460848 |
|  2 | test       | LOG_HPPB       | r2                  | 0.422383 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.473294 |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.629536 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.349827 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.794092 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.630458 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.630259 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.319525 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.799187 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.183167 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.735989 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.541418 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.539605 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.392493 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.737053 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.259913 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.718091 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.512253 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.511374 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.3422   |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.719074 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.189787 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.505835 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.79596 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.392634 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.720113 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.254776 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.492923 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.560329 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.939565 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.507815 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.480336 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.691456 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.940349 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.321466 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.799853 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.897475 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.851846 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.613341 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7936038293694003,
    "polaris/pkis2-ret-wt-reg-v2": 521.2265984175505,
    "polaris/pkis2-kit-wt-cls-v2": 0.5695063330376905,
    "polaris/pkis2-kit-wt-reg-v2": 948.5013481184828,
    "polaris/pkis2-egfr-wt-reg-v2": 553.2456014512577,
    "polaris/adme-fang-solu-1": 0.7002235502040565,
    "polaris/adme-fang-rppb-1": 0.6570900949145635,
    "polaris/adme-fang-hppb-1": 0.6791886501115822,
    "polaris/adme-fang-perm-1": 0.7940918660136109,
    "polaris/adme-fang-rclint-1": 0.7359894139096985,
    "polaris/adme-fang-hclint-1": 0.7180913260700108,
    "tdcommons/lipophilicity-astrazeneca": 0.5058347956055687,
    "tdcommons/ppbr-az": 8.795964256655125,
    "tdcommons/clearance-hepatocyte-az": 0.39263433177685103,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7201128360532533,
    "tdcommons/half-life-obach": 0.2547763025934197,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.49292329509828714,
    "tdcommons/clearance-microsome-az": 0.5603287889247056,
    "tdcommons/dili": 0.9395652173913043,
    "tdcommons/bioavailability-ma": 0.5078150981044229,
    "tdcommons/vdss-lombardo": 0.4803355186892362,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6914556962025317,
    "tdcommons/pgp-broccatelli": 0.9403492402026127,
    "tdcommons/caco2-wang": 0.3214661115986919,
    "tdcommons/herg": 0.7998527245949927,
    "tdcommons/bbb-martins": 0.8974749843652282,
    "tdcommons/ames": 0.8518455423055082,
    "tdcommons/ld50-zhu": 0.6133413447688494
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.896226 |
|  1 | test       | CLS_RET        | f1          | 0.521739 |
|  2 | test       | CLS_RET        | roc_auc     | 0.933906 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.478066 |
|  4 | test       | CLS_RET        | pr_auc      | 0.843579 |
|  5 | test       | CLS_RET        | mcc         | 0.560462 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.748644 |
|  1 | test       | RET            | explained_var       |   0.541904 |
|  2 | test       | RET            | r2                  |   0.540717 |
|  3 | test       | RET            | mean_absolute_error |  18.325    |
|  4 | test       | RET            | spearmanr           |   0.66957  |
|  5 | test       | RET            | mean_squared_error  | 545.355    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.87069  |
|  1 | test       | CLS_KIT        | f1          | 0.571429 |
|  2 | test       | CLS_KIT        | roc_auc     | 0.844778 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.501147 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.728709 |
|  5 | test       | CLS_KIT        | mcc         | 0.525226 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.576312 |
|  1 | test       | KIT            | explained_var       |   0.328783 |
|  2 | test       | KIT            | r2                  |   0.328236 |
|  3 | test       | KIT            | mean_absolute_error |  23.3552   |
|  4 | test       | KIT            | spearmanr           |   0.542094 |
|  5 | test       | KIT            | mean_squared_error  | 810.607    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.507156 |
|  1 | test       | EGFR           | explained_var       |   0.257199 |
|  2 | test       | EGFR           | r2                  |   0.241514 |
|  3 | test       | EGFR           | mean_absolute_error |  19.5252   |
|  4 | test       | EGFR           | spearmanr           |   0.294129 |
|  5 | test       | EGFR           | mean_squared_error  | 611.164    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.682384 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.464796 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.463423 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.376074 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.566626 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.290921 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | LOG_RPPB       | pearsonr            |  0.00702348 |
|  1 | test       | LOG_RPPB       | explained_var       | -0.0129439  |
|  2 | test       | LOG_RPPB       | r2                  | -0.0379088  |
|  3 | test       | LOG_RPPB       | mean_absolute_error |  0.803866   |
|  4 | test       | LOG_RPPB       | spearmanr           |  0.14       |
|  5 | test       | LOG_RPPB       | mean_squared_error  |  0.922163   |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.666142 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.433177 |
|  2 | test       | LOG_HPPB       | r2                  | 0.416395 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.501047 |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.605088 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.353454 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.790869 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.624878 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.6247   |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.31597  |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.808216 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.185921 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.747998 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.558895 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.555732 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.403196 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.74963  |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.250809 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.720306 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.514091 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.514091 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.337516 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.710754 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.188732 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.468789 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  8.5794 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.462401 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.661034 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0213235 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.394211 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.573467 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.949565 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.677752 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.362153 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.653481 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.93675 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.315054 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.797791 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.914204 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.853064 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.612571 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.8435786435786435,
    "polaris/pkis2-ret-wt-reg-v2": 545.3547172992594,
    "polaris/pkis2-kit-wt-cls-v2": 0.7287086269933609,
    "polaris/pkis2-kit-wt-reg-v2": 810.606858687971,
    "polaris/pkis2-egfr-wt-reg-v2": 611.164473646383,
    "polaris/adme-fang-solu-1": 0.6823835813116489,
    "polaris/adme-fang-rppb-1": 0.0070234841225999545,
    "polaris/adme-fang-hppb-1": 0.6661422888804198,
    "polaris/adme-fang-perm-1": 0.7908687284667666,
    "polaris/adme-fang-rclint-1": 0.7479982547182376,
    "polaris/adme-fang-hclint-1": 0.7203062330901907,
    "tdcommons/lipophilicity-astrazeneca": 0.46878937671298077,
    "tdcommons/ppbr-az": 8.57939893528046,
    "tdcommons/clearance-hepatocyte-az": 0.4624006817172439,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6610339363734572,
    "tdcommons/half-life-obach": 0.02132353492049774,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3942111295577495,
    "tdcommons/clearance-microsome-az": 0.5734668786359743,
    "tdcommons/dili": 0.9495652173913044,
    "tdcommons/bioavailability-ma": 0.6777519122048554,
    "tdcommons/vdss-lombardo": 0.36215341888761426,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6534810126582278,
    "tdcommons/pgp-broccatelli": 0.936750199946681,
    "tdcommons/caco2-wang": 0.3150544684390561,
    "tdcommons/herg": 0.7977908689248896,
    "tdcommons/bbb-martins": 0.9142041901188241,
    "tdcommons/ames": 0.8530635023203901,
    "tdcommons/ld50-zhu": 0.612571405144925
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.924528 |
|  1 | test       | CLS_RET        | f1          | 0.714286 |
|  2 | test       | CLS_RET        | roc_auc     | 0.923992 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.673092 |
|  4 | test       | CLS_RET        | pr_auc      | 0.862396 |
|  5 | test       | CLS_RET        | mcc         | 0.694283 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.69742  |
|  1 | test       | RET            | explained_var       |   0.475322 |
|  2 | test       | RET            | r2                  |   0.420006 |
|  3 | test       | RET            | mean_absolute_error |  19.6117   |
|  4 | test       | RET            | spearmanr           |   0.598868 |
|  5 | test       | RET            | mean_squared_error  | 688.688    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.887931 |
|  1 | test       | CLS_KIT        | f1          | 0.666667 |
|  2 | test       | CLS_KIT        | roc_auc     | 0.827853 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.600636 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.676243 |
|  5 | test       | CLS_KIT        | mcc         | 0.607849 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.522014 |
|  1 | test       | KIT            | explained_var       |   0.239562 |
|  2 | test       | KIT            | r2                  |   0.234983 |
|  3 | test       | KIT            | mean_absolute_error |  24.1229   |
|  4 | test       | KIT            | spearmanr           |   0.497437 |
|  5 | test       | KIT            | mean_squared_error  | 923.133    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.572174 |
|  1 | test       | EGFR           | explained_var       |   0.323572 |
|  2 | test       | EGFR           | r2                  |   0.323546 |
|  3 | test       | EGFR           | mean_absolute_error |  17.8822   |
|  4 | test       | EGFR           | spearmanr           |   0.425103 |
|  5 | test       | EGFR           | mean_squared_error  | 545.066    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.679775 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.456899 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.453326 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.385757 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.565044 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.296395 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.729671 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.462    |
|  2 | test       | LOG_RPPB       | r2                  | 0.460049 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.525705 |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.788696 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.479737 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.663344 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.438343 |
|  2 | test       | LOG_HPPB       | r2                  | 0.374274 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.504335 |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.617465 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.378964 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.783901 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.613434 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.6124   |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.328789 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.801561 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.192014 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.736051 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.53906  |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.537234 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.411128 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.739596 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.261251 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.722798 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.522262 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.512061 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.340913 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.725522 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.18952  |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.490094 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.66233 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.393638 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.649422 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.337185 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.43364 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.589488 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.944348 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.735949 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.296823 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.648056 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.945548 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.387194 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.833726 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.91352 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.850491 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.585139 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.8623959026570415,
    "polaris/pkis2-ret-wt-reg-v2": 688.6875008135049,
    "polaris/pkis2-kit-wt-cls-v2": 0.6762432357488428,
    "polaris/pkis2-kit-wt-reg-v2": 923.1334045977353,
    "polaris/pkis2-egfr-wt-reg-v2": 545.0656000878529,
    "polaris/adme-fang-solu-1": 0.6797753242150979,
    "polaris/adme-fang-rppb-1": 0.7296713412326099,
    "polaris/adme-fang-hppb-1": 0.6633436670188378,
    "polaris/adme-fang-perm-1": 0.7839008135648361,
    "polaris/adme-fang-rclint-1": 0.7360507993602234,
    "polaris/adme-fang-hclint-1": 0.7227979704501122,
    "tdcommons/lipophilicity-astrazeneca": 0.4900941756225768,
    "tdcommons/ppbr-az": 9.662332561950137,
    "tdcommons/clearance-hepatocyte-az": 0.3936382117966009,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6494219169669492,
    "tdcommons/half-life-obach": 0.3371850271411872,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.43363996879977773,
    "tdcommons/clearance-microsome-az": 0.5894875536276621,
    "tdcommons/dili": 0.9443478260869566,
    "tdcommons/bioavailability-ma": 0.735949451280346,
    "tdcommons/vdss-lombardo": 0.2968226959658971,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6480560578661844,
    "tdcommons/pgp-broccatelli": 0.9455478539056251,
    "tdcommons/caco2-wang": 0.38719355355358764,
    "tdcommons/herg": 0.8337260677466863,
    "tdcommons/bbb-martins": 0.9135201688555347,
    "tdcommons/ames": 0.8504905128355752,
    "tdcommons/ld50-zhu": 0.5851394358674954
}
```
