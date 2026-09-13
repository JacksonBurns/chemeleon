# ChemProp Baseline Results
timestamp: 2026-09-13 12:54:48.012290
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.653239 |
|  1 | test       | CLS_RET        | roc_auc     | 0.848645 |
|  2 | test       | CLS_RET        | mcc         | 0.40138  |
|  3 | test       | CLS_RET        | accuracy    | 0.867925 |
|  4 | test       | CLS_RET        | cohen_kappa | 0.356461 |
|  5 | test       | CLS_RET        | f1          | 0.416667 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.332097 |
|  1 | test       | RET            | mean_squared_error  | 793.072    |
|  2 | test       | RET            | explained_var       |   0.357525 |
|  3 | test       | RET            | spearmanr           |   0.565527 |
|  4 | test       | RET            | pearsonr            |   0.597978 |
|  5 | test       | RET            | mean_absolute_error |  21.5033   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.577029 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.818665 |
|  2 | test       | CLS_KIT        | mcc         | 0.460742 |
|  3 | test       | CLS_KIT        | accuracy    | 0.844828 |
|  4 | test       | CLS_KIT        | cohen_kappa | 0.45738  |
|  5 | test       | CLS_KIT        | f1          | 0.55     |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.303326 |
|  1 | test       | KIT            | mean_squared_error  | 840.665    |
|  2 | test       | KIT            | explained_var       |   0.327078 |
|  3 | test       | KIT            | spearmanr           |   0.519484 |
|  4 | test       | KIT            | pearsonr            |   0.577179 |
|  5 | test       | KIT            | mean_absolute_error |  21.8952   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.429285 |
|  1 | test       | EGFR           | mean_squared_error  | 459.864    |
|  2 | test       | EGFR           | explained_var       |   0.429617 |
|  3 | test       | EGFR           | spearmanr           |   0.305592 |
|  4 | test       | EGFR           | pearsonr            |   0.656794 |
|  5 | test       | EGFR           | mean_absolute_error |  16.8498   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.389707 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.330888 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.390597 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.516622 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.625054 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.385578 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.143123 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.76132  |
|  2 | test       | LOG_RPPB       | explained_var       | 0.146762 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.503478 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.404264 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.679785 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.461548 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.326107 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.474404 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.745817 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.722666 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.501233 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.623487 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.186522 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.623709 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.78297  |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.790514 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.317793 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.518642 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.271747 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.528018 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.729705 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.729687 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.414558 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.475966 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.20354  |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.475967 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.726493 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.716871 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.350799 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.450255 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.56569 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.374963 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.586432 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.32604 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.43666 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.480817 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.927391 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.590289 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.100445 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.57561 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.907891 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.340337 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.86539 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.904667 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.844324 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.569112 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6532389562537256,
    "polaris/pkis2-ret-wt-reg-v2": 793.0718668829205,
    "polaris/pkis2-kit-wt-cls-v2": 0.577028634064629,
    "polaris/pkis2-kit-wt-reg-v2": 840.6654370167155,
    "polaris/pkis2-egfr-wt-reg-v2": 459.864077363245,
    "polaris/adme-fang-solu-1": 0.6250544998217591,
    "polaris/adme-fang-rppb-1": 0.4042641903671878,
    "polaris/adme-fang-hppb-1": 0.7226655691279167,
    "polaris/adme-fang-perm-1": 0.7905136619394019,
    "polaris/adme-fang-rclint-1": 0.729687149991936,
    "polaris/adme-fang-hclint-1": 0.7168709873885585,
    "tdcommons/lipophilicity-astrazeneca": 0.4502545158068339,
    "tdcommons/ppbr-az": 7.565692411364723,
    "tdcommons/clearance-hepatocyte-az": 0.3749629427110725,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.586432344230687,
    "tdcommons/half-life-obach": 0.32603971483701627,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.43665961393193986,
    "tdcommons/clearance-microsome-az": 0.4808165314247363,
    "tdcommons/dili": 0.9273913043478261,
    "tdcommons/bioavailability-ma": 0.5902893249085468,
    "tdcommons/vdss-lombardo": 0.10044480384979057,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5756103074141049,
    "tdcommons/pgp-broccatelli": 0.9078912290055985,
    "tdcommons/caco2-wang": 0.3403372058425401,
    "tdcommons/herg": 0.8653902798232695,
    "tdcommons/bbb-martins": 0.9046669793621013,
    "tdcommons/ames": 0.844324345493352,
    "tdcommons/ld50-zhu": 0.5691122919503342
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.682105 |
|  1 | test       | CLS_RET        | roc_auc     | 0.844679 |
|  2 | test       | CLS_RET        | mcc         | 0.449209 |
|  3 | test       | CLS_RET        | accuracy    | 0.877358 |
|  4 | test       | CLS_RET        | cohen_kappa | 0.383169 |
|  5 | test       | CLS_RET        | f1          | 0.434783 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.226741 |
|  1 | test       | RET            | mean_squared_error  | 918.171    |
|  2 | test       | RET            | explained_var       |   0.281277 |
|  3 | test       | RET            | spearmanr           |   0.540442 |
|  4 | test       | RET            | pearsonr            |   0.537565 |
|  5 | test       | RET            | mean_absolute_error |  22.686    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.533336 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.76354  |
|  2 | test       | CLS_KIT        | mcc         | 0.359135 |
|  3 | test       | CLS_KIT        | accuracy    | 0.818966 |
|  4 | test       | CLS_KIT        | cohen_kappa | 0.354873 |
|  5 | test       | CLS_KIT        | f1          | 0.461538 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.287068 |
|  1 | test       | KIT            | mean_squared_error  | 860.283    |
|  2 | test       | KIT            | explained_var       |   0.298618 |
|  3 | test       | KIT            | spearmanr           |   0.501477 |
|  4 | test       | KIT            | pearsonr            |   0.571663 |
|  5 | test       | KIT            | mean_absolute_error |  22.1237   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.4028   |
|  1 | test       | EGFR           | mean_squared_error  | 481.205    |
|  2 | test       | EGFR           | explained_var       |   0.402944 |
|  3 | test       | EGFR           | spearmanr           |   0.29344  |
|  4 | test       | EGFR           | pearsonr            |   0.641732 |
|  5 | test       | EGFR           | mean_absolute_error |  17.2924   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.38015  |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.33607  |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.384358 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.519895 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.62153  |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.404023 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.213087 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.699158 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.216299 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.621739 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.467391 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.622983 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.427782 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.346557 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.506865 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.714799 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.712895 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.488162 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.616445 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.19001  |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.616492 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.787161 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.785561 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.323661 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.524872 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.26823  |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.528126 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.73404  |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.730512 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.407562 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.495406 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.195989 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.499532 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.723426 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.721501 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.34614  |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.433533 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.79611 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.377093 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.680269 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0825916 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.386484 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.643503 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.930435 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.486199 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.403845 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.590303 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.868302 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.28987 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.771576 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.901384 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.829924 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.637828 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6821054506175614,
    "polaris/pkis2-ret-wt-reg-v2": 918.1711753924293,
    "polaris/pkis2-kit-wt-cls-v2": 0.5333359523647793,
    "polaris/pkis2-kit-wt-reg-v2": 860.2833717538887,
    "polaris/pkis2-egfr-wt-reg-v2": 481.2049355495591,
    "polaris/adme-fang-solu-1": 0.6215301280571739,
    "polaris/adme-fang-rppb-1": 0.46739144169202573,
    "polaris/adme-fang-hppb-1": 0.7128948849169324,
    "polaris/adme-fang-perm-1": 0.7855608632249067,
    "polaris/adme-fang-rclint-1": 0.730511613236206,
    "polaris/adme-fang-hclint-1": 0.7215013204723226,
    "tdcommons/lipophilicity-astrazeneca": 0.43353337079570403,
    "tdcommons/ppbr-az": 7.7961076131148515,
    "tdcommons/clearance-hepatocyte-az": 0.37709294720658465,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6802692372498671,
    "tdcommons/half-life-obach": 0.08259155378932057,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3864839376858693,
    "tdcommons/clearance-microsome-az": 0.643503361365594,
    "tdcommons/dili": 0.9304347826086956,
    "tdcommons/bioavailability-ma": 0.4861988693049551,
    "tdcommons/vdss-lombardo": 0.40384491568834907,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5903028933092225,
    "tdcommons/pgp-broccatelli": 0.8683017861903493,
    "tdcommons/caco2-wang": 0.2898704119969631,
    "tdcommons/herg": 0.7715758468335788,
    "tdcommons/bbb-martins": 0.9013836772983115,
    "tdcommons/ames": 0.8299242201727075,
    "tdcommons/ld50-zhu": 0.637828238229145
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.620079 |
|  1 | test       | CLS_RET        | roc_auc     | 0.837409 |
|  2 | test       | CLS_RET        | mcc         | 0.512494 |
|  3 | test       | CLS_RET        | accuracy    | 0.886792 |
|  4 | test       | CLS_RET        | cohen_kappa | 0.480816 |
|  5 | test       | CLS_RET        | f1          | 0.538462 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.328126 |
|  1 | test       | RET            | mean_squared_error  | 797.787    |
|  2 | test       | RET            | explained_var       |   0.328522 |
|  3 | test       | RET            | spearmanr           |   0.518142 |
|  4 | test       | RET            | pearsonr            |   0.575477 |
|  5 | test       | RET            | mean_absolute_error |  22.515    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.595955 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.799323 |
|  2 | test       | CLS_KIT        | mcc         | 0.443872 |
|  3 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  4 | test       | CLS_KIT        | cohen_kappa | 0.410287 |
|  5 | test       | CLS_KIT        | f1          | 0.484848 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.350636 |
|  1 | test       | KIT            | mean_squared_error  | 783.577    |
|  2 | test       | KIT            | explained_var       |   0.356054 |
|  3 | test       | KIT            | spearmanr           |   0.551382 |
|  4 | test       | KIT            | pearsonr            |   0.606725 |
|  5 | test       | KIT            | mean_absolute_error |  21.2936   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.394338 |
|  1 | test       | EGFR           | mean_squared_error  | 488.023    |
|  2 | test       | EGFR           | explained_var       |   0.394616 |
|  3 | test       | EGFR           | spearmanr           |   0.262689 |
|  4 | test       | EGFR           | pearsonr            |   0.632174 |
|  5 | test       | EGFR           | mean_absolute_error |  17.1844   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.358782 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.347655 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.358825 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.521149 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.600414 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.396231 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.394097 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.538334 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.402273 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.695652 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.63425  |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.544303 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.121625 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.531978 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.217167 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.707159 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.679222 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.653273 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.600679 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.197821 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.604088 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.77607  |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.777568 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.333638 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.510803 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.276173 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.514903 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.725167 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.720504 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.421471 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.471856 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.205136 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.47235  |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.700247 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.689082 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.357557 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.443042 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.47488 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.383066 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.606789 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.230062 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.44086 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.590266 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.916522 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.609245 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.49773 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.576062 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.889163 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.383695 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.82106 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.919012 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.844011 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.596404 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6200789412201274,
    "polaris/pkis2-ret-wt-reg-v2": 797.7868123808597,
    "polaris/pkis2-kit-wt-cls-v2": 0.5959548716022397,
    "polaris/pkis2-kit-wt-reg-v2": 783.5771009732659,
    "polaris/pkis2-egfr-wt-reg-v2": 488.02316535937837,
    "polaris/adme-fang-solu-1": 0.6004139958582255,
    "polaris/adme-fang-rppb-1": 0.6342498595305813,
    "polaris/adme-fang-hppb-1": 0.6792216177580586,
    "polaris/adme-fang-perm-1": 0.7775676077866488,
    "polaris/adme-fang-rclint-1": 0.7205040824373982,
    "polaris/adme-fang-hclint-1": 0.6890823925387871,
    "tdcommons/lipophilicity-astrazeneca": 0.44304210986409864,
    "tdcommons/ppbr-az": 7.474882018442444,
    "tdcommons/clearance-hepatocyte-az": 0.38306591442264665,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6067889019745747,
    "tdcommons/half-life-obach": 0.23006152687084447,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.44086028377888464,
    "tdcommons/clearance-microsome-az": 0.5902658630155562,
    "tdcommons/dili": 0.9165217391304348,
    "tdcommons/bioavailability-ma": 0.6092450947788494,
    "tdcommons/vdss-lombardo": 0.49772984775856904,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5760623869801085,
    "tdcommons/pgp-broccatelli": 0.8891628898960278,
    "tdcommons/caco2-wang": 0.3836946810928848,
    "tdcommons/herg": 0.821060382916053,
    "tdcommons/bbb-martins": 0.9190118824265165,
    "tdcommons/ames": 0.8440110438818069,
    "tdcommons/ld50-zhu": 0.5964043493735453
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.55409  |
|  1 | test       | CLS_RET        | roc_auc     | 0.842036 |
|  2 | test       | CLS_RET        | mcc         | 0.420262 |
|  3 | test       | CLS_RET        | accuracy    | 0.867925 |
|  4 | test       | CLS_RET        | cohen_kappa | 0.394286 |
|  5 | test       | CLS_RET        | f1          | 0.461538 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.27565  |
|  1 | test       | RET            | mean_squared_error  | 860.097    |
|  2 | test       | RET            | explained_var       |   0.280306 |
|  3 | test       | RET            | spearmanr           |   0.491235 |
|  4 | test       | RET            | pearsonr            |   0.531551 |
|  5 | test       | RET            | mean_absolute_error |  23.888    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.64041  |
|  1 | test       | CLS_KIT        | roc_auc     | 0.796905 |
|  2 | test       | CLS_KIT        | mcc         | 0.455516 |
|  3 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  4 | test       | CLS_KIT        | cohen_kappa | 0.434633 |
|  5 | test       | CLS_KIT        | f1          | 0.514286 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.298132 |
|  1 | test       | KIT            | mean_squared_error  | 846.933    |
|  2 | test       | KIT            | explained_var       |   0.372963 |
|  3 | test       | KIT            | spearmanr           |   0.573368 |
|  4 | test       | KIT            | pearsonr            |   0.612863 |
|  5 | test       | KIT            | mean_absolute_error |  21.4235   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.388094 |
|  1 | test       | EGFR           | mean_squared_error  | 493.054    |
|  2 | test       | EGFR           | explained_var       |   0.396912 |
|  3 | test       | EGFR           | spearmanr           |   0.291418 |
|  4 | test       | EGFR           | pearsonr            |   0.640553 |
|  5 | test       | EGFR           | mean_absolute_error |  17.3222   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.359348 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.347348 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.361579 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.496867 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.607779 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.41641  |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.176847 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.731356 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.196276 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.626957 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.444766 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.656086 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.386917 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.371307 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.497906 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.742303 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.764654 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.456198 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.631117 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.182742 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.631946 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.790414 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.79512  |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.316197 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.503879 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.280082 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.504185 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.718333 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.713143 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.41499  |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.501322 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.193691 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.501485 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.72351  |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.718454 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.332294 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.442395 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.34361 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.396631 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.625281 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.33013 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.391903 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.558929 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.935217 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.530762 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.319218 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.56137 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.909358 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.286328 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.852872 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.903768 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.846081 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.586314 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5540897251030122,
    "polaris/pkis2-ret-wt-reg-v2": 860.0971741455311,
    "polaris/pkis2-kit-wt-cls-v2": 0.6404097528923149,
    "polaris/pkis2-kit-wt-reg-v2": 846.9332513983607,
    "polaris/pkis2-egfr-wt-reg-v2": 493.05435425270855,
    "polaris/adme-fang-solu-1": 0.6077787749358238,
    "polaris/adme-fang-rppb-1": 0.4447658922261739,
    "polaris/adme-fang-hppb-1": 0.7646541960207816,
    "polaris/adme-fang-perm-1": 0.7951197580006311,
    "polaris/adme-fang-rclint-1": 0.7131430749470719,
    "polaris/adme-fang-hclint-1": 0.7184536423386861,
    "tdcommons/lipophilicity-astrazeneca": 0.4423954875923338,
    "tdcommons/ppbr-az": 7.343608388337765,
    "tdcommons/clearance-hepatocyte-az": 0.39663145471898903,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6252814729191336,
    "tdcommons/half-life-obach": 0.3301296260391686,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.39190259834798946,
    "tdcommons/clearance-microsome-az": 0.558928994889567,
    "tdcommons/dili": 0.9352173913043478,
    "tdcommons/bioavailability-ma": 0.5307615563684736,
    "tdcommons/vdss-lombardo": 0.3192177833254865,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.561369801084991,
    "tdcommons/pgp-broccatelli": 0.9093575046654225,
    "tdcommons/caco2-wang": 0.28632762917537485,
    "tdcommons/herg": 0.8528718703976436,
    "tdcommons/bbb-martins": 0.9037679799874923,
    "tdcommons/ames": 0.8460807926530773,
    "tdcommons/ld50-zhu": 0.5863143701153292
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.640153 |
|  1 | test       | CLS_RET        | roc_auc     | 0.834765 |
|  2 | test       | CLS_RET        | mcc         | 0.512494 |
|  3 | test       | CLS_RET        | accuracy    | 0.886792 |
|  4 | test       | CLS_RET        | cohen_kappa | 0.480816 |
|  5 | test       | CLS_RET        | f1          | 0.538462 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.304192 |
|  1 | test       | RET            | mean_squared_error  | 826.206    |
|  2 | test       | RET            | explained_var       |   0.33397  |
|  3 | test       | RET            | spearmanr           |   0.561178 |
|  4 | test       | RET            | pearsonr            |   0.578247 |
|  5 | test       | RET            | mean_absolute_error |  21.9055   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.640007 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.866054 |
|  2 | test       | CLS_KIT        | mcc         | 0.330432 |
|  3 | test       | CLS_KIT        | accuracy    | 0.836207 |
|  4 | test       | CLS_KIT        | cohen_kappa | 0.243132 |
|  5 | test       | CLS_KIT        | f1          | 0.296296 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.345191 |
|  1 | test       | KIT            | mean_squared_error  | 790.147    |
|  2 | test       | KIT            | explained_var       |   0.369845 |
|  3 | test       | KIT            | spearmanr           |   0.573403 |
|  4 | test       | KIT            | pearsonr            |   0.613237 |
|  5 | test       | KIT            | mean_absolute_error |  20.9331   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.317543 |
|  1 | test       | EGFR           | mean_squared_error  | 549.902    |
|  2 | test       | EGFR           | explained_var       |   0.326275 |
|  3 | test       | EGFR           | spearmanr           |   0.237669 |
|  4 | test       | EGFR           | pearsonr            |   0.602366 |
|  5 | test       | EGFR           | mean_absolute_error |  18.0963   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.360815 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.346552 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.401075 |
|  3 | test       | LOG_SOLUBILITY | spearmanr           | 0.506147 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.637116 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.373161 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.171272 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.73631  |
|  2 | test       | LOG_RPPB       | explained_var       | 0.205771 |
|  3 | test       | LOG_RPPB       | spearmanr           | 0.593913 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.456417 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.680546 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.506221 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.299052 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.595417 |
|  3 | test       | LOG_HPPB       | spearmanr           | 0.778364 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.78606  |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.424896 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.623648 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.186442 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.628854 |
|  3 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.783915 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.793884 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.319388 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.512137 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.27542  |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.514322 |
|  3 | test       | LOG_RLM_CLint  | spearmanr           | 0.723378 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.71886  |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.418429 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.45769  |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.210638 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.457759 |
|  3 | test       | LOG_HLM_CLint  | spearmanr           | 0.691119 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.68277  |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.351438 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.43832 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.74904 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.393221 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.571708 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.323081 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.379675 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.597456 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.94087 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.541071 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.397447 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.670547 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.923687 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.360514 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.836377 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.921025 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.81579 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.627336 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.640152924275817,
    "polaris/pkis2-ret-wt-reg-v2": 826.2055757990747,
    "polaris/pkis2-kit-wt-cls-v2": 0.6400073733058068,
    "polaris/pkis2-kit-wt-reg-v2": 790.1473358950786,
    "polaris/pkis2-egfr-wt-reg-v2": 549.9021893955879,
    "polaris/adme-fang-solu-1": 0.6371157142058103,
    "polaris/adme-fang-rppb-1": 0.45641741794228147,
    "polaris/adme-fang-hppb-1": 0.7860603095159101,
    "polaris/adme-fang-perm-1": 0.793883872839361,
    "polaris/adme-fang-rclint-1": 0.7188601614924062,
    "polaris/adme-fang-hclint-1": 0.6827699282103423,
    "tdcommons/lipophilicity-astrazeneca": 0.4383197101014001,
    "tdcommons/ppbr-az": 7.749040149286095,
    "tdcommons/clearance-hepatocyte-az": 0.3932213856822941,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5717075008119006,
    "tdcommons/half-life-obach": 0.3230807337572261,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3796749366741238,
    "tdcommons/clearance-microsome-az": 0.597456301166981,
    "tdcommons/dili": 0.9408695652173913,
    "tdcommons/bioavailability-ma": 0.541070834718989,
    "tdcommons/vdss-lombardo": 0.3974471054999935,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6705470162748643,
    "tdcommons/pgp-broccatelli": 0.9236870167955211,
    "tdcommons/caco2-wang": 0.3605139550193703,
    "tdcommons/herg": 0.8363770250368189,
    "tdcommons/bbb-martins": 0.9210248592870544,
    "tdcommons/ames": 0.8157904012218764,
    "tdcommons/ld50-zhu": 0.6273358566861029
}
```
