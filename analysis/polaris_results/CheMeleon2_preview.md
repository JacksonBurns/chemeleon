# chemeleon2_preview_initial_training_e4s281344 Baseline Results
timestamp: 2026-06-30 16:16:12.868147
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.820225 |
|  1 | test       | CLS_RET        | pr_auc      | 0.667847 |
|  2 | test       | CLS_RET        | f1          | 0.56     |
|  3 | test       | CLS_RET        | mcc         | 0.55641  |
|  4 | test       | CLS_RET        | accuracy    | 0.896226 |
|  5 | test       | CLS_RET        | cohen_kappa | 0.509672 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.579558 |
|  1 | test       | RET            | mean_absolute_error |  22.0196   |
|  2 | test       | RET            | spearmanr           |   0.570235 |
|  3 | test       | RET            | r2                  |   0.298764 |
|  4 | test       | RET            | mean_squared_error  | 832.652    |
|  5 | test       | RET            | explained_var       |   0.326876 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.809478 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.631836 |
|  2 | test       | CLS_KIT        | f1          | 0.512821 |
|  3 | test       | CLS_KIT        | mcc         | 0.421313 |
|  4 | test       | CLS_KIT        | accuracy    | 0.836207 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.416314 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.498848 |
|  1 | test       | KIT            | mean_absolute_error |  24.844    |
|  2 | test       | KIT            | spearmanr           |   0.443922 |
|  3 | test       | KIT            | r2                  |   0.185204 |
|  4 | test       | KIT            | mean_squared_error  | 983.201    |
|  5 | test       | KIT            | explained_var       |   0.190883 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.576818 |
|  1 | test       | EGFR           | mean_absolute_error |  18.7995   |
|  2 | test       | EGFR           | spearmanr           |   0.36976  |
|  3 | test       | EGFR           | r2                  |   0.29757  |
|  4 | test       | EGFR           | mean_squared_error  | 565.996    |
|  5 | test       | EGFR           | explained_var       |   0.2979   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.604041 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.42798  |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.467113 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.352004 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.351329 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.352199 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.655312 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.59157  |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.713913 |
|  3 | test       | LOG_RPPB       | r2                  | 0.36643  |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.562916 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.420466 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.733479 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.419931 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.682252 |
|  3 | test       | LOG_HPPB       | r2                  | 0.519748 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.290859 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.528782 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.777067 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.339763 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.757453 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.602011 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.197161 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.602879 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.705588 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.421042 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.706025 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.481474 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.29273  |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.487473 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.698169 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.365437 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.714854 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.447208 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.21471  |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.449023 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.534109 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.56839 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.409969 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.673177 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.27565 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.359368 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.613725 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.879565 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.72298 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.382962 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.644892 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.901426 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.297694 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.862445 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.89298 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.849449 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.610485 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.667847210150029,
    "polaris/pkis2-ret-wt-reg-v2": 832.6517280994207,
    "polaris/pkis2-kit-wt-cls-v2": 0.6318359085857409,
    "polaris/pkis2-kit-wt-reg-v2": 983.200863035486,
    "polaris/pkis2-egfr-wt-reg-v2": 565.9959732755873,
    "polaris/adme-fang-solu-1": 0.604041310248854,
    "polaris/adme-fang-rppb-1": 0.6553122808975679,
    "polaris/adme-fang-hppb-1": 0.7334787415122612,
    "polaris/adme-fang-perm-1": 0.7770670312062622,
    "polaris/adme-fang-rclint-1": 0.7055883439827008,
    "polaris/adme-fang-hclint-1": 0.6981690003941614,
    "tdcommons/lipophilicity-astrazeneca": 0.5341092945337296,
    "tdcommons/ppbr-az": 8.568390916745862,
    "tdcommons/clearance-hepatocyte-az": 0.4099690048754656,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6731771499547253,
    "tdcommons/half-life-obach": 0.2756503771063061,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3593682933436939,
    "tdcommons/clearance-microsome-az": 0.613725016647044,
    "tdcommons/dili": 0.8795652173913043,
    "tdcommons/bioavailability-ma": 0.7229797140006651,
    "tdcommons/vdss-lombardo": 0.3829617469861078,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6448915009041591,
    "tdcommons/pgp-broccatelli": 0.9014262863236471,
    "tdcommons/caco2-wang": 0.2976940350855902,
    "tdcommons/herg": 0.8624447717231223,
    "tdcommons/bbb-martins": 0.8929799874921825,
    "tdcommons/ames": 0.8494487849771877,
    "tdcommons/ld50-zhu": 0.610484962769871
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.821547 |
|  1 | test       | CLS_RET        | pr_auc      | 0.708587 |
|  2 | test       | CLS_RET        | f1          | 0.615385 |
|  3 | test       | CLS_RET        | mcc         | 0.604725 |
|  4 | test       | CLS_RET        | accuracy    | 0.90566  |
|  5 | test       | CLS_RET        | cohen_kappa | 0.567347 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.616528 |
|  1 | test       | RET            | mean_absolute_error |  21.2423   |
|  2 | test       | RET            | spearmanr           |   0.611301 |
|  3 | test       | RET            | r2                  |   0.350642 |
|  4 | test       | RET            | mean_squared_error  | 771.051    |
|  5 | test       | RET            | explained_var       |   0.379992 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.772727 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.544279 |
|  2 | test       | CLS_KIT        | f1          | 0.444444 |
|  3 | test       | CLS_KIT        | mcc         | 0.360788 |
|  4 | test       | CLS_KIT        | accuracy    | 0.827586 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.348315 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | pearsonr            |    0.523466 |
|  1 | test       | KIT            | mean_absolute_error |   24.1199   |
|  2 | test       | KIT            | spearmanr           |    0.445334 |
|  3 | test       | KIT            | r2                  |    0.167257 |
|  4 | test       | KIT            | mean_squared_error  | 1004.86     |
|  5 | test       | KIT            | explained_var       |    0.177512 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.639129 |
|  1 | test       | EGFR           | mean_absolute_error |  17.4984   |
|  2 | test       | EGFR           | spearmanr           |   0.37343  |
|  3 | test       | EGFR           | r2                  |   0.379347 |
|  4 | test       | EGFR           | mean_squared_error  | 500.102    |
|  5 | test       | EGFR           | explained_var       |   0.393997 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.588249 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.427266 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.475481 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.330845 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.362801 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.334073 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.738234 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.479869 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.662609 |
|  3 | test       | LOG_RPPB       | r2                  | 0.513878 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.431911 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.544168 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.753636 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.443231 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.75743  |
|  3 | test       | LOG_HPPB       | r2                  | 0.559864 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.266564 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.566764 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.781568 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.338641 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.779554 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.607548 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.194418 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.609864 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.714076 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.41596  |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.722217 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.506485 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.27861  |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.506486 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.680029 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.377785 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.686774 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.414027 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.227598 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.414262 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.526324 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  8.5458 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.404958 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.689213 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr |  0.3298 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.351876 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.587094 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.863043 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.557366 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.356203 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.661166 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.902959 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.296505 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.797349 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.905019 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.845272 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.618956 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7085871317769816,
    "polaris/pkis2-ret-wt-reg-v2": 771.0514499072914,
    "polaris/pkis2-kit-wt-cls-v2": 0.5442794447458406,
    "polaris/pkis2-kit-wt-reg-v2": 1004.8574000004512,
    "polaris/pkis2-egfr-wt-reg-v2": 500.1023640890141,
    "polaris/adme-fang-solu-1": 0.5882488243691155,
    "polaris/adme-fang-rppb-1": 0.7382341694474823,
    "polaris/adme-fang-hppb-1": 0.7536357733073201,
    "polaris/adme-fang-perm-1": 0.7815682904074248,
    "polaris/adme-fang-rclint-1": 0.7140755028419536,
    "polaris/adme-fang-hclint-1": 0.6800292753593902,
    "tdcommons/lipophilicity-astrazeneca": 0.5263241534516925,
    "tdcommons/ppbr-az": 8.545803266603746,
    "tdcommons/clearance-hepatocyte-az": 0.4049580513595035,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6892131252217614,
    "tdcommons/half-life-obach": 0.3297999503677059,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3518763580496368,
    "tdcommons/clearance-microsome-az": 0.5870943519856813,
    "tdcommons/dili": 0.8630434782608696,
    "tdcommons/bioavailability-ma": 0.5573661456601264,
    "tdcommons/vdss-lombardo": 0.3562028532263209,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6611663652802893,
    "tdcommons/pgp-broccatelli": 0.9029592108770994,
    "tdcommons/caco2-wang": 0.29650518994482705,
    "tdcommons/herg": 0.7973490427098675,
    "tdcommons/bbb-martins": 0.9050187617260788,
    "tdcommons/ames": 0.8452720828682763,
    "tdcommons/ld50-zhu": 0.6189556738533413
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.843358 |
|  1 | test       | CLS_RET        | pr_auc      | 0.677078 |
|  2 | test       | CLS_RET        | f1          | 0.642857 |
|  3 | test       | CLS_RET        | mcc         | 0.609983 |
|  4 | test       | CLS_RET        | accuracy    | 0.90566  |
|  5 | test       | CLS_RET        | cohen_kappa | 0.591365 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.602449 |
|  1 | test       | RET            | mean_absolute_error |  20.9919   |
|  2 | test       | RET            | spearmanr           |   0.58325  |
|  3 | test       | RET            | r2                  |   0.35187  |
|  4 | test       | RET            | mean_squared_error  | 769.593    |
|  5 | test       | RET            | explained_var       |   0.355783 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.774662 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.574499 |
|  2 | test       | CLS_KIT        | f1          | 0.473684 |
|  3 | test       | CLS_KIT        | mcc         | 0.380427 |
|  4 | test       | CLS_KIT        | accuracy    | 0.827586 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.37365  |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.499698 |
|  1 | test       | KIT            | mean_absolute_error |  24.3915   |
|  2 | test       | KIT            | spearmanr           |   0.43453  |
|  3 | test       | KIT            | r2                  |   0.215265 |
|  4 | test       | KIT            | mean_squared_error  | 946.927    |
|  5 | test       | KIT            | explained_var       |   0.218024 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.634902 |
|  1 | test       | EGFR           | mean_absolute_error |  17.9663   |
|  2 | test       | EGFR           | spearmanr           |   0.410169 |
|  3 | test       | EGFR           | r2                  |   0.366309 |
|  4 | test       | EGFR           | mean_squared_error  | 510.608    |
|  5 | test       | EGFR           | explained_var       |   0.374136 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.602624 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.417714 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.461981 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.355329 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.349527 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.357769 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.74769  |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.490932 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.722609 |
|  3 | test       | LOG_RPPB       | r2                  | 0.530384 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.417245 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.543986 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.809709 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.466463 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.805256 |
|  3 | test       | LOG_HPPB       | r2                  | 0.469814 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.321101 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.653815 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.752203 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.359127 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.751308 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.564719 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.215635 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.564767 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.68509  |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.42656  |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.688857 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.467915 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.300385 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.468154 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.697016 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.35307  |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.710634 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.473558 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.204475 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.474527 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.530802 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.28167 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.417289 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.713054 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0848232 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.368844 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.599446 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.860435 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.677087 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.381176 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.648056 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.915956 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.278433 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.822975 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.920302 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.860197 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.618218 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6770783740226042,
    "polaris/pkis2-ret-wt-reg-v2": 769.592736447799,
    "polaris/pkis2-kit-wt-cls-v2": 0.5744985394535262,
    "polaris/pkis2-kit-wt-reg-v2": 946.9271205264927,
    "polaris/pkis2-egfr-wt-reg-v2": 510.60800213845334,
    "polaris/adme-fang-solu-1": 0.6026239051615274,
    "polaris/adme-fang-rppb-1": 0.7476900631916935,
    "polaris/adme-fang-hppb-1": 0.8097094550166893,
    "polaris/adme-fang-perm-1": 0.7522030831082401,
    "polaris/adme-fang-rclint-1": 0.6850897943196042,
    "polaris/adme-fang-hclint-1": 0.6970161858802224,
    "tdcommons/lipophilicity-astrazeneca": 0.5308018328178497,
    "tdcommons/ppbr-az": 8.281666153581924,
    "tdcommons/clearance-hepatocyte-az": 0.41728905483515666,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.7130535825401799,
    "tdcommons/half-life-obach": 0.08482319306840691,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.36884426395330017,
    "tdcommons/clearance-microsome-az": 0.5994461719162928,
    "tdcommons/dili": 0.8604347826086957,
    "tdcommons/bioavailability-ma": 0.6770867974725641,
    "tdcommons/vdss-lombardo": 0.38117556808453174,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6480560578661845,
    "tdcommons/pgp-broccatelli": 0.9159557451346308,
    "tdcommons/caco2-wang": 0.27843302993616803,
    "tdcommons/herg": 0.8229749631811488,
    "tdcommons/bbb-martins": 0.920301751094434,
    "tdcommons/ames": 0.8601969883882591,
    "tdcommons/ld50-zhu": 0.6182177457512635
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.844019 |
|  1 | test       | CLS_RET        | pr_auc      | 0.719621 |
|  2 | test       | CLS_RET        | f1          | 0.538462 |
|  3 | test       | CLS_RET        | mcc         | 0.512494 |
|  4 | test       | CLS_RET        | accuracy    | 0.886792 |
|  5 | test       | CLS_RET        | cohen_kappa | 0.480816 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.606274 |
|  1 | test       | RET            | mean_absolute_error |  21.6399   |
|  2 | test       | RET            | spearmanr           |   0.593972 |
|  3 | test       | RET            | r2                  |   0.358723 |
|  4 | test       | RET            | mean_squared_error  | 761.456    |
|  5 | test       | RET            | explained_var       |   0.366391 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.785783 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.576348 |
|  2 | test       | CLS_KIT        | f1          | 0.4      |
|  3 | test       | CLS_KIT        | mcc         | 0.389019 |
|  4 | test       | CLS_KIT        | accuracy    | 0.844828 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.332481 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.517653 |
|  1 | test       | KIT            | mean_absolute_error |  23.8993   |
|  2 | test       | KIT            | spearmanr           |   0.4734   |
|  3 | test       | KIT            | r2                  |   0.23137  |
|  4 | test       | KIT            | mean_squared_error  | 927.494    |
|  5 | test       | KIT            | explained_var       |   0.240744 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.589043 |
|  1 | test       | EGFR           | mean_absolute_error |  19.1499   |
|  2 | test       | EGFR           | spearmanr           |   0.336599 |
|  3 | test       | EGFR           | r2                  |   0.277587 |
|  4 | test       | EGFR           | mean_squared_error  | 582.098    |
|  5 | test       | EGFR           | explained_var       |   0.282314 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.609699 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.403582 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.487436 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.363417 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.345142 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.371658 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.770976 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.454943 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.726087 |
|  3 | test       | LOG_RPPB       | r2                  | 0.55967  |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.391225 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.587603 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.791119 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.442752 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.754832 |
|  3 | test       | LOG_HPPB       | r2                  | 0.492017 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.307654 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.617873 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.786976 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.335882 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.778307 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.616788 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.18984  |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.617043 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.702392 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.423321 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.69996  |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.491147 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.28727  |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.491232 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.699477 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.351063 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.713383 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.45714  |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.210852 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.45837  |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.529069 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.33668 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.376553 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.692793 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.237016 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.39835 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.558794 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.903913 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.692717 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.485211 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.624774 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.904692 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.277717 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.84595 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.915494 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.855049 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.618932 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.719620665831758,
    "polaris/pkis2-ret-wt-reg-v2": 761.4556974539698,
    "polaris/pkis2-kit-wt-cls-v2": 0.5763475662205791,
    "polaris/pkis2-kit-wt-reg-v2": 927.4937088724505,
    "polaris/pkis2-egfr-wt-reg-v2": 582.0977936919434,
    "polaris/adme-fang-solu-1": 0.6096987820310753,
    "polaris/adme-fang-rppb-1": 0.7709764001419889,
    "polaris/adme-fang-hppb-1": 0.7911186590851969,
    "polaris/adme-fang-perm-1": 0.7869756465737621,
    "polaris/adme-fang-rclint-1": 0.7023923099896195,
    "polaris/adme-fang-hclint-1": 0.6994773175860143,
    "tdcommons/lipophilicity-astrazeneca": 0.5290690667856307,
    "tdcommons/ppbr-az": 8.336684369955591,
    "tdcommons/clearance-hepatocyte-az": 0.3765528465893744,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6927927460910113,
    "tdcommons/half-life-obach": 0.2370156651356483,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3983495006395527,
    "tdcommons/clearance-microsome-az": 0.5587940157772637,
    "tdcommons/dili": 0.9039130434782608,
    "tdcommons/bioavailability-ma": 0.6927169936814099,
    "tdcommons/vdss-lombardo": 0.48521061209344163,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6247739602169982,
    "tdcommons/pgp-broccatelli": 0.9046920821114369,
    "tdcommons/caco2-wang": 0.27771730015765184,
    "tdcommons/herg": 0.8459499263622975,
    "tdcommons/bbb-martins": 0.9154940587867418,
    "tdcommons/ames": 0.8550490512835576,
    "tdcommons/ld50-zhu": 0.6189322880324233
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | roc_auc     | 0.840714 |
|  1 | test       | CLS_RET        | pr_auc      | 0.710403 |
|  2 | test       | CLS_RET        | f1          | 0.62069  |
|  3 | test       | CLS_RET        | mcc         | 0.5741   |
|  4 | test       | CLS_RET        | accuracy    | 0.896226 |
|  5 | test       | CLS_RET        | cohen_kappa | 0.562641 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.553159 |
|  1 | test       | RET            | mean_absolute_error |  23.4152   |
|  2 | test       | RET            | spearmanr           |   0.548071 |
|  3 | test       | RET            | r2                  |   0.280131 |
|  4 | test       | RET            | mean_squared_error  | 854.776    |
|  5 | test       | RET            | explained_var       |   0.289693 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | roc_auc     | 0.798839 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.566748 |
|  2 | test       | CLS_KIT        | f1          | 0.444444 |
|  3 | test       | CLS_KIT        | mcc         | 0.360788 |
|  4 | test       | CLS_KIT        | accuracy    | 0.827586 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.348315 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.503699 |
|  1 | test       | KIT            | mean_absolute_error |  24.1726   |
|  2 | test       | KIT            | spearmanr           |   0.458005 |
|  3 | test       | KIT            | r2                  |   0.181143 |
|  4 | test       | KIT            | mean_squared_error  | 988.102    |
|  5 | test       | KIT            | explained_var       |   0.19153  |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.563794 |
|  1 | test       | EGFR           | mean_absolute_error |  19.7448   |
|  2 | test       | EGFR           | spearmanr           |   0.331283 |
|  3 | test       | EGFR           | r2                  |   0.281541 |
|  4 | test       | EGFR           | mean_squared_error  | 578.912    |
|  5 | test       | EGFR           | explained_var       |   0.303608 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.656652 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.39094  |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.518748 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.42081  |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.314024 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.429948 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.742103 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.523533 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.756522 |
|  3 | test       | LOG_RPPB       | r2                  | 0.513657 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.432107 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.530395 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.718757 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.528239 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.699366 |
|  3 | test       | LOG_HPPB       | r2                  | 0.362358 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.386181 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.514435 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.78631  |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.334966 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.781026 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.617108 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.189682 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.617117 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.700407 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.428924 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.704087 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.479925 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.293605 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.486405 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.697603 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.360587 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.715291 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.458678 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.210255 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.458832 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.514622 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.44886 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.458648 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.644453 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0742133 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.344863 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.603997 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  |    0.88 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.654805 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.364933 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.633816 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.934551 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.293621 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.859794 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.917722 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.849891 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.660251 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7104028736580292,
    "polaris/pkis2-ret-wt-reg-v2": 854.775993628834,
    "polaris/pkis2-kit-wt-cls-v2": 0.5667477199990966,
    "polaris/pkis2-kit-wt-reg-v2": 988.101710759602,
    "polaris/pkis2-egfr-wt-reg-v2": 578.911724275376,
    "polaris/adme-fang-solu-1": 0.656651625931481,
    "polaris/adme-fang-rppb-1": 0.742103372602504,
    "polaris/adme-fang-hppb-1": 0.7187568430680896,
    "polaris/adme-fang-perm-1": 0.7863100776006956,
    "polaris/adme-fang-rclint-1": 0.700406809620078,
    "polaris/adme-fang-hclint-1": 0.6976029561583786,
    "tdcommons/lipophilicity-astrazeneca": 0.5146216843071438,
    "tdcommons/ppbr-az": 8.448864420445533,
    "tdcommons/clearance-hepatocyte-az": 0.4586477991787389,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6444534887499815,
    "tdcommons/half-life-obach": 0.07421328163707096,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3448626351383929,
    "tdcommons/clearance-microsome-az": 0.6039967228152073,
    "tdcommons/dili": 0.88,
    "tdcommons/bioavailability-ma": 0.6548054539408048,
    "tdcommons/vdss-lombardo": 0.36493308852116035,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6338155515370705,
    "tdcommons/pgp-broccatelli": 0.9345507864569448,
    "tdcommons/caco2-wang": 0.29362090477843245,
    "tdcommons/herg": 0.8597938144329896,
    "tdcommons/bbb-martins": 0.9177220137585991,
    "tdcommons/ames": 0.8498913235034952,
    "tdcommons/ld50-zhu": 0.6602510589004693
}
```
