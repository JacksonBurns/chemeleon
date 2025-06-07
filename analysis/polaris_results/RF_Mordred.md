# Random Forest Baseline Results
timestamp: 2025-06-05 09:08:36.624268
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.272727 |
|  1 | test       | CLS_RET        | pr_auc      | 0.424536 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.215541 |
|  3 | test       | CLS_RET        | mcc         | 0.266557 |
|  4 | test       | CLS_RET        | roc_auc     | 0.728685 |
|  5 | test       | CLS_RET        | accuracy    | 0.849057 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 948.733    |
|  1 | test       | RET            | explained_var       |   0.228378 |
|  2 | test       | RET            | mean_absolute_error |  23.5413   |
|  3 | test       | RET            | r2                  |   0.201003 |
|  4 | test       | RET            | pearsonr            |   0.477959 |
|  5 | test       | RET            | spearmanr           |   0.457443 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.432432 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.528372 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.329295 |
|  3 | test       | CLS_KIT        | mcc         | 0.337847 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.790135 |
|  5 | test       | CLS_KIT        | accuracy    | 0.818966 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_squared_error  | 867.584    |
|  1 | test       | KIT            | explained_var       |   0.286036 |
|  2 | test       | KIT            | mean_absolute_error |  23.5457   |
|  3 | test       | KIT            | r2                  |   0.281018 |
|  4 | test       | KIT            | pearsonr            |   0.536991 |
|  5 | test       | KIT            | spearmanr           |   0.487856 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 514.957    |
|  1 | test       | EGFR           | explained_var       |   0.362066 |
|  2 | test       | EGFR           | mean_absolute_error |  17.6102   |
|  3 | test       | EGFR           | r2                  |   0.360912 |
|  4 | test       | EGFR           | pearsonr            |   0.605712 |
|  5 | test       | EGFR           | spearmanr           |   0.358143 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.38763  |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.285608 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.435306 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.285051 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.53621  |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.455171 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.499332 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.438003 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.508196 |
|  3 | test       | LOG_RPPB       | r2                  | 0.437994 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.696383 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.832174 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.237494 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.65428  |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.392077 |
|  3 | test       | LOG_HPPB       | r2                  | 0.607861 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.810455 |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.814119 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.241688 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.51234  |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.38705  |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.512129 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.726028 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.717949 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.337696 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.401827 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.465775 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.401825 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.634284 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.633687 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.232478 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.401928 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.386903 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.401462 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.635156 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.642709 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.582145 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.65084 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.296368 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.639051 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.321151 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.343236 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.513451 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.93913 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.641669 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.485273 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.648282 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.892195 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.313271 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.801178 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.877482 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.847607 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.62747 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.42453568106157136,
    "polaris/pkis2-ret-wt-reg-v2": 948.7332679787094,
    "polaris/pkis2-kit-wt-cls-v2": 0.5283717760092553,
    "polaris/pkis2-kit-wt-reg-v2": 867.5837621571959,
    "polaris/pkis2-egfr-wt-reg-v2": 514.9571847016972,
    "polaris/adme-fang-solu-1": 0.5362095232329354,
    "polaris/adme-fang-rppb-1": 0.6963829662099205,
    "polaris/adme-fang-hppb-1": 0.8104548528427337,
    "polaris/adme-fang-perm-1": 0.7260280586863765,
    "polaris/adme-fang-rclint-1": 0.6342843257338214,
    "polaris/adme-fang-hclint-1": 0.6351560373796259,
    "tdcommons/lipophilicity-astrazeneca": 0.5821450799306234,
    "tdcommons/ppbr-az": 8.650838637241097,
    "tdcommons/clearance-hepatocyte-az": 0.2963675047906221,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6390512967621402,
    "tdcommons/half-life-obach": 0.3211509985562523,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3432361645904026,
    "tdcommons/clearance-microsome-az": 0.5134507045580553,
    "tdcommons/dili": 0.9391304347826087,
    "tdcommons/bioavailability-ma": 0.6416694379780512,
    "tdcommons/vdss-lombardo": 0.48527336388515635,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6482820976491862,
    "tdcommons/pgp-broccatelli": 0.8921954145561184,
    "tdcommons/caco2-wang": 0.3132711822529553,
    "tdcommons/herg": 0.8011782032400588,
    "tdcommons/bbb-martins": 0.877482020012508,
    "tdcommons/ames": 0.8476071589418238,
    "tdcommons/ld50-zhu": 0.6274696501195027
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.272727 |
|  1 | test       | CLS_RET        | pr_auc      | 0.41899  |
|  2 | test       | CLS_RET        | cohen_kappa | 0.215541 |
|  3 | test       | CLS_RET        | mcc         | 0.266557 |
|  4 | test       | CLS_RET        | roc_auc     | 0.757436 |
|  5 | test       | CLS_RET        | accuracy    | 0.849057 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 989.07     |
|  1 | test       | RET            | explained_var       |   0.201657 |
|  2 | test       | RET            | mean_absolute_error |  23.9394   |
|  3 | test       | RET            | r2                  |   0.167033 |
|  4 | test       | RET            | pearsonr            |   0.450163 |
|  5 | test       | RET            | spearmanr           |   0.429934 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.540541 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.612952 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.457048 |
|  3 | test       | CLS_KIT        | mcc         | 0.468918 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.779739 |
|  5 | test       | CLS_KIT        | accuracy    | 0.853448 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_squared_error  | 884.464    |
|  1 | test       | KIT            | explained_var       |   0.274623 |
|  2 | test       | KIT            | mean_absolute_error |  23.5659   |
|  3 | test       | KIT            | r2                  |   0.267029 |
|  4 | test       | KIT            | pearsonr            |   0.527724 |
|  5 | test       | KIT            | spearmanr           |   0.486078 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 525.994    |
|  1 | test       | EGFR           | explained_var       |   0.348296 |
|  2 | test       | EGFR           | mean_absolute_error |  17.7983   |
|  3 | test       | EGFR           | r2                  |   0.347214 |
|  4 | test       | EGFR           | pearsonr            |   0.591934 |
|  5 | test       | EGFR           | spearmanr           |   0.344683 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.391045 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.279018 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.439855 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.278752 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.529331 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.438825 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.43617  |
|  1 | test       | LOG_RPPB       | explained_var       | 0.509087 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.488844 |
|  3 | test       | LOG_RPPB       | r2                  | 0.509084 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.751125 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.848696 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.230762 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.667771 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.380266 |
|  3 | test       | LOG_HPPB       | r2                  | 0.618977 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.81851  |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.832302 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.23916  |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.517612 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.382735 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.517231 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.729735 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.714955 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.336471 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.403995 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.466746 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.403995 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.636161 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.638649 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.237015 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.390073 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.38859  |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.389782 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.624927 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.633656 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.57911 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.48898 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.320316 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.602959 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.352554 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.352327 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.531801 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.92413 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.696043 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.471002 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.676876 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.898594 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.327235 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.783358 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.874961 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.846991 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.639518 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.41899042410611353,
    "polaris/pkis2-ret-wt-reg-v2": 989.0696491188388,
    "polaris/pkis2-kit-wt-cls-v2": 0.6129519899095477,
    "polaris/pkis2-kit-wt-reg-v2": 884.4644972641013,
    "polaris/pkis2-egfr-wt-reg-v2": 525.994317536522,
    "polaris/adme-fang-solu-1": 0.5293307811958299,
    "polaris/adme-fang-rppb-1": 0.7511245986783879,
    "polaris/adme-fang-hppb-1": 0.8185101282064952,
    "polaris/adme-fang-perm-1": 0.7297352986685504,
    "polaris/adme-fang-rclint-1": 0.6361614386877628,
    "polaris/adme-fang-hclint-1": 0.6249271871778355,
    "tdcommons/lipophilicity-astrazeneca": 0.5791096051590783,
    "tdcommons/ppbr-az": 8.488976169920564,
    "tdcommons/clearance-hepatocyte-az": 0.3203156218191087,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6029586839510781,
    "tdcommons/half-life-obach": 0.3525540122109843,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.35232675685189485,
    "tdcommons/clearance-microsome-az": 0.5318006368234307,
    "tdcommons/dili": 0.9241304347826087,
    "tdcommons/bioavailability-ma": 0.6960425673428665,
    "tdcommons/vdss-lombardo": 0.47100158877215087,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6768761301989151,
    "tdcommons/pgp-broccatelli": 0.8985937083444414,
    "tdcommons/caco2-wang": 0.32723547235680894,
    "tdcommons/herg": 0.7833578792341679,
    "tdcommons/bbb-martins": 0.874960913070669,
    "tdcommons/ames": 0.8469913254616303,
    "tdcommons/ld50-zhu": 0.6395177601580692
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.347826 |
|  1 | test       | CLS_RET        | pr_auc      | 0.424255 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.288272 |
|  3 | test       | CLS_RET        | mcc         | 0.337956 |
|  4 | test       | CLS_RET        | roc_auc     | 0.733972 |
|  5 | test       | CLS_RET        | accuracy    | 0.858491 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 991.704    |
|  1 | test       | RET            | explained_var       |   0.193856 |
|  2 | test       | RET            | mean_absolute_error |  23.9925   |
|  3 | test       | RET            | r2                  |   0.164814 |
|  4 | test       | RET            | pearsonr            |   0.442945 |
|  5 | test       | RET            | spearmanr           |   0.430997 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.526316 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.547095 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.436285 |
|  3 | test       | CLS_KIT        | mcc         | 0.444197 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.783849 |
|  5 | test       | CLS_KIT        | accuracy    | 0.844828 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_squared_error  | 929.914    |
|  1 | test       | KIT            | explained_var       |   0.234544 |
|  2 | test       | KIT            | mean_absolute_error |  23.9324   |
|  3 | test       | KIT            | r2                  |   0.229364 |
|  4 | test       | KIT            | pearsonr            |   0.496219 |
|  5 | test       | KIT            | spearmanr           |   0.448536 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 516.82     |
|  1 | test       | EGFR           | explained_var       |   0.35939  |
|  2 | test       | EGFR           | mean_absolute_error |  17.6787   |
|  3 | test       | EGFR           | r2                  |   0.3586   |
|  4 | test       | EGFR           | pearsonr            |   0.601695 |
|  5 | test       | EGFR           | spearmanr           |   0.333879 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.381076 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.297342 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.435483 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.29714  |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.547044 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.451144 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.456019 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.487747 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.484973 |
|  3 | test       | LOG_RPPB       | r2                  | 0.486743 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.729274 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.813043 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.235923 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.654586 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.386556 |
|  3 | test       | LOG_HPPB       | r2                  | 0.610455 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.811405 |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.815952 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.243084 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.509489 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.385552 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.50931  |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.722658 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.718896 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.330979 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.413744 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.459623 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.413723 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.644205 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.645889 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.232823 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.40138  |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.386715 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.400574 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.634438 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.641295 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.583067 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.66189 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.314395 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.633786 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.439078 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.343511 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.485208 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.929565 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.66129 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.519411 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.656985 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.892962 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.305364 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.817526 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.873632 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.848916 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.635504 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.4242545472901411,
    "polaris/pkis2-ret-wt-reg-v2": 991.7041834116138,
    "polaris/pkis2-kit-wt-cls-v2": 0.5470945603970429,
    "polaris/pkis2-kit-wt-reg-v2": 929.9137082877505,
    "polaris/pkis2-egfr-wt-reg-v2": 516.8197904763579,
    "polaris/adme-fang-solu-1": 0.5470436836730058,
    "polaris/adme-fang-rppb-1": 0.7292737223857819,
    "polaris/adme-fang-hppb-1": 0.8114050999458244,
    "polaris/adme-fang-perm-1": 0.7226575658732739,
    "polaris/adme-fang-rclint-1": 0.6442050906675219,
    "polaris/adme-fang-hclint-1": 0.6344376766236837,
    "tdcommons/lipophilicity-astrazeneca": 0.5830668231589454,
    "tdcommons/ppbr-az": 8.661894501223761,
    "tdcommons/clearance-hepatocyte-az": 0.31439475338345674,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6337860516670732,
    "tdcommons/half-life-obach": 0.4390775466877196,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.34351108659354856,
    "tdcommons/clearance-microsome-az": 0.485207715931403,
    "tdcommons/dili": 0.9295652173913043,
    "tdcommons/bioavailability-ma": 0.661290322580645,
    "tdcommons/vdss-lombardo": 0.5194109467472516,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.656984629294756,
    "tdcommons/pgp-broccatelli": 0.8929618768328447,
    "tdcommons/caco2-wang": 0.30536391653066797,
    "tdcommons/herg": 0.8175257731958763,
    "tdcommons/bbb-martins": 0.8736319574734208,
    "tdcommons/ames": 0.8489161722375609,
    "tdcommons/ld50-zhu": 0.6355040952201142
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.272727 |
|  1 | test       | CLS_RET        | pr_auc      | 0.435149 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.215541 |
|  3 | test       | CLS_RET        | mcc         | 0.266557 |
|  4 | test       | CLS_RET        | roc_auc     | 0.763054 |
|  5 | test       | CLS_RET        | accuracy    | 0.849057 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 979.739    |
|  1 | test       | RET            | explained_var       |   0.207521 |
|  2 | test       | RET            | mean_absolute_error |  23.7473   |
|  3 | test       | RET            | r2                  |   0.174891 |
|  4 | test       | RET            | pearsonr            |   0.456182 |
|  5 | test       | RET            | spearmanr           |   0.458572 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.514286 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.568372 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.434633 |
|  3 | test       | CLS_KIT        | mcc         | 0.455516 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.790377 |
|  5 | test       | CLS_KIT        | accuracy    | 0.853448 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_squared_error  | 857.112    |
|  1 | test       | KIT            | explained_var       |   0.295232 |
|  2 | test       | KIT            | mean_absolute_error |  23.0956   |
|  3 | test       | KIT            | r2                  |   0.289696 |
|  4 | test       | KIT            | pearsonr            |   0.545324 |
|  5 | test       | KIT            | spearmanr           |   0.508984 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 527.29     |
|  1 | test       | EGFR           | explained_var       |   0.346195 |
|  2 | test       | EGFR           | mean_absolute_error |  17.9463   |
|  3 | test       | EGFR           | r2                  |   0.345606 |
|  4 | test       | EGFR           | pearsonr            |   0.590399 |
|  5 | test       | EGFR           | spearmanr           |   0.320402 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.390772 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.279597 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.439711 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.279256 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.530124 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.446993 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.463777 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.478194 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.481523 |
|  3 | test       | LOG_RPPB       | r2                  | 0.478012 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.74237  |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.818261 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.234384 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.655962 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.389905 |
|  3 | test       | LOG_HPPB       | r2                  | 0.612997 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.813314 |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.815036 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.238962 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.517752 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.384187 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.517631 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.730261 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.716793 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.337345 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.402481 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.464562 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.402447 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.634997 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.637751 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.234796 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.395908 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.388353 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.395494 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.629836 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.63415  |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.585335 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.64395 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.307289 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.616584 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.345166 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.330362 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.50978 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.939783 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.670602 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.481279 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.65269 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.895661 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.313177 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.790869 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.876329 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.844284 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.632114 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.43514913531571775,
    "polaris/pkis2-ret-wt-reg-v2": 979.7387156693242,
    "polaris/pkis2-kit-wt-cls-v2": 0.5683717594681063,
    "polaris/pkis2-kit-wt-reg-v2": 857.1120712468954,
    "polaris/pkis2-egfr-wt-reg-v2": 527.2898017996328,
    "polaris/adme-fang-solu-1": 0.5301240232229776,
    "polaris/adme-fang-rppb-1": 0.7423695082046937,
    "polaris/adme-fang-hppb-1": 0.8133142078162978,
    "polaris/adme-fang-perm-1": 0.7302612661195375,
    "polaris/adme-fang-rclint-1": 0.6349973324108293,
    "polaris/adme-fang-hclint-1": 0.6298356591737979,
    "tdcommons/lipophilicity-astrazeneca": 0.5853345172234944,
    "tdcommons/ppbr-az": 8.64394621792761,
    "tdcommons/clearance-hepatocyte-az": 0.3072888711232589,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6165837305604205,
    "tdcommons/half-life-obach": 0.345166072144174,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.33036171963693695,
    "tdcommons/clearance-microsome-az": 0.5097795818862642,
    "tdcommons/dili": 0.9397826086956522,
    "tdcommons/bioavailability-ma": 0.6706019288327236,
    "tdcommons/vdss-lombardo": 0.4812788887642876,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6526898734177217,
    "tdcommons/pgp-broccatelli": 0.8956611570247935,
    "tdcommons/caco2-wang": 0.31317674360841197,
    "tdcommons/herg": 0.7908689248895434,
    "tdcommons/bbb-martins": 0.8763289555972483,
    "tdcommons/ames": 0.8442842037243729,
    "tdcommons/ld50-zhu": 0.6321138691276271
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.363636 |
|  1 | test       | CLS_RET        | pr_auc      | 0.494992 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.313599 |
|  3 | test       | CLS_RET        | mcc         | 0.387824 |
|  4 | test       | CLS_RET        | roc_auc     | 0.777594 |
|  5 | test       | CLS_RET        | accuracy    | 0.867925 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 985.127    |
|  1 | test       | RET            | explained_var       |   0.201267 |
|  2 | test       | RET            | mean_absolute_error |  23.8362   |
|  3 | test       | RET            | r2                  |   0.170353 |
|  4 | test       | RET            | pearsonr            |   0.451062 |
|  5 | test       | RET            | spearmanr           |   0.418432 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.5      |
|  1 | test       | CLS_KIT        | pr_auc      | 0.626527 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.413483 |
|  3 | test       | CLS_KIT        | mcc         | 0.428291 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.809961 |
|  5 | test       | CLS_KIT        | accuracy    | 0.844828 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_squared_error  | 892.668    |
|  1 | test       | KIT            | explained_var       |   0.266206 |
|  2 | test       | KIT            | mean_absolute_error |  23.7006   |
|  3 | test       | KIT            | r2                  |   0.26023  |
|  4 | test       | KIT            | pearsonr            |   0.520746 |
|  5 | test       | KIT            | spearmanr           |   0.474523 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 503.609    |
|  1 | test       | EGFR           | explained_var       |   0.375132 |
|  2 | test       | EGFR           | mean_absolute_error |  17.1966   |
|  3 | test       | EGFR           | r2                  |   0.374995 |
|  4 | test       | EGFR           | pearsonr            |   0.617468 |
|  5 | test       | EGFR           | spearmanr           |   0.369952 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.386554 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.287179 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.440776 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.287035 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.537356 |
|  5 | test       | LOG_SOLUBILITY | spearmanr           | 0.450982 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.502196 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.43538  |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.534432 |
|  3 | test       | LOG_RPPB       | r2                  | 0.43477  |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.709945 |
|  5 | test       | LOG_RPPB       | spearmanr           | 0.798261 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.226304 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.67331  |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.393825 |
|  3 | test       | LOG_HPPB       | r2                  | 0.626338 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.827073 |
|  5 | test       | LOG_HPPB       | spearmanr           | 0.833066 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.243081 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.509449 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.38582  |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.509317 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.722441 |
|  5 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.715976 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.327714 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.419561 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.460102 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.419506 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.649364 |
|  5 | test       | LOG_RLM_CLint  | spearmanr           | 0.650511 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.231247 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.40516  |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.384263 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.404633 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.637987 |
|  5 | test       | LOG_HLM_CLint  | spearmanr           | 0.643029 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.584748 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.69739 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.326163 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.634498 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.319173 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.335627 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.499395 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.93087 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.658131 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.487221 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.665348 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.88683 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.322283 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.800736 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.882837 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.855452 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.635483 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.4949917083755303,
    "polaris/pkis2-ret-wt-reg-v2": 985.1270057767781,
    "polaris/pkis2-kit-wt-cls-v2": 0.6265268700939152,
    "polaris/pkis2-kit-wt-reg-v2": 892.6681550668416,
    "polaris/pkis2-egfr-wt-reg-v2": 503.60920572800364,
    "polaris/adme-fang-solu-1": 0.5373560942826231,
    "polaris/adme-fang-rppb-1": 0.7099451993044406,
    "polaris/adme-fang-hppb-1": 0.8270732870794986,
    "polaris/adme-fang-perm-1": 0.7224413017476272,
    "polaris/adme-fang-rclint-1": 0.6493639594515674,
    "polaris/adme-fang-hclint-1": 0.63798742035071,
    "tdcommons/lipophilicity-astrazeneca": 0.5847475846835546,
    "tdcommons/ppbr-az": 8.697385564268384,
    "tdcommons/clearance-hepatocyte-az": 0.32616297823090545,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6344978484837788,
    "tdcommons/half-life-obach": 0.31917291357963185,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3356268655279182,
    "tdcommons/clearance-microsome-az": 0.4993951109302643,
    "tdcommons/dili": 0.9308695652173913,
    "tdcommons/bioavailability-ma": 0.6581310276022614,
    "tdcommons/vdss-lombardo": 0.4872206964987398,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6653481012658228,
    "tdcommons/pgp-broccatelli": 0.886830178619035,
    "tdcommons/caco2-wang": 0.32228319391201155,
    "tdcommons/herg": 0.8007363770250369,
    "tdcommons/bbb-martins": 0.8828369293308319,
    "tdcommons/ames": 0.855452427108422,
    "tdcommons/ld50-zhu": 0.6354834999373543
}
```
