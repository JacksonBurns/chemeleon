# ChemProp Baseline Results
timestamp: 2025-07-08 19:27:49.916526
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0        |
|  1 | test       | CLS_RET        | accuracy    | 0.839623 |
|  2 | test       | CLS_RET        | roc_auc     | 0.846001 |
|  3 | test       | CLS_RET        | mcc         | 0        |
|  4 | test       | CLS_RET        | pr_auc      | 0.583458 |
|  5 | test       | CLS_RET        | cohen_kappa | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 712.248    |
|  1 | test       | RET            | mean_absolute_error |  19.4937   |
|  2 | test       | RET            | spearmanr           |   0.63351  |
|  3 | test       | RET            | pearsonr            |   0.69023  |
|  4 | test       | RET            | explained_var       |   0.47071  |
|  5 | test       | RET            | r2                  |   0.400164 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.651163 |
|  1 | test       | CLS_KIT        | accuracy    | 0.87069  |
|  2 | test       | CLS_KIT        | roc_auc     | 0.831238 |
|  3 | test       | CLS_KIT        | mcc         | 0.572083 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.702527 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.57185  |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_squared_error  | 755.96     |
|  1 | test       | KIT            | mean_absolute_error |  20.917    |
|  2 | test       | KIT            | spearmanr           |   0.559809 |
|  3 | test       | KIT            | pearsonr            |   0.629337 |
|  4 | test       | KIT            | explained_var       |   0.382066 |
|  5 | test       | KIT            | r2                  |   0.373523 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 441.163    |
|  1 | test       | EGFR           | mean_absolute_error |  16.1534   |
|  2 | test       | EGFR           | spearmanr           |   0.384235 |
|  3 | test       | EGFR           | pearsonr            |   0.676033 |
|  4 | test       | EGFR           | explained_var       |   0.453874 |
|  5 | test       | EGFR           | r2                  |   0.452495 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.317604 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.372927 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.563221 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.646625 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.418123 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.414208 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.437737 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.507709 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.786087 |
|  3 | test       | LOG_RPPB       | pearsonr            | 0.735996 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.508256 |
|  5 | test       | LOG_RPPB       | r2                  | 0.50732  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.243678 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.411198 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.764    |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.786216 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.60482  |
|  5 | test       | LOG_HPPB       | r2                  | 0.597651 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.178426 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.304227 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.798317 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.800108 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.640168 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.639829 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.253145 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.398811 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.753647 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.745135 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.555204 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.551593 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.191249 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.339441 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.717487 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.716149 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.508719 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.50761  |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.463359 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.41873 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.367918 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.700659 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.356007 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.429551 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.590641 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.906957 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.60725 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.486851 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.607821 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.934751 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.346683 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.879087 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.890205 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.851109 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.518538 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5834577436138595,
    "polaris/pkis2-ret-wt-reg-v2": 712.2481819743998,
    "polaris/pkis2-kit-wt-cls-v2": 0.7025273317162799,
    "polaris/pkis2-kit-wt-reg-v2": 755.959866552676,
    "polaris/pkis2-egfr-wt-reg-v2": 441.16265190280114,
    "polaris/adme-fang-solu-1": 0.6466246887523937,
    "polaris/adme-fang-rppb-1": 0.7359961248751199,
    "polaris/adme-fang-hppb-1": 0.7862155859908148,
    "polaris/adme-fang-perm-1": 0.8001082473010575,
    "polaris/adme-fang-rclint-1": 0.7451353512135628,
    "polaris/adme-fang-hclint-1": 0.7161487752294597,
    "tdcommons/lipophilicity-astrazeneca": 0.46335897564888,
    "tdcommons/ppbr-az": 8.418730325715913,
    "tdcommons/clearance-hepatocyte-az": 0.36791770407668656,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7006589048642645,
    "tdcommons/half-life-obach": 0.3560068657157322,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.42955113429482794,
    "tdcommons/clearance-microsome-az": 0.5906410547649475,
    "tdcommons/dili": 0.9069565217391304,
    "tdcommons/bioavailability-ma": 0.6072497505819754,
    "tdcommons/vdss-lombardo": 0.486850708389396,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6078209764918625,
    "tdcommons/pgp-broccatelli": 0.9347507331378299,
    "tdcommons/caco2-wang": 0.3466834571267936,
    "tdcommons/herg": 0.8790868924889544,
    "tdcommons/bbb-martins": 0.8902048155096934,
    "tdcommons/ames": 0.8511092835183771,
    "tdcommons/ld50-zhu": 0.5185375196401418
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0        |
|  1 | test       | CLS_RET        | accuracy    | 0.839623 |
|  2 | test       | CLS_RET        | roc_auc     | 0.81692  |
|  3 | test       | CLS_RET        | mcc         | 0        |
|  4 | test       | CLS_RET        | pr_auc      | 0.467364 |
|  5 | test       | CLS_RET        | cohen_kappa | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 631.94     |
|  1 | test       | RET            | mean_absolute_error |  18.5722   |
|  2 | test       | RET            | spearmanr           |   0.664381 |
|  3 | test       | RET            | pearsonr            |   0.719313 |
|  4 | test       | RET            | explained_var       |   0.509345 |
|  5 | test       | RET            | r2                  |   0.467797 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.619048 |
|  1 | test       | CLS_KIT        | accuracy    | 0.862069 |
|  2 | test       | CLS_KIT        | roc_auc     | 0.870406 |
|  3 | test       | CLS_KIT        | mcc         | 0.535976 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.713209 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.53507  |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_squared_error  | 866.669    |
|  1 | test       | KIT            | mean_absolute_error |  21.6608   |
|  2 | test       | KIT            | spearmanr           |   0.564872 |
|  3 | test       | KIT            | pearsonr            |   0.59258  |
|  4 | test       | KIT            | explained_var       |   0.300232 |
|  5 | test       | KIT            | r2                  |   0.281777 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 448.919    |
|  1 | test       | EGFR           | mean_absolute_error |  16.4807   |
|  2 | test       | EGFR           | spearmanr           |   0.355894 |
|  3 | test       | EGFR           | pearsonr            |   0.666365 |
|  4 | test       | EGFR           | explained_var       |   0.442868 |
|  5 | test       | EGFR           | r2                  |   0.442868 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.298895 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.362332 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.573845 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.671681 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.451155 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.448716 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.505484 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.560179 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.762609 |
|  3 | test       | LOG_RPPB       | pearsonr            | 0.702794 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.43419  |
|  5 | test       | LOG_RPPB       | r2                  | 0.43107  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.250851 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.433425 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.768584 |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.785145 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.590353 |
|  5 | test       | LOG_HPPB       | r2                  | 0.585808 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.167216 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.291516 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.811103 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.814028 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.662498 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.662458 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.260059 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.410062 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.737031 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.737468 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.54371  |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.539346 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.193608 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.34975  |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.717063 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.71486  |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.503134 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.501536 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.446466 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  7.5273 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.348746 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.699305 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.355095 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.427069 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.602604 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.913043 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.568008 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.524809 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.627712 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.938683 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.275044 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.83461 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.903221 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.842625 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.541008 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.4673641106213646,
    "polaris/pkis2-ret-wt-reg-v2": 631.9401287154933,
    "polaris/pkis2-kit-wt-cls-v2": 0.7132093564460336,
    "polaris/pkis2-kit-wt-reg-v2": 866.6686588764775,
    "polaris/pkis2-egfr-wt-reg-v2": 448.9190402098691,
    "polaris/adme-fang-solu-1": 0.6716808099315366,
    "polaris/adme-fang-rppb-1": 0.7027942316324713,
    "polaris/adme-fang-hppb-1": 0.7851450814774055,
    "polaris/adme-fang-perm-1": 0.8140284221942755,
    "polaris/adme-fang-rclint-1": 0.7374680752408025,
    "polaris/adme-fang-hclint-1": 0.7148597043281067,
    "tdcommons/lipophilicity-astrazeneca": 0.4464659704934983,
    "tdcommons/ppbr-az": 7.527298697265188,
    "tdcommons/clearance-hepatocyte-az": 0.34874632136643313,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6993052276666517,
    "tdcommons/half-life-obach": 0.3550946561263043,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4270694655447076,
    "tdcommons/clearance-microsome-az": 0.6026037202179366,
    "tdcommons/dili": 0.9130434782608696,
    "tdcommons/bioavailability-ma": 0.5680079813767874,
    "tdcommons/vdss-lombardo": 0.5248089856247106,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6277124773960217,
    "tdcommons/pgp-broccatelli": 0.9386830178619036,
    "tdcommons/caco2-wang": 0.2750440989904384,
    "tdcommons/herg": 0.8346097201767304,
    "tdcommons/bbb-martins": 0.9032207629768605,
    "tdcommons/ames": 0.8426246842507197,
    "tdcommons/ld50-zhu": 0.5410080564631823
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0        |
|  1 | test       | CLS_RET        | accuracy    | 0.839623 |
|  2 | test       | CLS_RET        | roc_auc     | 0.870456 |
|  3 | test       | CLS_RET        | mcc         | 0        |
|  4 | test       | CLS_RET        | pr_auc      | 0.635269 |
|  5 | test       | CLS_RET        | cohen_kappa | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 620.788    |
|  1 | test       | RET            | mean_absolute_error |  19.2791   |
|  2 | test       | RET            | spearmanr           |   0.663986 |
|  3 | test       | RET            | pearsonr            |   0.697909 |
|  4 | test       | RET            | explained_var       |   0.481415 |
|  5 | test       | RET            | r2                  |   0.477189 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.590909 |
|  1 | test       | CLS_KIT        | accuracy    | 0.844828 |
|  2 | test       | CLS_KIT        | roc_auc     | 0.840909 |
|  3 | test       | CLS_KIT        | mcc         | 0.495164 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.65524  |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.495164 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_squared_error  | 769.478    |
|  1 | test       | KIT            | mean_absolute_error |  21.7661   |
|  2 | test       | KIT            | spearmanr           |   0.565257 |
|  3 | test       | KIT            | pearsonr            |   0.613981 |
|  4 | test       | KIT            | explained_var       |   0.362482 |
|  5 | test       | KIT            | r2                  |   0.36232  |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 441.568    |
|  1 | test       | EGFR           | mean_absolute_error |  16.0998   |
|  2 | test       | EGFR           | spearmanr           |   0.430292 |
|  3 | test       | EGFR           | pearsonr            |   0.685314 |
|  4 | test       | EGFR           | explained_var       |   0.465446 |
|  5 | test       | EGFR           | r2                  |   0.451992 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.326264 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.380468 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.562075 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.638276 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.407054 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.398236 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.339171 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.445722 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.8      |
|  3 | test       | LOG_RPPB       | pearsonr            | 0.821974 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.619354 |
|  5 | test       | LOG_RPPB       | r2                  | 0.618258 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.397769 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.576467 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.722744 |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.704203 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.441559 |
|  5 | test       | LOG_HPPB       | r2                  | 0.343224 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.170998 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.299915 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.806913 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.809335 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.654865 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.654822 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.245137 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.390838 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.753986 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.752833 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.566271 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.565778 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.194647 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.344046 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.721638 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.715176 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.502224 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.498862 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.449229 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.12541 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.395346 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.70778 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.247017 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.463714 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.574992 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.917391 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.577985 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.556352 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.62726 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.931618 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.378796 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.854639 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.900328 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.859769 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.522133 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6352687828048509,
    "polaris/pkis2-ret-wt-reg-v2": 620.7884400393269,
    "polaris/pkis2-kit-wt-cls-v2": 0.6552404530976548,
    "polaris/pkis2-kit-wt-reg-v2": 769.4779442817862,
    "polaris/pkis2-egfr-wt-reg-v2": 441.5675342932106,
    "polaris/adme-fang-solu-1": 0.6382759965053513,
    "polaris/adme-fang-rppb-1": 0.821974229750903,
    "polaris/adme-fang-hppb-1": 0.7042034371531388,
    "polaris/adme-fang-perm-1": 0.8093350778965687,
    "polaris/adme-fang-rclint-1": 0.7528333210786511,
    "polaris/adme-fang-hclint-1": 0.7151760878458506,
    "tdcommons/lipophilicity-astrazeneca": 0.44922936537152247,
    "tdcommons/ppbr-az": 8.125407402570856,
    "tdcommons/clearance-hepatocyte-az": 0.3953462523058095,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7077800636714491,
    "tdcommons/half-life-obach": 0.2470173322836907,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4637138762707645,
    "tdcommons/clearance-microsome-az": 0.5749924998947105,
    "tdcommons/dili": 0.9173913043478261,
    "tdcommons/bioavailability-ma": 0.5779847023611573,
    "tdcommons/vdss-lombardo": 0.5563524192148013,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6272603978300181,
    "tdcommons/pgp-broccatelli": 0.9316182351372968,
    "tdcommons/caco2-wang": 0.3787955541299339,
    "tdcommons/herg": 0.854639175257732,
    "tdcommons/bbb-martins": 0.9003283302063789,
    "tdcommons/ames": 0.8597691358749927,
    "tdcommons/ld50-zhu": 0.5221333696864778
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0        |
|  1 | test       | CLS_RET        | accuracy    | 0.839623 |
|  2 | test       | CLS_RET        | roc_auc     | 0.802379 |
|  3 | test       | CLS_RET        | mcc         | 0        |
|  4 | test       | CLS_RET        | pr_auc      | 0.53337  |
|  5 | test       | CLS_RET        | cohen_kappa | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 683.405    |
|  1 | test       | RET            | mean_absolute_error |  20.2356   |
|  2 | test       | RET            | spearmanr           |   0.566478 |
|  3 | test       | RET            | pearsonr            |   0.668684 |
|  4 | test       | RET            | explained_var       |   0.447132 |
|  5 | test       | RET            | r2                  |   0.424455 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.6      |
|  1 | test       | CLS_KIT        | accuracy    | 0.862069 |
|  2 | test       | CLS_KIT        | roc_auc     | 0.832205 |
|  3 | test       | CLS_KIT        | mcc         | 0.521477 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.709392 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.517672 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_squared_error  | 783.053    |
|  1 | test       | KIT            | mean_absolute_error |  20.6858   |
|  2 | test       | KIT            | spearmanr           |   0.60664  |
|  3 | test       | KIT            | pearsonr            |   0.633528 |
|  4 | test       | KIT            | explained_var       |   0.390552 |
|  5 | test       | KIT            | r2                  |   0.35107  |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 481.131    |
|  1 | test       | EGFR           | mean_absolute_error |  17.3356   |
|  2 | test       | EGFR           | spearmanr           |   0.305    |
|  3 | test       | EGFR           | pearsonr            |   0.63717  |
|  4 | test       | EGFR           | explained_var       |   0.405648 |
|  5 | test       | EGFR           | r2                  |   0.402891 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.326388 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.379904 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.552588 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.634039 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.398887 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.398007 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.54275  |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.599596 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.805217 |
|  3 | test       | LOG_RPPB       | pearsonr            | 0.735116 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.390473 |
|  5 | test       | LOG_RPPB       | r2                  | 0.389127 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.294914 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.471288 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.729315 |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.76059  |
|  4 | test       | LOG_HPPB       | explained_var       | 0.574362 |
|  5 | test       | LOG_HPPB       | r2                  | 0.513052 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.162592 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.295187 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.812433 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.820301 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.672578 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.671792 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.243059 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.388271 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.758702 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.75487  |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.569804 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.569459 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.190543 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.337446 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.720544 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.718662 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.512269 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.509429 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.450879 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.91069 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.345165 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.579959 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0950905 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.39242 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.582704 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.927826 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.623213 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.536851 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.608047 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.92662 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.408867 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.874816 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.887645 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.838274 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.543267 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5333701075884064,
    "polaris/pkis2-ret-wt-reg-v2": 683.4053094399807,
    "polaris/pkis2-kit-wt-cls-v2": 0.7093917446925342,
    "polaris/pkis2-kit-wt-reg-v2": 783.0529414449845,
    "polaris/pkis2-egfr-wt-reg-v2": 481.13139431660926,
    "polaris/adme-fang-solu-1": 0.6340392666870083,
    "polaris/adme-fang-rppb-1": 0.7351161726484898,
    "polaris/adme-fang-hppb-1": 0.7605896544575934,
    "polaris/adme-fang-perm-1": 0.8203010545901732,
    "polaris/adme-fang-rclint-1": 0.7548695662830245,
    "polaris/adme-fang-hclint-1": 0.7186624874212756,
    "tdcommons/lipophilicity-astrazeneca": 0.45087883795443034,
    "tdcommons/ppbr-az": 7.9106930484669356,
    "tdcommons/clearance-hepatocyte-az": 0.34516455031525933,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5799587073677613,
    "tdcommons/half-life-obach": 0.09509053250863346,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3924204731106458,
    "tdcommons/clearance-microsome-az": 0.5827040077476275,
    "tdcommons/dili": 0.9278260869565218,
    "tdcommons/bioavailability-ma": 0.623212504156967,
    "tdcommons/vdss-lombardo": 0.5368506271660768,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6080470162748645,
    "tdcommons/pgp-broccatelli": 0.9266195681151692,
    "tdcommons/caco2-wang": 0.4088670305958843,
    "tdcommons/herg": 0.8748159057437408,
    "tdcommons/bbb-martins": 0.8876446216385241,
    "tdcommons/ames": 0.838273708120386,
    "tdcommons/ld50-zhu": 0.5432673355723266
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0        |
|  1 | test       | CLS_RET        | accuracy    | 0.839623 |
|  2 | test       | CLS_RET        | roc_auc     | 0.832783 |
|  3 | test       | CLS_RET        | mcc         | 0        |
|  4 | test       | CLS_RET        | pr_auc      | 0.609745 |
|  5 | test       | CLS_RET        | cohen_kappa | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 672.625    |
|  1 | test       | RET            | mean_absolute_error |  19.2047   |
|  2 | test       | RET            | spearmanr           |   0.620272 |
|  3 | test       | RET            | pearsonr            |   0.696103 |
|  4 | test       | RET            | explained_var       |   0.482051 |
|  5 | test       | RET            | r2                  |   0.433533 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.682927 |
|  1 | test       | CLS_KIT        | accuracy    | 0.887931 |
|  2 | test       | CLS_KIT        | roc_auc     | 0.885397 |
|  3 | test       | CLS_KIT        | mcc         | 0.617745 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.744158 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.615306 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_squared_error  | 927.252    |
|  1 | test       | KIT            | mean_absolute_error |  22.8331   |
|  2 | test       | KIT            | spearmanr           |   0.468232 |
|  3 | test       | KIT            | pearsonr            |   0.541696 |
|  4 | test       | KIT            | explained_var       |   0.241421 |
|  5 | test       | KIT            | r2                  |   0.23157  |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 479.886    |
|  1 | test       | EGFR           | mean_absolute_error |  16.6415   |
|  2 | test       | EGFR           | spearmanr           |   0.396222 |
|  3 | test       | EGFR           | pearsonr            |   0.654623 |
|  4 | test       | EGFR           | explained_var       |   0.424383 |
|  5 | test       | EGFR           | r2                  |   0.404437 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.310837 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.360291 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.569427 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.680402 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.456856 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.426689 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.323384 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.452134 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.843478 |
|  3 | test       | LOG_RPPB       | pearsonr            | 0.851843 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.639494 |
|  5 | test       | LOG_RPPB       | r2                  | 0.636026 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.293324 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.4783   |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.741691 |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.752856 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.541837 |
|  5 | test       | LOG_HPPB       | r2                  | 0.515677 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.17671  |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.304847 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.800181 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.802342 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.643434 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.643294 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.24092  |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.388535 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.763936 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.758842 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.575823 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.573248 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.190273 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.335917 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.726792 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.724226 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.520551 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.510122 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.439375 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.51473 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.344362 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.665051 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.327002 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.414102 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.592574 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.93913 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.612903 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.572783 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.636076 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.930152 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.376048 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.856406 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.915299 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.855106 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.53959 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6097445793609381,
    "polaris/pkis2-ret-wt-reg-v2": 672.6252560282944,
    "polaris/pkis2-kit-wt-cls-v2": 0.7441577870619223,
    "polaris/pkis2-kit-wt-reg-v2": 927.252012566312,
    "polaris/pkis2-egfr-wt-reg-v2": 479.8861463828697,
    "polaris/adme-fang-solu-1": 0.6804024672089137,
    "polaris/adme-fang-rppb-1": 0.851842844403386,
    "polaris/adme-fang-hppb-1": 0.7528559449898607,
    "polaris/adme-fang-perm-1": 0.8023424147408593,
    "polaris/adme-fang-rclint-1": 0.7588419390285611,
    "polaris/adme-fang-hclint-1": 0.7242256716127562,
    "tdcommons/lipophilicity-astrazeneca": 0.43937542982328504,
    "tdcommons/ppbr-az": 8.514730446803549,
    "tdcommons/clearance-hepatocyte-az": 0.3443620110626752,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6650505326292938,
    "tdcommons/half-life-obach": 0.327002348433972,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.414102449354936,
    "tdcommons/clearance-microsome-az": 0.5925743287610782,
    "tdcommons/dili": 0.9391304347826087,
    "tdcommons/bioavailability-ma": 0.6129032258064516,
    "tdcommons/vdss-lombardo": 0.572782838930454,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6360759493670887,
    "tdcommons/pgp-broccatelli": 0.9301519594774728,
    "tdcommons/caco2-wang": 0.37604775831449744,
    "tdcommons/herg": 0.8564064801178204,
    "tdcommons/bbb-martins": 0.9152986241400876,
    "tdcommons/ames": 0.85510583720065,
    "tdcommons/ld50-zhu": 0.539589997048307
}
```
