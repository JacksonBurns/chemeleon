# ChemProp Baseline Results
timestamp: 2025-06-06 23:20:07.989092
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.642857 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.591365 |
|  2 | test       | CLS_RET        | mcc         | 0.609983 |
|  3 | test       | CLS_RET        | accuracy    | 0.90566  |
|  4 | test       | CLS_RET        | roc_auc     | 0.832122 |
|  5 | test       | CLS_RET        | pr_auc      | 0.657563 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.49856  |
|  1 | test       | RET            | r2                  |   0.204942 |
|  2 | test       | RET            | explained_var       |   0.257053 |
|  3 | test       | RET            | mean_absolute_error |  23.6621   |
|  4 | test       | RET            | pearsonr            |   0.54294  |
|  5 | test       | RET            | mean_squared_error  | 944.056    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.428571 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.302605 |
|  2 | test       | CLS_KIT        | mcc         | 0.303118 |
|  3 | test       | CLS_KIT        | accuracy    | 0.793103 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.737427 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.490613 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | spearmanr           |    0.333934  |
|  1 | test       | KIT            | r2                  |   -0.0631132 |
|  2 | test       | KIT            | explained_var       |   -0.0571691 |
|  3 | test       | KIT            | mean_absolute_error |   29.163     |
|  4 | test       | KIT            | pearsonr            |    0.36803   |
|  5 | test       | KIT            | mean_squared_error  | 1282.84      |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.424573 |
|  1 | test       | EGFR           | r2                  |   0.378191 |
|  2 | test       | EGFR           | explained_var       |   0.378322 |
|  3 | test       | EGFR           | mean_absolute_error |  17.5655   |
|  4 | test       | EGFR           | pearsonr            |   0.630163 |
|  5 | test       | EGFR           | mean_squared_error  | 501.034    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.471513 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.347773 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.349057 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.420317 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.590899 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.353623 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.738261 |
|  1 | test       | LOG_RPPB       | r2                  | 0.44491  |
|  2 | test       | LOG_RPPB       | explained_var       | 0.454281 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.493664 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.676666 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.493188 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.809229 |
|  1 | test       | LOG_HPPB       | r2                  | 0.645561 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.646232 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.383932 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.807531 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.214662 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.751906 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.531752 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.547023 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.362228 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.739656 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.231967 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.673595 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.436636 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.438999 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.447797 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.668377 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.318043 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.634085 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.335721 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.336171 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.40034  |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.613046 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.258013 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.559718 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.16942 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.313868 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.676485 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.255893 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.365057 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.529936 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.865652 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.578317 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0740708 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.599684 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.914223 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.308849 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.819588 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.915963 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.833545 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.645132 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6575626297435373,
    "polaris/pkis2-ret-wt-reg-v2": 944.0557074100828,
    "polaris/pkis2-kit-wt-cls-v2": 0.4906133922513919,
    "polaris/pkis2-kit-wt-reg-v2": 1282.8417438100803,
    "polaris/pkis2-egfr-wt-reg-v2": 501.0337308111496,
    "polaris/adme-fang-solu-1": 0.5908993161443318,
    "polaris/adme-fang-rppb-1": 0.6766658258356164,
    "polaris/adme-fang-hppb-1": 0.807530720628163,
    "polaris/adme-fang-perm-1": 0.7396562793073957,
    "polaris/adme-fang-rclint-1": 0.6683768391483795,
    "polaris/adme-fang-hclint-1": 0.6130462577886803,
    "tdcommons/lipophilicity-astrazeneca": 0.5597181161301477,
    "tdcommons/ppbr-az": 9.1694166264679,
    "tdcommons/clearance-hepatocyte-az": 0.3138676591028712,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6764845895113879,
    "tdcommons/half-life-obach": 0.2558930828075622,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3650569674560604,
    "tdcommons/clearance-microsome-az": 0.5299357967994661,
    "tdcommons/dili": 0.8656521739130435,
    "tdcommons/bioavailability-ma": 0.5783172597273029,
    "tdcommons/vdss-lombardo": 0.07407083976754714,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5996835443037974,
    "tdcommons/pgp-broccatelli": 0.9142228739002932,
    "tdcommons/caco2-wang": 0.30884883802595875,
    "tdcommons/herg": 0.8195876288659794,
    "tdcommons/bbb-martins": 0.9159631019387118,
    "tdcommons/ames": 0.8335448119211263,
    "tdcommons/ld50-zhu": 0.6451317310913973
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.592593 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.537669 |
|  2 | test       | CLS_RET        | mcc         | 0.562567 |
|  3 | test       | CLS_RET        | accuracy    | 0.896226 |
|  4 | test       | CLS_RET        | roc_auc     | 0.814937 |
|  5 | test       | CLS_RET        | pr_auc      | 0.646496 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.557968 |
|  1 | test       | RET            | r2                  |   0.288536 |
|  2 | test       | RET            | explained_var       |   0.333515 |
|  3 | test       | RET            | mean_absolute_error |  21.2012   |
|  4 | test       | RET            | pearsonr            |   0.580946 |
|  5 | test       | RET            | mean_squared_error  | 844.796    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.428571 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.302605 |
|  2 | test       | CLS_KIT        | mcc         | 0.303118 |
|  3 | test       | CLS_KIT        | accuracy    | 0.793103 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.755803 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.411204 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | spearmanr           |    0.399019  |
|  1 | test       | KIT            | r2                  |   -0.0222145 |
|  2 | test       | KIT            | explained_var       |   -0.0161092 |
|  3 | test       | KIT            | mean_absolute_error |   28.0812    |
|  4 | test       | KIT            | pearsonr            |    0.396526  |
|  5 | test       | KIT            | mean_squared_error  | 1233.49      |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.389518 |
|  1 | test       | EGFR           | r2                  |   0.348821 |
|  2 | test       | EGFR           | explained_var       |   0.37779  |
|  3 | test       | EGFR           | mean_absolute_error |  18.5595   |
|  4 | test       | EGFR           | pearsonr            |   0.619641 |
|  5 | test       | EGFR           | mean_squared_error  | 524.7      |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.494626 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.306311 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.306314 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.433419 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.580667 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.376103 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.766957 |
|  1 | test       | LOG_RPPB       | r2                  | 0.544943 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.566594 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.501699 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.82439  |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.40431  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.661624 |
|  1 | test       | LOG_HPPB       | r2                  | 0.259334 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.431041 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.550326 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.67312  |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.448576 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.750269 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.548359 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.548794 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.364696 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.746625 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.22374  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.674955 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.441166 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.449326 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.445414 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.671969 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.315486 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.644231 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.347938 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.347955 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.396177 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.629965 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.253267 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.531983 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.96271 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.292936 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.640836 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.331422 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.36057 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.436793 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.867826 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.526438 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.311445 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.637206 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.909291 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.31773 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.826362 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.919168 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.835221 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.631425 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6464961939351923,
    "polaris/pkis2-ret-wt-reg-v2": 844.7955654153885,
    "polaris/pkis2-kit-wt-cls-v2": 0.4112037647991453,
    "polaris/pkis2-kit-wt-reg-v2": 1233.4899856638733,
    "polaris/pkis2-egfr-wt-reg-v2": 524.6998631506724,
    "polaris/adme-fang-solu-1": 0.5806667278795618,
    "polaris/adme-fang-rppb-1": 0.8243895462964138,
    "polaris/adme-fang-hppb-1": 0.6731196063519949,
    "polaris/adme-fang-perm-1": 0.746625299624559,
    "polaris/adme-fang-rclint-1": 0.6719692376705009,
    "polaris/adme-fang-hclint-1": 0.6299651590412755,
    "tdcommons/lipophilicity-astrazeneca": 0.5319826101859411,
    "tdcommons/ppbr-az": 8.962711855593223,
    "tdcommons/clearance-hepatocyte-az": 0.2929359811427562,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6408358289061187,
    "tdcommons/half-life-obach": 0.3314219253336458,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3605698740037232,
    "tdcommons/clearance-microsome-az": 0.4367926667707861,
    "tdcommons/dili": 0.8678260869565217,
    "tdcommons/bioavailability-ma": 0.5264383106085799,
    "tdcommons/vdss-lombardo": 0.31144499588102836,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6372061482820975,
    "tdcommons/pgp-broccatelli": 0.9092908557717942,
    "tdcommons/caco2-wang": 0.317729504703329,
    "tdcommons/herg": 0.8263622974963181,
    "tdcommons/bbb-martins": 0.91916823014384,
    "tdcommons/ames": 0.835220975542893,
    "tdcommons/ld50-zhu": 0.6314253254949804
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0        |
|  1 | test       | CLS_RET        | cohen_kappa | 0        |
|  2 | test       | CLS_RET        | mcc         | 0        |
|  3 | test       | CLS_RET        | accuracy    | 0.839623 |
|  4 | test       | CLS_RET        | roc_auc     | 0.780568 |
|  5 | test       | CLS_RET        | pr_auc      | 0.526503 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | RET            | spearmanr           |    0.534787 |
|  1 | test       | RET            | r2                  |    0.145591 |
|  2 | test       | RET            | explained_var       |    0.253747 |
|  3 | test       | RET            | mean_absolute_error |   23.7839   |
|  4 | test       | RET            | pearsonr            |    0.539026 |
|  5 | test       | RET            | mean_squared_error  | 1014.53     |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.341463 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.20102  |
|  2 | test       | CLS_KIT        | mcc         | 0.201817 |
|  3 | test       | CLS_KIT        | accuracy    | 0.767241 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.729691 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.43901  |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | spearmanr           |    0.46365  |
|  1 | test       | KIT            | r2                  |    0.161035 |
|  2 | test       | KIT            | explained_var       |    0.161038 |
|  3 | test       | KIT            | mean_absolute_error |   25.2607   |
|  4 | test       | KIT            | pearsonr            |    0.48621  |
|  5 | test       | KIT            | mean_squared_error  | 1012.37     |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.365777 |
|  1 | test       | EGFR           | r2                  |   0.381289 |
|  2 | test       | EGFR           | explained_var       |   0.385749 |
|  3 | test       | EGFR           | mean_absolute_error |  17.9741   |
|  4 | test       | EGFR           | pearsonr            |   0.626833 |
|  5 | test       | EGFR           | mean_squared_error  | 498.537    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.444146 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.272532 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.279603 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.434351 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.533309 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.394418 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.854783 |
|  1 | test       | LOG_RPPB       | r2                  | 0.612661 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.623774 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.414436 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.791468 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.344144 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.733287 |
|  1 | test       | LOG_HPPB       | r2                  | 0.460907 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.540533 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.455446 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.750506 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.326496 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.714207 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.504283 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.504383 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.380315 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.72238  |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.245574 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.683337 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.45059  |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.450593 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.43806  |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.67474  |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.310166 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.639011 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.374825 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.381944 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.395549 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.627164 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.242824 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.54709 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.68653 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.294197 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.661878 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.227419 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.423355 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.477538 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.861739 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.602594 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.328488 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.616863 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.902893 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.312815 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.830781 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.917487 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.831504 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.651671 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5265029090746984,
    "polaris/pkis2-ret-wt-reg-v2": 1014.5300901803994,
    "polaris/pkis2-kit-wt-cls-v2": 0.43900992753147683,
    "polaris/pkis2-kit-wt-reg-v2": 1012.3661100056662,
    "polaris/pkis2-egfr-wt-reg-v2": 498.5374788359469,
    "polaris/adme-fang-solu-1": 0.5333088441112769,
    "polaris/adme-fang-rppb-1": 0.7914676605322,
    "polaris/adme-fang-hppb-1": 0.7505055920117528,
    "polaris/adme-fang-perm-1": 0.7223804038743578,
    "polaris/adme-fang-rclint-1": 0.6747403314867202,
    "polaris/adme-fang-hclint-1": 0.6271636252902889,
    "tdcommons/lipophilicity-astrazeneca": 0.547089942250933,
    "tdcommons/ppbr-az": 8.686528802643096,
    "tdcommons/clearance-hepatocyte-az": 0.29419654318785643,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6618779055488319,
    "tdcommons/half-life-obach": 0.2274194604894319,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4233549152761465,
    "tdcommons/clearance-microsome-az": 0.47753799274095415,
    "tdcommons/dili": 0.8617391304347826,
    "tdcommons/bioavailability-ma": 0.6025939474559361,
    "tdcommons/vdss-lombardo": 0.3284875308013125,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6168625678119349,
    "tdcommons/pgp-broccatelli": 0.9028925619834711,
    "tdcommons/caco2-wang": 0.31281536704893015,
    "tdcommons/herg": 0.8307805596465391,
    "tdcommons/bbb-martins": 0.917487492182614,
    "tdcommons/ames": 0.8315044351759385,
    "tdcommons/ld50-zhu": 0.651671135635918
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.32     |
|  1 | test       | CLS_RET        | cohen_kappa | 0.24222  |
|  2 | test       | CLS_RET        | mcc         | 0.264433 |
|  3 | test       | CLS_RET        | accuracy    | 0.839623 |
|  4 | test       | CLS_RET        | roc_auc     | 0.806345 |
|  5 | test       | CLS_RET        | pr_auc      | 0.521025 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.50987  |
|  1 | test       | RET            | r2                  |   0.229074 |
|  2 | test       | RET            | explained_var       |   0.250689 |
|  3 | test       | RET            | mean_absolute_error |  23.0421   |
|  4 | test       | RET            | pearsonr            |   0.547367 |
|  5 | test       | RET            | mean_squared_error  | 915.402    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.418605 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.286417 |
|  2 | test       | CLS_KIT        | mcc         | 0.286534 |
|  3 | test       | CLS_KIT        | accuracy    | 0.784483 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.77176  |
|  5 | test       | CLS_KIT        | pr_auc      | 0.447963 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | spearmanr           |    0.46931  |
|  1 | test       | KIT            | r2                  |    0.152811 |
|  2 | test       | KIT            | explained_var       |    0.172464 |
|  3 | test       | KIT            | mean_absolute_error |   24.5044   |
|  4 | test       | KIT            | pearsonr            |    0.486044 |
|  5 | test       | KIT            | mean_squared_error  | 1022.29     |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.346987 |
|  1 | test       | EGFR           | r2                  |   0.362041 |
|  2 | test       | EGFR           | explained_var       |   0.368602 |
|  3 | test       | EGFR           | mean_absolute_error |  17.7872   |
|  4 | test       | EGFR           | pearsonr            |   0.619606 |
|  5 | test       | EGFR           | mean_squared_error  | 514.047    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.373005 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.232023 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.246314 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.441235 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.506288 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.416381 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.8      |
|  1 | test       | LOG_RPPB       | r2                  | 0.629761 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.629879 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.450087 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.802899 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.328951 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.817633 |
|  1 | test       | LOG_HPPB       | r2                  | 0.5868   |
|  2 | test       | LOG_HPPB       | explained_var       | 0.680301 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.418857 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.833032 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.25025  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.718569 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.512835 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.513146 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.382153 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.718657 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.241338 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.665423 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.43205  |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.436056 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.454741 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.663381 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.320632 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.642926 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.371542 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.375222 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.389693 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.623864 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.244099 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.557135 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.75774 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.338162 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.631478 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.216578 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.362154 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.442396 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.866087 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.641171 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.119758 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.632911 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.908158 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.305016 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.811929 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.917722 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.839423 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.674936 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5210247774791268,
    "polaris/pkis2-ret-wt-reg-v2": 915.4019307399365,
    "polaris/pkis2-kit-wt-cls-v2": 0.4479626883623749,
    "polaris/pkis2-kit-wt-reg-v2": 1022.2889988195308,
    "polaris/pkis2-egfr-wt-reg-v2": 514.0470815519745,
    "polaris/adme-fang-solu-1": 0.5062879573281891,
    "polaris/adme-fang-rppb-1": 0.8028992996530686,
    "polaris/adme-fang-hppb-1": 0.8330320018497795,
    "polaris/adme-fang-perm-1": 0.7186569683087568,
    "polaris/adme-fang-rclint-1": 0.6633807919306963,
    "polaris/adme-fang-hclint-1": 0.623864399607601,
    "tdcommons/lipophilicity-astrazeneca": 0.5571348857652573,
    "tdcommons/ppbr-az": 8.757737235681743,
    "tdcommons/clearance-hepatocyte-az": 0.33816195389943804,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6314781129294593,
    "tdcommons/half-life-obach": 0.21657782512845117,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.36215381592327506,
    "tdcommons/clearance-microsome-az": 0.44239649124855046,
    "tdcommons/dili": 0.8660869565217391,
    "tdcommons/bioavailability-ma": 0.6411706019288328,
    "tdcommons/vdss-lombardo": 0.11975777442622772,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6329113924050632,
    "tdcommons/pgp-broccatelli": 0.908157824580112,
    "tdcommons/caco2-wang": 0.3050161668455859,
    "tdcommons/herg": 0.8119293078055965,
    "tdcommons/bbb-martins": 0.9177220137585991,
    "tdcommons/ames": 0.8394231334077424,
    "tdcommons/ld50-zhu": 0.674936410336759
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.642857 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.591365 |
|  2 | test       | CLS_RET        | mcc         | 0.609983 |
|  3 | test       | CLS_RET        | accuracy    | 0.90566  |
|  4 | test       | CLS_RET        | roc_auc     | 0.864508 |
|  5 | test       | CLS_RET        | pr_auc      | 0.696713 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.548724 |
|  1 | test       | RET            | r2                  |   0.28739  |
|  2 | test       | RET            | explained_var       |   0.342846 |
|  3 | test       | RET            | mean_absolute_error |  22.2406   |
|  4 | test       | RET            | pearsonr            |   0.601246 |
|  5 | test       | RET            | mean_squared_error  | 846.157    |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.408163 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.251779 |
|  2 | test       | CLS_KIT        | mcc         | 0.253901 |
|  3 | test       | CLS_KIT        | accuracy    | 0.75     |
|  4 | test       | CLS_KIT        | roc_auc     | 0.734526 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.42218  |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | spearmanr           |    0.407365  |
|  1 | test       | KIT            | r2                  |    0.0938868 |
|  2 | test       | KIT            | explained_var       |    0.0994629 |
|  3 | test       | KIT            | mean_absolute_error |   26.5213    |
|  4 | test       | KIT            | pearsonr            |    0.4312    |
|  5 | test       | KIT            | mean_squared_error  | 1093.39      |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.350586 |
|  1 | test       | EGFR           | r2                  |   0.233136 |
|  2 | test       | EGFR           | explained_var       |   0.233212 |
|  3 | test       | EGFR           | mean_absolute_error |  19.3031   |
|  4 | test       | EGFR           | pearsonr            |   0.533956 |
|  5 | test       | EGFR           | mean_squared_error  | 617.915    |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.532715 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.362727 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.365498 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.418699 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.606469 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.345516 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.853043 |
|  1 | test       | LOG_RPPB       | r2                  | 0.528585 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.530378 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.456464 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.730235 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.418844 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.792421 |
|  1 | test       | LOG_HPPB       | r2                  | 0.626369 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.676714 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.403098 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.823341 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.226285 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.713259 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.514577 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.514577 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.382677 |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.717353 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.240475 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.668143 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.437859 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.438595 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.450805 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.668873 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.317353 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.650254 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.381798 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.387146 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.390076 |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.630894 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.240116 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.537453 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.62976 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.293177 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.605958 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.213467 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.318231 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.438363 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.856087 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.530096 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0477536 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.596293 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.920021 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.361099 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.81134 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.906113 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.828205 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.639796 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6967128833524808,
    "polaris/pkis2-ret-wt-reg-v2": 846.1566363499628,
    "polaris/pkis2-kit-wt-cls-v2": 0.42217991689633655,
    "polaris/pkis2-kit-wt-reg-v2": 1093.392317844313,
    "polaris/pkis2-egfr-wt-reg-v2": 617.9149489871204,
    "polaris/adme-fang-solu-1": 0.6064689261371241,
    "polaris/adme-fang-rppb-1": 0.730234754765895,
    "polaris/adme-fang-hppb-1": 0.8233412111283326,
    "polaris/adme-fang-perm-1": 0.7173534775840057,
    "polaris/adme-fang-rclint-1": 0.6688726587595071,
    "polaris/adme-fang-hclint-1": 0.6308943018613449,
    "tdcommons/lipophilicity-astrazeneca": 0.5374525668734597,
    "tdcommons/ppbr-az": 8.629759540591982,
    "tdcommons/clearance-hepatocyte-az": 0.29317706491907836,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6059576580570296,
    "tdcommons/half-life-obach": 0.21346653987828082,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.31823095089786146,
    "tdcommons/clearance-microsome-az": 0.43836348739943765,
    "tdcommons/dili": 0.8560869565217392,
    "tdcommons/bioavailability-ma": 0.5300964416361822,
    "tdcommons/vdss-lombardo": 0.04775355096063739,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5962929475587704,
    "tdcommons/pgp-broccatelli": 0.920021327645961,
    "tdcommons/caco2-wang": 0.36109856261366974,
    "tdcommons/herg": 0.811340206185567,
    "tdcommons/bbb-martins": 0.9061131957473421,
    "tdcommons/ames": 0.8282049775793534,
    "tdcommons/ld50-zhu": 0.6397963591654343
}
```
