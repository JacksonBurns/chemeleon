# ChemProp Baseline Results
timestamp: 2025-06-06 23:23:53.158371
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.591365 |
|  1 | test       | CLS_RET        | f1          | 0.642857 |
|  2 | test       | CLS_RET        | roc_auc     | 0.857898 |
|  3 | test       | CLS_RET        | accuracy    | 0.90566  |
|  4 | test       | CLS_RET        | mcc         | 0.609983 |
|  5 | test       | CLS_RET        | pr_auc      | 0.681292 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.495958 |
|  1 | test       | RET            | r2                  |   0.179054 |
|  2 | test       | RET            | mean_squared_error  | 974.795    |
|  3 | test       | RET            | mean_absolute_error |  23.6964   |
|  4 | test       | RET            | pearsonr            |   0.505761 |
|  5 | test       | RET            | explained_var       |   0.182599 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.23875  |
|  1 | test       | CLS_KIT        | f1          | 0.322581 |
|  2 | test       | CLS_KIT        | roc_auc     | 0.75     |
|  3 | test       | CLS_KIT        | accuracy    | 0.818966 |
|  4 | test       | CLS_KIT        | mcc         | 0.270692 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.449859 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | spearmanr           |    0.387884  |
|  1 | test       | KIT            | r2                  |    0.0391298 |
|  2 | test       | KIT            | mean_squared_error  | 1159.47      |
|  3 | test       | KIT            | mean_absolute_error |   27.5895    |
|  4 | test       | KIT            | pearsonr            |    0.395621  |
|  5 | test       | KIT            | explained_var       |    0.0401712 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.406145 |
|  1 | test       | EGFR           | r2                  |   0.360949 |
|  2 | test       | EGFR           | mean_squared_error  | 514.927    |
|  3 | test       | EGFR           | mean_absolute_error |  18.0044   |
|  4 | test       | EGFR           | pearsonr            |   0.61038  |
|  5 | test       | EGFR           | explained_var       |   0.365195 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.391055 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.266667 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.397597 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.451693 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.524401 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.270578 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.83913  |
|  1 | test       | LOG_RPPB       | r2                  | 0.558417 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.392338 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.449085 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.771678 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.558775 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.861487 |
|  1 | test       | LOG_HPPB       | r2                  | 0.713281 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.173648 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.339894 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.847101 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.716726 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.742498 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.541898 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.22694  |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.373739 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.741292 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.546705 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.6707   |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.423095 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.325688 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.442002 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.667183 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.423266 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.652253 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.361348 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.248059 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.391975 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.636645 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.363136 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.563106 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.72626 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.347704 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.654724 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.229983 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.357391 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.510614 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  |    0.89 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.672098 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0586414 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.595615 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.914889 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.302594 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.829455 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.915299 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.826932 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.642665 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6812923652772394,
    "polaris/pkis2-ret-wt-reg-v2": 974.7948850814573,
    "polaris/pkis2-kit-wt-cls-v2": 0.4498589599917152,
    "polaris/pkis2-kit-wt-reg-v2": 1159.4666851823354,
    "polaris/pkis2-egfr-wt-reg-v2": 514.9274188562918,
    "polaris/adme-fang-solu-1": 0.5244006133822321,
    "polaris/adme-fang-rppb-1": 0.7716782840022649,
    "polaris/adme-fang-hppb-1": 0.8471007506189976,
    "polaris/adme-fang-perm-1": 0.7412924262400828,
    "polaris/adme-fang-rclint-1": 0.6671832316542522,
    "polaris/adme-fang-hclint-1": 0.6366447653936873,
    "tdcommons/lipophilicity-astrazeneca": 0.5631056279738744,
    "tdcommons/ppbr-az": 8.726259480921655,
    "tdcommons/clearance-hepatocyte-az": 0.34770351191320226,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6547239890342633,
    "tdcommons/half-life-obach": 0.22998291577950858,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.35739104665610866,
    "tdcommons/clearance-microsome-az": 0.5106144190126893,
    "tdcommons/dili": 0.89,
    "tdcommons/bioavailability-ma": 0.6720984369803791,
    "tdcommons/vdss-lombardo": 0.05864140112741096,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.595614828209765,
    "tdcommons/pgp-broccatelli": 0.9148893628365768,
    "tdcommons/caco2-wang": 0.3025941727443654,
    "tdcommons/herg": 0.8294550810014727,
    "tdcommons/bbb-martins": 0.9152986241400876,
    "tdcommons/ames": 0.8269321897824512,
    "tdcommons/ld50-zhu": 0.6426650862293735
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.420521 |
|  1 | test       | CLS_RET        | f1          | 0.48     |
|  2 | test       | CLS_RET        | roc_auc     | 0.847984 |
|  3 | test       | CLS_RET        | accuracy    | 0.877358 |
|  4 | test       | CLS_RET        | mcc         | 0.459084 |
|  5 | test       | CLS_RET        | pr_auc      | 0.634402 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.571758 |
|  1 | test       | RET            | r2                  |   0.272874 |
|  2 | test       | RET            | mean_squared_error  | 863.394    |
|  3 | test       | RET            | mean_absolute_error |  21.8068   |
|  4 | test       | RET            | pearsonr            |   0.575206 |
|  5 | test       | RET            | explained_var       |   0.316971 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.102064 |
|  1 | test       | CLS_KIT        | f1          | 0.228571 |
|  2 | test       | CLS_KIT        | roc_auc     | 0.744197 |
|  3 | test       | CLS_KIT        | accuracy    | 0.767241 |
|  4 | test       | CLS_KIT        | mcc         | 0.106968 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.379229 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |         Score |
|---:|:-----------|:---------------|:--------------------|--------------:|
|  0 | test       | KIT            | spearmanr           |    0.402228   |
|  1 | test       | KIT            | r2                  |    0.0012489  |
|  2 | test       | KIT            | mean_squared_error  | 1205.18       |
|  3 | test       | KIT            | mean_absolute_error |   27.5013     |
|  4 | test       | KIT            | pearsonr            |    0.405581   |
|  5 | test       | KIT            | explained_var       |    0.00242809 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.329513 |
|  1 | test       | EGFR           | r2                  |   0.304382 |
|  2 | test       | EGFR           | mean_squared_error  | 560.507    |
|  3 | test       | EGFR           | mean_absolute_error |  18.3961   |
|  4 | test       | EGFR           | pearsonr            |   0.590193 |
|  5 | test       | EGFR           | explained_var       |   0.305291 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.497512 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.317272 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.37016  |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.417776 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.572239 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.319561 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.853913 |
|  1 | test       | LOG_RPPB       | r2                  | 0.637299 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.322254 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.423712 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.822259 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.675346 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.823898 |
|  1 | test       | LOG_HPPB       | r2                  | 0.395743 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.365961 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.521377 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.800767 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.539085 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.717108 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.503279 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.246072 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.381503 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.718634 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.511222 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.663771 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.421531 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.326571 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.447862 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.658104 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.426221 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.625647 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.369421 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.244923 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.396307 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.612923 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.374978 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.553907 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.78796 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.326086 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.692319 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.190346 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.368032 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.442213 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.866522 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.661124 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.321055 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.620479 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.916756 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.31676 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.820177 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.924523 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.825238 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.650236 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6344018471678046,
    "polaris/pkis2-ret-wt-reg-v2": 863.3936273610473,
    "polaris/pkis2-kit-wt-cls-v2": 0.3792292700630764,
    "polaris/pkis2-kit-wt-reg-v2": 1205.1770215162046,
    "polaris/pkis2-egfr-wt-reg-v2": 560.5067840620939,
    "polaris/adme-fang-solu-1": 0.5722389133202895,
    "polaris/adme-fang-rppb-1": 0.8222592683886304,
    "polaris/adme-fang-hppb-1": 0.8007673688768613,
    "polaris/adme-fang-perm-1": 0.7186336035546137,
    "polaris/adme-fang-rclint-1": 0.6581035983343694,
    "polaris/adme-fang-hclint-1": 0.6129233702564325,
    "tdcommons/lipophilicity-astrazeneca": 0.5539071068820499,
    "tdcommons/ppbr-az": 8.787958548721559,
    "tdcommons/clearance-hepatocyte-az": 0.32608606496850845,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6923192660916531,
    "tdcommons/half-life-obach": 0.19034570177471713,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.36803213035465504,
    "tdcommons/clearance-microsome-az": 0.44221299212990506,
    "tdcommons/dili": 0.8665217391304347,
    "tdcommons/bioavailability-ma": 0.6611240438975723,
    "tdcommons/vdss-lombardo": 0.3210545643858381,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6204792043399638,
    "tdcommons/pgp-broccatelli": 0.9167555318581712,
    "tdcommons/caco2-wang": 0.3167599020517874,
    "tdcommons/herg": 0.8201767304860088,
    "tdcommons/bbb-martins": 0.924523139462164,
    "tdcommons/ames": 0.8252384029450351,
    "tdcommons/ld50-zhu": 0.6502356497773621
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.288272 |
|  1 | test       | CLS_RET        | f1          | 0.347826 |
|  2 | test       | CLS_RET        | roc_auc     | 0.843358 |
|  3 | test       | CLS_RET        | accuracy    | 0.858491 |
|  4 | test       | CLS_RET        | mcc         | 0.337956 |
|  5 | test       | CLS_RET        | pr_auc      | 0.647609 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.558475 |
|  1 | test       | RET            | r2                  |   0.1688   |
|  2 | test       | RET            | mean_squared_error  | 986.972    |
|  3 | test       | RET            | mean_absolute_error |  23.9517   |
|  4 | test       | RET            | pearsonr            |   0.543209 |
|  5 | test       | RET            | explained_var       |   0.262144 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.12311  |
|  1 | test       | CLS_KIT        | f1          | 0.263158 |
|  2 | test       | CLS_KIT        | roc_auc     | 0.743714 |
|  3 | test       | CLS_KIT        | accuracy    | 0.758621 |
|  4 | test       | CLS_KIT        | mcc         | 0.125343 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.443002 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | spearmanr           |    0.441186 |
|  1 | test       | KIT            | r2                  |    0.126232 |
|  2 | test       | KIT            | mean_squared_error  | 1054.36     |
|  3 | test       | KIT            | mean_absolute_error |   25.4355   |
|  4 | test       | KIT            | pearsonr            |    0.454487 |
|  5 | test       | KIT            | explained_var       |    0.147185 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.291249 |
|  1 | test       | EGFR           | r2                  |   0.235819 |
|  2 | test       | EGFR           | mean_squared_error  | 615.753    |
|  3 | test       | EGFR           | mean_absolute_error |  19.7576   |
|  4 | test       | EGFR           | pearsonr            |   0.564754 |
|  5 | test       | EGFR           | explained_var       |   0.245346 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.462209 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.27692  |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.392039 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.440303 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.544041 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.276939 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.858261 |
|  1 | test       | LOG_RPPB       | r2                  | 0.581096 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.372188 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.455901 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.763845 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.581099 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.819772 |
|  1 | test       | LOG_HPPB       | r2                  | 0.58894  |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.248954 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.449422 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.790621 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.625068 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.722478 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.519694 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.23794  |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.370595 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.722984 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.519891 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.689533 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.455261 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.307529 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.43328  |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.68317  |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.455278 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.645115 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.371833 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.243986 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.389064 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.634585 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.373737 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.538226 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  8.9236 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.242568 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.678997 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.252649 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.373601 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.557608 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.846957 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.612571 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.129708 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.581374 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.91089 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.313749 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.826068 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.927416 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.836071 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.666828 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6476094203091332,
    "polaris/pkis2-ret-wt-reg-v2": 986.9716979726006,
    "polaris/pkis2-kit-wt-cls-v2": 0.44300175942139053,
    "polaris/pkis2-kit-wt-reg-v2": 1054.3615002469435,
    "polaris/pkis2-egfr-wt-reg-v2": 615.7532205868615,
    "polaris/adme-fang-solu-1": 0.5440414920033536,
    "polaris/adme-fang-rppb-1": 0.7638451744261556,
    "polaris/adme-fang-hppb-1": 0.7906211418309839,
    "polaris/adme-fang-perm-1": 0.7229835690575251,
    "polaris/adme-fang-rclint-1": 0.6831699654927046,
    "polaris/adme-fang-hclint-1": 0.6345851747277493,
    "tdcommons/lipophilicity-astrazeneca": 0.5382256717227754,
    "tdcommons/ppbr-az": 8.923601403961454,
    "tdcommons/clearance-hepatocyte-az": 0.24256774805178352,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6789972155357473,
    "tdcommons/half-life-obach": 0.25264912892002467,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.37360094937444177,
    "tdcommons/clearance-microsome-az": 0.557607804756423,
    "tdcommons/dili": 0.8469565217391305,
    "tdcommons/bioavailability-ma": 0.6125706684403058,
    "tdcommons/vdss-lombardo": 0.1297080878756876,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5813743218806511,
    "tdcommons/pgp-broccatelli": 0.9108904292188751,
    "tdcommons/caco2-wang": 0.31374891991146225,
    "tdcommons/herg": 0.8260677466863035,
    "tdcommons/bbb-martins": 0.9274155722326455,
    "tdcommons/ames": 0.8360708061642093,
    "tdcommons/ld50-zhu": 0.6668277686174571
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.509609 |
|  1 | test       | CLS_RET        | f1          | 0.580645 |
|  2 | test       | CLS_RET        | roc_auc     | 0.837409 |
|  3 | test       | CLS_RET        | accuracy    | 0.877358 |
|  4 | test       | CLS_RET        | mcc         | 0.512903 |
|  5 | test       | CLS_RET        | pr_auc      | 0.604567 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.4969   |
|  1 | test       | RET            | r2                  |   0.241483 |
|  2 | test       | RET            | mean_squared_error  | 900.667    |
|  3 | test       | RET            | mean_absolute_error |  22.9613   |
|  4 | test       | RET            | pearsonr            |   0.529059 |
|  5 | test       | RET            | explained_var       |   0.267125 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.216216 |
|  1 | test       | CLS_KIT        | f1          | 0.35     |
|  2 | test       | CLS_KIT        | roc_auc     | 0.762089 |
|  3 | test       | CLS_KIT        | accuracy    | 0.775862 |
|  4 | test       | CLS_KIT        | mcc         | 0.217805 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.420924 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | spearmanr           |    0.447578 |
|  1 | test       | KIT            | r2                  |    0.123644 |
|  2 | test       | KIT            | mean_squared_error  | 1057.48     |
|  3 | test       | KIT            | mean_absolute_error |   25.183    |
|  4 | test       | KIT            | pearsonr            |    0.476491 |
|  5 | test       | KIT            | explained_var       |    0.150924 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.282645 |
|  1 | test       | EGFR           | r2                  |   0.203417 |
|  2 | test       | EGFR           | mean_squared_error  | 641.861    |
|  3 | test       | EGFR           | mean_absolute_error |  19.7692   |
|  4 | test       | EGFR           | pearsonr            |   0.500374 |
|  5 | test       | EGFR           | explained_var       |   0.203445 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.398688 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.247383 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.408053 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.452925 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.516357 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.249711 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.86087  |
|  1 | test       | LOG_RPPB       | r2                  | 0.576356 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.3764   |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.496119 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.762203 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.580824 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.815036 |
|  1 | test       | LOG_HPPB       | r2                  | 0.632767 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.22241  |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.379086 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.821764 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.643093 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.74949  |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.555347 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.220278 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.358481 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.751095 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.555358 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.677074 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.434183 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.319428 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.448587 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.669015 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.437969 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.657906 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.378681 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.241326 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.38883  |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.64395  |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.381599 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.555013 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  8.7343 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.324915 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.633689 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr |  0.2468 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.347039 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.512182 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.856522 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.635517 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.378927 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.613472 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.878232 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.321817 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.836377 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.926829 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.847702 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.651885 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6045667616895714,
    "polaris/pkis2-ret-wt-reg-v2": 900.6672773096184,
    "polaris/pkis2-kit-wt-cls-v2": 0.42092378960399374,
    "polaris/pkis2-kit-wt-reg-v2": 1057.4842220880626,
    "polaris/pkis2-egfr-wt-reg-v2": 641.8611113719277,
    "polaris/adme-fang-solu-1": 0.5163574910276286,
    "polaris/adme-fang-rppb-1": 0.7622029320593778,
    "polaris/adme-fang-hppb-1": 0.8217639837813872,
    "polaris/adme-fang-perm-1": 0.7510951921188256,
    "polaris/adme-fang-rclint-1": 0.6690151810525026,
    "polaris/adme-fang-hclint-1": 0.6439500487851932,
    "tdcommons/lipophilicity-astrazeneca": 0.5550132062605448,
    "tdcommons/ppbr-az": 8.734298377403848,
    "tdcommons/clearance-hepatocyte-az": 0.32491532493144437,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6336886247340754,
    "tdcommons/half-life-obach": 0.24680025567016375,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3470386360820772,
    "tdcommons/clearance-microsome-az": 0.5121823990977086,
    "tdcommons/dili": 0.8565217391304347,
    "tdcommons/bioavailability-ma": 0.6355171267043566,
    "tdcommons/vdss-lombardo": 0.3789268633490591,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6134719710669078,
    "tdcommons/pgp-broccatelli": 0.8782324713409757,
    "tdcommons/caco2-wang": 0.32181704780472986,
    "tdcommons/herg": 0.8363770250368189,
    "tdcommons/bbb-martins": 0.9268292682926829,
    "tdcommons/ames": 0.8477021284928234,
    "tdcommons/ld50-zhu": 0.6518846817687658
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.591365 |
|  1 | test       | CLS_RET        | f1          | 0.642857 |
|  2 | test       | CLS_RET        | roc_auc     | 0.865829 |
|  3 | test       | CLS_RET        | accuracy    | 0.90566  |
|  4 | test       | CLS_RET        | mcc         | 0.609983 |
|  5 | test       | CLS_RET        | pr_auc      | 0.713174 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.570969 |
|  1 | test       | RET            | r2                  |   0.184053 |
|  2 | test       | RET            | mean_squared_error  | 968.86     |
|  3 | test       | RET            | mean_absolute_error |  23.1075   |
|  4 | test       | RET            | pearsonr            |   0.532793 |
|  5 | test       | RET            | explained_var       |   0.277345 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.132775 |
|  1 | test       | CLS_KIT        | f1          | 0.242424 |
|  2 | test       | CLS_KIT        | roc_auc     | 0.750967 |
|  3 | test       | CLS_KIT        | accuracy    | 0.784483 |
|  4 | test       | CLS_KIT        | mcc         | 0.143644 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.389203 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | spearmanr           |    0.355493  |
|  1 | test       | KIT            | r2                  |    0.019817  |
|  2 | test       | KIT            | mean_squared_error  | 1182.77      |
|  3 | test       | KIT            | mean_absolute_error |   27.116     |
|  4 | test       | KIT            | pearsonr            |    0.361756  |
|  5 | test       | KIT            | explained_var       |    0.0343883 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.241458 |
|  1 | test       | EGFR           | r2                  |   0.263278 |
|  2 | test       | EGFR           | mean_squared_error  | 593.627    |
|  3 | test       | EGFR           | mean_absolute_error |  19.5047   |
|  4 | test       | EGFR           | pearsonr            |   0.521307 |
|  5 | test       | EGFR           | explained_var       |   0.268098 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.472286 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.27982  |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.390466 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.442758 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.53958  |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.286715 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.903478 |
|  1 | test       | LOG_RPPB       | r2                  | 0.682723 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.281895 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.414353 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.850239 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.690821 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.668653 |
|  1 | test       | LOG_HPPB       | r2                  | 0.448308 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.334126 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.454904 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.740148 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.547761 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.715583 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.525184 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.23522  |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.379592 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.728239 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.526098 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.674467 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.430671 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.321411 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.444724 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.672648 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.434009 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.670391 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.414984 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.227226 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.381171 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.649499 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.416283 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.551014 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.20717 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.326345 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.626934 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.281807 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.388366 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.527299 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.822174 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.661124 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.376715 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.61415 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.912823 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.443976 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.824595 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.917292 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.828229 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.632582 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.713173864644453,
    "polaris/pkis2-ret-wt-reg-v2": 968.8596302290076,
    "polaris/pkis2-kit-wt-cls-v2": 0.38920290388981943,
    "polaris/pkis2-kit-wt-reg-v2": 1182.771207887748,
    "polaris/pkis2-egfr-wt-reg-v2": 593.6274537075941,
    "polaris/adme-fang-solu-1": 0.5395799076088247,
    "polaris/adme-fang-rppb-1": 0.8502388381846764,
    "polaris/adme-fang-hppb-1": 0.7401482860538211,
    "polaris/adme-fang-perm-1": 0.7282391049942644,
    "polaris/adme-fang-rclint-1": 0.672647993460319,
    "polaris/adme-fang-hclint-1": 0.649499202641301,
    "tdcommons/lipophilicity-astrazeneca": 0.551013578522773,
    "tdcommons/ppbr-az": 9.20716883814612,
    "tdcommons/clearance-hepatocyte-az": 0.3263445321526043,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.626934190803303,
    "tdcommons/half-life-obach": 0.2818065647965801,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.38836561093433386,
    "tdcommons/clearance-microsome-az": 0.5272986360912562,
    "tdcommons/dili": 0.8221739130434783,
    "tdcommons/bioavailability-ma": 0.6611240438975724,
    "tdcommons/vdss-lombardo": 0.37671450918824745,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6141500904159133,
    "tdcommons/pgp-broccatelli": 0.9128232471340977,
    "tdcommons/caco2-wang": 0.44397603690346527,
    "tdcommons/herg": 0.8245949926362297,
    "tdcommons/bbb-martins": 0.91729205753596,
    "tdcommons/ames": 0.8282294542677555,
    "tdcommons/ld50-zhu": 0.6325819011270113
}
```
