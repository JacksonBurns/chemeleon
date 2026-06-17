# chemeleon2_preview_initial_training_e4s281344 Baseline Results
timestamp: 2026-06-16 14:43:31.460656
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.654781 |
|  1 | test       | CLS_RET        | roc_auc     | 0.854594 |
|  2 | test       | CLS_RET        | f1          | 0.533333 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.457999 |
|  4 | test       | CLS_RET        | mcc         | 0.463591 |
|  5 | test       | CLS_RET        | accuracy    | 0.867925 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.587472 |
|  1 | test       | RET            | r2                  |   0.374317 |
|  2 | test       | RET            | pearsonr            |   0.616649 |
|  3 | test       | RET            | explained_var       |   0.379416 |
|  4 | test       | RET            | mean_absolute_error |  21.1132   |
|  5 | test       | RET            | mean_squared_error  | 742.94     |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.571335 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.789652 |
|  2 | test       | CLS_KIT        | f1          | 0.540541 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.457048 |
|  4 | test       | CLS_KIT        | mcc         | 0.468918 |
|  5 | test       | CLS_KIT        | accuracy    | 0.853448 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.483    |
|  1 | test       | KIT            | r2                  |   0.277873 |
|  2 | test       | KIT            | pearsonr            |   0.545096 |
|  3 | test       | KIT            | explained_var       |   0.283325 |
|  4 | test       | KIT            | mean_absolute_error |  23.845    |
|  5 | test       | KIT            | mean_squared_error  | 871.379    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.512894 |
|  1 | test       | EGFR           | r2                  |   0.504233 |
|  2 | test       | EGFR           | pearsonr            |   0.711981 |
|  3 | test       | EGFR           | explained_var       |   0.506916 |
|  4 | test       | EGFR           | mean_absolute_error |  14.9632   |
|  5 | test       | EGFR           | mean_squared_error  | 399.473    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.521628 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.418024 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.651152 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.418032 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.374822 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.315535 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.618261 |
|  1 | test       | LOG_RPPB       | r2                  | 0.26287  |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.567924 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.308935 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.637234 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.654926 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.674918 |
|  1 | test       | LOG_HPPB       | r2                  | 0.437352 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.696251 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.484489 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.484887 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.340762 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.805732 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.661083 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.815111 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.66364  |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.293824 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.167897 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.739732 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.543254 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.742332 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.550409 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.396599 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.257853 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.698343 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.469282 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.702722 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.469506 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.346778 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.206136 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.441414 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.09756 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.419772 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.688232 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.31132 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.412133 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.577015 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  |    0.92 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.649485 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.452119 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.650656 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.93735 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.295402 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.867452 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.879866 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.848669 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.582685 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6547814813224636,
    "polaris/pkis2-ret-wt-reg-v2": 742.9396311934097,
    "polaris/pkis2-kit-wt-cls-v2": 0.5713354289396123,
    "polaris/pkis2-kit-wt-reg-v2": 871.3791523417469,
    "polaris/pkis2-egfr-wt-reg-v2": 399.4733512954565,
    "polaris/adme-fang-solu-1": 0.6511518541466687,
    "polaris/adme-fang-rppb-1": 0.5679235310605855,
    "polaris/adme-fang-hppb-1": 0.6962512040361964,
    "polaris/adme-fang-perm-1": 0.815111497803438,
    "polaris/adme-fang-rclint-1": 0.7423323757907818,
    "polaris/adme-fang-hclint-1": 0.7027220526327816,
    "tdcommons/lipophilicity-astrazeneca": 0.4414142130215962,
    "tdcommons/ppbr-az": 8.09755838957157,
    "tdcommons/clearance-hepatocyte-az": 0.41977150307664574,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6882317308435388,
    "tdcommons/half-life-obach": 0.3113195716175975,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4121327457404256,
    "tdcommons/clearance-microsome-az": 0.5770151273373407,
    "tdcommons/dili": 0.92,
    "tdcommons/bioavailability-ma": 0.6494845360824741,
    "tdcommons/vdss-lombardo": 0.4521190893395269,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6506555153707052,
    "tdcommons/pgp-broccatelli": 0.9373500399893362,
    "tdcommons/caco2-wang": 0.2954024474296486,
    "tdcommons/herg": 0.8674521354933725,
    "tdcommons/bbb-martins": 0.8798663227016885,
    "tdcommons/ames": 0.8486694472184692,
    "tdcommons/ld50-zhu": 0.5826847487296077
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.795869 |
|  1 | test       | CLS_RET        | roc_auc     | 0.883675 |
|  2 | test       | CLS_RET        | f1          | 0.521739 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.478066 |
|  4 | test       | CLS_RET        | mcc         | 0.560462 |
|  5 | test       | CLS_RET        | accuracy    | 0.896226 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.647083 |
|  1 | test       | RET            | r2                  |   0.45596  |
|  2 | test       | RET            | pearsonr            |   0.684052 |
|  3 | test       | RET            | explained_var       |   0.463472 |
|  4 | test       | RET            | mean_absolute_error |  19.4113   |
|  5 | test       | RET            | mean_squared_error  | 645.996    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.64586  |
|  1 | test       | CLS_KIT        | roc_auc     | 0.814797 |
|  2 | test       | CLS_KIT        | f1          | 0.651163 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.57185  |
|  4 | test       | CLS_KIT        | mcc         | 0.572083 |
|  5 | test       | CLS_KIT        | accuracy    | 0.87069  |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.52242  |
|  1 | test       | KIT            | r2                  |   0.265318 |
|  2 | test       | KIT            | pearsonr            |   0.572136 |
|  3 | test       | KIT            | explained_var       |   0.265973 |
|  4 | test       | KIT            | mean_absolute_error |  22.9939   |
|  5 | test       | KIT            | mean_squared_error  | 886.529    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.352466 |
|  1 | test       | EGFR           | r2                  |   0.423413 |
|  2 | test       | EGFR           | pearsonr            |   0.663692 |
|  3 | test       | EGFR           | explained_var       |   0.425324 |
|  4 | test       | EGFR           | mean_absolute_error |  16.3464   |
|  5 | test       | EGFR           | mean_squared_error  | 464.596    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.548783 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.387317 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.64801  |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.388161 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.39298  |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.332184 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.772174 |
|  1 | test       | LOG_RPPB       | r2                  | 0.493126 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.773267 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.544591 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.566918 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.450348 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.682099 |
|  1 | test       | LOG_HPPB       | r2                  | 0.486985 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.70201  |
|  3 | test       | LOG_HPPB       | explained_var       | 0.490758 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.469553 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.310702 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.789713 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.644786 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.808464 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.644801 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.318255 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.17597  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.741785 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.554161 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.745808 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.556182 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.399396 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.251696 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.680457 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.463358 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.691851 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.470852 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.352969 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.208437 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.457269 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.25174 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.415321 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.681788 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.357423 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.412105 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.631962 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.912174 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.506817 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.546414 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.665235 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.924354 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.271437 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.840795 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.882192 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.832977 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.575202 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7958692107677781,
    "polaris/pkis2-ret-wt-reg-v2": 645.9962859346607,
    "polaris/pkis2-kit-wt-cls-v2": 0.6458604581723029,
    "polaris/pkis2-kit-wt-reg-v2": 886.5286754915626,
    "polaris/pkis2-egfr-wt-reg-v2": 464.5958139964892,
    "polaris/adme-fang-solu-1": 0.6480097296339151,
    "polaris/adme-fang-rppb-1": 0.7732668423194029,
    "polaris/adme-fang-hppb-1": 0.7020102943066231,
    "polaris/adme-fang-perm-1": 0.8084638343657172,
    "polaris/adme-fang-rclint-1": 0.7458078289167469,
    "polaris/adme-fang-hclint-1": 0.6918510902740033,
    "tdcommons/lipophilicity-astrazeneca": 0.4572686565660295,
    "tdcommons/ppbr-az": 8.251735453870086,
    "tdcommons/clearance-hepatocyte-az": 0.4153210347599732,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6817878705681784,
    "tdcommons/half-life-obach": 0.357422741829804,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4121046961399632,
    "tdcommons/clearance-microsome-az": 0.6319624429837423,
    "tdcommons/dili": 0.9121739130434783,
    "tdcommons/bioavailability-ma": 0.506817426005986,
    "tdcommons/vdss-lombardo": 0.5464136335320441,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6652350813743219,
    "tdcommons/pgp-broccatelli": 0.9243535057318049,
    "tdcommons/caco2-wang": 0.27143701048027297,
    "tdcommons/herg": 0.8407952871870398,
    "tdcommons/bbb-martins": 0.8821919949968731,
    "tdcommons/ames": 0.8329769527502007,
    "tdcommons/ld50-zhu": 0.5752020949343061
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.685097 |
|  1 | test       | CLS_RET        | roc_auc     | 0.88037  |
|  2 | test       | CLS_RET        | f1          | 0.5      |
|  3 | test       | CLS_RET        | cohen_kappa | 0.427911 |
|  4 | test       | CLS_RET        | mcc         | 0.441383 |
|  5 | test       | CLS_RET        | accuracy    | 0.867925 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.622899 |
|  1 | test       | RET            | r2                  |   0.372875 |
|  2 | test       | RET            | pearsonr            |   0.62577  |
|  3 | test       | RET            | explained_var       |   0.383728 |
|  4 | test       | RET            | mean_absolute_error |  21.1246   |
|  5 | test       | RET            | mean_squared_error  | 744.652    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.680635 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.826886 |
|  2 | test       | CLS_KIT        | f1          | 0.622222 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.531369 |
|  4 | test       | CLS_KIT        | mcc         | 0.531571 |
|  5 | test       | CLS_KIT        | accuracy    | 0.853448 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.497948 |
|  1 | test       | KIT            | r2                  |   0.229597 |
|  2 | test       | KIT            | pearsonr            |   0.522216 |
|  3 | test       | KIT            | explained_var       |   0.247253 |
|  4 | test       | KIT            | mean_absolute_error |  24.0651   |
|  5 | test       | KIT            | mean_squared_error  | 929.634    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.434551 |
|  1 | test       | EGFR           | r2                  |   0.500411 |
|  2 | test       | EGFR           | pearsonr            |   0.71129  |
|  3 | test       | EGFR           | explained_var       |   0.500504 |
|  4 | test       | EGFR           | mean_absolute_error |  16.2058   |
|  5 | test       | EGFR           | mean_squared_error  | 402.553    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.515552 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.399561 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.636365 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.403493 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.414571 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.325545 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.772174 |
|  1 | test       | LOG_RPPB       | r2                  | 0.527402 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.772638 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.54747  |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.535988 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.419895 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.707006 |
|  1 | test       | LOG_HPPB       | r2                  | 0.295401 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.677657 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.342394 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.598718 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.426732 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.785522 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.633522 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.796327 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.634105 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.312137 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.181551 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.721917 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.526524 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.726643 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.526994 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.411531 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.267298 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.70203  |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.479583 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.705823 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.480489 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.340922 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.202135 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.441179 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.50798 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.402415 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.733532 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.258179 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   |  0.3364 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.613803 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.906087 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.628533 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.593208 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.64297 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.930019 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.378869 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.848012 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.899097 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.853167 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.58341 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6850971351071161,
    "polaris/pkis2-ret-wt-reg-v2": 744.6517384615352,
    "polaris/pkis2-kit-wt-cls-v2": 0.6806346852772743,
    "polaris/pkis2-kit-wt-reg-v2": 929.6335752031583,
    "polaris/pkis2-egfr-wt-reg-v2": 402.55296275890146,
    "polaris/adme-fang-solu-1": 0.6363651646778467,
    "polaris/adme-fang-rppb-1": 0.7726381372801178,
    "polaris/adme-fang-hppb-1": 0.6776573203516681,
    "polaris/adme-fang-perm-1": 0.7963267951968944,
    "polaris/adme-fang-rclint-1": 0.7266434515145045,
    "polaris/adme-fang-hclint-1": 0.7058229788430039,
    "tdcommons/lipophilicity-astrazeneca": 0.44117869362944645,
    "tdcommons/ppbr-az": 8.50797629068064,
    "tdcommons/clearance-hepatocyte-az": 0.4024147288591287,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.733531625966324,
    "tdcommons/half-life-obach": 0.2581793896160396,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.33639996662897487,
    "tdcommons/clearance-microsome-az": 0.6138029046908443,
    "tdcommons/dili": 0.9060869565217391,
    "tdcommons/bioavailability-ma": 0.6285334220152976,
    "tdcommons/vdss-lombardo": 0.5932075301276103,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6429701627486437,
    "tdcommons/pgp-broccatelli": 0.930018661690216,
    "tdcommons/caco2-wang": 0.3788692221544874,
    "tdcommons/herg": 0.8480117820324007,
    "tdcommons/bbb-martins": 0.8990970919324578,
    "tdcommons/ames": 0.8531672834792143,
    "tdcommons/ld50-zhu": 0.5834098379499051
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.645021 |
|  1 | test       | CLS_RET        | roc_auc     | 0.837409 |
|  2 | test       | CLS_RET        | f1          | 0.5      |
|  3 | test       | CLS_RET        | cohen_kappa | 0.448395 |
|  4 | test       | CLS_RET        | mcc         | 0.504899 |
|  5 | test       | CLS_RET        | accuracy    | 0.886792 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.564423 |
|  1 | test       | RET            | r2                  |   0.374075 |
|  2 | test       | RET            | pearsonr            |   0.637737 |
|  3 | test       | RET            | explained_var       |   0.406574 |
|  4 | test       | RET            | mean_absolute_error |  20.6494   |
|  5 | test       | RET            | mean_squared_error  | 743.227    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.655656 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.823501 |
|  2 | test       | CLS_KIT        | f1          | 0.585366 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.496939 |
|  4 | test       | CLS_KIT        | mcc         | 0.498909 |
|  5 | test       | CLS_KIT        | accuracy    | 0.853448 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.567504 |
|  1 | test       | KIT            | r2                  |   0.320678 |
|  2 | test       | KIT            | pearsonr            |   0.611371 |
|  3 | test       | KIT            | explained_var       |   0.347639 |
|  4 | test       | KIT            | mean_absolute_error |  21.666    |
|  5 | test       | KIT            | mean_squared_error  | 819.727    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.431608 |
|  1 | test       | EGFR           | r2                  |   0.427413 |
|  2 | test       | EGFR           | pearsonr            |   0.678434 |
|  3 | test       | EGFR           | explained_var       |   0.429889 |
|  4 | test       | EGFR           | mean_absolute_error |  16.4216   |
|  5 | test       | EGFR           | mean_squared_error  | 461.372    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.550733 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.433954 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.659474 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.433962 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.370922 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.306898 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.749565 |
|  1 | test       | LOG_RPPB       | r2                  | 0.507109 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.757685 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.520834 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.544308 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.437925 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.738941 |
|  1 | test       | LOG_HPPB       | r2                  | 0.357845 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.739314 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.546184 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.529855 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.388914 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.802265 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.66107  |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.817547 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.667065 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.297938 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.167903 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.73893  |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.545927 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.740846 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.5481   |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.402502 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.256344 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.722735 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.510915 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.724736 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.511034 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.329204 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.189965 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.447296 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.27887 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.401211 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.676239 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.387276 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.348336 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.634608 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.933913 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.639508 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.62404 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.642518 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.920954 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.334592 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.87187 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.904159 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.845766 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.602299 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6450210929017158,
    "polaris/pkis2-ret-wt-reg-v2": 743.2266198937962,
    "polaris/pkis2-kit-wt-cls-v2": 0.6556557295796797,
    "polaris/pkis2-kit-wt-reg-v2": 819.7273677020871,
    "polaris/pkis2-egfr-wt-reg-v2": 461.3724414267688,
    "polaris/adme-fang-solu-1": 0.6594736866615925,
    "polaris/adme-fang-rppb-1": 0.7576845343962684,
    "polaris/adme-fang-hppb-1": 0.7393136786066258,
    "polaris/adme-fang-perm-1": 0.8175465528592557,
    "polaris/adme-fang-rclint-1": 0.7408461843924882,
    "polaris/adme-fang-hclint-1": 0.7247358907244814,
    "tdcommons/lipophilicity-astrazeneca": 0.4472958355006717,
    "tdcommons/ppbr-az": 8.278872471299284,
    "tdcommons/clearance-hepatocyte-az": 0.4012111959035027,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6762394820539205,
    "tdcommons/half-life-obach": 0.38727565431590605,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.34833624066940844,
    "tdcommons/clearance-microsome-az": 0.6346083017068279,
    "tdcommons/dili": 0.9339130434782608,
    "tdcommons/bioavailability-ma": 0.6395078150981044,
    "tdcommons/vdss-lombardo": 0.6240403400027662,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.64251808318264,
    "tdcommons/pgp-broccatelli": 0.9209544121567582,
    "tdcommons/caco2-wang": 0.3345916540629628,
    "tdcommons/herg": 0.8718703976435935,
    "tdcommons/bbb-martins": 0.9041588492808005,
    "tdcommons/ames": 0.8457655329064598,
    "tdcommons/ld50-zhu": 0.6022985367174885
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.650558 |
|  1 | test       | CLS_RET        | roc_auc     | 0.847984 |
|  2 | test       | CLS_RET        | f1          | 0.518519 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.453608 |
|  4 | test       | CLS_RET        | mcc         | 0.474614 |
|  5 | test       | CLS_RET        | accuracy    | 0.877358 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.57111  |
|  1 | test       | RET            | r2                  |   0.35179  |
|  2 | test       | RET            | pearsonr            |   0.606661 |
|  3 | test       | RET            | explained_var       |   0.363446 |
|  4 | test       | RET            | mean_absolute_error |  20.838    |
|  5 | test       | RET            | mean_squared_error  | 769.688    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.635502 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.831721 |
|  2 | test       | CLS_KIT        | f1          | 0.608696 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.51215  |
|  4 | test       | CLS_KIT        | mcc         | 0.512904 |
|  5 | test       | CLS_KIT        | accuracy    | 0.844828 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.48552  |
|  1 | test       | KIT            | r2                  |   0.235017 |
|  2 | test       | KIT            | pearsonr            |   0.549135 |
|  3 | test       | KIT            | explained_var       |   0.242615 |
|  4 | test       | KIT            | mean_absolute_error |  23.1311   |
|  5 | test       | KIT            | mean_squared_error  | 923.093    |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.400937 |
|  1 | test       | EGFR           | r2                  |   0.403786 |
|  2 | test       | EGFR           | pearsonr            |   0.649557 |
|  3 | test       | EGFR           | explained_var       |   0.41159  |
|  4 | test       | EGFR           | mean_absolute_error |  16.8287   |
|  5 | test       | EGFR           | mean_squared_error  | 480.411    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.570244 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.465075 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.684052 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.467032 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.36736  |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.290025 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.887826 |
|  1 | test       | LOG_RPPB       | r2                  | 0.558047 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.861977 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.65665  |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.546572 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.392667 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.699671 |
|  1 | test       | LOG_HPPB       | r2                  | 0.222095 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.71163  |
|  3 | test       | LOG_HPPB       | explained_var       | 0.506388 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.569883 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.471129 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.795568 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.657204 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.811156 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.657939 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.307017 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.169819 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.746992 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.555865 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.747822 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.55618  |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.400521 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.250733 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.700344 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.454917 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.706389 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.464572 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.351314 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.211715 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.43523 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.65722 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.414695 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.648699 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.446811 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.371175 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.600891 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.908261 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.453608 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr |  0.4416 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.664218 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.935151 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.321107 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.851841 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.912523 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.84311 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.570669 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6505580609333548,
    "polaris/pkis2-ret-wt-reg-v2": 769.6879264437441,
    "polaris/pkis2-kit-wt-cls-v2": 0.6355023842975634,
    "polaris/pkis2-kit-wt-reg-v2": 923.0928820158363,
    "polaris/pkis2-egfr-wt-reg-v2": 480.41054929648936,
    "polaris/adme-fang-solu-1": 0.6840521347035697,
    "polaris/adme-fang-rppb-1": 0.8619768953161155,
    "polaris/adme-fang-hppb-1": 0.7116300327160686,
    "polaris/adme-fang-perm-1": 0.8111558530887081,
    "polaris/adme-fang-rclint-1": 0.7478221552821104,
    "polaris/adme-fang-hclint-1": 0.7063888548029529,
    "tdcommons/lipophilicity-astrazeneca": 0.4352299868038722,
    "tdcommons/ppbr-az": 8.657221878133647,
    "tdcommons/clearance-hepatocyte-az": 0.4146948614323969,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6486993594971152,
    "tdcommons/half-life-obach": 0.4468114195646968,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3711746108291182,
    "tdcommons/clearance-microsome-az": 0.6008910394202237,
    "tdcommons/dili": 0.9082608695652175,
    "tdcommons/bioavailability-ma": 0.4536082474226804,
    "tdcommons/vdss-lombardo": 0.4415998381859355,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6642179023508137,
    "tdcommons/pgp-broccatelli": 0.9351506264996001,
    "tdcommons/caco2-wang": 0.32110725739816526,
    "tdcommons/herg": 0.851840942562592,
    "tdcommons/bbb-martins": 0.9125234521575986,
    "tdcommons/ames": 0.8431103017486146,
    "tdcommons/ld50-zhu": 0.570668915593737
}
```
