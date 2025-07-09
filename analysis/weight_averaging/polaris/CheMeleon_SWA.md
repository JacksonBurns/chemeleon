# ChemProp Baseline Results
timestamp: 2025-07-08 14:30:29.712386
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.848645 |
|  1 | test       | CLS_RET        | f1          | 0        |
|  2 | test       | CLS_RET        | accuracy    | 0.839623 |
|  3 | test       | CLS_RET        | pr_auc      | 0.569869 |
|  4 | test       | CLS_RET        | mcc         | 0        |
|  5 | test       | CLS_RET        | cohen_kappa | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.483593 |
|  1 | test       | RET            | r2                  |   0.435223 |
|  2 | test       | RET            | spearmanr           |   0.642785 |
|  3 | test       | RET            | mean_absolute_error |  18.9093   |
|  4 | test       | RET            | mean_squared_error  | 670.619    |
|  5 | test       | RET            | pearsonr            |   0.698348 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.850097 |
|  1 | test       | CLS_KIT        | f1          | 0.466667 |
|  2 | test       | CLS_KIT        | accuracy    | 0.862069 |
|  3 | test       | CLS_KIT        | pr_auc      | 0.72211  |
|  4 | test       | CLS_KIT        | mcc         | 0.475801 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.40665  |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.374114 |
|  1 | test       | KIT            | r2                  |   0.339847 |
|  2 | test       | KIT            | spearmanr           |   0.543286 |
|  3 | test       | KIT            | mean_absolute_error |  21.5793   |
|  4 | test       | KIT            | mean_squared_error  | 796.596    |
|  5 | test       | KIT            | pearsonr            |   0.61793  |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.463009 |
|  1 | test       | EGFR           | r2                  |   0.460229 |
|  2 | test       | EGFR           | spearmanr           |   0.389993 |
|  3 | test       | EGFR           | mean_absolute_error |  16.4105   |
|  4 | test       | EGFR           | mean_squared_error  | 434.931    |
|  5 | test       | EGFR           | pearsonr            |   0.682114 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.431858 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.427955 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.584003 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.369845 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.310151 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.657303 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.488043 |
|  1 | test       | LOG_RPPB       | r2                  | 0.487679 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.768696 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.51587  |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.455188 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.734159 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.584523 |
|  1 | test       | LOG_HPPB       | r2                  | 0.566862 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.772404 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.435582 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.262325 |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.773196 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.654886 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.654545 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.808395 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.302397 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.171136 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.809458 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.558195 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.552685 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.752457 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.400713 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.252529 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.747185 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.506719 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.498468 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.7171   |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.3422   |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.1948   |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.714706 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.445053 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  8.0452 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.398322 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.699718 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.209801 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.443346 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.577147 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  |     0.9 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.582973 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.584222 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.62387 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.92682 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.360757 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.855817 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.879182 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.836556 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.517209 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5698690534387517,
    "polaris/pkis2-ret-wt-reg-v2": 670.6185582667616,
    "polaris/pkis2-kit-wt-cls-v2": 0.7221102567779885,
    "polaris/pkis2-kit-wt-reg-v2": 796.5960778435806,
    "polaris/pkis2-egfr-wt-reg-v2": 434.930599924199,
    "polaris/adme-fang-solu-1": 0.6573028797817033,
    "polaris/adme-fang-rppb-1": 0.7341592170003981,
    "polaris/adme-fang-hppb-1": 0.7731959129687276,
    "polaris/adme-fang-perm-1": 0.8094578738358673,
    "polaris/adme-fang-rclint-1": 0.7471847513154783,
    "polaris/adme-fang-hclint-1": 0.7147064004881769,
    "tdcommons/lipophilicity-astrazeneca": 0.4450534935338157,
    "tdcommons/ppbr-az": 8.045200733328121,
    "tdcommons/clearance-hepatocyte-az": 0.3983217978726508,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6997178086069339,
    "tdcommons/half-life-obach": 0.20980063254924686,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.44334559612621977,
    "tdcommons/clearance-microsome-az": 0.5771473362941589,
    "tdcommons/dili": 0.8999999999999999,
    "tdcommons/bioavailability-ma": 0.5829730628533423,
    "tdcommons/vdss-lombardo": 0.5842224615799274,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6238698010849909,
    "tdcommons/pgp-broccatelli": 0.9268195147960544,
    "tdcommons/caco2-wang": 0.36075727101386784,
    "tdcommons/herg": 0.8558173784977909,
    "tdcommons/bbb-martins": 0.879182301438399,
    "tdcommons/ames": 0.8365564236621041,
    "tdcommons/ld50-zhu": 0.5172091968772536
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.8308   |
|  1 | test       | CLS_RET        | f1          | 0        |
|  2 | test       | CLS_RET        | accuracy    | 0.839623 |
|  3 | test       | CLS_RET        | pr_auc      | 0.570258 |
|  4 | test       | CLS_RET        | mcc         | 0        |
|  5 | test       | CLS_RET        | cohen_kappa | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.481486 |
|  1 | test       | RET            | r2                  |   0.370199 |
|  2 | test       | RET            | spearmanr           |   0.664908 |
|  3 | test       | RET            | mean_absolute_error |  19.7214   |
|  4 | test       | RET            | mean_squared_error  | 747.828    |
|  5 | test       | RET            | pearsonr            |   0.715224 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.797872 |
|  1 | test       | CLS_KIT        | f1          | 0.594595 |
|  2 | test       | CLS_KIT        | accuracy    | 0.87069  |
|  3 | test       | CLS_KIT        | pr_auc      | 0.645129 |
|  4 | test       | CLS_KIT        | mcc         | 0.534453 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.520925 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.305238 |
|  1 | test       | KIT            | r2                  |   0.295316 |
|  2 | test       | KIT            | spearmanr           |   0.551005 |
|  3 | test       | KIT            | mean_absolute_error |  21.8192   |
|  4 | test       | KIT            | mean_squared_error  | 850.331    |
|  5 | test       | KIT            | pearsonr            |   0.5904   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.455571 |
|  1 | test       | EGFR           | r2                  |   0.453988 |
|  2 | test       | EGFR           | spearmanr           |   0.378222 |
|  3 | test       | EGFR           | mean_absolute_error |  16.1431   |
|  4 | test       | EGFR           | mean_squared_error  | 439.959    |
|  5 | test       | EGFR           | pearsonr            |   0.677159 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.433746 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.431401 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.574866 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.381314 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.308282 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.663503 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.646459 |
|  1 | test       | LOG_RPPB       | r2                  | 0.645709 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.822609 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.42684  |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.314781 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.831385 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.571335 |
|  1 | test       | LOG_HPPB       | r2                  | 0.56853  |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.736038 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.425192 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.261315 |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.757131 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.675251 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.674612 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.812338 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.289895 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.161195 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.821884 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.552411 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.5518   |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.747205 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.397312 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.253029 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.743727 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.495841 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.495509 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.711669 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.349111 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.195949 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.709323 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.461554 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.77616 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.371172 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.717037 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.180914 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.416311 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.567848 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  |    0.92 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.60725 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.367959 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.629069 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.914756 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.315076 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.822239 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.905546 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.843823 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.536845 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.570257587319813,
    "polaris/pkis2-ret-wt-reg-v2": 747.8284059011859,
    "polaris/pkis2-kit-wt-cls-v2": 0.6451291680454561,
    "polaris/pkis2-kit-wt-reg-v2": 850.3309039674285,
    "polaris/pkis2-egfr-wt-reg-v2": 439.9590495699154,
    "polaris/adme-fang-solu-1": 0.6635026061691662,
    "polaris/adme-fang-rppb-1": 0.8313845256509707,
    "polaris/adme-fang-hppb-1": 0.7571313729996438,
    "polaris/adme-fang-perm-1": 0.8218843413273544,
    "polaris/adme-fang-rclint-1": 0.7437268379109999,
    "polaris/adme-fang-hclint-1": 0.7093231386253074,
    "tdcommons/lipophilicity-astrazeneca": 0.4615537146386646,
    "tdcommons/ppbr-az": 7.776156822300129,
    "tdcommons/clearance-hepatocyte-az": 0.3711720437545717,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.717036763414961,
    "tdcommons/half-life-obach": 0.18091384487012488,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.41631134938937675,
    "tdcommons/clearance-microsome-az": 0.5678479645507968,
    "tdcommons/dili": 0.92,
    "tdcommons/bioavailability-ma": 0.6072497505819755,
    "tdcommons/vdss-lombardo": 0.36795895452110605,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6290687160940326,
    "tdcommons/pgp-broccatelli": 0.9147560650493202,
    "tdcommons/caco2-wang": 0.3150763771087312,
    "tdcommons/herg": 0.822238586156112,
    "tdcommons/bbb-martins": 0.905546435272045,
    "tdcommons/ames": 0.84382306291488,
    "tdcommons/ld50-zhu": 0.5368454765086246
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.857237 |
|  1 | test       | CLS_RET        | f1          | 0        |
|  2 | test       | CLS_RET        | accuracy    | 0.839623 |
|  3 | test       | CLS_RET        | pr_auc      | 0.622532 |
|  4 | test       | CLS_RET        | mcc         | 0        |
|  5 | test       | CLS_RET        | cohen_kappa | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.478474 |
|  1 | test       | RET            | r2                  |   0.470859 |
|  2 | test       | RET            | spearmanr           |   0.66675  |
|  3 | test       | RET            | mean_absolute_error |  19.0487   |
|  4 | test       | RET            | mean_squared_error  | 628.304    |
|  5 | test       | RET            | pearsonr            |   0.695154 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.835106 |
|  1 | test       | CLS_KIT        | f1          | 0.296296 |
|  2 | test       | CLS_KIT        | accuracy    | 0.836207 |
|  3 | test       | CLS_KIT        | pr_auc      | 0.561018 |
|  4 | test       | CLS_KIT        | mcc         | 0.330432 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.243132 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.387297 |
|  1 | test       | KIT            | r2                  |   0.346633 |
|  2 | test       | KIT            | spearmanr           |   0.580729 |
|  3 | test       | KIT            | mean_absolute_error |  20.8654   |
|  4 | test       | KIT            | mean_squared_error  | 788.407    |
|  5 | test       | KIT            | pearsonr            |   0.625258 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.451494 |
|  1 | test       | EGFR           | r2                  |   0.446639 |
|  2 | test       | EGFR           | spearmanr           |   0.398982 |
|  3 | test       | EGFR           | mean_absolute_error |  16.7434   |
|  4 | test       | EGFR           | mean_squared_error  | 445.881    |
|  5 | test       | EGFR           | pearsonr            |   0.682694 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.404001 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.399771 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.564857 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.38259  |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.325431 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.635769 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.606525 |
|  1 | test       | LOG_RPPB       | r2                  | 0.605148 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.79913  |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.465707 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.350819 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.826625 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.600655 |
|  1 | test       | LOG_HPPB       | r2                  | 0.581757 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.771946 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.424105 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.253304 |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.776395 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.627714 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.620359 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.77974  |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.319828 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.188071 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.79274  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.548584 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.546457 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.742101 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.394864 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.256044 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.741429 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.507645 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.504295 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.724647 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.34019  |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.192537 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.716986 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.461877 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.85668 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.394868 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.698016 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.240549 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.437066 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.596247 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.883043 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.611906 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.501846 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.610533 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.909024 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.31937 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.862445 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.909826 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.859428 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.514215 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6225316778473764,
    "polaris/pkis2-ret-wt-reg-v2": 628.3044533535854,
    "polaris/pkis2-kit-wt-cls-v2": 0.5610183885653507,
    "polaris/pkis2-kit-wt-reg-v2": 788.406931570769,
    "polaris/pkis2-egfr-wt-reg-v2": 445.88065589452333,
    "polaris/adme-fang-solu-1": 0.6357687075041423,
    "polaris/adme-fang-rppb-1": 0.8266253372257346,
    "polaris/adme-fang-hppb-1": 0.7763953209014267,
    "polaris/adme-fang-perm-1": 0.7927396802904878,
    "polaris/adme-fang-rclint-1": 0.7414294360441612,
    "polaris/adme-fang-hclint-1": 0.7169864420556019,
    "tdcommons/lipophilicity-astrazeneca": 0.4618771851403372,
    "tdcommons/ppbr-az": 7.856683798911107,
    "tdcommons/clearance-hepatocyte-az": 0.3948675026548251,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6980160756939899,
    "tdcommons/half-life-obach": 0.24054893701320232,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4370662721919584,
    "tdcommons/clearance-microsome-az": 0.5962471516776178,
    "tdcommons/dili": 0.8830434782608696,
    "tdcommons/bioavailability-ma": 0.6119055537080146,
    "tdcommons/vdss-lombardo": 0.5018460944773021,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6105334538878843,
    "tdcommons/pgp-broccatelli": 0.9090242601972808,
    "tdcommons/caco2-wang": 0.31937027887928726,
    "tdcommons/herg": 0.8624447717231223,
    "tdcommons/bbb-martins": 0.909826454033771,
    "tdcommons/ames": 0.8594284203724374,
    "tdcommons/ld50-zhu": 0.514214957489535
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.566424 |
|  1 | test       | CLS_RET        | f1          | 0        |
|  2 | test       | CLS_RET        | accuracy    | 0.839623 |
|  3 | test       | CLS_RET        | pr_auc      | 0.176926 |
|  4 | test       | CLS_RET        | mcc         | 0        |
|  5 | test       | CLS_RET        | cohen_kappa | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.471974 |
|  1 | test       | RET            | r2                  |   0.458202 |
|  2 | test       | RET            | spearmanr           |   0.59699  |
|  3 | test       | RET            | mean_absolute_error |  19.6862   |
|  4 | test       | RET            | mean_squared_error  | 643.334    |
|  5 | test       | RET            | pearsonr            |   0.687078 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.852515 |
|  1 | test       | CLS_KIT        | f1          | 0.666667 |
|  2 | test       | CLS_KIT        | accuracy    | 0.87069  |
|  3 | test       | CLS_KIT        | pr_auc      | 0.721702 |
|  4 | test       | CLS_KIT        | mcc         | 0.586725 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.586502 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.369941 |
|  1 | test       | KIT            | r2                  |   0.344116 |
|  2 | test       | KIT            | spearmanr           |   0.555087 |
|  3 | test       | KIT            | mean_absolute_error |  21.0756   |
|  4 | test       | KIT            | mean_squared_error  | 791.444    |
|  5 | test       | KIT            | pearsonr            |   0.617083 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.430689 |
|  1 | test       | EGFR           | r2                  |   0.428999 |
|  2 | test       | EGFR           | spearmanr           |   0.35224  |
|  3 | test       | EGFR           | mean_absolute_error |  16.7274   |
|  4 | test       | EGFR           | mean_squared_error  | 460.095    |
|  5 | test       | EGFR           | pearsonr            |   0.666583 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.405873 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.405858 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.555451 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.379794 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.322131 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.644947 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.546797 |
|  1 | test       | LOG_RPPB       | r2                  | 0.538531 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.763478 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.506883 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.410007 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.78089  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.541123 |
|  1 | test       | LOG_HPPB       | r2                  | 0.490762 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.716785 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.48657  |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.308414 |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.73694  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.665144 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.662696 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.806342 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.300649 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.167098 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.815564 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.561854 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.560384 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.75496  |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.395429 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.248182 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.749573 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.531398 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.521093 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.735268 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.330779 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.186012 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.731104 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.450781 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.44965 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.391739 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.61754 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.295684 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.43413 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.601881 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.926522 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.645494 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.53851 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.587703 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.924687 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.377552 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.875847 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.807653 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.841996 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.528556 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.17692567930248676,
    "polaris/pkis2-ret-wt-reg-v2": 643.3339030869732,
    "polaris/pkis2-kit-wt-cls-v2": 0.7217020984218352,
    "polaris/pkis2-kit-wt-reg-v2": 791.4443878852776,
    "polaris/pkis2-egfr-wt-reg-v2": 460.0945556500524,
    "polaris/adme-fang-solu-1": 0.6449469980871474,
    "polaris/adme-fang-rppb-1": 0.780889505830801,
    "polaris/adme-fang-hppb-1": 0.7369400966197742,
    "polaris/adme-fang-perm-1": 0.8155639718040579,
    "polaris/adme-fang-rclint-1": 0.7495728357998396,
    "polaris/adme-fang-hclint-1": 0.731103669226024,
    "tdcommons/lipophilicity-astrazeneca": 0.4507811715091978,
    "tdcommons/ppbr-az": 7.449647102151232,
    "tdcommons/clearance-hepatocyte-az": 0.39173913136263266,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6175404705784815,
    "tdcommons/half-life-obach": 0.29568395778597384,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.43412985840606355,
    "tdcommons/clearance-microsome-az": 0.6018805178091579,
    "tdcommons/dili": 0.9265217391304348,
    "tdcommons/bioavailability-ma": 0.6454938476887264,
    "tdcommons/vdss-lombardo": 0.5385097058648883,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5877034358047016,
    "tdcommons/pgp-broccatelli": 0.9246867501999467,
    "tdcommons/caco2-wang": 0.3775519342476981,
    "tdcommons/herg": 0.8758468335787923,
    "tdcommons/bbb-martins": 0.807653220762977,
    "tdcommons/ames": 0.841996122892557,
    "tdcommons/ld50-zhu": 0.5285560438139352
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.840714 |
|  1 | test       | CLS_RET        | f1          | 0        |
|  2 | test       | CLS_RET        | accuracy    | 0.839623 |
|  3 | test       | CLS_RET        | pr_auc      | 0.615548 |
|  4 | test       | CLS_RET        | mcc         | 0        |
|  5 | test       | CLS_RET        | cohen_kappa | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | explained_var       |   0.431421 |
|  1 | test       | RET            | r2                  |   0.407195 |
|  2 | test       | RET            | spearmanr           |   0.625542 |
|  3 | test       | RET            | mean_absolute_error |  20.5606   |
|  4 | test       | RET            | mean_squared_error  | 703.9      |
|  5 | test       | RET            | pearsonr            |   0.663404 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.890232 |
|  1 | test       | CLS_KIT        | f1          | 0.666667 |
|  2 | test       | CLS_KIT        | accuracy    | 0.896552 |
|  3 | test       | CLS_KIT        | pr_auc      | 0.779992 |
|  4 | test       | CLS_KIT        | mcc         | 0.630797 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.608989 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | explained_var       |   0.312038 |
|  1 | test       | KIT            | r2                  |   0.301392 |
|  2 | test       | KIT            | spearmanr           |   0.542047 |
|  3 | test       | KIT            | mean_absolute_error |  21.4265   |
|  4 | test       | KIT            | mean_squared_error  | 842.999    |
|  5 | test       | KIT            | pearsonr            |   0.588108 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | explained_var       |   0.364551 |
|  1 | test       | EGFR           | r2                  |   0.355216 |
|  2 | test       | EGFR           | spearmanr           |   0.334194 |
|  3 | test       | EGFR           | mean_absolute_error |  17.5259   |
|  4 | test       | EGFR           | mean_squared_error  | 519.546    |
|  5 | test       | EGFR           | pearsonr            |   0.622516 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       | 0.464386 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.452136 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.597472 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.357711 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.29704  |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.683781 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | explained_var       | 0.658301 |
|  1 | test       | LOG_RPPB       | r2                  | 0.657051 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.82     |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.421118 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.304704 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.854752 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | explained_var       | 0.513244 |
|  1 | test       | LOG_HPPB       | r2                  | 0.476001 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.698602 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.491812 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.317354 |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.723833 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.62437  |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.623968 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.787316 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.310971 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.186283 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.791212 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       | 0.562556 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.561102 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.754241 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.393709 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.247777 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.750218 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       | 0.517426 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.514253 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.72354  |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.330834 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.188669 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.721399 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.452708 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.03836 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.370089 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.667413 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.306165 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.430807 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.630345 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.898696 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.632524 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.504302 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.63472 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.926953 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.385487 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.846686 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.862609 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.845082 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.533074 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6155483569778558,
    "polaris/pkis2-ret-wt-reg-v2": 703.8999132938341,
    "polaris/pkis2-kit-wt-cls-v2": 0.779992161151148,
    "polaris/pkis2-kit-wt-reg-v2": 842.9992420777728,
    "polaris/pkis2-egfr-wt-reg-v2": 519.546490298924,
    "polaris/adme-fang-solu-1": 0.6837813133913168,
    "polaris/adme-fang-rppb-1": 0.8547521311154419,
    "polaris/adme-fang-hppb-1": 0.7238332843456654,
    "polaris/adme-fang-perm-1": 0.7912123893900311,
    "polaris/adme-fang-rclint-1": 0.7502182090769346,
    "polaris/adme-fang-hclint-1": 0.7213991035908838,
    "tdcommons/lipophilicity-astrazeneca": 0.4527084432272684,
    "tdcommons/ppbr-az": 8.038363750642015,
    "tdcommons/clearance-hepatocyte-az": 0.3700894524846135,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6674128945878478,
    "tdcommons/half-life-obach": 0.30616461181210075,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.43080659696024454,
    "tdcommons/clearance-microsome-az": 0.6303450374395214,
    "tdcommons/dili": 0.8986956521739131,
    "tdcommons/bioavailability-ma": 0.6325241104090455,
    "tdcommons/vdss-lombardo": 0.5043015731771546,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6347197106690778,
    "tdcommons/pgp-broccatelli": 0.9269528125833111,
    "tdcommons/caco2-wang": 0.38548748593374405,
    "tdcommons/herg": 0.8466863033873343,
    "tdcommons/bbb-martins": 0.8626094434021263,
    "tdcommons/ames": 0.8450821437662769,
    "tdcommons/ld50-zhu": 0.5330742957911407
}
```
