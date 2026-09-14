# ChemProp Baseline Results
timestamp: 2026-09-14 13:33:32.583577
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.516129 |
|  1 | test       | CLS_RET        | roc_auc     | 0.877065 |
|  2 | test       | CLS_RET        | pr_auc      | 0.698193 |
|  3 | test       | CLS_RET        | mcc         | 0.436971 |
|  4 | test       | CLS_RET        | accuracy    | 0.858491 |
|  5 | test       | CLS_RET        | cohen_kappa | 0.434164 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.377547 |
|  1 | test       | RET            | spearmanr           |   0.602381 |
|  2 | test       | RET            | pearsonr            |   0.642359 |
|  3 | test       | RET            | mean_absolute_error |  20.8327   |
|  4 | test       | RET            | explained_var       |   0.403595 |
|  5 | test       | RET            | mean_squared_error  | 739.104    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.564103 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.860735 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.663437 |
|  3 | test       | CLS_KIT        | mcc         | 0.483492 |
|  4 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.477754 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.279357 |
|  1 | test       | KIT            | spearmanr           |   0.510423 |
|  2 | test       | KIT            | pearsonr            |   0.602464 |
|  3 | test       | KIT            | mean_absolute_error |  21.4367   |
|  4 | test       | KIT            | explained_var       |   0.355892 |
|  5 | test       | KIT            | mean_squared_error  | 869.589    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.398153 |
|  1 | test       | EGFR           | spearmanr           |   0.316404 |
|  2 | test       | EGFR           | pearsonr            |   0.63182  |
|  3 | test       | EGFR           | mean_absolute_error |  17.2152   |
|  4 | test       | EGFR           | explained_var       |   0.398367 |
|  5 | test       | EGFR           | mean_squared_error  | 484.95     |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.342893 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.460064 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.593517 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.413964 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.346318 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.356269 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.124773 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.512174 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.3693   |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.645684 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.132354 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.777623 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.283865 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.775155 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.741729 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.59194  |
|  4 | test       | LOG_HPPB       | explained_var       | 0.311906 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.433719 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.616166 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.790852 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.791541 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.309605 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.62559  |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.190148 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.525643 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.748073 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.741395 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.409285 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.546661 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.267795 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.466199 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.715936 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.70354  |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.347801 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.469248 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.207334 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.442961 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.48491 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.402118 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.668282 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.266816 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.436195 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.597204 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.932609 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.63718 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.509118 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.574254 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.91189 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.322623 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.855228 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.908185 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.850757 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.601212 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.698193031177516,
    "polaris/pkis2-ret-wt-reg-v2": 739.1041216923271,
    "polaris/pkis2-kit-wt-cls-v2": 0.6634374574149149,
    "polaris/pkis2-kit-wt-reg-v2": 869.5888592979896,
    "polaris/pkis2-egfr-wt-reg-v2": 484.94965691060236,
    "polaris/adme-fang-solu-1": 0.5935174644063691,
    "polaris/adme-fang-rppb-1": 0.369300368368586,
    "polaris/adme-fang-hppb-1": 0.7417290049462558,
    "polaris/adme-fang-perm-1": 0.7915411245456998,
    "polaris/adme-fang-rclint-1": 0.7413946069436159,
    "polaris/adme-fang-hclint-1": 0.7035397290358234,
    "tdcommons/lipophilicity-astrazeneca": 0.44296051863261626,
    "tdcommons/ppbr-az": 7.48491155825702,
    "tdcommons/clearance-hepatocyte-az": 0.40211845706207694,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6682817851105219,
    "tdcommons/half-life-obach": 0.26681553260400903,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4361950946278795,
    "tdcommons/clearance-microsome-az": 0.5972038946941373,
    "tdcommons/dili": 0.932608695652174,
    "tdcommons/bioavailability-ma": 0.6371799135350849,
    "tdcommons/vdss-lombardo": 0.509117526898837,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5742540687160941,
    "tdcommons/pgp-broccatelli": 0.9118901626233005,
    "tdcommons/caco2-wang": 0.32262315559403976,
    "tdcommons/herg": 0.8552282768777615,
    "tdcommons/bbb-martins": 0.9081848030018762,
    "tdcommons/ames": 0.8507568192053888,
    "tdcommons/ld50-zhu": 0.6012124959896641
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.666667 |
|  1 | test       | CLS_RET        | roc_auc     | 0.884997 |
|  2 | test       | CLS_RET        | pr_auc      | 0.741348 |
|  3 | test       | CLS_RET        | mcc         | 0.65052  |
|  4 | test       | CLS_RET        | accuracy    | 0.915094 |
|  5 | test       | CLS_RET        | cohen_kappa | 0.621729 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.242452 |
|  1 | test       | RET            | spearmanr           |   0.526176 |
|  2 | test       | RET            | pearsonr            |   0.585991 |
|  3 | test       | RET            | mean_absolute_error |  22.4844   |
|  4 | test       | RET            | explained_var       |   0.321014 |
|  5 | test       | RET            | mean_squared_error  | 899.516    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.571429 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.816248 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.699382 |
|  3 | test       | CLS_KIT        | mcc         | 0.477761 |
|  4 | test       | CLS_KIT        | accuracy    | 0.844828 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.476954 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.282136 |
|  1 | test       | KIT            | spearmanr           |   0.531735 |
|  2 | test       | KIT            | pearsonr            |   0.594358 |
|  3 | test       | KIT            | mean_absolute_error |  21.6855   |
|  4 | test       | KIT            | explained_var       |   0.319912 |
|  5 | test       | KIT            | mean_squared_error  | 866.235    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.341661 |
|  1 | test       | EGFR           | spearmanr           |   0.201741 |
|  2 | test       | EGFR           | pearsonr            |   0.588173 |
|  3 | test       | EGFR           | mean_absolute_error |  18.4518   |
|  4 | test       | EGFR           | explained_var       |   0.343963 |
|  5 | test       | EGFR           | mean_squared_error  | 530.469    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.389763 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.524627 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.626228 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.401002 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.392007 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.330858 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.218353 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.628696 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.516453 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.655335 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.226756 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.694479 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.44866  |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.712507 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.713128 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.471637 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.464862 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.333913 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.590556 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.77674  |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.784336 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.341697 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.614727 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.202835 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.528091 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.727922 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.730702 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.410168 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.531996 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.266413 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.467643 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.706528 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.70412  |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.359064 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.469835 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.206773 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.436039 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.46798 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.434004 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   |  0.7129 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.038136 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.379094 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.617057 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.943043 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.452278 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.452376 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.583748 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.91409 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.31691 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.821797 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.908028 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.836355 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.547744 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7413478264344135,
    "polaris/pkis2-ret-wt-reg-v2": 899.5161137930697,
    "polaris/pkis2-kit-wt-cls-v2": 0.6993821658007096,
    "polaris/pkis2-kit-wt-reg-v2": 866.2353801957939,
    "polaris/pkis2-egfr-wt-reg-v2": 530.4689089883942,
    "polaris/adme-fang-solu-1": 0.6262282534353292,
    "polaris/adme-fang-rppb-1": 0.5164529523203908,
    "polaris/adme-fang-hppb-1": 0.7131283461504299,
    "polaris/adme-fang-perm-1": 0.7843358885000061,
    "polaris/adme-fang-rclint-1": 0.7307021180917919,
    "polaris/adme-fang-hclint-1": 0.7041195429529125,
    "tdcommons/lipophilicity-astrazeneca": 0.43603908869198393,
    "tdcommons/ppbr-az": 7.467977513294527,
    "tdcommons/clearance-hepatocyte-az": 0.43400431890469776,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7128998905978897,
    "tdcommons/half-life-obach": 0.03813601718609578,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.37909364133055656,
    "tdcommons/clearance-microsome-az": 0.6170568081876683,
    "tdcommons/dili": 0.9430434782608696,
    "tdcommons/bioavailability-ma": 0.4522780179580978,
    "tdcommons/vdss-lombardo": 0.4523755142515162,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.58374773960217,
    "tdcommons/pgp-broccatelli": 0.9140895761130365,
    "tdcommons/caco2-wang": 0.3169095737771507,
    "tdcommons/herg": 0.8217967599410898,
    "tdcommons/bbb-martins": 0.9080284552845528,
    "tdcommons/ames": 0.836354735749672,
    "tdcommons/ld50-zhu": 0.5477435731636171
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.551724 |
|  1 | test       | CLS_RET        | roc_auc     | 0.881692 |
|  2 | test       | CLS_RET        | pr_auc      | 0.640854 |
|  3 | test       | CLS_RET        | mcc         | 0.49296  |
|  4 | test       | CLS_RET        | accuracy    | 0.877358 |
|  5 | test       | CLS_RET        | cohen_kappa | 0.483121 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.453645 |
|  1 | test       | RET            | spearmanr           |   0.596291 |
|  2 | test       | RET            | pearsonr            |   0.690766 |
|  3 | test       | RET            | mean_absolute_error |  18.899    |
|  4 | test       | RET            | explained_var       |   0.476111 |
|  5 | test       | RET            | mean_squared_error  | 648.745    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.6      |
|  1 | test       | CLS_KIT        | roc_auc     | 0.824952 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.704646 |
|  3 | test       | CLS_KIT        | mcc         | 0.521477 |
|  4 | test       | CLS_KIT        | accuracy    | 0.862069 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.517672 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.333192 |
|  1 | test       | KIT            | spearmanr           |   0.556176 |
|  2 | test       | KIT            | pearsonr            |   0.616426 |
|  3 | test       | KIT            | mean_absolute_error |  20.9156   |
|  4 | test       | KIT            | explained_var       |   0.367996 |
|  5 | test       | KIT            | mean_squared_error  | 804.627    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.475584 |
|  1 | test       | EGFR           | spearmanr           |   0.391678 |
|  2 | test       | EGFR           | pearsonr            |   0.692347 |
|  3 | test       | EGFR           | mean_absolute_error |  16.1962   |
|  4 | test       | EGFR           | explained_var       |   0.475598 |
|  5 | test       | EGFR           | mean_squared_error  | 422.558    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.375292 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.54774  |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.623935 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.372201 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.389129 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.338704 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.528869 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.817391 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.753931 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.471191 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.528943 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.418592 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |     Score |
|---:|:-----------|:---------------|:--------------------|----------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.0852817 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.691573  |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.642118  |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.663329  |
|  4 | test       | LOG_HPPB       | explained_var       | 0.158879  |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.553989  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.614932 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.79091  |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.79497  |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.328008 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.630892 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.19076  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.528196 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.735049 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.72957  |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.411166 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.529146 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.266354 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.430511 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.704186 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.68974  |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.359911 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.448431 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.221195 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.436123 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.58905 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.406847 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.646472 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.26776 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.443124 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.627075 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.932609 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.608247 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.50043 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.583296 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.903892 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.38722 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.850221 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.907677 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.840698 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.567457 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6408543134622039,
    "polaris/pkis2-ret-wt-reg-v2": 648.7446896904758,
    "polaris/pkis2-kit-wt-cls-v2": 0.7046455291037736,
    "polaris/pkis2-kit-wt-reg-v2": 804.6271149596254,
    "polaris/pkis2-egfr-wt-reg-v2": 422.55784556639054,
    "polaris/adme-fang-solu-1": 0.6239349539787575,
    "polaris/adme-fang-rppb-1": 0.7539305583689333,
    "polaris/adme-fang-hppb-1": 0.6421176424762388,
    "polaris/adme-fang-perm-1": 0.794969822590737,
    "polaris/adme-fang-rclint-1": 0.7295697002971506,
    "polaris/adme-fang-hclint-1": 0.689740459111175,
    "tdcommons/lipophilicity-astrazeneca": 0.43612287355036966,
    "tdcommons/ppbr-az": 7.589050893766509,
    "tdcommons/clearance-hepatocyte-az": 0.406847489379481,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6464722404077313,
    "tdcommons/half-life-obach": 0.267760017685531,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.44312386399789355,
    "tdcommons/clearance-microsome-az": 0.6270754167170769,
    "tdcommons/dili": 0.932608695652174,
    "tdcommons/bioavailability-ma": 0.6082474226804124,
    "tdcommons/vdss-lombardo": 0.5004304319615716,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5832956600361664,
    "tdcommons/pgp-broccatelli": 0.9038922953878965,
    "tdcommons/caco2-wang": 0.387219954382626,
    "tdcommons/herg": 0.850220913107511,
    "tdcommons/bbb-martins": 0.9076766729205753,
    "tdcommons/ames": 0.840697879339717,
    "tdcommons/ld50-zhu": 0.5674569633023181
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.6875   |
|  1 | test       | CLS_RET        | roc_auc     | 0.859881 |
|  2 | test       | CLS_RET        | pr_auc      | 0.684927 |
|  3 | test       | CLS_RET        | mcc         | 0.633917 |
|  4 | test       | CLS_RET        | accuracy    | 0.90566  |
|  5 | test       | CLS_RET        | cohen_kappa | 0.6322   |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.394077 |
|  1 | test       | RET            | spearmanr           |   0.57635  |
|  2 | test       | RET            | pearsonr            |   0.640305 |
|  3 | test       | RET            | mean_absolute_error |  20.9827   |
|  4 | test       | RET            | explained_var       |   0.405879 |
|  5 | test       | RET            | mean_squared_error  | 719.476    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.564103 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.8206   |
|  2 | test       | CLS_KIT        | pr_auc      | 0.633936 |
|  3 | test       | CLS_KIT        | mcc         | 0.483492 |
|  4 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.477754 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.297585 |
|  1 | test       | KIT            | spearmanr           |   0.538046 |
|  2 | test       | KIT            | pearsonr            |   0.607884 |
|  3 | test       | KIT            | mean_absolute_error |  21.1859   |
|  4 | test       | KIT            | explained_var       |   0.366429 |
|  5 | test       | KIT            | mean_squared_error  | 847.593    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.430826 |
|  1 | test       | EGFR           | spearmanr           |   0.290697 |
|  2 | test       | EGFR           | pearsonr            |   0.658434 |
|  3 | test       | EGFR           | mean_absolute_error |  16.7708   |
|  4 | test       | EGFR           | explained_var       |   0.43117  |
|  5 | test       | EGFR           | mean_squared_error  | 458.623    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.387537 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.516    |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.622906 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.394071 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.38801  |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.332064 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.338799 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.713913 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.617631 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.56206  |
|  4 | test       | LOG_RPPB       | explained_var       | 0.339232 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.587465 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.380311 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.701811 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.747402 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.483076 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.505194 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.375307 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.616985 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.785496 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.788329 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.326734 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.616994 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.189743 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.503125 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.710981 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.714305 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.415703 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.507869 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.280508 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.433332 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.709557 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.700157 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.353617 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.433766 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.220099 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.424495 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.48021 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.438573 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.517537 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.32176 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.376613 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.611618 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.851739 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.559694 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.513644 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.558657 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.903759 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.348299 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.845803 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.833607 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.845045 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.605822 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6849271643389291,
    "polaris/pkis2-ret-wt-reg-v2": 719.4762382333707,
    "polaris/pkis2-kit-wt-cls-v2": 0.6339362247040448,
    "polaris/pkis2-kit-wt-reg-v2": 847.5930218892768,
    "polaris/pkis2-egfr-wt-reg-v2": 458.62262517687316,
    "polaris/adme-fang-solu-1": 0.622906216145895,
    "polaris/adme-fang-rppb-1": 0.6176311959642725,
    "polaris/adme-fang-hppb-1": 0.7474022332888864,
    "polaris/adme-fang-perm-1": 0.7883291081930578,
    "polaris/adme-fang-rclint-1": 0.7143053395243274,
    "polaris/adme-fang-hclint-1": 0.7001571625228343,
    "tdcommons/lipophilicity-astrazeneca": 0.4244946015108199,
    "tdcommons/ppbr-az": 7.4802094690531025,
    "tdcommons/clearance-hepatocyte-az": 0.4385725007238221,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5175369000453444,
    "tdcommons/half-life-obach": 0.32176037345663155,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.37661287839794694,
    "tdcommons/clearance-microsome-az": 0.6116182413688395,
    "tdcommons/dili": 0.8517391304347826,
    "tdcommons/bioavailability-ma": 0.559694047223146,
    "tdcommons/vdss-lombardo": 0.5136444455254078,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5586573236889694,
    "tdcommons/pgp-broccatelli": 0.9037589976006398,
    "tdcommons/caco2-wang": 0.34829939514129976,
    "tdcommons/herg": 0.8458026509572901,
    "tdcommons/bbb-martins": 0.8336069418386491,
    "tdcommons/ames": 0.845044939199906,
    "tdcommons/ld50-zhu": 0.6058223190230189
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.538462 |
|  1 | test       | CLS_RET        | roc_auc     | 0.860542 |
|  2 | test       | CLS_RET        | pr_auc      | 0.709554 |
|  3 | test       | CLS_RET        | mcc         | 0.512494 |
|  4 | test       | CLS_RET        | accuracy    | 0.886792 |
|  5 | test       | CLS_RET        | cohen_kappa | 0.480816 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.356492 |
|  1 | test       | RET            | spearmanr           |   0.602194 |
|  2 | test       | RET            | pearsonr            |   0.611378 |
|  3 | test       | RET            | mean_absolute_error |  20.6926   |
|  4 | test       | RET            | explained_var       |   0.370504 |
|  5 | test       | RET            | mean_squared_error  | 764.105    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.648649 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.844778 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.741989 |
|  3 | test       | CLS_KIT        | mcc         | 0.599989 |
|  4 | test       | CLS_KIT        | accuracy    | 0.887931 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.584802 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.263953 |
|  1 | test       | KIT            | spearmanr           |   0.498833 |
|  2 | test       | KIT            | pearsonr            |   0.554344 |
|  3 | test       | KIT            | mean_absolute_error |  21.9158   |
|  4 | test       | KIT            | explained_var       |   0.293502 |
|  5 | test       | KIT            | mean_squared_error  | 888.176    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.413448 |
|  1 | test       | EGFR           | spearmanr           |   0.330623 |
|  2 | test       | EGFR           | pearsonr            |   0.647361 |
|  3 | test       | EGFR           | mean_absolute_error |  17.0372   |
|  4 | test       | EGFR           | explained_var       |   0.413516 |
|  5 | test       | EGFR           | mean_squared_error  | 472.625    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.415953 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.549809 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.649484 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.370561 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.421829 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.316658 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.210711 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.552174 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.499899 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.634948 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.237804 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.701269 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.357799 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.79945  |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.751824 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.50515  |
|  4 | test       | LOG_HPPB       | explained_var       | 0.553331 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.388942 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.611534 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.786451 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.783096 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.323711 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.611905 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.192443 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.542777 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.744678 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.740162 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.399744 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.546369 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.258122 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.432517 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.718729 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.701349 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.360702 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.432711 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.220416 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.417899 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.14007 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.414315 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.582764 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.14694 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.432808 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.620048 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.932609 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.629199 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.392957 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.650882 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.928286 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.338059 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.820471 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.918269 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.831982 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.580823 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7095544055481382,
    "polaris/pkis2-ret-wt-reg-v2": 764.1050549714026,
    "polaris/pkis2-kit-wt-cls-v2": 0.7419886359224697,
    "polaris/pkis2-kit-wt-reg-v2": 888.1763509879612,
    "polaris/pkis2-egfr-wt-reg-v2": 472.6253644413554,
    "polaris/adme-fang-solu-1": 0.6494841235503493,
    "polaris/adme-fang-rppb-1": 0.4998987651795074,
    "polaris/adme-fang-hppb-1": 0.7518240429401002,
    "polaris/adme-fang-perm-1": 0.7830956910567459,
    "polaris/adme-fang-rclint-1": 0.7401620647607149,
    "polaris/adme-fang-hclint-1": 0.7013492650690344,
    "tdcommons/lipophilicity-astrazeneca": 0.41789903734979167,
    "tdcommons/ppbr-az": 8.140065974199707,
    "tdcommons/clearance-hepatocyte-az": 0.41431514766262956,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5827641104647288,
    "tdcommons/half-life-obach": 0.14694049367941808,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4328082025855349,
    "tdcommons/clearance-microsome-az": 0.6200484720672185,
    "tdcommons/dili": 0.9326086956521739,
    "tdcommons/bioavailability-ma": 0.629198536747589,
    "tdcommons/vdss-lombardo": 0.39295706552157555,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6508815551537069,
    "tdcommons/pgp-broccatelli": 0.9282857904558784,
    "tdcommons/caco2-wang": 0.3380591036458781,
    "tdcommons/herg": 0.8204712812960236,
    "tdcommons/bbb-martins": 0.9182692307692307,
    "tdcommons/ames": 0.8319822201335447,
    "tdcommons/ld50-zhu": 0.5808229898154654
}
```
