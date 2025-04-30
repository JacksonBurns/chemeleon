# ibm-research/MoLFormer-XL-both-10pct Results
timestamp: 2025-04-30 11:59:18.217892
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | mcc         | 0.655239 |
|  1 | test       | CLS_RET        | accuracy    | 0.915094 |
|  2 | test       | CLS_RET        | f1          | 0.689655 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.642161 |
|  4 | test       | CLS_RET        | pr_auc      | 0.685265 |
|  5 | test       | CLS_RET        | roc_auc     | 0.892267 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | RET            | spearmanr           |    0.434232  |
|  1 | test       | RET            | mean_squared_error  | 1359.02      |
|  2 | test       | RET            | pearsonr            |    0.149066  |
|  3 | test       | RET            | mean_absolute_error |   26.664     |
|  4 | test       | RET            | r2                  |   -0.144528  |
|  5 | test       | RET            | explained_var       |    0.0204633 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | mcc         | 0.421313 |
|  1 | test       | CLS_KIT        | accuracy    | 0.836207 |
|  2 | test       | CLS_KIT        | f1          | 0.512821 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.416314 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.632308 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.838491 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | spearmanr           |    0.344766  |
|  1 | test       | KIT            | mean_squared_error  | 1147.58      |
|  2 | test       | KIT            | pearsonr            |    0.31965   |
|  3 | test       | KIT            | mean_absolute_error |   28.3009    |
|  4 | test       | KIT            | r2                  |    0.0489797 |
|  5 | test       | KIT            | explained_var       |    0.0909732 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | EGFR           | spearmanr           |   0.20341   |
|  1 | test       | EGFR           | mean_squared_error  | 759.689     |
|  2 | test       | EGFR           | pearsonr            |   0.283237  |
|  3 | test       | EGFR           | mean_absolute_error |  20.3928    |
|  4 | test       | EGFR           | r2                  |   0.0571864 |
|  5 | test       | EGFR           | explained_var       |   0.0783601 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.50592  |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.373118 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.582896 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.408725 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.311817 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.324883 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.751304 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.563473 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.607575 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.531506 |
|  4 | test       | LOG_RPPB       | r2                  | 0.365802 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.366042 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.696004 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.306326 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.751536 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.443295 |
|  4 | test       | LOG_HPPB       | r2                  | 0.494209 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.563839 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.781326 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.191294 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.78747  |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.317289 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.613853 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.61813  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.724771 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.275077 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.723601 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.41629  |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.512744 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.51512  |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.708218 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.210701 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.699032 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.360554 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.45753  |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.458533 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.513913 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 10.2262 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.215392 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.672302 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.124162 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.350583 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |      Score |
|---:|:-----------|:---------------|:----------|-----------:|
|  0 | test       | Y              | spearmanr | -0.0685902 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.841739 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.731626 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.565538 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.622288 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.89856 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.393156 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.776141 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.863157 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.855378 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.621254 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6852654827355725,
    "polaris/pkis2-ret-wt-reg-v2": 1359.0186003050162,
    "polaris/pkis2-kit-wt-cls-v2": 0.6323076141849994,
    "polaris/pkis2-kit-wt-reg-v2": 1147.5810763280138,
    "polaris/pkis2-egfr-wt-reg-v2": 759.6894641861445,
    "polaris/adme-fang-solu-1": 0.5828956129679115,
    "polaris/adme-fang-rppb-1": 0.6075753709346396,
    "polaris/adme-fang-hppb-1": 0.7515361678445367,
    "polaris/adme-fang-perm-1": 0.7874704469571652,
    "polaris/adme-fang-rclint-1": 0.7236011874505472,
    "polaris/adme-fang-hclint-1": 0.6990324015659282,
    "tdcommons/lipophilicity-astrazeneca": 0.5139134507442026,
    "tdcommons/ppbr-az": 10.22624198572367,
    "tdcommons/clearance-hepatocyte-az": 0.2153920289958245,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6723022167841135,
    "tdcommons/half-life-obach": 0.12416217119104643,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3505828619738079,
    "tdcommons/clearance-microsome-az": -0.06859023796430883,
    "tdcommons/dili": 0.8417391304347825,
    "tdcommons/bioavailability-ma": 0.7316262055204523,
    "tdcommons/vdss-lombardo": 0.5655377180973229,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6222875226039782,
    "tdcommons/pgp-broccatelli": 0.8985603838976273,
    "tdcommons/caco2-wang": 0.39315628053354124,
    "tdcommons/herg": 0.7761413843888071,
    "tdcommons/bbb-martins": 0.863156660412758,
    "tdcommons/ames": 0.85537801797568,
    "tdcommons/ld50-zhu": 0.6212541171526876
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | mcc         | 0.604725 |
|  1 | test       | CLS_RET        | accuracy    | 0.90566  |
|  2 | test       | CLS_RET        | f1          | 0.615385 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.567347 |
|  4 | test       | CLS_RET        | pr_auc      | 0.741432 |
|  5 | test       | CLS_RET        | roc_auc     | 0.88698  |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | RET            | spearmanr           |    0.526394  |
|  1 | test       | RET            | mean_squared_error  | 1124.43      |
|  2 | test       | RET            | pearsonr            |    0.528656  |
|  3 | test       | RET            | mean_absolute_error |   24.8156    |
|  4 | test       | RET            | r2                  |    0.0530401 |
|  5 | test       | RET            | explained_var       |    0.142011  |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | mcc         | 0.360788 |
|  1 | test       | CLS_KIT        | accuracy    | 0.827586 |
|  2 | test       | CLS_KIT        | f1          | 0.444444 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.348315 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.568735 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.832689 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | spearmanr           |    0.369772  |
|  1 | test       | KIT            | mean_squared_error  | 1091.24      |
|  2 | test       | KIT            | pearsonr            |    0.336501  |
|  3 | test       | KIT            | mean_absolute_error |   27.7604    |
|  4 | test       | KIT            | r2                  |    0.0956668 |
|  5 | test       | KIT            | explained_var       |    0.111879  |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | EGFR           | spearmanr           |   0.210118   |
|  1 | test       | EGFR           | mean_squared_error  | 798.468      |
|  2 | test       | EGFR           | pearsonr            |   0.209828   |
|  3 | test       | EGFR           | mean_absolute_error |  21.7654     |
|  4 | test       | EGFR           | r2                  |   0.00906004 |
|  5 | test       | EGFR           | explained_var       |   0.0225358  |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.480059 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.392463 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.556038 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.433312 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.276136 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.287378 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.86     |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.406232 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.757268 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.468859 |
|  4 | test       | LOG_RPPB       | r2                  | 0.542779 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.544997 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.647108 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.336849 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.723001 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.492978 |
|  4 | test       | LOG_HPPB       | r2                  | 0.443812 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.521417 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.784006 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.183945 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.794061 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.321527 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.628689 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.629429 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.714183 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.288486 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.714362 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.424774 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.488992 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.501402 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.708884 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.209625 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.702593 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.362432 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.460299 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.462294 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.502215 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 10.5759 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.266747 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.700692 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.327441 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.365147 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.238136 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.837391 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.730961 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.653099 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.647604 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.922021 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.402102 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.756406 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.872342 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.56642 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.634092 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7414323492607899,
    "polaris/pkis2-ret-wt-reg-v2": 1124.4250269297188,
    "polaris/pkis2-kit-wt-cls-v2": 0.5687345018899432,
    "polaris/pkis2-kit-wt-reg-v2": 1091.2444389055463,
    "polaris/pkis2-egfr-wt-reg-v2": 798.4681764690388,
    "polaris/adme-fang-solu-1": 0.5560376659265465,
    "polaris/adme-fang-rppb-1": 0.7572680001809684,
    "polaris/adme-fang-hppb-1": 0.7230009834019818,
    "polaris/adme-fang-perm-1": 0.7940605090042357,
    "polaris/adme-fang-rclint-1": 0.714361755632358,
    "polaris/adme-fang-hclint-1": 0.7025926795466753,
    "tdcommons/lipophilicity-astrazeneca": 0.5022154106524374,
    "tdcommons/ppbr-az": 10.575902495409807,
    "tdcommons/clearance-hepatocyte-az": 0.26674747648073166,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.700692245822261,
    "tdcommons/half-life-obach": 0.32744137925182043,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3651473277170073,
    "tdcommons/clearance-microsome-az": 0.23813593023416166,
    "tdcommons/dili": 0.837391304347826,
    "tdcommons/bioavailability-ma": 0.730961090788161,
    "tdcommons/vdss-lombardo": 0.6530994724636123,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6476039783001808,
    "tdcommons/pgp-broccatelli": 0.922020794454812,
    "tdcommons/caco2-wang": 0.40210241421089593,
    "tdcommons/herg": 0.7564064801178204,
    "tdcommons/bbb-martins": 0.8723420888055035,
    "tdcommons/ames": 0.5664199416475749,
    "tdcommons/ld50-zhu": 0.6340916558208906
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | mcc         | 0.562567 |
|  1 | test       | CLS_RET        | accuracy    | 0.896226 |
|  2 | test       | CLS_RET        | f1          | 0.592593 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.537669 |
|  4 | test       | CLS_RET        | pr_auc      | 0.716341 |
|  5 | test       | CLS_RET        | roc_auc     | 0.874422 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |          Score |
|---:|:-----------|:---------------|:--------------------|---------------:|
|  0 | test       | RET            | spearmanr           |   -0.302726    |
|  1 | test       | RET            | mean_squared_error  | 1266.19        |
|  2 | test       | RET            | pearsonr            |   -0.273778    |
|  3 | test       | RET            | mean_absolute_error |   26.974       |
|  4 | test       | RET            | r2                  |   -0.0663468   |
|  5 | test       | RET            | explained_var       |   -4.58584e-06 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | mcc         | 0.403382 |
|  1 | test       | CLS_KIT        | accuracy    | 0.836207 |
|  2 | test       | CLS_KIT        | f1          | 0.486486 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.393172 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.595807 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.818182 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | spearmanr           |    0.330233  |
|  1 | test       | KIT            | mean_squared_error  | 1130.5       |
|  2 | test       | KIT            | pearsonr            |    0.309916  |
|  3 | test       | KIT            | mean_absolute_error |   27.9061    |
|  4 | test       | KIT            | r2                  |    0.0631374 |
|  5 | test       | KIT            | explained_var       |    0.0915426 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | EGFR           | spearmanr           |   0.249156  |
|  1 | test       | EGFR           | mean_squared_error  | 738.814     |
|  2 | test       | EGFR           | pearsonr            |   0.301939  |
|  3 | test       | EGFR           | mean_absolute_error |  21.4966    |
|  4 | test       | EGFR           | r2                  |   0.0830938 |
|  5 | test       | EGFR           | explained_var       |   0.0868411 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.490499 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.379288 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.578267 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.417179 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.300437 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.326368 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.872174 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.486999 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.702934 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.556152 |
|  4 | test       | LOG_RPPB       | r2                  | 0.451875 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.46977  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.733135 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.319164 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.75227  |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.467175 |
|  4 | test       | LOG_HPPB       | r2                  | 0.473013 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.56448  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.778303 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.191847 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.783875 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.312844 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.612737 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.613342 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.733888 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.276097 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.728151 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.412653 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.510938 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.516302 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.715756 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.201379 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.712397 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.352713 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.48153  |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.48197  |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.493553 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 10.5773 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.307409 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.669709 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | -0.239079 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.418882 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.230883 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.858261 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.619554 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.586201 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.623644 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.923687 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.389784 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.765538 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.885475 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.854816 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.791812 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7163410770902874,
    "polaris/pkis2-ret-wt-reg-v2": 1266.1856204926735,
    "polaris/pkis2-kit-wt-cls-v2": 0.5958070309636848,
    "polaris/pkis2-kit-wt-reg-v2": 1130.4970993368051,
    "polaris/pkis2-egfr-wt-reg-v2": 738.8141376456437,
    "polaris/adme-fang-solu-1": 0.5782666080492838,
    "polaris/adme-fang-rppb-1": 0.7029337751855126,
    "polaris/adme-fang-hppb-1": 0.752270089706317,
    "polaris/adme-fang-perm-1": 0.7838752761631055,
    "polaris/adme-fang-rclint-1": 0.7281510457503755,
    "polaris/adme-fang-hclint-1": 0.7123970059515434,
    "tdcommons/lipophilicity-astrazeneca": 0.49355294375508535,
    "tdcommons/ppbr-az": 10.577345024204424,
    "tdcommons/clearance-hepatocyte-az": 0.30740918748954443,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6697090313365345,
    "tdcommons/half-life-obach": -0.23907852284533956,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.41888232660977864,
    "tdcommons/clearance-microsome-az": 0.2308833556845446,
    "tdcommons/dili": 0.8582608695652174,
    "tdcommons/bioavailability-ma": 0.6195543731293648,
    "tdcommons/vdss-lombardo": 0.586200938457843,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6236437613019892,
    "tdcommons/pgp-broccatelli": 0.9236870167955212,
    "tdcommons/caco2-wang": 0.3897842759719681,
    "tdcommons/herg": 0.7655375552282768,
    "tdcommons/bbb-martins": 0.8854752970606629,
    "tdcommons/ames": 0.8548160332099708,
    "tdcommons/ld50-zhu": 0.7918124510477296
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | mcc         | 0.562567 |
|  1 | test       | CLS_RET        | accuracy    | 0.896226 |
|  2 | test       | CLS_RET        | f1          | 0.592593 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.537669 |
|  4 | test       | CLS_RET        | pr_auc      | 0.698874 |
|  5 | test       | CLS_RET        | roc_auc     | 0.902181 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | RET            | spearmanr           |    0.47094   |
|  1 | test       | RET            | mean_squared_error  | 1199.57      |
|  2 | test       | RET            | pearsonr            |    0.427914  |
|  3 | test       | RET            | mean_absolute_error |   25.1256    |
|  4 | test       | RET            | r2                  |   -0.0102462 |
|  5 | test       | RET            | explained_var       |    0.135802  |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | mcc         | 0.483492 |
|  1 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  2 | test       | CLS_KIT        | f1          | 0.564103 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.477754 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.668221 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.852998 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | spearmanr           |    0.415079 |
|  1 | test       | KIT            | mean_squared_error  | 1027.3      |
|  2 | test       | KIT            | pearsonr            |    0.413318 |
|  3 | test       | KIT            | mean_absolute_error |   26.2967   |
|  4 | test       | KIT            | r2                  |    0.148662 |
|  5 | test       | KIT            | explained_var       |    0.16755  |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.218731 |
|  1 | test       | EGFR           | mean_squared_error  | 753.24     |
|  2 | test       | EGFR           | pearsonr            |   0.358525 |
|  3 | test       | EGFR           | mean_absolute_error |  20.2993   |
|  4 | test       | EGFR           | r2                  |   0.065191 |
|  5 | test       | EGFR           | explained_var       |   0.121376 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.501597 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.388377 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.568968 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.428602 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.283673 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.299079 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.812174 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.480971 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.701704 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.553695 |
|  4 | test       | LOG_RPPB       | r2                  | 0.45866  |
|  5 | test       | LOG_RPPB       | explained_var       | 0.460684 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.680266 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.323696 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.717412 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.454707 |
|  4 | test       | LOG_HPPB       | r2                  | 0.465529 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.513509 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.790523 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.184951 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.794321 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.321175 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.626657 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.626667 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.732573 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.272109 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.727696 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.420065 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.518002 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.524592 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.705352 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.20635  |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.704613 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.353954 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.468731 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.468836 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.505892 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 10.1535 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.244352 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.659936 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.164637 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.367925 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.407977 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.887391 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.662454 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.603142 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.613924 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.902359 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.579499 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.782327 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.892042 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.857481 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.632142 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6988742588290531,
    "polaris/pkis2-ret-wt-reg-v2": 1199.57142577541,
    "polaris/pkis2-kit-wt-cls-v2": 0.6682207927305761,
    "polaris/pkis2-kit-wt-reg-v2": 1027.2955065638143,
    "polaris/pkis2-egfr-wt-reg-v2": 753.2395819651505,
    "polaris/adme-fang-solu-1": 0.5689684884920423,
    "polaris/adme-fang-rppb-1": 0.701704046637676,
    "polaris/adme-fang-hppb-1": 0.7174121669588354,
    "polaris/adme-fang-perm-1": 0.7943214828943682,
    "polaris/adme-fang-rclint-1": 0.7276959122124786,
    "polaris/adme-fang-hclint-1": 0.7046131033951475,
    "tdcommons/lipophilicity-astrazeneca": 0.5058922318670028,
    "tdcommons/ppbr-az": 10.153532873163924,
    "tdcommons/clearance-hepatocyte-az": 0.24435213942397913,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6599357238188415,
    "tdcommons/half-life-obach": 0.16463655669314392,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3679248145195101,
    "tdcommons/clearance-microsome-az": 0.4079770559474727,
    "tdcommons/dili": 0.8873913043478261,
    "tdcommons/bioavailability-ma": 0.662454273362155,
    "tdcommons/vdss-lombardo": 0.6031415665266907,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6139240506329114,
    "tdcommons/pgp-broccatelli": 0.9023593708344442,
    "tdcommons/caco2-wang": 0.5794993542581077,
    "tdcommons/herg": 0.7823269513991163,
    "tdcommons/bbb-martins": 0.8920419011882427,
    "tdcommons/ames": 0.8574810550431768,
    "tdcommons/ld50-zhu": 0.6321416836191416
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | mcc         | 0.562567 |
|  1 | test       | CLS_RET        | accuracy    | 0.896226 |
|  2 | test       | CLS_RET        | f1          | 0.592593 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.537669 |
|  4 | test       | CLS_RET        | pr_auc      | 0.717766 |
|  5 | test       | CLS_RET        | roc_auc     | 0.858559 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | RET            | spearmanr           |    0.545272  |
|  1 | test       | RET            | mean_squared_error  | 1251.06      |
|  2 | test       | RET            | pearsonr            |    0.433399  |
|  3 | test       | RET            | mean_absolute_error |   25.7843    |
|  4 | test       | RET            | r2                  |   -0.0536044 |
|  5 | test       | RET            | explained_var       |    0.0926744 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | mcc         | 0.535976 |
|  1 | test       | CLS_KIT        | accuracy    | 0.862069 |
|  2 | test       | CLS_KIT        | f1          | 0.619048 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.53507  |
|  4 | test       | CLS_KIT        | pr_auc      | 0.670391 |
|  5 | test       | CLS_KIT        | roc_auc     | 0.862186 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | spearmanr           |    0.366948 |
|  1 | test       | KIT            | mean_squared_error  | 1085.87     |
|  2 | test       | KIT            | pearsonr            |    0.384268 |
|  3 | test       | KIT            | mean_absolute_error |   27.2136   |
|  4 | test       | KIT            | r2                  |    0.100121 |
|  5 | test       | KIT            | explained_var       |    0.142356 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.253782 |
|  1 | test       | EGFR           | mean_squared_error  | 700.606    |
|  2 | test       | EGFR           | pearsonr            |   0.407328 |
|  3 | test       | EGFR           | mean_absolute_error |  20.1139   |
|  4 | test       | EGFR           | r2                  |   0.130512 |
|  5 | test       | EGFR           | explained_var       |   0.158411 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.514799 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.366863 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.597589 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.422301 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.323354 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.341474 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.864348 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.425334 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.762702 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.497845 |
|  4 | test       | LOG_RPPB       | r2                  | 0.52128  |
|  5 | test       | LOG_RPPB       | explained_var       | 0.523073 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.684239 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.316087 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.724922 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.47475  |
|  4 | test       | LOG_HPPB       | r2                  | 0.478093 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.513115 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.792484 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.181599 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.800469 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.306432 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.633425 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.63781  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.721153 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.296318 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.716282 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.429545 |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.475119 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.502508 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.72081  |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.203875 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.709592 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.354017 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.475103 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.475589 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.512099 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 10.3105 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.220427 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.660889 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.312763 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.348653 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.420157 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.861739 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.666445 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.588742 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.623418 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.919088 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.368575 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.779971 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.902908 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.539216 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.634623 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.7177664339332828,
    "polaris/pkis2-ret-wt-reg-v2": 1251.0552233308902,
    "polaris/pkis2-kit-wt-cls-v2": 0.6703907271416001,
    "polaris/pkis2-kit-wt-reg-v2": 1085.8697279717437,
    "polaris/pkis2-egfr-wt-reg-v2": 700.6063972838089,
    "polaris/adme-fang-solu-1": 0.597589101677514,
    "polaris/adme-fang-rppb-1": 0.7627019669397783,
    "polaris/adme-fang-hppb-1": 0.7249217659544267,
    "polaris/adme-fang-perm-1": 0.8004687350665166,
    "polaris/adme-fang-rclint-1": 0.7162816949708143,
    "polaris/adme-fang-hclint-1": 0.7095916945084295,
    "tdcommons/lipophilicity-astrazeneca": 0.5120986479584216,
    "tdcommons/ppbr-az": 10.310471324067635,
    "tdcommons/clearance-hepatocyte-az": 0.2204269262078558,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6608892691759787,
    "tdcommons/half-life-obach": 0.31276311557508946,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3486534162171543,
    "tdcommons/clearance-microsome-az": 0.42015673893396804,
    "tdcommons/dili": 0.8617391304347826,
    "tdcommons/bioavailability-ma": 0.666444961755903,
    "tdcommons/vdss-lombardo": 0.588741928699666,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6234177215189873,
    "tdcommons/pgp-broccatelli": 0.9190882431351639,
    "tdcommons/caco2-wang": 0.3685751035199846,
    "tdcommons/herg": 0.7799705449189985,
    "tdcommons/bbb-martins": 0.9029080675422139,
    "tdcommons/ames": 0.5392155710900937,
    "tdcommons/ld50-zhu": 0.6346225908918859
}
```
