# chemeleon2_preview_initial_training_e4s281344 Baseline Results
timestamp: 2026-06-08 16:21:58.303798
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.867151 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.356461 |
|  2 | test       | CLS_RET        | f1          | 0.416667 |
|  3 | test       | CLS_RET        | accuracy    | 0.867925 |
|  4 | test       | CLS_RET        | mcc         | 0.40138  |
|  5 | test       | CLS_RET        | pr_auc      | 0.611689 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.532094 |
|  1 | test       | RET            | pearsonr            |   0.53532  |
|  2 | test       | RET            | explained_var       |   0.286566 |
|  3 | test       | RET            | mean_squared_error  | 860.757    |
|  4 | test       | RET            | mean_absolute_error |  22.8518   |
|  5 | test       | RET            | r2                  |   0.275094 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.808994 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.456674 |
|  2 | test       | CLS_KIT        | f1          | 0.529412 |
|  3 | test       | CLS_KIT        | accuracy    | 0.862069 |
|  4 | test       | CLS_KIT        | mcc         | 0.485525 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.612769 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.48083  |
|  1 | test       | KIT            | pearsonr            |   0.538385 |
|  2 | test       | KIT            | explained_var       |   0.264255 |
|  3 | test       | KIT            | mean_squared_error  | 902.031    |
|  4 | test       | KIT            | mean_absolute_error |  23.1696   |
|  5 | test       | KIT            | r2                  |   0.252472 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.337701 |
|  1 | test       | EGFR           | pearsonr            |   0.670638 |
|  2 | test       | EGFR           | explained_var       |   0.440148 |
|  3 | test       | EGFR           | mean_squared_error  | 466.033    |
|  4 | test       | EGFR           | mean_absolute_error |  17.7972   |
|  5 | test       | EGFR           | r2                  |   0.421629 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.548963 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.648506 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.416363 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.316683 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.40513  |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.415906 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.622609 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.508411 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.252694 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.667087 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.546832 |
|  5 | test       | LOG_RPPB       | r2                  | 0.249184 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.794255 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.799248 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.637886 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.251271 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.403396 |
|  5 | test       | LOG_HPPB       | r2                  | 0.585113 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.794512 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.799733 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.639009 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.179225 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.317988 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.638216 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.745831 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.739782 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.547276 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.257671 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.39909  |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.543577 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.715505 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.695022 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.464451 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.208704 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.35259  |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.462671 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |   0.503 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.27221 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.427863 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.684638 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.320788 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.368911 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.609792 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  |    0.92 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.626206 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.417841 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.66241 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.933284 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.292029 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.852283 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.889697 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.842372 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.582455 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6116886969970317,
    "polaris/pkis2-ret-wt-reg-v2": 860.7574218780727,
    "polaris/pkis2-kit-wt-cls-v2": 0.6127690850499291,
    "polaris/pkis2-kit-wt-reg-v2": 902.0306544667382,
    "polaris/pkis2-egfr-wt-reg-v2": 466.03295427682923,
    "polaris/adme-fang-solu-1": 0.6485061098899917,
    "polaris/adme-fang-rppb-1": 0.5084112613653348,
    "polaris/adme-fang-hppb-1": 0.7992484420542789,
    "polaris/adme-fang-perm-1": 0.7997325607892927,
    "polaris/adme-fang-rclint-1": 0.7397820542133509,
    "polaris/adme-fang-hclint-1": 0.6950221829748523,
    "tdcommons/lipophilicity-astrazeneca": 0.5030000952936354,
    "tdcommons/ppbr-az": 8.272212494114857,
    "tdcommons/clearance-hepatocyte-az": 0.42786321487221,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6846375788620056,
    "tdcommons/half-life-obach": 0.3207880144682898,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.36891055508095144,
    "tdcommons/clearance-microsome-az": 0.6097916013114492,
    "tdcommons/dili": 0.92,
    "tdcommons/bioavailability-ma": 0.6262055204522781,
    "tdcommons/vdss-lombardo": 0.41784094943895567,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6624095840867992,
    "tdcommons/pgp-broccatelli": 0.9332844574780058,
    "tdcommons/caco2-wang": 0.2920288391115629,
    "tdcommons/herg": 0.8522827687776141,
    "tdcommons/bbb-martins": 0.8896966854283928,
    "tdcommons/ames": 0.8423720848264113,
    "tdcommons/ld50-zhu": 0.5824548167614556
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.854594 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.509672 |
|  2 | test       | CLS_RET        | f1          | 0.56     |
|  3 | test       | CLS_RET        | accuracy    | 0.896226 |
|  4 | test       | CLS_RET        | mcc         | 0.55641  |
|  5 | test       | CLS_RET        | pr_auc      | 0.725544 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.582815 |
|  1 | test       | RET            | pearsonr            |   0.602692 |
|  2 | test       | RET            | explained_var       |   0.351175 |
|  3 | test       | RET            | mean_squared_error  | 817.282    |
|  4 | test       | RET            | mean_absolute_error |  22.059    |
|  5 | test       | RET            | r2                  |   0.311707 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.808994 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.493566 |
|  2 | test       | CLS_KIT        | f1          | 0.595745 |
|  3 | test       | CLS_KIT        | accuracy    | 0.836207 |
|  4 | test       | CLS_KIT        | mcc         | 0.495152 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.646969 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.527307 |
|  1 | test       | KIT            | pearsonr            |   0.564455 |
|  2 | test       | KIT            | explained_var       |   0.299193 |
|  3 | test       | KIT            | mean_squared_error  | 845.985    |
|  4 | test       | KIT            | mean_absolute_error |  22.8506   |
|  5 | test       | KIT            | r2                  |   0.298917 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.255846 |
|  1 | test       | EGFR           | pearsonr            |   0.635183 |
|  2 | test       | EGFR           | explained_var       |   0.402679 |
|  3 | test       | EGFR           | mean_squared_error  | 483.087    |
|  4 | test       | EGFR           | mean_absolute_error |  17.3199   |
|  5 | test       | EGFR           | r2                  |   0.400465 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.569927 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.672633 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.450039 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.298544 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.379684 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.449362 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.796522 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.753274 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.553354 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.403203 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.466524 |
|  5 | test       | LOG_RPPB       | r2                  | 0.546189 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.778516 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.818995 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.666638 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.217345 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.369173 |
|  5 | test       | LOG_HPPB       | r2                  | 0.641132 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.792111 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.793341 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.62939  |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.183977 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.318341 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.628623 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.745596 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.738391 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.544963 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.258595 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.400093 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.541939 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.684439 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.679135 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.449504 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.213872 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.361951 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.449365 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.491607 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.47605 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.408974 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.684536 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.303522 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.362487 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.634424 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.904783 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.563352 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.456631 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.647378 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.918888 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.302236 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.834021 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.889501 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.841495 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.618663 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7255437211683817,
    "polaris/pkis2-ret-wt-reg-v2": 817.2820684678765,
    "polaris/pkis2-kit-wt-cls-v2": 0.6469691259659553,
    "polaris/pkis2-kit-wt-reg-v2": 845.9852962327503,
    "polaris/pkis2-egfr-wt-reg-v2": 483.0866558084404,
    "polaris/adme-fang-solu-1": 0.672632755707746,
    "polaris/adme-fang-rppb-1": 0.753274206251865,
    "polaris/adme-fang-hppb-1": 0.8189947801663079,
    "polaris/adme-fang-perm-1": 0.7933412848488749,
    "polaris/adme-fang-rclint-1": 0.738391297501956,
    "polaris/adme-fang-hclint-1": 0.6791347578663258,
    "tdcommons/lipophilicity-astrazeneca": 0.4916069537628264,
    "tdcommons/ppbr-az": 8.476050577180757,
    "tdcommons/clearance-hepatocyte-az": 0.40897420417854546,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6845364428888254,
    "tdcommons/half-life-obach": 0.30352188697214066,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3624871629443121,
    "tdcommons/clearance-microsome-az": 0.634424410761262,
    "tdcommons/dili": 0.9047826086956522,
    "tdcommons/bioavailability-ma": 0.5633521782507482,
    "tdcommons/vdss-lombardo": 0.45663070998318295,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6473779385171792,
    "tdcommons/pgp-broccatelli": 0.9188882964542788,
    "tdcommons/caco2-wang": 0.3022355488866115,
    "tdcommons/herg": 0.8340206185567011,
    "tdcommons/bbb-martins": 0.8895012507817386,
    "tdcommons/ames": 0.8414948403140848,
    "tdcommons/ld50-zhu": 0.6186629797718683
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.883675 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.331371 |
|  2 | test       | CLS_RET        | f1          | 0.4      |
|  3 | test       | CLS_RET        | accuracy    | 0.858491 |
|  4 | test       | CLS_RET        | mcc         | 0.361758 |
|  5 | test       | CLS_RET        | pr_auc      | 0.657218 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.50787  |
|  1 | test       | RET            | pearsonr            |   0.528588 |
|  2 | test       | RET            | explained_var       |   0.279245 |
|  3 | test       | RET            | mean_squared_error  | 857.87     |
|  4 | test       | RET            | mean_absolute_error |  23.3234   |
|  5 | test       | RET            | r2                  |   0.277526 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.797389 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.501147 |
|  2 | test       | CLS_KIT        | f1          | 0.571429 |
|  3 | test       | CLS_KIT        | accuracy    | 0.87069  |
|  4 | test       | CLS_KIT        | mcc         | 0.525226 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.615112 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.499518 |
|  1 | test       | KIT            | pearsonr            |   0.554377 |
|  2 | test       | KIT            | explained_var       |   0.292126 |
|  3 | test       | KIT            | mean_squared_error  | 862.017    |
|  4 | test       | KIT            | mean_absolute_error |  23.075    |
|  5 | test       | KIT            | r2                  |   0.285631 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.302797 |
|  1 | test       | EGFR           | pearsonr            |   0.624096 |
|  2 | test       | EGFR           | explained_var       |   0.389136 |
|  3 | test       | EGFR           | mean_squared_error  | 497.397    |
|  4 | test       | EGFR           | mean_absolute_error |  18.3282   |
|  5 | test       | EGFR           | r2                  |   0.382705 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.546598 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.646764 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.418188 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.316821 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.390588 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.415653 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.743478 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.672073 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.445091 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.493438 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.461646 |
|  5 | test       | LOG_RPPB       | r2                  | 0.444628 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.761708 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.705242 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.449304 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.363655 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.529813 |
|  5 | test       | LOG_HPPB       | r2                  | 0.399551 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.789627 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.785944 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.617707 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.191109 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.327504 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.614227 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.744274 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.738689 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.544965 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.259325 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.401206 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.540647 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.698401 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.686672 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.458865 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.210314 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.359154 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.458525 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.505141 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.63796 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.419346 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.727195 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.238972 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.385645 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.631229 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.902174 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.558031 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.490185 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.660375 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.927419 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.292722 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.819146 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.903631 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.848693 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.606298 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6572175301891616,
    "polaris/pkis2-ret-wt-reg-v2": 857.8698278039868,
    "polaris/pkis2-kit-wt-cls-v2": 0.6151124071691584,
    "polaris/pkis2-kit-wt-reg-v2": 862.0174015468903,
    "polaris/pkis2-egfr-wt-reg-v2": 497.3968216399359,
    "polaris/adme-fang-solu-1": 0.6467639295349518,
    "polaris/adme-fang-rppb-1": 0.6720733960055232,
    "polaris/adme-fang-hppb-1": 0.7052415612850145,
    "polaris/adme-fang-perm-1": 0.7859436296642182,
    "polaris/adme-fang-rclint-1": 0.7386890749947308,
    "polaris/adme-fang-hclint-1": 0.6866716264309849,
    "tdcommons/lipophilicity-astrazeneca": 0.5051411293574742,
    "tdcommons/ppbr-az": 8.637963332447468,
    "tdcommons/clearance-hepatocyte-az": 0.4193461162861257,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7271952792212372,
    "tdcommons/half-life-obach": 0.23897208273629023,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3856446908720869,
    "tdcommons/clearance-microsome-az": 0.6312287973985583,
    "tdcommons/dili": 0.9021739130434783,
    "tdcommons/bioavailability-ma": 0.5580312603924177,
    "tdcommons/vdss-lombardo": 0.4901854947702227,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.660375226039783,
    "tdcommons/pgp-broccatelli": 0.9274193548387096,
    "tdcommons/caco2-wang": 0.29272212772941186,
    "tdcommons/herg": 0.8191458026509573,
    "tdcommons/bbb-martins": 0.9036311757348342,
    "tdcommons/ames": 0.8486929448393351,
    "tdcommons/ld50-zhu": 0.6062977644632569
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.864508 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.591365 |
|  2 | test       | CLS_RET        | f1          | 0.642857 |
|  3 | test       | CLS_RET        | accuracy    | 0.90566  |
|  4 | test       | CLS_RET        | mcc         | 0.609983 |
|  5 | test       | CLS_RET        | pr_auc      | 0.703198 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.58201  |
|  1 | test       | RET            | pearsonr            |   0.59864  |
|  2 | test       | RET            | explained_var       |   0.357874 |
|  3 | test       | RET            | mean_squared_error  | 762.628    |
|  4 | test       | RET            | mean_absolute_error |  22.3646   |
|  5 | test       | RET            | r2                  |   0.357736 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.820116 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.584802 |
|  2 | test       | CLS_KIT        | f1          | 0.648649 |
|  3 | test       | CLS_KIT        | accuracy    | 0.887931 |
|  4 | test       | CLS_KIT        | mcc         | 0.599989 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.695943 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.525871 |
|  1 | test       | KIT            | pearsonr            |   0.589746 |
|  2 | test       | KIT            | explained_var       |   0.33219  |
|  3 | test       | KIT            | mean_squared_error  | 840.072    |
|  4 | test       | KIT            | mean_absolute_error |  21.5737   |
|  5 | test       | KIT            | r2                  |   0.303818 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.255315 |
|  1 | test       | EGFR           | pearsonr            |   0.625077 |
|  2 | test       | EGFR           | explained_var       |   0.390321 |
|  3 | test       | EGFR           | mean_squared_error  | 537.326    |
|  4 | test       | EGFR           | mean_absolute_error |  19.3066   |
|  5 | test       | EGFR           | r2                  |   0.333151 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.551505 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.653257 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.426412 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.311841 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.400008 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.424838 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.76087  |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.702817 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.408212 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.567794 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.620756 |
|  5 | test       | LOG_RPPB       | r2                  | 0.36094  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.813966 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.829283 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.687477 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.245628 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.424564 |
|  5 | test       | LOG_HPPB       | r2                  | 0.594432 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.770086 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.772194 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.596258 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.200018 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.335223 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.596243 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.717393 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.716751 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.512717 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.276635 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.420091 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.509984 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.692589 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.685112 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.463133 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.209328 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.35422  |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.461064 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.511784 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.96751 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.422756 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.660523 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.331568 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.381413 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.625189 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.905217 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.584636 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.469033 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.637997 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.916289 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.291342 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.84109 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.909338 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.842605 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.598346 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7031976779753377,
    "polaris/pkis2-ret-wt-reg-v2": 762.6276148918181,
    "polaris/pkis2-kit-wt-cls-v2": 0.695942726566932,
    "polaris/pkis2-kit-wt-reg-v2": 840.0720324877313,
    "polaris/pkis2-egfr-wt-reg-v2": 537.3255974121753,
    "polaris/adme-fang-solu-1": 0.6532565941080586,
    "polaris/adme-fang-rppb-1": 0.7028171058322304,
    "polaris/adme-fang-hppb-1": 0.8292825953154515,
    "polaris/adme-fang-perm-1": 0.7721938791764541,
    "polaris/adme-fang-rclint-1": 0.7167509474170414,
    "polaris/adme-fang-hclint-1": 0.6851120057227422,
    "tdcommons/lipophilicity-astrazeneca": 0.5117837470996948,
    "tdcommons/ppbr-az": 7.96751179812846,
    "tdcommons/clearance-hepatocyte-az": 0.42275626441845887,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6605230912220232,
    "tdcommons/half-life-obach": 0.33156826893959523,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3814126245028167,
    "tdcommons/clearance-microsome-az": 0.6251890564041842,
    "tdcommons/dili": 0.9052173913043479,
    "tdcommons/bioavailability-ma": 0.5846358496840705,
    "tdcommons/vdss-lombardo": 0.46903347854917116,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.637997287522604,
    "tdcommons/pgp-broccatelli": 0.9162889896027725,
    "tdcommons/caco2-wang": 0.2913417933868744,
    "tdcommons/herg": 0.8410898379970545,
    "tdcommons/bbb-martins": 0.9093378674171357,
    "tdcommons/ames": 0.842605102899998,
    "tdcommons/ld50-zhu": 0.598346359714281
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.858559 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.448395 |
|  2 | test       | CLS_RET        | f1          | 0.5      |
|  3 | test       | CLS_RET        | accuracy    | 0.886792 |
|  4 | test       | CLS_RET        | mcc         | 0.504899 |
|  5 | test       | CLS_RET        | pr_auc      | 0.673463 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.533856 |
|  1 | test       | RET            | pearsonr            |   0.549582 |
|  2 | test       | RET            | explained_var       |   0.30194  |
|  3 | test       | RET            | mean_squared_error  | 864.229    |
|  4 | test       | RET            | mean_absolute_error |  22.7145   |
|  5 | test       | RET            | r2                  |   0.27217  |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.821567 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.54382  |
|  2 | test       | CLS_KIT        | f1          | 0.611111 |
|  3 | test       | CLS_KIT        | accuracy    | 0.87931  |
|  4 | test       | CLS_KIT        | mcc         | 0.563295 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.624494 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.481095 |
|  1 | test       | KIT            | pearsonr            |   0.536196 |
|  2 | test       | KIT            | explained_var       |   0.259773 |
|  3 | test       | KIT            | mean_squared_error  | 902.168    |
|  4 | test       | KIT            | mean_absolute_error |  23.1405   |
|  5 | test       | KIT            | r2                  |   0.252358 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.303189 |
|  1 | test       | EGFR           | pearsonr            |   0.643943 |
|  2 | test       | EGFR           | explained_var       |   0.407309 |
|  3 | test       | EGFR           | mean_squared_error  | 487.345    |
|  4 | test       | EGFR           | mean_absolute_error |  17.5965   |
|  5 | test       | EGFR           | r2                  |   0.39518  |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.557261 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.667388 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.444332 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.319803 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.39119  |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.410152 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.81913  |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.783448 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.590548 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.368997 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.437134 |
|  5 | test       | LOG_RPPB       | r2                  | 0.584688 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.837956 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.826496 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.651137 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.25117  |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.418034 |
|  5 | test       | LOG_HPPB       | r2                  | 0.585281 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.790392 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.793841 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.629874 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.183358 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.323778 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.629873 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.733159 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.728899 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.531286 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.264951 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.407152 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.53068  |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.719316 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.703079 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.471003 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.205621 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.353317 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.470609 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.529014 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.53407 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.385752 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.633791 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr |   0.349 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.366693 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.644104 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.898696 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.59694 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.391687 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.672129 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.928019 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.299008 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.826362 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.899351 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.848256 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  0.6156 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6734633030564496,
    "polaris/pkis2-ret-wt-reg-v2": 864.2291290080526,
    "polaris/pkis2-kit-wt-cls-v2": 0.6244940341614681,
    "polaris/pkis2-kit-wt-reg-v2": 902.1682182291989,
    "polaris/pkis2-egfr-wt-reg-v2": 487.34480529564684,
    "polaris/adme-fang-solu-1": 0.6673876553475779,
    "polaris/adme-fang-rppb-1": 0.7834483117211454,
    "polaris/adme-fang-hppb-1": 0.8264955754207893,
    "polaris/adme-fang-perm-1": 0.7938413329140811,
    "polaris/adme-fang-rclint-1": 0.7288993413904653,
    "polaris/adme-fang-hclint-1": 0.703079243895953,
    "tdcommons/lipophilicity-astrazeneca": 0.5290139116786776,
    "tdcommons/ppbr-az": 8.534067959589267,
    "tdcommons/clearance-hepatocyte-az": 0.3857522313799602,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6337910183280023,
    "tdcommons/half-life-obach": 0.3489998630754041,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.36669296737333495,
    "tdcommons/clearance-microsome-az": 0.6441042417088596,
    "tdcommons/dili": 0.8986956521739131,
    "tdcommons/bioavailability-ma": 0.59694047223146,
    "tdcommons/vdss-lombardo": 0.39168714557607065,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.672129294755877,
    "tdcommons/pgp-broccatelli": 0.928019194881365,
    "tdcommons/caco2-wang": 0.29900798362425085,
    "tdcommons/herg": 0.8263622974963181,
    "tdcommons/bbb-martins": 0.8993511569731081,
    "tdcommons/ames": 0.848256280718244,
    "tdcommons/ld50-zhu": 0.6155999330235431
}
```
