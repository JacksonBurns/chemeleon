# Descriptor MLP Results
timestamp: 2025-04-29 10:44:04.081685
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | mcc         | 0.266557 |
|  1 | test       | CLS_RET        | accuracy    | 0.849057 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.215541 |
|  3 | test       | CLS_RET        | roc_auc     | 0.811633 |
|  4 | test       | CLS_RET        | pr_auc      | 0.555752 |
|  5 | test       | CLS_RET        | f1          | 0.272727 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.530025 |
|  1 | test       | RET            | spearmanr           |   0.544067 |
|  2 | test       | RET            | mean_squared_error  | 936.125    |
|  3 | test       | RET            | explained_var       |   0.280601 |
|  4 | test       | RET            | r2                  |   0.211621 |
|  5 | test       | RET            | mean_absolute_error |  22.3491   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | mcc         | 0.27854  |
|  1 | test       | CLS_KIT        | accuracy    | 0.793103 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.276507 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.752901 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.490614 |
|  5 | test       | CLS_KIT        | f1          | 0.4      |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | pearsonr            |    0.395956  |
|  1 | test       | KIT            | spearmanr           |    0.369034  |
|  2 | test       | KIT            | mean_squared_error  | 1105.43      |
|  3 | test       | KIT            | explained_var       |    0.0839577 |
|  4 | test       | KIT            | r2                  |    0.083912  |
|  5 | test       | KIT            | mean_absolute_error |   26.7021    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.632024 |
|  1 | test       | EGFR           | spearmanr           |   0.366298 |
|  2 | test       | EGFR           | mean_squared_error  | 484.498    |
|  3 | test       | EGFR           | explained_var       |   0.399246 |
|  4 | test       | EGFR           | r2                  |   0.398713 |
|  5 | test       | EGFR           | mean_absolute_error |  17.1255   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.568039 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.477108 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.370374 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.318199 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.316879 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.40519  |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.808385 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.885217 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.325091 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.635899 |
|  4 | test       | LOG_RPPB       | r2                  | 0.634105 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.391674 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.848951 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.844068 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.178127 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.720269 |
|  4 | test       | LOG_HPPB       | r2                  | 0.705886 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.352082 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.784897 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.77282  |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.191187 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.61535  |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.61407  |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.320312 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.692972 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.688777 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.297268 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.473816 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.473437 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.424629 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.667666 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.687542 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.221242 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.430418 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.430391 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.355317 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.536806 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.75616 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.340319 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.684044 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.310717 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.378652 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.505613 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.921739 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.703026 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.48669 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.615619 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.920355 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.285739 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.862592 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.904667 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.839919 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.600394 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5557516498259664,
    "polaris/pkis2-ret-wt-reg-v2": 936.1249791769513,
    "polaris/pkis2-kit-wt-cls-v2": 0.49061386300403287,
    "polaris/pkis2-kit-wt-reg-v2": 1105.4287836076464,
    "polaris/pkis2-egfr-wt-reg-v2": 484.4981844144503,
    "polaris/adme-fang-solu-1": 0.5680385162028907,
    "polaris/adme-fang-rppb-1": 0.8083851233811654,
    "polaris/adme-fang-hppb-1": 0.8489510022999709,
    "polaris/adme-fang-perm-1": 0.7848974677259866,
    "polaris/adme-fang-rclint-1": 0.6929721190482513,
    "polaris/adme-fang-hclint-1": 0.667666484535421,
    "tdcommons/lipophilicity-astrazeneca": 0.5368057989449727,
    "tdcommons/ppbr-az": 7.756164214214399,
    "tdcommons/clearance-hepatocyte-az": 0.3403192936818789,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6840437354131604,
    "tdcommons/half-life-obach": 0.3107166612813052,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3786521772362438,
    "tdcommons/clearance-microsome-az": 0.5056130678542436,
    "tdcommons/dili": 0.9217391304347826,
    "tdcommons/bioavailability-ma": 0.7030262720319255,
    "tdcommons/vdss-lombardo": 0.4866904564384475,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6156193490054249,
    "tdcommons/pgp-broccatelli": 0.9203545721141029,
    "tdcommons/caco2-wang": 0.2857393337323871,
    "tdcommons/herg": 0.8625920471281296,
    "tdcommons/bbb-martins": 0.9046669793621012,
    "tdcommons/ames": 0.8399185415809982,
    "tdcommons/ld50-zhu": 0.6003942798742261
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | mcc         | 0.387824 |
|  1 | test       | CLS_RET        | accuracy    | 0.867925 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.313599 |
|  3 | test       | CLS_RET        | roc_auc     | 0.791143 |
|  4 | test       | CLS_RET        | pr_auc      | 0.591853 |
|  5 | test       | CLS_RET        | f1          | 0.363636 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.5975   |
|  1 | test       | RET            | spearmanr           |   0.606052 |
|  2 | test       | RET            | mean_squared_error  | 796.232    |
|  3 | test       | RET            | explained_var       |   0.346441 |
|  4 | test       | RET            | r2                  |   0.329435 |
|  5 | test       | RET            | mean_absolute_error |  20.5508   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | mcc         | 0.270793 |
|  1 | test       | CLS_KIT        | accuracy    | 0.775862 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.270793 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.751934 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.431825 |
|  5 | test       | CLS_KIT        | f1          | 0.409091 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |         Score |
|---:|:-----------|:---------------|:--------------------|--------------:|
|  0 | test       | KIT            | pearsonr            |    0.402584   |
|  1 | test       | KIT            | spearmanr           |    0.375452   |
|  2 | test       | KIT            | mean_squared_error  | 1212.32       |
|  3 | test       | KIT            | explained_var       |   -0.00130959 |
|  4 | test       | KIT            | r2                  |   -0.00467182 |
|  5 | test       | KIT            | mean_absolute_error |   27.0826     |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.62734  |
|  1 | test       | EGFR           | spearmanr           |   0.309505 |
|  2 | test       | EGFR           | mean_squared_error  | 496.376    |
|  3 | test       | EGFR           | explained_var       |   0.386097 |
|  4 | test       | EGFR           | r2                  |   0.383972 |
|  5 | test       | EGFR           | mean_absolute_error |  17.6177   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.557746 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.471879 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.374805 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.310045 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.308706 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.425052 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.846517 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.891304 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.308975 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.65458  |
|  4 | test       | LOG_RPPB       | r2                  | 0.652244 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.377607 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.824255 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.83276  |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.233736 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.645542 |
|  4 | test       | LOG_HPPB       | r2                  | 0.614066 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.433796 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.772821 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.761331 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.201211 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.594605 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.593835 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.330232 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.692502 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.689004 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.29825  |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.471697 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.471696 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.426773 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.655917 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.668247 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.229035 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.411351 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.410327 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.363468 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.514894 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.82026 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.326473 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.687367 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.336793 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.363413 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.561534 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.915217 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.666445 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.495842 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.603187 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.879432 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.280043 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.845803 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.915768 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.840909 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.642224 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5918526949967363,
    "polaris/pkis2-ret-wt-reg-v2": 796.2318762483071,
    "polaris/pkis2-kit-wt-cls-v2": 0.4318253114691642,
    "polaris/pkis2-kit-wt-reg-v2": 1212.3214554426622,
    "polaris/pkis2-egfr-wt-reg-v2": 496.37631574506526,
    "polaris/adme-fang-solu-1": 0.5577464692362151,
    "polaris/adme-fang-rppb-1": 0.8465165748792502,
    "polaris/adme-fang-hppb-1": 0.8242545873332449,
    "polaris/adme-fang-perm-1": 0.7728213266134383,
    "polaris/adme-fang-rclint-1": 0.6925024458467064,
    "polaris/adme-fang-hclint-1": 0.6559171641265735,
    "tdcommons/lipophilicity-astrazeneca": 0.5148938108909697,
    "tdcommons/ppbr-az": 7.8202590631201785,
    "tdcommons/clearance-hepatocyte-az": 0.32647340900592825,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6873670638347193,
    "tdcommons/half-life-obach": 0.336792748192586,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.36341260871540376,
    "tdcommons/clearance-microsome-az": 0.5615337762962774,
    "tdcommons/dili": 0.9152173913043478,
    "tdcommons/bioavailability-ma": 0.6664449617559028,
    "tdcommons/vdss-lombardo": 0.49584229591045387,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6031871609403254,
    "tdcommons/pgp-broccatelli": 0.8794321514262864,
    "tdcommons/caco2-wang": 0.2800426345116585,
    "tdcommons/herg": 0.8458026509572901,
    "tdcommons/bbb-martins": 0.9157676672920576,
    "tdcommons/ames": 0.8409093579275098,
    "tdcommons/ld50-zhu": 0.6422241807867936
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | mcc         | 0.337956 |
|  1 | test       | CLS_RET        | accuracy    | 0.858491 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.288272 |
|  3 | test       | CLS_RET        | roc_auc     | 0.811633 |
|  4 | test       | CLS_RET        | pr_auc      | 0.606147 |
|  5 | test       | CLS_RET        | f1          | 0.347826 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.568307 |
|  1 | test       | RET            | spearmanr           |   0.591051 |
|  2 | test       | RET            | mean_squared_error  | 821.398    |
|  3 | test       | RET            | explained_var       |   0.317318 |
|  4 | test       | RET            | r2                  |   0.308241 |
|  5 | test       | RET            | mean_absolute_error |  21.7982   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | mcc         | 0.270692 |
|  1 | test       | CLS_KIT        | accuracy    | 0.818966 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.23875  |
|  3 | test       | CLS_KIT        | roc_auc     | 0.746132 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.483828 |
|  5 | test       | CLS_KIT        | f1          | 0.322581 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | pearsonr            |    0.430483  |
|  1 | test       | KIT            | spearmanr           |    0.395491  |
|  2 | test       | KIT            | mean_squared_error  | 1115.74      |
|  3 | test       | KIT            | explained_var       |    0.0979469 |
|  4 | test       | KIT            | r2                  |    0.0753664 |
|  5 | test       | KIT            | mean_absolute_error |   25.3962    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.652469 |
|  1 | test       | EGFR           | spearmanr           |   0.356727 |
|  2 | test       | EGFR           | mean_squared_error  | 466.633    |
|  3 | test       | EGFR           | explained_var       |   0.42537  |
|  4 | test       | EGFR           | r2                  |   0.420885 |
|  5 | test       | EGFR           | mean_absolute_error |  16.7151   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.530287 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.448588 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.391409 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.279547 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.278081 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.42434  |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.855067 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.92087  |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.272102 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.694327 |
|  4 | test       | LOG_RPPB       | r2                  | 0.693746 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.363878 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.782963 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.803576 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.303001 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.586485 |
|  4 | test       | LOG_HPPB       | r2                  | 0.4997   |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.501369 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.749843 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.744939 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.218762 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.559027 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.558407 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.353235 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.696407 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.691196 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.292272 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.482297 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.482286 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.423042 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.643036 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.656098 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.234702 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.403346 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.395735 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.370359 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.521364 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.94272 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.323059 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.659581 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.34559 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.384066 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr |  0.5643 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.872174 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.647822 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.474404 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.603865 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.924487 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.292852 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  |  0.8243 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.913149 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.847675 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.621272 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6061473656153586,
    "polaris/pkis2-ret-wt-reg-v2": 821.3984685348846,
    "polaris/pkis2-kit-wt-cls-v2": 0.4838284579451936,
    "polaris/pkis2-kit-wt-reg-v2": 1115.7406677125966,
    "polaris/pkis2-egfr-wt-reg-v2": 466.6326723276264,
    "polaris/adme-fang-solu-1": 0.5302874648150562,
    "polaris/adme-fang-rppb-1": 0.8550671556997718,
    "polaris/adme-fang-hppb-1": 0.7829634006107961,
    "polaris/adme-fang-perm-1": 0.7498429566963315,
    "polaris/adme-fang-rclint-1": 0.6964072098630967,
    "polaris/adme-fang-hclint-1": 0.643035962526125,
    "tdcommons/lipophilicity-astrazeneca": 0.5213639254342941,
    "tdcommons/ppbr-az": 7.942715118353611,
    "tdcommons/clearance-hepatocyte-az": 0.3230586704806771,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6595810601439986,
    "tdcommons/half-life-obach": 0.34559047015395444,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.38406645034696635,
    "tdcommons/clearance-microsome-az": 0.5643004688700353,
    "tdcommons/dili": 0.8721739130434782,
    "tdcommons/bioavailability-ma": 0.647821749251746,
    "tdcommons/vdss-lombardo": 0.47440396249236005,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.603865280289331,
    "tdcommons/pgp-broccatelli": 0.9244868035190615,
    "tdcommons/caco2-wang": 0.292851992089039,
    "tdcommons/herg": 0.824300441826215,
    "tdcommons/bbb-martins": 0.9131488430268918,
    "tdcommons/ames": 0.8476747146018133,
    "tdcommons/ld50-zhu": 0.621271789411408
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | mcc         | 0        |
|  1 | test       | CLS_RET        | accuracy    | 0.839623 |
|  2 | test       | CLS_RET        | cohen_kappa | 0        |
|  3 | test       | CLS_RET        | roc_auc     | 0.781229 |
|  4 | test       | CLS_RET        | pr_auc      | 0.419093 |
|  5 | test       | CLS_RET        | f1          | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.569913 |
|  1 | test       | RET            | spearmanr           |   0.575738 |
|  2 | test       | RET            | mean_squared_error  | 822.029    |
|  3 | test       | RET            | explained_var       |   0.32122  |
|  4 | test       | RET            | r2                  |   0.30771  |
|  5 | test       | RET            | mean_absolute_error |  21.7123   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | mcc         | 0.268906 |
|  1 | test       | CLS_KIT        | accuracy    | 0.810345 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.252927 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.772727 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.478174 |
|  5 | test       | CLS_KIT        | f1          | 0.352941 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | pearsonr            |    0.473682 |
|  1 | test       | KIT            | spearmanr           |    0.466443 |
|  2 | test       | KIT            | mean_squared_error  | 1085.08     |
|  3 | test       | KIT            | explained_var       |    0.149535 |
|  4 | test       | KIT            | r2                  |    0.100775 |
|  5 | test       | KIT            | mean_absolute_error |   24.6304   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.554741 |
|  1 | test       | EGFR           | spearmanr           |   0.264579 |
|  2 | test       | EGFR           | mean_squared_error  | 563.551    |
|  3 | test       | EGFR           | explained_var       |   0.307598 |
|  4 | test       | EGFR           | r2                  |   0.300605 |
|  5 | test       | EGFR           | mean_absolute_error |  19.2199   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.548782 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.452639 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.379064 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.300958 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.300851 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.430851 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.780093 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.815652 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.417184 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.532098 |
|  4 | test       | LOG_RPPB       | r2                  | 0.530453 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.504351 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.827318 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.797616 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.261102 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.684401 |
|  4 | test       | LOG_HPPB       | r2                  | 0.568881 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.41099  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.776544 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.763161 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.196896 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.602987 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.602545 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.328933 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.686999 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.682851 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.301967 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.468657 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.465112 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.431248 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.66342  |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.68167  |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.222667 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.430519 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.426722 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.358179 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.524595 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.96492 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.322288 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.642623 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.358766 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.365929 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.574332 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.87913 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.626538 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.485338 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.618784 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.92542 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.275974 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.856996 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.900211 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.846768 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.642198 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.41909323569053614,
    "polaris/pkis2-ret-wt-reg-v2": 822.0287709909212,
    "polaris/pkis2-kit-wt-cls-v2": 0.47817426603366175,
    "polaris/pkis2-kit-wt-reg-v2": 1085.080767656236,
    "polaris/pkis2-egfr-wt-reg-v2": 563.5508137345107,
    "polaris/adme-fang-solu-1": 0.5487821279430616,
    "polaris/adme-fang-rppb-1": 0.780092749662225,
    "polaris/adme-fang-hppb-1": 0.8273177677066439,
    "polaris/adme-fang-perm-1": 0.7765435258467267,
    "polaris/adme-fang-rclint-1": 0.6869993804338705,
    "polaris/adme-fang-hclint-1": 0.6634204029636178,
    "tdcommons/lipophilicity-astrazeneca": 0.5245949012949354,
    "tdcommons/ppbr-az": 7.964917150234707,
    "tdcommons/clearance-hepatocyte-az": 0.32228784440196684,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6426232970958652,
    "tdcommons/half-life-obach": 0.35876632100932243,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.36592858900252156,
    "tdcommons/clearance-microsome-az": 0.5743315758053211,
    "tdcommons/dili": 0.8791304347826087,
    "tdcommons/bioavailability-ma": 0.6265380778184236,
    "tdcommons/vdss-lombardo": 0.485338344284702,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6187839059674503,
    "tdcommons/pgp-broccatelli": 0.9254198880298588,
    "tdcommons/caco2-wang": 0.2759735077410688,
    "tdcommons/herg": 0.8569955817378498,
    "tdcommons/bbb-martins": 0.9002110694183865,
    "tdcommons/ames": 0.8467680980634045,
    "tdcommons/ld50-zhu": 0.6421983352991499
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | mcc         | 0.387824 |
|  1 | test       | CLS_RET        | accuracy    | 0.867925 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.313599 |
|  3 | test       | CLS_RET        | roc_auc     | 0.812954 |
|  4 | test       | CLS_RET        | pr_auc      | 0.613259 |
|  5 | test       | CLS_RET        | f1          | 0.363636 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.587339 |
|  1 | test       | RET            | spearmanr           |   0.573227 |
|  2 | test       | RET            | mean_squared_error  | 804.804    |
|  3 | test       | RET            | explained_var       |   0.344579 |
|  4 | test       | RET            | r2                  |   0.322216 |
|  5 | test       | RET            | mean_absolute_error |  21.5471   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | mcc         | 0.1967   |
|  1 | test       | CLS_KIT        | accuracy    | 0.793103 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.185012 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.754352 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.451246 |
|  5 | test       | CLS_KIT        | f1          | 0.294118 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | pearsonr            |    0.425467  |
|  1 | test       | KIT            | spearmanr           |    0.40798   |
|  2 | test       | KIT            | mean_squared_error  | 1109.93      |
|  3 | test       | KIT            | explained_var       |    0.100737  |
|  4 | test       | KIT            | r2                  |    0.0801813 |
|  5 | test       | KIT            | mean_absolute_error |   25.5751    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.630679 |
|  1 | test       | EGFR           | spearmanr           |   0.346826 |
|  2 | test       | EGFR           | mean_squared_error  | 498.865    |
|  3 | test       | EGFR           | explained_var       |   0.392606 |
|  4 | test       | EGFR           | r2                  |   0.380883 |
|  5 | test       | EGFR           | mean_absolute_error |  17.3438   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.557127 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.454181 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.37503  |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.310081 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.308291 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.419216 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.87396  |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.917391 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.242929 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.742387 |
|  4 | test       | LOG_RPPB       | r2                  | 0.72658  |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.372921 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.820228 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.820689 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.275742 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.666508 |
|  4 | test       | LOG_HPPB       | r2                  | 0.544708 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.432735 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.756947 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.746497 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.211575 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.572915 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.572914 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.346859 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.703347 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.70017  |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.289985 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.486764 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.486338 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.422541 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.676042 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.690282 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.216635 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.442266 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.442251 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.352061 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.497424 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.11853 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.346529 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.653158 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.335881 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.42589 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.570283 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.917391 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.62288 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.432634 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.616524 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.930419 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.277218 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.843741 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.922803 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  |  0.8409 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.649339 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6132591554388084,
    "polaris/pkis2-ret-wt-reg-v2": 804.8038833002827,
    "polaris/pkis2-kit-wt-cls-v2": 0.45124631780921354,
    "polaris/pkis2-kit-wt-reg-v2": 1109.9305536225918,
    "polaris/pkis2-egfr-wt-reg-v2": 498.8650631751344,
    "polaris/adme-fang-solu-1": 0.5571268497352206,
    "polaris/adme-fang-rppb-1": 0.8739600199816558,
    "polaris/adme-fang-hppb-1": 0.8202281335752931,
    "polaris/adme-fang-perm-1": 0.7569474711198562,
    "polaris/adme-fang-rclint-1": 0.7033474968031737,
    "polaris/adme-fang-hclint-1": 0.6760418723499149,
    "tdcommons/lipophilicity-astrazeneca": 0.49742403111003697,
    "tdcommons/ppbr-az": 8.11852557733362,
    "tdcommons/clearance-hepatocyte-az": 0.3465287493197509,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6531579070099672,
    "tdcommons/half-life-obach": 0.3358805363784602,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4258900050092144,
    "tdcommons/clearance-microsome-az": 0.5702826604104192,
    "tdcommons/dili": 0.9173913043478261,
    "tdcommons/bioavailability-ma": 0.6228799467908215,
    "tdcommons/vdss-lombardo": 0.4326335219780372,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6165235081374322,
    "tdcommons/pgp-broccatelli": 0.9304185550519862,
    "tdcommons/caco2-wang": 0.2772175312137814,
    "tdcommons/herg": 0.843740795287187,
    "tdcommons/bbb-martins": 0.9228033145716074,
    "tdcommons/ames": 0.8408995672521491,
    "tdcommons/ld50-zhu": 0.6493389191014518
}
```
