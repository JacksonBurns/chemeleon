# chemeleon2_preview_initial_training_e4s281344 Baseline Results
timestamp: 2026-06-25 18:26:39.407265
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.867925 |
|  1 | test       | CLS_RET        | pr_auc      | 0.626898 |
|  2 | test       | CLS_RET        | mcc         | 0.486398 |
|  3 | test       | CLS_RET        | f1          | 0.5625   |
|  4 | test       | CLS_RET        | roc_auc     | 0.850628 |
|  5 | test       | CLS_RET        | cohen_kappa | 0.48508  |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.449804 |
|  1 | test       | RET            | mean_squared_error  | 981.886    |
|  2 | test       | RET            | mean_absolute_error |  23.0066   |
|  3 | test       | RET            | r2                  |   0.173082 |
|  4 | test       | RET            | pearsonr            |   0.49152  |
|  5 | test       | RET            | explained_var       |   0.240014 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.767241 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.599088 |
|  2 | test       | CLS_KIT        | mcc         | 0.400608 |
|  3 | test       | CLS_KIT        | f1          | 0.526316 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.804642 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.382492 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.467905 |
|  1 | test       | KIT            | mean_squared_error  | 969.501    |
|  2 | test       | KIT            | mean_absolute_error |  22.5981   |
|  3 | test       | KIT            | r2                  |   0.196558 |
|  4 | test       | KIT            | pearsonr            |   0.555807 |
|  5 | test       | KIT            | explained_var       |   0.273269 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.409286 |
|  1 | test       | EGFR           | mean_squared_error  | 438.7      |
|  2 | test       | EGFR           | mean_absolute_error |  16.0566   |
|  3 | test       | EGFR           | r2                  |   0.455551 |
|  4 | test       | EGFR           | pearsonr            |   0.677053 |
|  5 | test       | EGFR           | explained_var       |   0.457915 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.542999 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.334296 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.373265 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.383421 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.631793 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.395568 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.735652 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.53779  |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.59523  |
|  3 | test       | LOG_RPPB       | r2                  | 0.39471  |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.688658 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.471805 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.653526 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.328224 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.451781 |
|  3 | test       | LOG_HPPB       | r2                  | 0.458053 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.687737 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.458117 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.762252 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.192887 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.316947 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.610639 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.784703 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.611421 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.704899 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.28407  |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.42359  |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.496815 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.70831  |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.500883 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.653244 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.238337 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.381135 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.386377 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.642343 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.400805 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.464779 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.46047 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.345948 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.590062 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.157297 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.391091 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.562194 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.931304 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.559361 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.458086 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.61042 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.900626 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.330836 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.839764 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.861984 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.830592 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.58287 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6268979102297381,
    "polaris/pkis2-ret-wt-reg-v2": 981.8861515269032,
    "polaris/pkis2-kit-wt-cls-v2": 0.5990877701914504,
    "polaris/pkis2-kit-wt-reg-v2": 969.5007162815759,
    "polaris/pkis2-egfr-wt-reg-v2": 438.6999933994946,
    "polaris/adme-fang-solu-1": 0.6317925828444609,
    "polaris/adme-fang-rppb-1": 0.6886583901590924,
    "polaris/adme-fang-hppb-1": 0.6877368446892799,
    "polaris/adme-fang-perm-1": 0.784702732275957,
    "polaris/adme-fang-rclint-1": 0.7083099139305491,
    "polaris/adme-fang-hclint-1": 0.6423426068130828,
    "tdcommons/lipophilicity-astrazeneca": 0.46477899561041874,
    "tdcommons/ppbr-az": 8.460469009317524,
    "tdcommons/clearance-hepatocyte-az": 0.34594831030554035,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5900616030126379,
    "tdcommons/half-life-obach": 0.15729678074566994,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.39109121557692716,
    "tdcommons/clearance-microsome-az": 0.5621938909104401,
    "tdcommons/dili": 0.931304347826087,
    "tdcommons/bioavailability-ma": 0.5593614898570003,
    "tdcommons/vdss-lombardo": 0.45808624723253477,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6104204339963833,
    "tdcommons/pgp-broccatelli": 0.9006264996001065,
    "tdcommons/caco2-wang": 0.33083554145021554,
    "tdcommons/herg": 0.8397643593519882,
    "tdcommons/bbb-martins": 0.8619840525328331,
    "tdcommons/ames": 0.8305919442323133,
    "tdcommons/ld50-zhu": 0.5828696688734629
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.839623 |
|  1 | test       | CLS_RET        | pr_auc      | 0.59718  |
|  2 | test       | CLS_RET        | mcc         | 0        |
|  3 | test       | CLS_RET        | f1          | 0        |
|  4 | test       | CLS_RET        | roc_auc     | 0.771315 |
|  5 | test       | CLS_RET        | cohen_kappa | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.577985 |
|  1 | test       | RET            | mean_squared_error  | 901.469    |
|  2 | test       | RET            | mean_absolute_error |  21.201    |
|  3 | test       | RET            | r2                  |   0.240808 |
|  4 | test       | RET            | pearsonr            |   0.560451 |
|  5 | test       | RET            | explained_var       |   0.274186 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.784483 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.495147 |
|  2 | test       | CLS_KIT        | mcc         | 0.357973 |
|  3 | test       | CLS_KIT        | f1          | 0.489796 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.738878 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.354982 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.591468 |
|  1 | test       | KIT            | mean_squared_error  | 858.898    |
|  2 | test       | KIT            | mean_absolute_error |  21.4106   |
|  3 | test       | KIT            | r2                  |   0.288216 |
|  4 | test       | KIT            | pearsonr            |   0.603223 |
|  5 | test       | KIT            | explained_var       |   0.296376 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.2495   |
|  1 | test       | EGFR           | mean_squared_error  | 455.284    |
|  2 | test       | EGFR           | mean_absolute_error |  16.6081   |
|  3 | test       | EGFR           | r2                  |   0.43497  |
|  4 | test       | EGFR           | pearsonr            |   0.661087 |
|  5 | test       | EGFR           | explained_var       |   0.437034 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.561271 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.353626 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.405911 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.347769 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.628945 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.362127 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.812174 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.438348 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.530914 |
|  3 | test       | LOG_RPPB       | r2                  | 0.506633 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.748652 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.537701 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.698296 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.371663 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.545782 |
|  3 | test       | LOG_HPPB       | r2                  | 0.38633  |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.696253 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.453835 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.712262 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.218442 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.345564 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.559053 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.748789 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.559503 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.726721 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.273166 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.415248 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.516129 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.728284 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.52992  |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.660333 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.229132 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.379089 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.410077 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.659142 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.420438 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.452296 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.22296 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.352264 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.699109 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.336751 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.432923 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.592291 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.906522 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.492517 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.303823 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.607708 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.906492 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.342482 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.812224 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.877502 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.822291 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.645397 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5971802661286221,
    "polaris/pkis2-ret-wt-reg-v2": 901.4689007927241,
    "polaris/pkis2-kit-wt-cls-v2": 0.49514683045296604,
    "polaris/pkis2-kit-wt-reg-v2": 858.8981537842338,
    "polaris/pkis2-egfr-wt-reg-v2": 455.28373327116475,
    "polaris/adme-fang-solu-1": 0.6289451559496863,
    "polaris/adme-fang-rppb-1": 0.7486521657145785,
    "polaris/adme-fang-hppb-1": 0.6962527081673533,
    "polaris/adme-fang-perm-1": 0.7487889206708349,
    "polaris/adme-fang-rclint-1": 0.7282843774347515,
    "polaris/adme-fang-hclint-1": 0.6591415177824347,
    "tdcommons/lipophilicity-astrazeneca": 0.452296261253811,
    "tdcommons/ppbr-az": 8.222964679533767,
    "tdcommons/clearance-hepatocyte-az": 0.3522638818550722,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6991090403873566,
    "tdcommons/half-life-obach": 0.33675087338472753,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.43292277536913776,
    "tdcommons/clearance-microsome-az": 0.5922908876966864,
    "tdcommons/dili": 0.9065217391304348,
    "tdcommons/bioavailability-ma": 0.49251745926172263,
    "tdcommons/vdss-lombardo": 0.30382323787491433,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6077079566003616,
    "tdcommons/pgp-broccatelli": 0.9064916022394028,
    "tdcommons/caco2-wang": 0.34248169482609686,
    "tdcommons/herg": 0.8122238586156112,
    "tdcommons/bbb-martins": 0.8775015634771732,
    "tdcommons/ames": 0.8222914096614384,
    "tdcommons/ld50-zhu": 0.645397347509619
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.858491 |
|  1 | test       | CLS_RET        | pr_auc      | 0.511767 |
|  2 | test       | CLS_RET        | mcc         | 0.462044 |
|  3 | test       | CLS_RET        | f1          | 0.545455 |
|  4 | test       | CLS_RET        | roc_auc     | 0.821547 |
|  5 | test       | CLS_RET        | cohen_kappa | 0.461747 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.550015 |
|  1 | test       | RET            | mean_squared_error  | 742.055    |
|  2 | test       | RET            | mean_absolute_error |  21.0985   |
|  3 | test       | RET            | r2                  |   0.375062 |
|  4 | test       | RET            | pearsonr            |   0.620252 |
|  5 | test       | RET            | explained_var       |   0.383628 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.844828 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.632641 |
|  2 | test       | CLS_KIT        | mcc         | 0.477761 |
|  3 | test       | CLS_KIT        | f1          | 0.571429 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.777079 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.476954 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.538831 |
|  1 | test       | KIT            | mean_squared_error  | 795.598    |
|  2 | test       | KIT            | mean_absolute_error |  21.6243   |
|  3 | test       | KIT            | r2                  |   0.340674 |
|  4 | test       | KIT            | pearsonr            |   0.598287 |
|  5 | test       | KIT            | explained_var       |   0.352284 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.41371  |
|  1 | test       | EGFR           | mean_squared_error  | 416.469    |
|  2 | test       | EGFR           | mean_absolute_error |  15.5597   |
|  3 | test       | EGFR           | r2                  |   0.483141 |
|  4 | test       | EGFR           | pearsonr            |   0.698723 |
|  5 | test       | EGFR           | explained_var       |   0.485621 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.589431 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.31427  |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.370261 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.420357 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.654529 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.421906 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.688696 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.427618 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.506181 |
|  3 | test       | LOG_RPPB       | r2                  | 0.518709 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.746205 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.520764 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.664069 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.517241 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.636443 |
|  3 | test       | LOG_HPPB       | r2                  | 0.145958 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.616948 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.165582 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.760218 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.220031 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.340221 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.555846 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.755366 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.561003 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.721364 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.274633 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.411982 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.513531 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.724284 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.513708 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.672933 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.22293  |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.364506 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.426045 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.671931 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.438775 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.44824 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.69531 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.367748 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.652364 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.151825 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.43285 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.578686 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.888261 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.382441 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.460455 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.602735 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.897294 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.385142 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.833579 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.906875 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.842174 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.592663 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5117671572163219,
    "polaris/pkis2-ret-wt-reg-v2": 742.0549595288148,
    "polaris/pkis2-kit-wt-cls-v2": 0.6326406830374741,
    "polaris/pkis2-kit-wt-reg-v2": 795.5983207132523,
    "polaris/pkis2-egfr-wt-reg-v2": 416.46885481823284,
    "polaris/adme-fang-solu-1": 0.654528979317872,
    "polaris/adme-fang-rppb-1": 0.7462054914930192,
    "polaris/adme-fang-hppb-1": 0.6169482189316045,
    "polaris/adme-fang-perm-1": 0.7553664884613225,
    "polaris/adme-fang-rclint-1": 0.7242837992096665,
    "polaris/adme-fang-hclint-1": 0.6719312668812906,
    "tdcommons/lipophilicity-astrazeneca": 0.4482403860035397,
    "tdcommons/ppbr-az": 8.695306091308595,
    "tdcommons/clearance-hepatocyte-az": 0.3677476743065932,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6523637979910586,
    "tdcommons/half-life-obach": 0.1518245442603629,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4328500057990223,
    "tdcommons/clearance-microsome-az": 0.5786861340348599,
    "tdcommons/dili": 0.8882608695652173,
    "tdcommons/bioavailability-ma": 0.38244097106750913,
    "tdcommons/vdss-lombardo": 0.4604550305818243,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.602735081374322,
    "tdcommons/pgp-broccatelli": 0.8972940549186884,
    "tdcommons/caco2-wang": 0.38514218980649173,
    "tdcommons/herg": 0.833578792341679,
    "tdcommons/bbb-martins": 0.9068753908692934,
    "tdcommons/ames": 0.8421743131841234,
    "tdcommons/ld50-zhu": 0.592663187679967
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.839623 |
|  1 | test       | CLS_RET        | pr_auc      | 0.655976 |
|  2 | test       | CLS_RET        | mcc         | 0        |
|  3 | test       | CLS_RET        | f1          | 0        |
|  4 | test       | CLS_RET        | roc_auc     | 0.855915 |
|  5 | test       | CLS_RET        | cohen_kappa | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.553569 |
|  1 | test       | RET            | mean_squared_error  | 872.546    |
|  2 | test       | RET            | mean_absolute_error |  21.9717   |
|  3 | test       | RET            | r2                  |   0.265166 |
|  4 | test       | RET            | pearsonr            |   0.542939 |
|  5 | test       | RET            | explained_var       |   0.267284 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.87069  |
|  1 | test       | CLS_KIT        | pr_auc      | 0.737378 |
|  2 | test       | CLS_KIT        | mcc         | 0.586725 |
|  3 | test       | CLS_KIT        | f1          | 0.666667 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.827853 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.586502 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.508233 |
|  1 | test       | KIT            | mean_squared_error  | 992.793    |
|  2 | test       | KIT            | mean_absolute_error |  23.4748   |
|  3 | test       | KIT            | r2                  |   0.177255 |
|  4 | test       | KIT            | pearsonr            |   0.543295 |
|  5 | test       | KIT            | explained_var       |   0.184627 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.363671 |
|  1 | test       | EGFR           | mean_squared_error  | 442.643    |
|  2 | test       | EGFR           | mean_absolute_error |  16.2882   |
|  3 | test       | EGFR           | r2                  |   0.450657 |
|  4 | test       | EGFR           | pearsonr            |   0.67411  |
|  5 | test       | EGFR           | explained_var       |   0.451615 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.561456 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.339561 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.384184 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.37371  |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.621634 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.375947 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.792174 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.529601 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.618003 |
|  3 | test       | LOG_RPPB       | r2                  | 0.403926 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.729594 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.459685 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.655359 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.454005 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.57499  |
|  3 | test       | LOG_HPPB       | r2                  | 0.250369 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.639264 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.343413 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.72162  |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.255586 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.412636 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.484074 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.740093 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.543956 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.703481 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.287976 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.429326 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.489896 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.703106 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.492811 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.694963 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.213737 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.338636 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.449713 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.700162 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.449985 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.461475 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.18684 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.38853 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.63969 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.344537 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.336187 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.566618 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.827391 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.668773 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.259272 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.631781 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.909291 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.484321 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.813991 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.910686 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.829527 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.641791 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6559758154530387,
    "polaris/pkis2-ret-wt-reg-v2": 872.5460187372906,
    "polaris/pkis2-kit-wt-cls-v2": 0.7373781086271016,
    "polaris/pkis2-kit-wt-reg-v2": 992.7929328846832,
    "polaris/pkis2-egfr-wt-reg-v2": 442.6432830542122,
    "polaris/adme-fang-solu-1": 0.6216342840459783,
    "polaris/adme-fang-rppb-1": 0.7295938700669671,
    "polaris/adme-fang-hppb-1": 0.6392635805490535,
    "polaris/adme-fang-perm-1": 0.7400934873473364,
    "polaris/adme-fang-rclint-1": 0.7031063010304734,
    "polaris/adme-fang-hclint-1": 0.7001615756112469,
    "tdcommons/lipophilicity-astrazeneca": 0.4614746949048269,
    "tdcommons/ppbr-az": 7.186840680826968,
    "tdcommons/clearance-hepatocyte-az": 0.3885301057558954,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6396898709492286,
    "tdcommons/half-life-obach": 0.3445367514868167,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.33618674601966225,
    "tdcommons/clearance-microsome-az": 0.5666179135093105,
    "tdcommons/dili": 0.8273913043478262,
    "tdcommons/bioavailability-ma": 0.6687728633189225,
    "tdcommons/vdss-lombardo": 0.2592721792608314,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6317811934900543,
    "tdcommons/pgp-broccatelli": 0.9092908557717942,
    "tdcommons/caco2-wang": 0.4843210231664301,
    "tdcommons/herg": 0.8139911634756996,
    "tdcommons/bbb-martins": 0.9106863664790494,
    "tdcommons/ames": 0.8295267187530596,
    "tdcommons/ld50-zhu": 0.6417909342039261
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.858491 |
|  1 | test       | CLS_RET        | pr_auc      | 0.549988 |
|  2 | test       | CLS_RET        | mcc         | 0.318193 |
|  3 | test       | CLS_RET        | f1          | 0.285714 |
|  4 | test       | CLS_RET        | roc_auc     | 0.803701 |
|  5 | test       | CLS_RET        | cohen_kappa | 0.239234 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.470231 |
|  1 | test       | RET            | mean_squared_error  | 965.059    |
|  2 | test       | RET            | mean_absolute_error |  23.7443   |
|  3 | test       | RET            | r2                  |   0.187254 |
|  4 | test       | RET            | pearsonr            |   0.461596 |
|  5 | test       | RET            | explained_var       |   0.212884 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.844828 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.633355 |
|  2 | test       | CLS_KIT        | mcc         | 0.530957 |
|  3 | test       | CLS_KIT        | f1          | 0.625    |
|  4 | test       | CLS_KIT        | roc_auc     | 0.799323 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.528029 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.493335 |
|  1 | test       | KIT            | mean_squared_error  | 927.276    |
|  2 | test       | KIT            | mean_absolute_error |  22.4878   |
|  3 | test       | KIT            | r2                  |   0.23155  |
|  4 | test       | KIT            | pearsonr            |   0.557766 |
|  5 | test       | KIT            | explained_var       |   0.236887 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.447108 |
|  1 | test       | EGFR           | mean_squared_error  | 437.108    |
|  2 | test       | EGFR           | mean_absolute_error |  15.943    |
|  3 | test       | EGFR           | r2                  |   0.457527 |
|  4 | test       | EGFR           | pearsonr            |   0.691791 |
|  5 | test       | EGFR           | explained_var       |   0.470179 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.576256 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.335241 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.371659 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.381677 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.665332 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.414936 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.650435 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.733671 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.720373 |
|  3 | test       | LOG_RPPB       | r2                  | 0.174242 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.552271 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.267887 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.666972 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.357939 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.488079 |
|  3 | test       | LOG_HPPB       | r2                  | 0.40899  |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.716901 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.505731 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.718044 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.233103 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.362781 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.529458 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.728387 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.53032  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.714023 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.281894 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.423227 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.500669 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.713114 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.508081 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.687885 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.211471 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.346454 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.455548 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.691035 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.455618 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.443352 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.63591 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.422444 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.677972 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.197378 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.380097 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.600064 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  |    0.91 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.510476 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.514621 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.644552 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.888563 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.358502 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.784389 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.882427 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.819362 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.583398 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5499877816047446,
    "polaris/pkis2-ret-wt-reg-v2": 965.0591673342789,
    "polaris/pkis2-kit-wt-cls-v2": 0.6333550344789255,
    "polaris/pkis2-kit-wt-reg-v2": 927.2761267949506,
    "polaris/pkis2-egfr-wt-reg-v2": 437.10760389362076,
    "polaris/adme-fang-solu-1": 0.6653321286115286,
    "polaris/adme-fang-rppb-1": 0.5522714445100656,
    "polaris/adme-fang-hppb-1": 0.7169010490131426,
    "polaris/adme-fang-perm-1": 0.7283873866166996,
    "polaris/adme-fang-rclint-1": 0.7131138172236811,
    "polaris/adme-fang-hclint-1": 0.691034965440053,
    "tdcommons/lipophilicity-astrazeneca": 0.4433521101077398,
    "tdcommons/ppbr-az": 8.635913976624956,
    "tdcommons/clearance-hepatocyte-az": 0.42244427487622954,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6779720421382136,
    "tdcommons/half-life-obach": 0.19737800197970584,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.38009725750515744,
    "tdcommons/clearance-microsome-az": 0.6000642064503142,
    "tdcommons/dili": 0.91,
    "tdcommons/bioavailability-ma": 0.5104755570335883,
    "tdcommons/vdss-lombardo": 0.5146207102869892,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6445524412296564,
    "tdcommons/pgp-broccatelli": 0.8885630498533724,
    "tdcommons/caco2-wang": 0.3585016060198439,
    "tdcommons/herg": 0.7843888070692194,
    "tdcommons/bbb-martins": 0.8824265165728581,
    "tdcommons/ames": 0.8193620395934911,
    "tdcommons/ld50-zhu": 0.5833976193358353
}
```
