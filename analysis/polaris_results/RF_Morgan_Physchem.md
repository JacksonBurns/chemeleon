# Random Forest Baseline Results
timestamp: 2025-10-06 15:52:33.327426
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.867925 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.356461 |
|  2 | test       | CLS_RET        | pr_auc      | 0.702296 |
|  3 | test       | CLS_RET        | mcc         | 0.40138  |
|  4 | test       | CLS_RET        | roc_auc     | 0.870787 |
|  5 | test       | CLS_RET        | f1          | 0.416667 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.37823  |
|  1 | test       | RET            | pearsonr            |   0.633146 |
|  2 | test       | RET            | mean_absolute_error |  20.7948   |
|  3 | test       | RET            | spearmanr           |   0.587224 |
|  4 | test       | RET            | mean_squared_error  | 738.292    |
|  5 | test       | RET            | explained_var       |   0.397307 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.862069 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.456674 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.639495 |
|  3 | test       | CLS_KIT        | mcc         | 0.485525 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.827369 |
|  5 | test       | CLS_KIT        | f1          | 0.529412 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.345187 |
|  1 | test       | KIT            | pearsonr            |   0.597525 |
|  2 | test       | KIT            | mean_absolute_error |  22.1839   |
|  3 | test       | KIT            | spearmanr           |   0.534787 |
|  4 | test       | KIT            | mean_squared_error  | 790.152    |
|  5 | test       | KIT            | explained_var       |   0.357021 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.394776 |
|  1 | test       | EGFR           | pearsonr            |   0.629572 |
|  2 | test       | EGFR           | mean_absolute_error |  16.923    |
|  3 | test       | EGFR           | spearmanr           |   0.369061 |
|  4 | test       | EGFR           | mean_squared_error  | 487.67     |
|  5 | test       | EGFR           | explained_var       |   0.396351 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.320169 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.576637 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.415963 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.484762 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.36859  |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.322975 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.498376 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.747581 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.475935 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.827826 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.445684 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.50043  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.559473 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.769676 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.394869 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.771335 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.2668   |
|  5 | test       | LOG_HPPB       | explained_var       | 0.592395 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.534406 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.742268 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.370155 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.734897 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.230652 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.534444 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.430775 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.656515 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.451224 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.662888 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.321352 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.430935 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.427349 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.655691 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.373156 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.658386 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.222423 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.428455 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.61872 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.42369 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.45287 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   |  0.7033 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.273986 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.386397 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.558189 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.937174 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.725141 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.513721 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.685014 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.91219 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.289759 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.856112 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.914087 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.851282 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.613274 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7022962189182829,
    "polaris/pkis2-ret-wt-reg-v2": 738.292302641741,
    "polaris/pkis2-kit-wt-cls-v2": 0.6394949390649558,
    "polaris/pkis2-kit-wt-reg-v2": 790.1523181514195,
    "polaris/pkis2-egfr-wt-reg-v2": 487.6700519336694,
    "polaris/adme-fang-solu-1": 0.5766367970185527,
    "polaris/adme-fang-rppb-1": 0.7475813075561359,
    "polaris/adme-fang-hppb-1": 0.7696757012383167,
    "polaris/adme-fang-perm-1": 0.7422680612964714,
    "polaris/adme-fang-rclint-1": 0.6565145508787393,
    "polaris/adme-fang-hclint-1": 0.6556908660676479,
    "tdcommons/lipophilicity-astrazeneca": 0.6187204014266818,
    "tdcommons/ppbr-az": 8.423688779930663,
    "tdcommons/clearance-hepatocyte-az": 0.4528695627538572,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7032998125195432,
    "tdcommons/half-life-obach": 0.273986386783736,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.38639745307808004,
    "tdcommons/clearance-microsome-az": 0.5581885932519405,
    "tdcommons/dili": 0.9371739130434783,
    "tdcommons/bioavailability-ma": 0.7251413368806119,
    "tdcommons/vdss-lombardo": 0.51372074311984,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6850135623869801,
    "tdcommons/pgp-broccatelli": 0.9121900826446281,
    "tdcommons/caco2-wang": 0.28975931479742817,
    "tdcommons/herg": 0.8561119293078056,
    "tdcommons/bbb-martins": 0.9140869293308318,
    "tdcommons/ames": 0.8512815994047269,
    "tdcommons/ld50-zhu": 0.6132743802516271
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.867925 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.356461 |
|  2 | test       | CLS_RET        | pr_auc      | 0.655123 |
|  3 | test       | CLS_RET        | mcc         | 0.40138  |
|  4 | test       | CLS_RET        | roc_auc     | 0.879709 |
|  5 | test       | CLS_RET        | f1          | 0.416667 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.380311 |
|  1 | test       | RET            | pearsonr            |   0.635088 |
|  2 | test       | RET            | mean_absolute_error |  20.9061   |
|  3 | test       | RET            | spearmanr           |   0.583701 |
|  4 | test       | RET            | mean_squared_error  | 735.822    |
|  5 | test       | RET            | explained_var       |   0.398669 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.434633 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.6631   |
|  3 | test       | CLS_KIT        | mcc         | 0.455516 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.829545 |
|  5 | test       | CLS_KIT        | f1          | 0.514286 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.347859 |
|  1 | test       | KIT            | pearsonr            |   0.59887  |
|  2 | test       | KIT            | mean_absolute_error |  22.1337   |
|  3 | test       | KIT            | spearmanr           |   0.540347 |
|  4 | test       | KIT            | mean_squared_error  | 786.928    |
|  5 | test       | KIT            | explained_var       |   0.358601 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.390839 |
|  1 | test       | EGFR           | pearsonr            |   0.626689 |
|  2 | test       | EGFR           | mean_absolute_error |  16.9823   |
|  3 | test       | EGFR           | spearmanr           |   0.368623 |
|  4 | test       | EGFR           | mean_squared_error  | 490.843    |
|  5 | test       | EGFR           | explained_var       |   0.392661 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.317998 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.57448  |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.41743  |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.484744 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.369767 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.320745 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.497907 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.739643 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.472594 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.806957 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.446101 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.501675 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.56388  |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.771291 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.394674 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.797311 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.264131 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.594889 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.533577 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.741649 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.370795 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.732194 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.231063 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.53362  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.423929 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.651289 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.454833 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.656637 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.325217 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.42416  |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.426743 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.654842 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.372726 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.654756 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.222659 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.427618 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.612669 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.34085 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.457497 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.682015 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.287431 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.405668 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.559682 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.931087 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.712005 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.526579 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.668174 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.916456 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.293053 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.860088 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.909572 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.853044 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.617335 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.655122818661775,
    "polaris/pkis2-ret-wt-reg-v2": 735.8218841595075,
    "polaris/pkis2-kit-wt-cls-v2": 0.6631003706029861,
    "polaris/pkis2-kit-wt-reg-v2": 786.9283760890141,
    "polaris/pkis2-egfr-wt-reg-v2": 490.8431297957482,
    "polaris/adme-fang-solu-1": 0.5744801635859775,
    "polaris/adme-fang-rppb-1": 0.7396428576488158,
    "polaris/adme-fang-hppb-1": 0.7712908116149757,
    "polaris/adme-fang-perm-1": 0.7416493460973683,
    "polaris/adme-fang-rclint-1": 0.6512885886198646,
    "polaris/adme-fang-hclint-1": 0.65484215594887,
    "tdcommons/lipophilicity-astrazeneca": 0.6126691195294786,
    "tdcommons/ppbr-az": 8.340848801959568,
    "tdcommons/clearance-hepatocyte-az": 0.45749745970707306,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6820148166515971,
    "tdcommons/half-life-obach": 0.2874305188377004,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4056683783858003,
    "tdcommons/clearance-microsome-az": 0.5596815842299602,
    "tdcommons/dili": 0.9310869565217392,
    "tdcommons/bioavailability-ma": 0.7120053209178583,
    "tdcommons/vdss-lombardo": 0.5265785447387326,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6681735985533455,
    "tdcommons/pgp-broccatelli": 0.9164556118368434,
    "tdcommons/caco2-wang": 0.29305341585230255,
    "tdcommons/herg": 0.8600883652430044,
    "tdcommons/bbb-martins": 0.9095723889931208,
    "tdcommons/ames": 0.8530439209696685,
    "tdcommons/ld50-zhu": 0.6173350299031295
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.867925 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.356461 |
|  2 | test       | CLS_RET        | pr_auc      | 0.671395 |
|  3 | test       | CLS_RET        | mcc         | 0.40138  |
|  4 | test       | CLS_RET        | roc_auc     | 0.890945 |
|  5 | test       | CLS_RET        | f1          | 0.416667 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.378143 |
|  1 | test       | RET            | pearsonr            |   0.633224 |
|  2 | test       | RET            | mean_absolute_error |  20.7227   |
|  3 | test       | RET            | spearmanr           |   0.586855 |
|  4 | test       | RET            | mean_squared_error  | 738.396    |
|  5 | test       | RET            | explained_var       |   0.397448 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.434633 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.66433  |
|  3 | test       | CLS_KIT        | mcc         | 0.455516 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.832205 |
|  5 | test       | CLS_KIT        | f1          | 0.514286 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.339051 |
|  1 | test       | KIT            | pearsonr            |   0.590865 |
|  2 | test       | KIT            | mean_absolute_error |  22.33     |
|  3 | test       | KIT            | spearmanr           |   0.526737 |
|  4 | test       | KIT            | mean_squared_error  | 797.556    |
|  5 | test       | KIT            | explained_var       |   0.349115 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.396929 |
|  1 | test       | EGFR           | pearsonr            |   0.631604 |
|  2 | test       | EGFR           | mean_absolute_error |  16.966    |
|  3 | test       | EGFR           | spearmanr           |   0.376298 |
|  4 | test       | EGFR           | mean_squared_error  | 485.935    |
|  5 | test       | EGFR           | explained_var       |   0.398816 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.316038 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.571402 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.417547 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.482317 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.37083  |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.31893  |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.492942 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.73684  |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.476963 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.830435 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.450512 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.495221 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.547803 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.757172 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.398714 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.759111 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.273868 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.573191 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.534354 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.742338 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.370344 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.734766 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.230677 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.534449 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.42753  |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.654026 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.453312 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.658862 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.323184 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.427672 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.427519 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.655727 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.373998 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.655653 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.222357 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.428586 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.616013 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.40959 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.445383 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.702467 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.30195 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.379456 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.558298 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.935652 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.715996 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.506501 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.668965 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.916756 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.290832 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.849485 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.915846 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.852872 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.616022 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6713953767885993,
    "polaris/pkis2-ret-wt-reg-v2": 738.3956308354489,
    "polaris/pkis2-kit-wt-cls-v2": 0.6643296234867189,
    "polaris/pkis2-kit-wt-reg-v2": 797.5564732856708,
    "polaris/pkis2-egfr-wt-reg-v2": 485.93520583959486,
    "polaris/adme-fang-solu-1": 0.5714022344521235,
    "polaris/adme-fang-rppb-1": 0.7368396602411788,
    "polaris/adme-fang-hppb-1": 0.7571721407044744,
    "polaris/adme-fang-perm-1": 0.7423379587534549,
    "polaris/adme-fang-rclint-1": 0.6540255567285498,
    "polaris/adme-fang-hclint-1": 0.655727232871322,
    "tdcommons/lipophilicity-astrazeneca": 0.6160126505763417,
    "tdcommons/ppbr-az": 8.409592311320063,
    "tdcommons/clearance-hepatocyte-az": 0.4453830982444433,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7024671621072562,
    "tdcommons/half-life-obach": 0.3019502790186238,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.37945612856429467,
    "tdcommons/clearance-microsome-az": 0.5582982383275713,
    "tdcommons/dili": 0.9356521739130435,
    "tdcommons/bioavailability-ma": 0.7159960093116062,
    "tdcommons/vdss-lombardo": 0.5065011608087224,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6689647377938517,
    "tdcommons/pgp-broccatelli": 0.9167555318581712,
    "tdcommons/caco2-wang": 0.29083218098212205,
    "tdcommons/herg": 0.8494845360824742,
    "tdcommons/bbb-martins": 0.9158458411507192,
    "tdcommons/ames": 0.8528716050833185,
    "tdcommons/ld50-zhu": 0.6160223779775329
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.867925 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.356461 |
|  2 | test       | CLS_RET        | pr_auc      | 0.661677 |
|  3 | test       | CLS_RET        | mcc         | 0.40138  |
|  4 | test       | CLS_RET        | roc_auc     | 0.892928 |
|  5 | test       | CLS_RET        | f1          | 0.416667 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.399526 |
|  1 | test       | RET            | pearsonr            |   0.65252  |
|  2 | test       | RET            | mean_absolute_error |  20.4289   |
|  3 | test       | RET            | spearmanr           |   0.591821 |
|  4 | test       | RET            | mean_squared_error  | 713.006    |
|  5 | test       | RET            | explained_var       |   0.419534 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.434633 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.658438 |
|  3 | test       | CLS_KIT        | mcc         | 0.455516 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.821325 |
|  5 | test       | CLS_KIT        | f1          | 0.514286 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.353331 |
|  1 | test       | KIT            | pearsonr            |   0.602194 |
|  2 | test       | KIT            | mean_absolute_error |  22.0227   |
|  3 | test       | KIT            | spearmanr           |   0.546976 |
|  4 | test       | KIT            | mean_squared_error  | 780.325    |
|  5 | test       | KIT            | explained_var       |   0.362638 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.394218 |
|  1 | test       | EGFR           | pearsonr            |   0.628827 |
|  2 | test       | EGFR           | mean_absolute_error |  16.9349   |
|  3 | test       | EGFR           | spearmanr           |   0.380753 |
|  4 | test       | EGFR           | mean_squared_error  | 488.12     |
|  5 | test       | EGFR           | explained_var       |   0.395252 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.31828  |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.574354 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.417285 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.483585 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.369614 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.320981 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.520859 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.758855 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.463716 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.825217 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.425708 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.522779 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.564671 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.770215 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.389709 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.786004 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.263652 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.593227 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.53516  |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.743719 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.37063  |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.735899 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.230278 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.535248 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.429779 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.655843 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.451919 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.660873 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.321914 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.430062 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.431774 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.658983 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.372603 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.658935 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.220705 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.432722 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.618985 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.36609 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.44295 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.699393 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.290467 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.397675 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.552027 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.927609 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.711506 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.510611 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.682753 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.916022 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.294397 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.850074 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.913852 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.849638 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.616369 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6616765295085815,
    "polaris/pkis2-ret-wt-reg-v2": 713.0064644675158,
    "polaris/pkis2-kit-wt-cls-v2": 0.6584377928207618,
    "polaris/pkis2-kit-wt-reg-v2": 780.3250566238698,
    "polaris/pkis2-egfr-wt-reg-v2": 488.11988789049997,
    "polaris/adme-fang-solu-1": 0.5743540444422812,
    "polaris/adme-fang-rppb-1": 0.7588553361533161,
    "polaris/adme-fang-hppb-1": 0.7702147598625363,
    "polaris/adme-fang-perm-1": 0.7437186814346628,
    "polaris/adme-fang-rclint-1": 0.6558428668795881,
    "polaris/adme-fang-hclint-1": 0.6589832917170034,
    "tdcommons/lipophilicity-astrazeneca": 0.6189848849489796,
    "tdcommons/ppbr-az": 8.36609366442348,
    "tdcommons/clearance-hepatocyte-az": 0.4429504803578977,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6993925428598509,
    "tdcommons/half-life-obach": 0.2904671560668705,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.39767463893449473,
    "tdcommons/clearance-microsome-az": 0.552026880867008,
    "tdcommons/dili": 0.927608695652174,
    "tdcommons/bioavailability-ma": 0.7115064848686399,
    "tdcommons/vdss-lombardo": 0.5106105212759879,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6827531645569621,
    "tdcommons/pgp-broccatelli": 0.9160223940282592,
    "tdcommons/caco2-wang": 0.29439655808968745,
    "tdcommons/herg": 0.8500736377025038,
    "tdcommons/bbb-martins": 0.9138524077548469,
    "tdcommons/ames": 0.849637745011651,
    "tdcommons/ld50-zhu": 0.6163685819554524
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.867925 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.356461 |
|  2 | test       | CLS_RET        | pr_auc      | 0.642802 |
|  3 | test       | CLS_RET        | mcc         | 0.40138  |
|  4 | test       | CLS_RET        | roc_auc     | 0.875413 |
|  5 | test       | CLS_RET        | f1          | 0.416667 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.383719 |
|  1 | test       | RET            | pearsonr            |   0.637204 |
|  2 | test       | RET            | mean_absolute_error |  20.8423   |
|  3 | test       | RET            | spearmanr           |   0.578628 |
|  4 | test       | RET            | mean_squared_error  | 731.775    |
|  5 | test       | RET            | explained_var       |   0.401906 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.434633 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.64359  |
|  3 | test       | CLS_KIT        | mcc         | 0.455516 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.817456 |
|  5 | test       | CLS_KIT        | f1          | 0.514286 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.352728 |
|  1 | test       | KIT            | pearsonr            |   0.601398 |
|  2 | test       | KIT            | mean_absolute_error |  22.1985   |
|  3 | test       | KIT            | spearmanr           |   0.543433 |
|  4 | test       | KIT            | mean_squared_error  | 781.053    |
|  5 | test       | KIT            | explained_var       |   0.361666 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.397478 |
|  1 | test       | EGFR           | pearsonr            |   0.631574 |
|  2 | test       | EGFR           | mean_absolute_error |  16.8909   |
|  3 | test       | EGFR           | spearmanr           |   0.362438 |
|  4 | test       | EGFR           | mean_squared_error  | 485.494    |
|  5 | test       | EGFR           | explained_var       |   0.39884  |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.323888 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.580213 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.417354 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.483201 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.366573 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.326509 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.512233 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.750619 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.472313 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.817391 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.433372 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.513011 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.558784 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.766704 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.395653 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.785392 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.267218 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.587803 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.534292 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.741684 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.370854 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.733477 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.230708 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.534374 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.433113 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.658404 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.450755 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.662974 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.320032 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.433244 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.431616 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.658885 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.372242 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.657408 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.220766 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.432576 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.612915 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.31931 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.44081 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.701919 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.279826 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.390227 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.54368 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.939783 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.710675 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.511877 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.673259 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.91399 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.285399 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.85729 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.909924 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.852545 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.615049 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6428021729193854,
    "polaris/pkis2-ret-wt-reg-v2": 731.7747044234593,
    "polaris/pkis2-kit-wt-cls-v2": 0.6435904039263369,
    "polaris/pkis2-kit-wt-reg-v2": 781.0527191325481,
    "polaris/pkis2-egfr-wt-reg-v2": 485.4935471331911,
    "polaris/adme-fang-solu-1": 0.5802129320447619,
    "polaris/adme-fang-rppb-1": 0.7506189492482753,
    "polaris/adme-fang-hppb-1": 0.7667044814177675,
    "polaris/adme-fang-perm-1": 0.7416841802547107,
    "polaris/adme-fang-rclint-1": 0.6584044243968235,
    "polaris/adme-fang-hclint-1": 0.6588851560782172,
    "tdcommons/lipophilicity-astrazeneca": 0.6129147870181406,
    "tdcommons/ppbr-az": 8.319313248932342,
    "tdcommons/clearance-hepatocyte-az": 0.4408098102232341,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7019193888443429,
    "tdcommons/half-life-obach": 0.27982551090151375,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.39022712464498477,
    "tdcommons/clearance-microsome-az": 0.5436802204982614,
    "tdcommons/dili": 0.9397826086956521,
    "tdcommons/bioavailability-ma": 0.7106750914532757,
    "tdcommons/vdss-lombardo": 0.5118773791455296,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6732594936708861,
    "tdcommons/pgp-broccatelli": 0.9139896027725939,
    "tdcommons/caco2-wang": 0.28539914140801037,
    "tdcommons/herg": 0.8572901325478645,
    "tdcommons/bbb-martins": 0.9099241713570981,
    "tdcommons/ames": 0.8525445965262684,
    "tdcommons/ld50-zhu": 0.6150487332533239
}
```
