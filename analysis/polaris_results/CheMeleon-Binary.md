# CheMeleon-Binary Random Forest Results
timestamp: 2025-08-30 15:55:55.695437
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.272727 |
|  1 | test       | CLS_RET        | accuracy    | 0.849057 |
|  2 | test       | CLS_RET        | pr_auc      | 0.60431  |
|  3 | test       | CLS_RET        | cohen_kappa | 0.215541 |
|  4 | test       | CLS_RET        | mcc         | 0.266557 |
|  5 | test       | CLS_RET        | roc_auc     | 0.835096 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.355803 |
|  1 | test       | RET            | pearsonr            |   0.629865 |
|  2 | test       | RET            | spearmanr           |   0.603444 |
|  3 | test       | RET            | mean_squared_error  | 764.923    |
|  4 | test       | RET            | explained_var       |   0.372937 |
|  5 | test       | RET            | mean_absolute_error |  21.0173   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.5      |
|  1 | test       | CLS_KIT        | accuracy    | 0.862069 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.5798   |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.432763 |
|  4 | test       | CLS_KIT        | mcc         | 0.478195 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.791586 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.191753 |
|  1 | test       | KIT            | pearsonr            |   0.454988 |
|  2 | test       | KIT            | spearmanr           |   0.420451 |
|  3 | test       | KIT            | mean_squared_error  | 975.299    |
|  4 | test       | KIT            | explained_var       |   0.20334  |
|  5 | test       | KIT            | mean_absolute_error |  24.8156   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.353469 |
|  1 | test       | EGFR           | pearsonr            |   0.605047 |
|  2 | test       | EGFR           | spearmanr           |   0.40453  |
|  3 | test       | EGFR           | mean_squared_error  | 520.954    |
|  4 | test       | EGFR           | explained_var       |   0.354207 |
|  5 | test       | EGFR           | mean_absolute_error |  17.1977   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.226798 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.487786 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.373073 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.419213 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.227937 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.466043 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.387881 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.732005 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.774783 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.543857 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.399217 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.583648 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.332295 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.629509 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.582015 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.404388 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.38791  |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.572422 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.400561 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.650155 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.631088 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.296958 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.400583 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.441289 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.28742  |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.558701 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.543993 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.402282 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.287721 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.525112 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.277017 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.548687 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.542472 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.280814 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.278681 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.44124  |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.735595 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 10.1229 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.344164 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.704705 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.328473 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.385896 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.504685 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.916087 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.666112 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.25195 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  |  0.6467 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.901993 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.36219 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.796465 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.870075 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.83332 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.635139 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6043103931503794,
    "polaris/pkis2-ret-wt-reg-v2": 764.9232655508387,
    "polaris/pkis2-kit-wt-cls-v2": 0.579800299359046,
    "polaris/pkis2-kit-wt-reg-v2": 975.2986959674331,
    "polaris/pkis2-egfr-wt-reg-v2": 520.9544487135416,
    "polaris/adme-fang-solu-1": 0.4877862840272474,
    "polaris/adme-fang-rppb-1": 0.7320049106352066,
    "polaris/adme-fang-hppb-1": 0.629509431216334,
    "polaris/adme-fang-perm-1": 0.6501546339466486,
    "polaris/adme-fang-rclint-1": 0.5587010677040989,
    "polaris/adme-fang-hclint-1": 0.5486866551966608,
    "tdcommons/lipophilicity-astrazeneca": 0.7355949809145882,
    "tdcommons/ppbr-az": 10.122856674959758,
    "tdcommons/clearance-hepatocyte-az": 0.3441637624951522,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.704705194567269,
    "tdcommons/half-life-obach": 0.328473083759476,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3858963298789634,
    "tdcommons/clearance-microsome-az": 0.5046853452725297,
    "tdcommons/dili": 0.9160869565217391,
    "tdcommons/bioavailability-ma": 0.6661124043897573,
    "tdcommons/vdss-lombardo": 0.2519495428446586,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6466998191681735,
    "tdcommons/pgp-broccatelli": 0.9019928019194882,
    "tdcommons/caco2-wang": 0.36218959154788083,
    "tdcommons/herg": 0.7964653902798232,
    "tdcommons/bbb-martins": 0.8700750469043151,
    "tdcommons/ames": 0.8333196263878282,
    "tdcommons/ld50-zhu": 0.6351393903802182
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.434783 |
|  1 | test       | CLS_RET        | accuracy    | 0.877358 |
|  2 | test       | CLS_RET        | pr_auc      | 0.611957 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.383169 |
|  4 | test       | CLS_RET        | mcc         | 0.449209 |
|  5 | test       | CLS_RET        | roc_auc     | 0.876404 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.373059 |
|  1 | test       | RET            | pearsonr            |   0.650371 |
|  2 | test       | RET            | spearmanr           |   0.614708 |
|  3 | test       | RET            | mean_squared_error  | 744.433    |
|  4 | test       | RET            | explained_var       |   0.396229 |
|  5 | test       | RET            | mean_absolute_error |  20.6209   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.37037  |
|  1 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.628345 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.322802 |
|  4 | test       | CLS_KIT        | mcc         | 0.438709 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.7853   |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.186831 |
|  1 | test       | KIT            | pearsonr            |   0.456621 |
|  2 | test       | KIT            | spearmanr           |   0.425992 |
|  3 | test       | KIT            | mean_squared_error  | 981.238    |
|  4 | test       | KIT            | explained_var       |   0.20365  |
|  5 | test       | KIT            | mean_absolute_error |  25.0789   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.374543 |
|  1 | test       | EGFR           | pearsonr            |   0.628329 |
|  2 | test       | EGFR           | spearmanr           |   0.442871 |
|  3 | test       | EGFR           | mean_squared_error  | 503.974    |
|  4 | test       | EGFR           | explained_var       |   0.37528  |
|  5 | test       | EGFR           | mean_absolute_error |  17.1087   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.223706 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.481851 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.377183 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.42089  |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.224374 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.470099 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.391294 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.689762 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.715652 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.540825 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.398771 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.56984  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.299796 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.611732 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.529911 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.424071 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.367268 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.583908 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.417759 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.669939 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.654473 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.288438 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.41776  |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.433173 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.288899 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.563722 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.552165 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.401447 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.288935 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.524827 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.276434 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.548035 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.538327 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.28104  |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.278141 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.443225 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.737159 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 10.0154 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.380175 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.660498 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.305351 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.357084 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.505077 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.93087 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.639674 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.262944 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.63811 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.899793 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.362602 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.830928 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.86988 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.832823 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.642867 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6119570674979525,
    "polaris/pkis2-ret-wt-reg-v2": 744.4329389056604,
    "polaris/pkis2-kit-wt-cls-v2": 0.628344536775406,
    "polaris/pkis2-kit-wt-reg-v2": 981.237832754071,
    "polaris/pkis2-egfr-wt-reg-v2": 503.9739328213735,
    "polaris/adme-fang-solu-1": 0.48185103134765794,
    "polaris/adme-fang-rppb-1": 0.6897617429145319,
    "polaris/adme-fang-hppb-1": 0.6117316791470211,
    "polaris/adme-fang-perm-1": 0.6699389746525614,
    "polaris/adme-fang-rclint-1": 0.5637218074338203,
    "polaris/adme-fang-hclint-1": 0.5480347945073109,
    "tdcommons/lipophilicity-astrazeneca": 0.7371586128117914,
    "tdcommons/ppbr-az": 10.015397086737554,
    "tdcommons/clearance-hepatocyte-az": 0.38017541267263144,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6604984488869783,
    "tdcommons/half-life-obach": 0.3053507094335063,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.35708414824211876,
    "tdcommons/clearance-microsome-az": 0.505077340729592,
    "tdcommons/dili": 0.9308695652173912,
    "tdcommons/bioavailability-ma": 0.6396740937811773,
    "tdcommons/vdss-lombardo": 0.2629437066045826,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6381103074141049,
    "tdcommons/pgp-broccatelli": 0.899793388429752,
    "tdcommons/caco2-wang": 0.3626022566019623,
    "tdcommons/herg": 0.8309278350515463,
    "tdcommons/bbb-martins": 0.8698796122576611,
    "tdcommons/ames": 0.8328232391470365,
    "tdcommons/ld50-zhu": 0.6428674209302575
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.363636 |
|  1 | test       | CLS_RET        | accuracy    | 0.867925 |
|  2 | test       | CLS_RET        | pr_auc      | 0.673668 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.313599 |
|  4 | test       | CLS_RET        | mcc         | 0.387824 |
|  5 | test       | CLS_RET        | roc_auc     | 0.890284 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.335149 |
|  1 | test       | RET            | pearsonr            |   0.610063 |
|  2 | test       | RET            | spearmanr           |   0.592196 |
|  3 | test       | RET            | mean_squared_error  | 789.447    |
|  4 | test       | RET            | explained_var       |   0.357966 |
|  5 | test       | RET            | mean_absolute_error |  21.35     |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.4      |
|  1 | test       | CLS_KIT        | accuracy    | 0.844828 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.575061 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.332481 |
|  4 | test       | CLS_KIT        | mcc         | 0.389019 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.778046 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.197144 |
|  1 | test       | KIT            | pearsonr            |   0.463698 |
|  2 | test       | KIT            | spearmanr           |   0.432864 |
|  3 | test       | KIT            | mean_squared_error  | 968.793    |
|  4 | test       | KIT            | explained_var       |   0.212478 |
|  5 | test       | KIT            | mean_absolute_error |  24.7622   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.368094 |
|  1 | test       | EGFR           | pearsonr            |   0.626646 |
|  2 | test       | EGFR           | spearmanr           |   0.41942  |
|  3 | test       | EGFR           | mean_squared_error  | 509.17     |
|  4 | test       | EGFR           | explained_var       |   0.369309 |
|  5 | test       | EGFR           | mean_absolute_error |  17.3848   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.216265 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.471708 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.366446 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.424924 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.217208 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.469532 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.426054 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.706788 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.761739 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.509941 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.429986 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.545409 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.370355 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.667862 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.633509 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.381337 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.424356 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.55411  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.410114 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.661176 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.638818 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.292225 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.410132 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.43627  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.301401 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.574425 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.559463 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.394389 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.301512 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.521138 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.275786 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.550391 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.536409 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.281292 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.277342 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.442156 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.736167 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.99959 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.385056 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.648438 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.324375 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.447218 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.509519 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.913261 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.641669 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.263968 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.642292 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.915889 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.369323 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.805891 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.880941 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.829256 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.637435 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6736682430768051,
    "polaris/pkis2-ret-wt-reg-v2": 789.447115985325,
    "polaris/pkis2-kit-wt-cls-v2": 0.5750607560867657,
    "polaris/pkis2-kit-wt-reg-v2": 968.7929594456809,
    "polaris/pkis2-egfr-wt-reg-v2": 509.1695458400848,
    "polaris/adme-fang-solu-1": 0.4717080671947104,
    "polaris/adme-fang-rppb-1": 0.7067875336297825,
    "polaris/adme-fang-hppb-1": 0.6678616361442612,
    "polaris/adme-fang-perm-1": 0.6611756911314414,
    "polaris/adme-fang-rclint-1": 0.5744252513513175,
    "polaris/adme-fang-hclint-1": 0.5503907319423238,
    "tdcommons/lipophilicity-astrazeneca": 0.7361669778911565,
    "tdcommons/ppbr-az": 9.999586552437327,
    "tdcommons/clearance-hepatocyte-az": 0.38505577091920146,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6484382329039435,
    "tdcommons/half-life-obach": 0.32437544780297506,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4472176273728715,
    "tdcommons/clearance-microsome-az": 0.5095188196909142,
    "tdcommons/dili": 0.9132608695652173,
    "tdcommons/bioavailability-ma": 0.6416694379780512,
    "tdcommons/vdss-lombardo": 0.2639683175446181,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6422920433996383,
    "tdcommons/pgp-broccatelli": 0.9158890962410023,
    "tdcommons/caco2-wang": 0.36932278291183285,
    "tdcommons/herg": 0.8058910162002946,
    "tdcommons/bbb-martins": 0.8809412132582864,
    "tdcommons/ames": 0.8292555170455658,
    "tdcommons/ld50-zhu": 0.6374350285510235
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.48     |
|  1 | test       | CLS_RET        | accuracy    | 0.877358 |
|  2 | test       | CLS_RET        | pr_auc      | 0.623255 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.420521 |
|  4 | test       | CLS_RET        | mcc         | 0.459084 |
|  5 | test       | CLS_RET        | roc_auc     | 0.868143 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.347031 |
|  1 | test       | RET            | pearsonr            |   0.616964 |
|  2 | test       | RET            | spearmanr           |   0.603708 |
|  3 | test       | RET            | mean_squared_error  | 775.339    |
|  4 | test       | RET            | explained_var       |   0.36562  |
|  5 | test       | RET            | mean_absolute_error |  21.1197   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.357143 |
|  1 | test       | CLS_KIT        | accuracy    | 0.844828 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.616303 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.300268 |
|  4 | test       | CLS_KIT        | mcc         | 0.383469 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.761605 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | r2                  |    0.165716 |
|  1 | test       | KIT            | pearsonr            |    0.434129 |
|  2 | test       | KIT            | spearmanr           |    0.392332 |
|  3 | test       | KIT            | mean_squared_error  | 1006.72     |
|  4 | test       | KIT            | explained_var       |    0.179954 |
|  5 | test       | KIT            | mean_absolute_error |   25.3216   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.382694 |
|  1 | test       | EGFR           | pearsonr            |   0.635626 |
|  2 | test       | EGFR           | spearmanr           |   0.427536 |
|  3 | test       | EGFR           | mean_squared_error  | 497.406    |
|  4 | test       | EGFR           | explained_var       |   0.383653 |
|  5 | test       | EGFR           | mean_absolute_error |  17.2592   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.239714 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.502376 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.408865 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.412211 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.240499 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.462175 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.410694 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.73218  |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.754783 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.523588 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.414977 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.575609 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.334632 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.622597 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.545955 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.402972 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.377839 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.574694 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.416387 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.668202 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.642629 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.289117 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.416388 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.43442  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.288139 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.562464 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.547239 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.401877 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.28818  |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.525435 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.282591 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.553583 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.542996 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.278649 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.284514 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.43926  |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.736549 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.94815 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.354547 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.673724 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.326697 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.387575 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.513335 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.938261 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.675258 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.270257 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.643761 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.894728 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.36191 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.83785 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.884948 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.836886 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.639943 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.62325480153306,
    "polaris/pkis2-ret-wt-reg-v2": 775.33854001913,
    "polaris/pkis2-kit-wt-cls-v2": 0.6163025399260009,
    "polaris/pkis2-kit-wt-reg-v2": 1006.7177333232759,
    "polaris/pkis2-egfr-wt-reg-v2": 497.40600282773926,
    "polaris/adme-fang-solu-1": 0.5023761604123129,
    "polaris/adme-fang-rppb-1": 0.7321803881431335,
    "polaris/adme-fang-hppb-1": 0.6225970883450475,
    "polaris/adme-fang-perm-1": 0.6682024895797213,
    "polaris/adme-fang-rclint-1": 0.562463980691908,
    "polaris/adme-fang-hclint-1": 0.5535827795357402,
    "tdcommons/lipophilicity-astrazeneca": 0.7365485243764172,
    "tdcommons/ppbr-az": 9.948147180277484,
    "tdcommons/clearance-hepatocyte-az": 0.3545466007444611,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6737237811488085,
    "tdcommons/half-life-obach": 0.3266974415116589,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3875749198280585,
    "tdcommons/clearance-microsome-az": 0.5133353783583688,
    "tdcommons/dili": 0.9382608695652174,
    "tdcommons/bioavailability-ma": 0.6752577319587629,
    "tdcommons/vdss-lombardo": 0.2702568606910458,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.64376130198915,
    "tdcommons/pgp-broccatelli": 0.8947280725139963,
    "tdcommons/caco2-wang": 0.36191035895652807,
    "tdcommons/herg": 0.8378497790868925,
    "tdcommons/bbb-martins": 0.8849476235146967,
    "tdcommons/ames": 0.8368863694217628,
    "tdcommons/ld50-zhu": 0.6399433344663531
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.416667 |
|  1 | test       | CLS_RET        | accuracy    | 0.867925 |
|  2 | test       | CLS_RET        | pr_auc      | 0.605337 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.356461 |
|  4 | test       | CLS_RET        | mcc         | 0.40138  |
|  5 | test       | CLS_RET        | roc_auc     | 0.858559 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.357871 |
|  1 | test       | RET            | pearsonr            |   0.627096 |
|  2 | test       | RET            | spearmanr           |   0.593066 |
|  3 | test       | RET            | mean_squared_error  | 762.468    |
|  4 | test       | RET            | explained_var       |   0.377478 |
|  5 | test       | RET            | mean_absolute_error |  20.8813   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.466667 |
|  1 | test       | CLS_KIT        | accuracy    | 0.862069 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.614274 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.40665  |
|  4 | test       | CLS_KIT        | mcc         | 0.475801 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.772485 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | r2                  |    0.150202 |
|  1 | test       | KIT            | pearsonr            |    0.41926  |
|  2 | test       | KIT            | spearmanr           |    0.380642 |
|  3 | test       | KIT            | mean_squared_error  | 1025.44     |
|  4 | test       | KIT            | explained_var       |    0.164671 |
|  5 | test       | KIT            | mean_absolute_error |   25.3509   |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.375778 |
|  1 | test       | EGFR           | pearsonr            |   0.629546 |
|  2 | test       | EGFR           | spearmanr           |   0.398819 |
|  3 | test       | EGFR           | mean_squared_error  | 502.978    |
|  4 | test       | EGFR           | explained_var       |   0.376719 |
|  5 | test       | EGFR           | mean_absolute_error |  17.2818   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.235217 |
|  1 | test       | LOG_SOLUBILITY | pearsonr            | 0.497135 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.399492 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.414649 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.236329 |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.462275 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.439563 |
|  1 | test       | LOG_RPPB       | pearsonr            | 0.731056 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.785217 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.497938 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.444795 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.540025 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | r2                  | 0.304623 |
|  1 | test       | LOG_HPPB       | pearsonr            | 0.606889 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.540759 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.421148 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.363771 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.577702 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.395832 |
|  1 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.646818 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.623354 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.2993   |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.395832 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.439898 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.303207 |
|  1 | test       | LOG_RLM_CLint  | pearsonr            | 0.583114 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.574219 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.39337  |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.303217 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.518234 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.280429 |
|  1 | test       | LOG_HLM_CLint  | pearsonr            | 0.557866 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.550304 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.279489 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.282482 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.439793 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.735599 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.95105 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.367892 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.696326 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.352566 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.353607 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.489617 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.909348 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.661124 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.275058 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.661958 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.90036 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.348204 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.813697 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.873827 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.828799 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.645299 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6053367720322738,
    "polaris/pkis2-ret-wt-reg-v2": 762.4678329433962,
    "polaris/pkis2-kit-wt-cls-v2": 0.6142741652878152,
    "polaris/pkis2-kit-wt-reg-v2": 1025.437360356615,
    "polaris/pkis2-egfr-wt-reg-v2": 502.97840729128086,
    "polaris/adme-fang-solu-1": 0.49713481314081104,
    "polaris/adme-fang-rppb-1": 0.7310563785737931,
    "polaris/adme-fang-hppb-1": 0.6068886072899102,
    "polaris/adme-fang-perm-1": 0.6468181118716216,
    "polaris/adme-fang-rclint-1": 0.583113586593953,
    "polaris/adme-fang-hclint-1": 0.5578657250180739,
    "tdcommons/lipophilicity-astrazeneca": 0.7355991174886621,
    "tdcommons/ppbr-az": 9.951054402732877,
    "tdcommons/clearance-hepatocyte-az": 0.3678917635207808,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6963260328281757,
    "tdcommons/half-life-obach": 0.35256620755609297,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3536069823726725,
    "tdcommons/clearance-microsome-az": 0.4896173807686737,
    "tdcommons/dili": 0.9093478260869565,
    "tdcommons/bioavailability-ma": 0.6611240438975723,
    "tdcommons/vdss-lombardo": 0.27505813245267324,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6619575045207956,
    "tdcommons/pgp-broccatelli": 0.9003599040255932,
    "tdcommons/caco2-wang": 0.3482038715711801,
    "tdcommons/herg": 0.8136966126656848,
    "tdcommons/bbb-martins": 0.873827392120075,
    "tdcommons/ames": 0.8287992715737533,
    "tdcommons/ld50-zhu": 0.64529925439515
}
```
