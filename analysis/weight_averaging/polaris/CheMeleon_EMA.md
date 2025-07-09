# ChemProp Baseline Results
timestamp: 2025-07-08 22:31:25.505072
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |     Score |
|---:|:-----------|:---------------|:------------|----------:|
|  0 | test       | CLS_RET        | accuracy    | 0.839623  |
|  1 | test       | CLS_RET        | mcc         | 0.128346  |
|  2 | test       | CLS_RET        | f1          | 0.105263  |
|  3 | test       | CLS_RET        | cohen_kappa | 0.0739979 |
|  4 | test       | CLS_RET        | roc_auc     | 0.793126  |
|  5 | test       | CLS_RET        | pr_auc      | 0.517357  |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  19.8241   |
|  1 | test       | RET            | spearmanr           |   0.631202 |
|  2 | test       | RET            | explained_var       |   0.466742 |
|  3 | test       | RET            | r2                  |   0.462691 |
|  4 | test       | RET            | mean_squared_error  | 638.004    |
|  5 | test       | RET            | pearsonr            |   0.693544 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.913793 |
|  1 | test       | CLS_KIT        | mcc         | 0.6983   |
|  2 | test       | CLS_KIT        | f1          | 0.722222 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.674157 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.838491 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.727105 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  22.0128   |
|  1 | test       | KIT            | spearmanr           |   0.540978 |
|  2 | test       | KIT            | explained_var       |   0.310993 |
|  3 | test       | KIT            | r2                  |   0.308552 |
|  4 | test       | KIT            | mean_squared_error  | 834.36     |
|  5 | test       | KIT            | pearsonr            |   0.588403 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  17.4547   |
|  1 | test       | EGFR           | spearmanr           |   0.324115 |
|  2 | test       | EGFR           | explained_var       |   0.37467  |
|  3 | test       | EGFR           | r2                  |   0.374635 |
|  4 | test       | EGFR           | mean_squared_error  | 503.899    |
|  5 | test       | EGFR           | pearsonr            |   0.637052 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.397306 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.494694 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.36549  |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.347432 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.353808 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.622287 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.613875 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.705217 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.338907 |
|  3 | test       | LOG_RPPB       | r2                  | 0.324435 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.600228 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.62397  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.540296 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.707923 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.489982 |
|  3 | test       | LOG_HPPB       | r2                  | 0.404645 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.36057  |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.715425 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.360505 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.768882 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.612306 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.557479 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.219222 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.784926 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.425253 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.713347 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.50672  |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.506473 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.278618 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.712843 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.373197 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.683737 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.463003 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.461343 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.20922  |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.680591 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.508442 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.29077 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.372517 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.613947 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.229985 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.409979 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.551189 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.895217 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.581643 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.441049 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.599231 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.932218 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.282976 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.808542 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.884498 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.845047 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.544739 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5173569418821493,
    "polaris/pkis2-ret-wt-reg-v2": 638.0039270674231,
    "polaris/pkis2-kit-wt-cls-v2": 0.7271047650456173,
    "polaris/pkis2-kit-wt-reg-v2": 834.3595109139271,
    "polaris/pkis2-egfr-wt-reg-v2": 503.8994940236783,
    "polaris/adme-fang-solu-1": 0.6222866582782323,
    "polaris/adme-fang-rppb-1": 0.6239703222357098,
    "polaris/adme-fang-hppb-1": 0.7154249903803566,
    "polaris/adme-fang-perm-1": 0.7849255452797055,
    "polaris/adme-fang-rclint-1": 0.7128425745991599,
    "polaris/adme-fang-hclint-1": 0.6805910074483921,
    "tdcommons/lipophilicity-astrazeneca": 0.5084421414591017,
    "tdcommons/ppbr-az": 8.290774697455609,
    "tdcommons/clearance-hepatocyte-az": 0.3725168355247644,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.613947265951327,
    "tdcommons/half-life-obach": 0.2299853548425819,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4099788453701136,
    "tdcommons/clearance-microsome-az": 0.5511893123649204,
    "tdcommons/dili": 0.8952173913043479,
    "tdcommons/bioavailability-ma": 0.5816428333887596,
    "tdcommons/vdss-lombardo": 0.44104929414860045,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5992314647377939,
    "tdcommons/pgp-broccatelli": 0.932218075179952,
    "tdcommons/caco2-wang": 0.2829756553165143,
    "tdcommons/herg": 0.8085419734904271,
    "tdcommons/bbb-martins": 0.8844981238273921,
    "tdcommons/ames": 0.8450468973349782,
    "tdcommons/ld50-zhu": 0.5447391518572187
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.839623 |
|  1 | test       | CLS_RET        | mcc         | 0        |
|  2 | test       | CLS_RET        | f1          | 0        |
|  3 | test       | CLS_RET        | cohen_kappa | 0        |
|  4 | test       | CLS_RET        | roc_auc     | 0.771315 |
|  5 | test       | CLS_RET        | pr_auc      | 0.395112 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  20.7132   |
|  1 | test       | RET            | spearmanr           |   0.633308 |
|  2 | test       | RET            | explained_var       |   0.388644 |
|  3 | test       | RET            | r2                  |   0.311757 |
|  4 | test       | RET            | mean_squared_error  | 817.223    |
|  5 | test       | RET            | pearsonr            |   0.657563 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.87931  |
|  1 | test       | CLS_KIT        | mcc         | 0.571739 |
|  2 | test       | CLS_KIT        | f1          | 0.631579 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.561555 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.859768 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.757732 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  22.1143   |
|  1 | test       | KIT            | spearmanr           |   0.543433 |
|  2 | test       | KIT            | explained_var       |   0.348676 |
|  3 | test       | KIT            | r2                  |   0.346933 |
|  4 | test       | KIT            | mean_squared_error  | 788.045    |
|  5 | test       | KIT            | pearsonr            |   0.595044 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  16.8635   |
|  1 | test       | EGFR           | spearmanr           |   0.29679  |
|  2 | test       | EGFR           | explained_var       |   0.424121 |
|  3 | test       | EGFR           | r2                  |   0.423971 |
|  4 | test       | EGFR           | mean_squared_error  | 464.146    |
|  5 | test       | EGFR           | pearsonr            |   0.654706 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.414981 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.533014 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.409767 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.391898 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.3297   |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.641588 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.665069 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.807826 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.487195 |
|  3 | test       | LOG_RPPB       | r2                  | 0.323643 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.600931 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.764046 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.525727 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.744289 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.521817 |
|  3 | test       | LOG_HPPB       | r2                  | 0.394281 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.366847 |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.727995 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.343119 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.760563 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.604354 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.585787 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.205198 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.777708 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.412689 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.738977 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.543232 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.53065  |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.264968 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.737775 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.365299 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.683766 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.462054 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.441939 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.216756 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.681481 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.565693 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.89397 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.400086 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.674953 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.351382 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.415255 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.57165 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.921304 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.616229 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.564259 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.653255 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.925153 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.349203 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.830191 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.911664 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.85136 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.627612 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.39511225876056916,
    "polaris/pkis2-ret-wt-reg-v2": 817.2232521542079,
    "polaris/pkis2-kit-wt-cls-v2": 0.757732367969562,
    "polaris/pkis2-kit-wt-reg-v2": 788.0453663663341,
    "polaris/pkis2-egfr-wt-reg-v2": 464.1462357925399,
    "polaris/adme-fang-solu-1": 0.6415881110070725,
    "polaris/adme-fang-rppb-1": 0.7640464976471348,
    "polaris/adme-fang-hppb-1": 0.7279947213933856,
    "polaris/adme-fang-perm-1": 0.7777082402150535,
    "polaris/adme-fang-rclint-1": 0.7377749130943696,
    "polaris/adme-fang-hclint-1": 0.6814805071603485,
    "tdcommons/lipophilicity-astrazeneca": 0.5656928986878622,
    "tdcommons/ppbr-az": 7.893973622057646,
    "tdcommons/clearance-hepatocyte-az": 0.4000856246922052,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6749534804970311,
    "tdcommons/half-life-obach": 0.35138240212868616,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4152552695442913,
    "tdcommons/clearance-microsome-az": 0.571649748148242,
    "tdcommons/dili": 0.921304347826087,
    "tdcommons/bioavailability-ma": 0.6162287994679082,
    "tdcommons/vdss-lombardo": 0.5642593454473982,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.653254972875226,
    "tdcommons/pgp-broccatelli": 0.9251532924553452,
    "tdcommons/caco2-wang": 0.34920319242215014,
    "tdcommons/herg": 0.8301914580265096,
    "tdcommons/bbb-martins": 0.9116635397123201,
    "tdcommons/ames": 0.8513599248076134,
    "tdcommons/ld50-zhu": 0.627612062518103
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.839623 |
|  1 | test       | CLS_RET        | mcc         | 0        |
|  2 | test       | CLS_RET        | f1          | 0        |
|  3 | test       | CLS_RET        | cohen_kappa | 0        |
|  4 | test       | CLS_RET        | roc_auc     | 0.798414 |
|  5 | test       | CLS_RET        | pr_auc      | 0.483333 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  20.7965   |
|  1 | test       | RET            | spearmanr           |   0.606786 |
|  2 | test       | RET            | explained_var       |   0.421925 |
|  3 | test       | RET            | r2                  |   0.421598 |
|  4 | test       | RET            | mean_squared_error  | 686.797    |
|  5 | test       | RET            | pearsonr            |   0.650282 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.810345 |
|  1 | test       | CLS_KIT        | mcc         | 0        |
|  2 | test       | CLS_KIT        | f1          | 0        |
|  3 | test       | CLS_KIT        | cohen_kappa | 0        |
|  4 | test       | CLS_KIT        | roc_auc     | 0.834139 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.586476 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  20.8942   |
|  1 | test       | KIT            | spearmanr           |   0.579955 |
|  2 | test       | KIT            | explained_var       |   0.381222 |
|  3 | test       | KIT            | r2                  |   0.36059  |
|  4 | test       | KIT            | mean_squared_error  | 771.566    |
|  5 | test       | KIT            | pearsonr            |   0.621932 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  18.6261   |
|  1 | test       | EGFR           | spearmanr           |   0.305446 |
|  2 | test       | EGFR           | explained_var       |   0.301444 |
|  3 | test       | EGFR           | r2                  |   0.294212 |
|  4 | test       | EGFR           | mean_squared_error  | 568.702    |
|  5 | test       | EGFR           | pearsonr            |   0.640483 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.397217 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.482502 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.362872 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.362844 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.345453 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.607176 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.542652 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.842609 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.50288  |
|  3 | test       | LOG_RPPB       | r2                  | 0.497941 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.446071 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.85025  |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.496979 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.724119 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.485838 |
|  3 | test       | LOG_HPPB       | r2                  | 0.469493 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.321296 |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.72073  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.332204 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.758819 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.587518 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.583809 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.206178 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.77153  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.439509 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.719633 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.516408 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.461036 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.304269 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.718826 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.355855 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.698715 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.482887 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.469462 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.206066 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.698662 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.534155 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.72825 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.368858 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.67368 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.316992 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.442391 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.595142 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  |    0.88 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.588959 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.540841 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.581374 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.935884 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.313274 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.851988 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.900915 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.850787 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.560842 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.48333345318270204,
    "polaris/pkis2-ret-wt-reg-v2": 686.7973147241216,
    "polaris/pkis2-kit-wt-cls-v2": 0.586475812269197,
    "polaris/pkis2-kit-wt-reg-v2": 771.5657576517881,
    "polaris/pkis2-egfr-wt-reg-v2": 568.7017426032012,
    "polaris/adme-fang-solu-1": 0.607176095245121,
    "polaris/adme-fang-rppb-1": 0.8502500044548036,
    "polaris/adme-fang-hppb-1": 0.7207304404321446,
    "polaris/adme-fang-perm-1": 0.7715303755607277,
    "polaris/adme-fang-rclint-1": 0.7188264085016487,
    "polaris/adme-fang-hclint-1": 0.6986621866742166,
    "tdcommons/lipophilicity-astrazeneca": 0.5341545515571321,
    "tdcommons/ppbr-az": 7.72824849683185,
    "tdcommons/clearance-hepatocyte-az": 0.368858389206368,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6736797795409415,
    "tdcommons/half-life-obach": 0.31699161279464155,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.44239136022843306,
    "tdcommons/clearance-microsome-az": 0.5951416120959339,
    "tdcommons/dili": 0.88,
    "tdcommons/bioavailability-ma": 0.5889590954439641,
    "tdcommons/vdss-lombardo": 0.5408413419529834,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5813743218806511,
    "tdcommons/pgp-broccatelli": 0.9358837643295123,
    "tdcommons/caco2-wang": 0.3132743649334248,
    "tdcommons/herg": 0.8519882179675995,
    "tdcommons/bbb-martins": 0.9009146341463414,
    "tdcommons/ames": 0.8507871702990073,
    "tdcommons/ld50-zhu": 0.5608415686719634
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.839623 |
|  1 | test       | CLS_RET        | mcc         | 0        |
|  2 | test       | CLS_RET        | f1          | 0        |
|  3 | test       | CLS_RET        | cohen_kappa | 0        |
|  4 | test       | CLS_RET        | roc_auc     | 0.815598 |
|  5 | test       | CLS_RET        | pr_auc      | 0.542968 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  22.0145   |
|  1 | test       | RET            | spearmanr           |   0.570969 |
|  2 | test       | RET            | explained_var       |   0.371885 |
|  3 | test       | RET            | r2                  |   0.341633 |
|  4 | test       | RET            | mean_squared_error  | 781.748    |
|  5 | test       | RET            | pearsonr            |   0.655232 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.793103 |
|  1 | test       | CLS_KIT        | mcc         | 0.1967   |
|  2 | test       | CLS_KIT        | f1          | 0.294118 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.185012 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.675048 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.459615 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  21.5154   |
|  1 | test       | KIT            | spearmanr           |   0.576962 |
|  2 | test       | KIT            | explained_var       |   0.352206 |
|  3 | test       | KIT            | r2                  |   0.348275 |
|  4 | test       | KIT            | mean_squared_error  | 786.426    |
|  5 | test       | KIT            | pearsonr            |   0.615994 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  16.0886   |
|  1 | test       | EGFR           | spearmanr           |   0.417709 |
|  2 | test       | EGFR           | explained_var       |   0.426817 |
|  3 | test       | EGFR           | r2                  |   0.425118 |
|  4 | test       | EGFR           | mean_squared_error  | 463.222    |
|  5 | test       | EGFR           | pearsonr            |   0.6588   |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.401502 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.55933  |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.380177 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.378368 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.337036 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.635504 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.728276 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.770435 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.17514  |
|  3 | test       | LOG_RPPB       | r2                  | 0.161258 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.745207 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.702849 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error |  0.643082  |
|  1 | test       | LOG_HPPB       | spearmanr           |  0.677057  |
|  2 | test       | LOG_HPPB       | explained_var       |  0.382176  |
|  3 | test       | LOG_HPPB       | r2                  | -0.0125948 |
|  4 | test       | LOG_HPPB       | mean_squared_error  |  0.613267  |
|  5 | test       | LOG_HPPB       | pearsonr            |  0.709154  |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.326082 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.768996 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.608088 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.606521 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.194927 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.781001 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.421217 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.715741 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.51604  |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.512887 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.274996 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.718594 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.343586 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.722421 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.51132  |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.473093 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.204656 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.71508  |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.488752 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.10588 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.413887 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.580623 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.316833 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.417602 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.546394 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.918261 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.631526 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.535831 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.587025 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.895828 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.373067 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.856996 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.869411 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.850104 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.618841 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.5429675663702705,
    "polaris/pkis2-ret-wt-reg-v2": 781.7479393645797,
    "polaris/pkis2-kit-wt-cls-v2": 0.4596148313384951,
    "polaris/pkis2-kit-wt-reg-v2": 786.4260302973075,
    "polaris/pkis2-egfr-wt-reg-v2": 463.22199533121903,
    "polaris/adme-fang-solu-1": 0.6355042399391314,
    "polaris/adme-fang-rppb-1": 0.7028493320703773,
    "polaris/adme-fang-hppb-1": 0.7091542091737802,
    "polaris/adme-fang-perm-1": 0.7810014717073027,
    "polaris/adme-fang-rclint-1": 0.7185936930883674,
    "polaris/adme-fang-hclint-1": 0.7150796469960252,
    "tdcommons/lipophilicity-astrazeneca": 0.48875171710195997,
    "tdcommons/ppbr-az": 9.105880717924116,
    "tdcommons/clearance-hepatocyte-az": 0.4138872353707527,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5806234170313845,
    "tdcommons/half-life-obach": 0.3168330736948746,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.41760177656549125,
    "tdcommons/clearance-microsome-az": 0.5463944747136298,
    "tdcommons/dili": 0.9182608695652174,
    "tdcommons/bioavailability-ma": 0.6315264383106085,
    "tdcommons/vdss-lombardo": 0.5358313544501089,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5870253164556961,
    "tdcommons/pgp-broccatelli": 0.8958277792588644,
    "tdcommons/caco2-wang": 0.37306747946713625,
    "tdcommons/herg": 0.8569955817378497,
    "tdcommons/bbb-martins": 0.869410569105691,
    "tdcommons/ames": 0.8501037811588243,
    "tdcommons/ld50-zhu": 0.6188407790167244
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.839623 |
|  1 | test       | CLS_RET        | mcc         | 0        |
|  2 | test       | CLS_RET        | f1          | 0        |
|  3 | test       | CLS_RET        | cohen_kappa | 0        |
|  4 | test       | CLS_RET        | roc_auc     | 0.747521 |
|  5 | test       | CLS_RET        | pr_auc      | 0.38472  |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  21.6108   |
|  1 | test       | RET            | spearmanr           |   0.566924 |
|  2 | test       | RET            | explained_var       |   0.369607 |
|  3 | test       | RET            | r2                  |   0.328271 |
|  4 | test       | RET            | mean_squared_error  | 797.615    |
|  5 | test       | RET            | pearsonr            |   0.616177 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.844828 |
|  1 | test       | CLS_KIT        | mcc         | 0.568    |
|  2 | test       | CLS_KIT        | f1          | 0.653846 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.556876 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.885397 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.69425  |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  20.6072   |
|  1 | test       | KIT            | spearmanr           |   0.563087 |
|  2 | test       | KIT            | explained_var       |   0.387792 |
|  3 | test       | KIT            | r2                  |   0.372169 |
|  4 | test       | KIT            | mean_squared_error  | 757.594    |
|  5 | test       | KIT            | pearsonr            |   0.630161 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  18.6655   |
|  1 | test       | EGFR           | spearmanr           |   0.245409 |
|  2 | test       | EGFR           | explained_var       |   0.286294 |
|  3 | test       | EGFR           | r2                  |   0.283888 |
|  4 | test       | EGFR           | mean_squared_error  | 577.021    |
|  5 | test       | EGFR           | pearsonr            |   0.572697 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.377527 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.528338 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.41322  |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.40097  |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.324781 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.644798 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.710938 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.721739 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.387742 |
|  3 | test       | LOG_RPPB       | r2                  | 0.248432 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.667754 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.656348 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.543155 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.729467 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.452916 |
|  3 | test       | LOG_HPPB       | r2                  | 0.385169 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.372366 |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.707935 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.340154 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.764969 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.601907 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.595778 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.200249 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.77601  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.415843 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.737447 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.537843 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.529783 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.265458 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.734868 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.366953 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.684142 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.455709 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.455519 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.211482 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.675068 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.527198 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.69251 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.350544 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.622247 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.231532 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.41975 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.59027 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.92913 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.610243 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.478804 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.633363 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.929819 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.351522 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.877025 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.900524 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.842852 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.594681 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.38471999082628794,
    "polaris/pkis2-ret-wt-reg-v2": 797.6149507732465,
    "polaris/pkis2-kit-wt-cls-v2": 0.6942497757130601,
    "polaris/pkis2-kit-wt-reg-v2": 757.5942342566427,
    "polaris/pkis2-egfr-wt-reg-v2": 577.020858415251,
    "polaris/adme-fang-solu-1": 0.6447979629541858,
    "polaris/adme-fang-rppb-1": 0.6563478412738681,
    "polaris/adme-fang-hppb-1": 0.7079352960377472,
    "polaris/adme-fang-perm-1": 0.7760103493612,
    "polaris/adme-fang-rclint-1": 0.7348684265520402,
    "polaris/adme-fang-hclint-1": 0.675068364364872,
    "tdcommons/lipophilicity-astrazeneca": 0.5271983683506648,
    "tdcommons/ppbr-az": 7.692509471913783,
    "tdcommons/clearance-hepatocyte-az": 0.35054434691435626,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6222471204538299,
    "tdcommons/half-life-obach": 0.23153172083107726,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.41975005970142343,
    "tdcommons/clearance-microsome-az": 0.5902700797665716,
    "tdcommons/dili": 0.9291304347826087,
    "tdcommons/bioavailability-ma": 0.6102427668772863,
    "tdcommons/vdss-lombardo": 0.4788037908655082,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6333634719710669,
    "tdcommons/pgp-broccatelli": 0.9298187150093308,
    "tdcommons/caco2-wang": 0.35152159763435115,
    "tdcommons/herg": 0.8770250368188512,
    "tdcommons/bbb-martins": 0.9005237648530331,
    "tdcommons/ames": 0.8428518279190897,
    "tdcommons/ld50-zhu": 0.5946809005059795
}
```
