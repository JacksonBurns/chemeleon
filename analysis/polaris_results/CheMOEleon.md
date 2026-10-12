# CheMOEleon Results
timestamp: 2026-10-10 16:07:25.363474
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.34067  |
|  1 | test       | CLS_RET        | accuracy    | 0.877358 |
|  2 | test       | CLS_RET        | f1          | 0.380952 |
|  3 | test       | CLS_RET        | mcc         | 0.453107 |
|  4 | test       | CLS_RET        | roc_auc     | 0.844679 |
|  5 | test       | CLS_RET        | pr_auc      | 0.693885 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.607287 |
|  1 | test       | RET            | mean_squared_error  | 736.773    |
|  2 | test       | RET            | pearsonr            |   0.646548 |
|  3 | test       | RET            | r2                  |   0.37951  |
|  4 | test       | RET            | mean_absolute_error |  20.7072   |
|  5 | test       | RET            | explained_var       |   0.417962 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.290954 |
|  1 | test       | CLS_KIT        | accuracy    | 0.827586 |
|  2 | test       | CLS_KIT        | f1          | 0.375    |
|  3 | test       | CLS_KIT        | mcc         | 0.321498 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.853482 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.589129 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.538684 |
|  1 | test       | KIT            | mean_squared_error  | 795.628    |
|  2 | test       | KIT            | pearsonr            |   0.592832 |
|  3 | test       | KIT            | r2                  |   0.34065  |
|  4 | test       | KIT            | mean_absolute_error |  22.6725   |
|  5 | test       | KIT            | explained_var       |   0.340661 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.371031 |
|  1 | test       | EGFR           | mean_squared_error  | 471.411    |
|  2 | test       | EGFR           | pearsonr            |   0.646451 |
|  3 | test       | EGFR           | r2                  |   0.414955 |
|  4 | test       | EGFR           | mean_absolute_error |  16.3378   |
|  5 | test       | EGFR           | explained_var       |   0.416423 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.502499 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.355368 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.592691 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.344556 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.419472 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.346139 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.612174 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.748755 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.474235 |
|  3 | test       | LOG_RPPB       | r2                  | 0.157264 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.667459 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.222882 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.745817 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.409655 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.655528 |
|  3 | test       | LOG_HPPB       | r2                  | 0.323599 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.57197  |
|  5 | test       | LOG_HPPB       | explained_var       | 0.385346 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.782231 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.192411 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.784897 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.611599 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.334002 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.61606  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.698552 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.296222 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.693255 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.47529  |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.438832 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.47834  |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.689483 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.208788 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.693464 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.462454 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.358855 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.46876  |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.455338 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.51872 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.408138 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.630576 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.236549 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.416867 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.591236 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.86913 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.613901 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.520203 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.588495 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.918955 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.484982 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.840795 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.852838 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.835497 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.570915 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.693885496459026,
    "polaris/pkis2-ret-wt-reg-v2": 736.7728973103067,
    "polaris/pkis2-kit-wt-cls-v2": 0.5891285019570237,
    "polaris/pkis2-kit-wt-reg-v2": 795.6275581676035,
    "polaris/pkis2-egfr-wt-reg-v2": 471.4109760717187,
    "polaris/adme-fang-solu-1": 0.5926906398677676,
    "polaris/adme-fang-rppb-1": 0.4742351875644767,
    "polaris/adme-fang-hppb-1": 0.6555277064249948,
    "polaris/adme-fang-perm-1": 0.7848968545880367,
    "polaris/adme-fang-rclint-1": 0.693254893511184,
    "polaris/adme-fang-hclint-1": 0.69346436327705,
    "tdcommons/lipophilicity-astrazeneca": 0.45533802059150874,
    "tdcommons/ppbr-az": 8.518724245402382,
    "tdcommons/clearance-hepatocyte-az": 0.40813809332635215,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6305762392796119,
    "tdcommons/half-life-obach": 0.23654887357293042,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.41686689517223563,
    "tdcommons/clearance-microsome-az": 0.591235505425232,
    "tdcommons/dili": 0.8691304347826088,
    "tdcommons/bioavailability-ma": 0.6139008979048886,
    "tdcommons/vdss-lombardo": 0.5202026574560851,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.588494575045208,
    "tdcommons/pgp-broccatelli": 0.9189549453479073,
    "tdcommons/caco2-wang": 0.48498201138345903,
    "tdcommons/herg": 0.8407952871870397,
    "tdcommons/bbb-martins": 0.8528377110694184,
    "tdcommons/ames": 0.8354970725880672,
    "tdcommons/ld50-zhu": 0.5709150904989695
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.509609 |
|  1 | test       | CLS_RET        | accuracy    | 0.877358 |
|  2 | test       | CLS_RET        | f1          | 0.580645 |
|  3 | test       | CLS_RET        | mcc         | 0.512903 |
|  4 | test       | CLS_RET        | roc_auc     | 0.860542 |
|  5 | test       | CLS_RET        | pr_auc      | 0.63741  |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.628615 |
|  1 | test       | RET            | mean_squared_error  | 788.085    |
|  2 | test       | RET            | pearsonr            |   0.585206 |
|  3 | test       | RET            | r2                  |   0.336296 |
|  4 | test       | RET            | mean_absolute_error |  22.4064   |
|  5 | test       | RET            | explained_var       |   0.336339 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.496939 |
|  1 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  2 | test       | CLS_KIT        | f1          | 0.585366 |
|  3 | test       | CLS_KIT        | mcc         | 0.498909 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.808511 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.626304 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.551744 |
|  1 | test       | KIT            | mean_squared_error  | 824.905    |
|  2 | test       | KIT            | pearsonr            |   0.591094 |
|  3 | test       | KIT            | r2                  |   0.316387 |
|  4 | test       | KIT            | mean_absolute_error |  21.9979   |
|  5 | test       | KIT            | explained_var       |   0.324302 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.277673 |
|  1 | test       | EGFR           | mean_squared_error  | 505.827    |
|  2 | test       | EGFR           | pearsonr            |   0.617969 |
|  3 | test       | EGFR           | r2                  |   0.372243 |
|  4 | test       | EGFR           | mean_absolute_error |  16.8322   |
|  5 | test       | EGFR           | explained_var       |   0.374803 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.513516 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.346063 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.617039 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.361717 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.410623 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.364186 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.777391 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.497145 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.69551  |
|  3 | test       | LOG_RPPB       | r2                  | 0.440456 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.535533 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.440459 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.672473 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.403094 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.65617  |
|  3 | test       | LOG_HPPB       | r2                  | 0.334431 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.529463 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.418782 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.771033 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.208655 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.776769 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.578808 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.349377 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.582389 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.676227 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.321587 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.667871 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.43036  |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.459919 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.430485 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.666307 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.224807 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.660985 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.421213 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.376013 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.422839 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.455607 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.57966 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.36436 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.643665 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.211048 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.431783 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.627611 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.886522 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.483206 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.520473 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.594146 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.922087 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.372877 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.840206 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.883814 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.84931 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.578748 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6374097570191029,
    "polaris/pkis2-ret-wt-reg-v2": 788.0849832907477,
    "polaris/pkis2-kit-wt-cls-v2": 0.6263041358027338,
    "polaris/pkis2-kit-wt-reg-v2": 824.9051319465328,
    "polaris/pkis2-egfr-wt-reg-v2": 505.8269881251924,
    "polaris/adme-fang-solu-1": 0.6170385806111716,
    "polaris/adme-fang-rppb-1": 0.6955097100727042,
    "polaris/adme-fang-hppb-1": 0.6561696974223417,
    "polaris/adme-fang-perm-1": 0.7767685488500213,
    "polaris/adme-fang-rclint-1": 0.6678713898788765,
    "polaris/adme-fang-hclint-1": 0.6609847084626784,
    "tdcommons/lipophilicity-astrazeneca": 0.45560723748661225,
    "tdcommons/ppbr-az": 8.579664476971292,
    "tdcommons/clearance-hepatocyte-az": 0.36436005865853077,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6436652506931732,
    "tdcommons/half-life-obach": 0.21104846914119735,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4317832689684109,
    "tdcommons/clearance-microsome-az": 0.6276114726870837,
    "tdcommons/dili": 0.8865217391304347,
    "tdcommons/bioavailability-ma": 0.48320585300964414,
    "tdcommons/vdss-lombardo": 0.5204729863974252,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5941455696202531,
    "tdcommons/pgp-broccatelli": 0.9220874433484405,
    "tdcommons/caco2-wang": 0.3728766381867797,
    "tdcommons/herg": 0.8402061855670104,
    "tdcommons/bbb-martins": 0.8838141025641026,
    "tdcommons/ames": 0.8493097573870646,
    "tdcommons/ld50-zhu": 0.5787483446085082
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.480816 |
|  1 | test       | CLS_RET        | accuracy    | 0.886792 |
|  2 | test       | CLS_RET        | f1          | 0.538462 |
|  3 | test       | CLS_RET        | mcc         | 0.512494 |
|  4 | test       | CLS_RET        | roc_auc     | 0.881031 |
|  5 | test       | CLS_RET        | pr_auc      | 0.681131 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.594413 |
|  1 | test       | RET            | mean_squared_error  | 683.541    |
|  2 | test       | RET            | pearsonr            |   0.656297 |
|  3 | test       | RET            | r2                  |   0.424341 |
|  4 | test       | RET            | mean_absolute_error |  20.1227   |
|  5 | test       | RET            | explained_var       |   0.4279   |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.410287 |
|  1 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  2 | test       | CLS_KIT        | f1          | 0.484848 |
|  3 | test       | CLS_KIT        | mcc         | 0.443872 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.867021 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.676785 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.584507 |
|  1 | test       | KIT            | mean_squared_error  | 801.452    |
|  2 | test       | KIT            | pearsonr            |   0.613696 |
|  3 | test       | KIT            | r2                  |   0.335823 |
|  4 | test       | KIT            | mean_absolute_error |  21.5981   |
|  5 | test       | KIT            | explained_var       |   0.366283 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.443166 |
|  1 | test       | EGFR           | mean_squared_error  | 423.301    |
|  2 | test       | EGFR           | pearsonr            |   0.689202 |
|  3 | test       | EGFR           | r2                  |   0.474661 |
|  4 | test       | EGFR           | mean_absolute_error |  16.1205   |
|  5 | test       | EGFR           | explained_var       |   0.474667 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.484187 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.373227 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.576809 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.311616 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.42934  |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.328457 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.762609 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.504738 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.713563 |
|  3 | test       | LOG_RPPB       | r2                  | 0.431909 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.526895 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.442063 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.681335 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.462344 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.558283 |
|  3 | test       | LOG_HPPB       | r2                  | 0.236602 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.608859 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.306776 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.778923 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.202885 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.776089 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.590455 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.351861 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.599407 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.705769 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.295365 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.697384 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.476808 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.437527 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.48225  |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.66835  |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.221101 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.665274 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.430754 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.370183 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.434661 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.476389 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.96943 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.394321 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.652391 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.28138 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.388824 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.572468 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.893478 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.550382 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.482446 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.596858 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.918622 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.423723 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.818999 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.884518 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.832221 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.551437 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6811305682147467,
    "polaris/pkis2-ret-wt-reg-v2": 683.5409474488904,
    "polaris/pkis2-kit-wt-cls-v2": 0.6767847384985692,
    "polaris/pkis2-kit-wt-reg-v2": 801.4515758870333,
    "polaris/pkis2-egfr-wt-reg-v2": 423.30132524545616,
    "polaris/adme-fang-solu-1": 0.5768088835774372,
    "polaris/adme-fang-rppb-1": 0.7135628509008316,
    "polaris/adme-fang-hppb-1": 0.5582828401117739,
    "polaris/adme-fang-perm-1": 0.7760893375058786,
    "polaris/adme-fang-rclint-1": 0.697383936295292,
    "polaris/adme-fang-hclint-1": 0.6652743114851788,
    "tdcommons/lipophilicity-astrazeneca": 0.47638894284339184,
    "tdcommons/ppbr-az": 8.969428436606856,
    "tdcommons/clearance-hepatocyte-az": 0.39432064335593403,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.652390650541292,
    "tdcommons/half-life-obach": 0.28137953908797564,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3888237361291108,
    "tdcommons/clearance-microsome-az": 0.5724684269942051,
    "tdcommons/dili": 0.8934782608695653,
    "tdcommons/bioavailability-ma": 0.5503824409710676,
    "tdcommons/vdss-lombardo": 0.48244582049948104,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5968580470162748,
    "tdcommons/pgp-broccatelli": 0.9186217008797655,
    "tdcommons/caco2-wang": 0.423722926935787,
    "tdcommons/herg": 0.8189985272459499,
    "tdcommons/bbb-martins": 0.8845176672920575,
    "tdcommons/ames": 0.832221112612348,
    "tdcommons/ld50-zhu": 0.5514373764527183
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.583552 |
|  1 | test       | CLS_RET        | accuracy    | 0.858491 |
|  2 | test       | CLS_RET        | f1          | 0.666667 |
|  3 | test       | CLS_RET        | mcc         | 0.612829 |
|  4 | test       | CLS_RET        | roc_auc     | 0.897555 |
|  5 | test       | CLS_RET        | pr_auc      | 0.719089 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.566853 |
|  1 | test       | RET            | mean_squared_error  | 771.075    |
|  2 | test       | RET            | pearsonr            |   0.602683 |
|  3 | test       | RET            | r2                  |   0.350622 |
|  4 | test       | RET            | mean_absolute_error |  21.6202   |
|  5 | test       | RET            | explained_var       |   0.356352 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.615306 |
|  1 | test       | CLS_KIT        | accuracy    | 0.887931 |
|  2 | test       | CLS_KIT        | f1          | 0.682927 |
|  3 | test       | CLS_KIT        | mcc         | 0.617745 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.918279 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.757649 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.527603 |
|  1 | test       | KIT            | mean_squared_error  | 916.703    |
|  2 | test       | KIT            | pearsonr            |   0.575745 |
|  3 | test       | KIT            | r2                  |   0.240312 |
|  4 | test       | KIT            | mean_absolute_error |  23.2183   |
|  5 | test       | KIT            | explained_var       |   0.323331 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.361417 |
|  1 | test       | EGFR           | mean_squared_error  | 492.332    |
|  2 | test       | EGFR           | pearsonr            |   0.639516 |
|  3 | test       | EGFR           | r2                  |   0.38899  |
|  4 | test       | EGFR           | mean_absolute_error |  16.5982   |
|  5 | test       | EGFR           | explained_var       |   0.39189  |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.54892  |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.328736 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.629967 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.393676 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.394346 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.394081 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.778261 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.584099 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.691506 |
|  3 | test       | LOG_RPPB       | r2                  | 0.342588 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.567776 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.342625 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.598365 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.43315  |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.625788 |
|  3 | test       | LOG_HPPB       | r2                  | 0.284805 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.53631  |
|  5 | test       | LOG_HPPB       | explained_var       | 0.380522 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.793417 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.196324 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.788174 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.6037   |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.328679 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.611902 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.704354 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.286051 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.703733 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.493305 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.430903 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.494578 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.676203 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.216122 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.680724 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.443573 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.35759  |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.451621 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.456912 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 7.93241 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.383805 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.655458 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.192861 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.458351 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.608701 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.861304 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.543066 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.513606 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.618784 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.905492 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.323098 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.781885 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.813673 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.832834 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.586009 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.719088966719376,
    "polaris/pkis2-ret-wt-reg-v2": 771.0752214791157,
    "polaris/pkis2-kit-wt-cls-v2": 0.757649356125461,
    "polaris/pkis2-kit-wt-reg-v2": 916.7033733330379,
    "polaris/pkis2-egfr-wt-reg-v2": 492.33232576190545,
    "polaris/adme-fang-solu-1": 0.6299667311404703,
    "polaris/adme-fang-rppb-1": 0.6915055664226509,
    "polaris/adme-fang-hppb-1": 0.6257880927205615,
    "polaris/adme-fang-perm-1": 0.788173561287692,
    "polaris/adme-fang-rclint-1": 0.7037330900799968,
    "polaris/adme-fang-hclint-1": 0.680724284892702,
    "tdcommons/lipophilicity-astrazeneca": 0.4569121260018576,
    "tdcommons/ppbr-az": 7.932408755171063,
    "tdcommons/clearance-hepatocyte-az": 0.38380468348383945,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6554583247310561,
    "tdcommons/half-life-obach": 0.19286136016059668,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.458350989862251,
    "tdcommons/clearance-microsome-az": 0.6087008322534833,
    "tdcommons/dili": 0.8613043478260869,
    "tdcommons/bioavailability-ma": 0.5430661789158631,
    "tdcommons/vdss-lombardo": 0.5136063776166396,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6187839059674504,
    "tdcommons/pgp-broccatelli": 0.9054918688349772,
    "tdcommons/caco2-wang": 0.32309752393215313,
    "tdcommons/herg": 0.7818851251840943,
    "tdcommons/bbb-martins": 0.813672607879925,
    "tdcommons/ames": 0.8328340088899333,
    "tdcommons/ld50-zhu": 0.5860093976047913
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | cohen_kappa | 0.555197 |
|  1 | test       | CLS_RET        | accuracy    | 0.877358 |
|  2 | test       | CLS_RET        | f1          | 0.628571 |
|  3 | test       | CLS_RET        | mcc         | 0.555522 |
|  4 | test       | CLS_RET        | roc_auc     | 0.86649  |
|  5 | test       | CLS_RET        | pr_auc      | 0.642954 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.601657 |
|  1 | test       | RET            | mean_squared_error  | 805.975    |
|  2 | test       | RET            | pearsonr            |   0.583206 |
|  3 | test       | RET            | r2                  |   0.32123  |
|  4 | test       | RET            | mean_absolute_error |  21.9216   |
|  5 | test       | RET            | explained_var       |   0.334076 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | cohen_kappa | 0.183099 |
|  1 | test       | CLS_KIT        | accuracy    | 0.827586 |
|  2 | test       | CLS_KIT        | f1          | 0.230769 |
|  3 | test       | CLS_KIT        | mcc         | 0.270121 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.852998 |
|  5 | test       | CLS_KIT        | pr_auc      | 0.638632 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.548127 |
|  1 | test       | KIT            | mean_squared_error  | 870.494    |
|  2 | test       | KIT            | pearsonr            |   0.570946 |
|  3 | test       | KIT            | r2                  |   0.278607 |
|  4 | test       | KIT            | mean_absolute_error |  22.5014   |
|  5 | test       | KIT            | explained_var       |   0.281918 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.379766 |
|  1 | test       | EGFR           | mean_squared_error  | 522.939    |
|  2 | test       | EGFR           | pearsonr            |   0.599098 |
|  3 | test       | EGFR           | r2                  |   0.351006 |
|  4 | test       | EGFR           | mean_absolute_error |  17.857    |
|  5 | test       | EGFR           | explained_var       |   0.353035 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.503506 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.343074 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.615977 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.367231 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.403984 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.378892 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.651304 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.705388 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.505954 |
|  3 | test       | LOG_RPPB       | r2                  | 0.206075 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.665296 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.239013 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.704255 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.416672 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.703047 |
|  3 | test       | LOG_HPPB       | r2                  | 0.312012 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.544846 |
|  5 | test       | LOG_HPPB       | explained_var       | 0.487991 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.775226 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.19728  |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.778257 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.601771 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.346122 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.60533  |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.703939 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.291786 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.697799 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.483147 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.43393  |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.483964 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.686643 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.220667 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.681949 |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.431871 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.362694 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.434936 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.455838 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.39201 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.307592 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.631151 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.155594 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.413729 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.612255 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.864348 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.572331 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.25391 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.627373 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.913223 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.427711 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.790133 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.877111 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.830132 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.59065 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6429537916483041,
    "polaris/pkis2-ret-wt-reg-v2": 805.9751596314685,
    "polaris/pkis2-kit-wt-cls-v2": 0.6386316349672762,
    "polaris/pkis2-kit-wt-reg-v2": 870.493985654735,
    "polaris/pkis2-egfr-wt-reg-v2": 522.9392937875115,
    "polaris/adme-fang-solu-1": 0.6159766165823874,
    "polaris/adme-fang-rppb-1": 0.5059538858233126,
    "polaris/adme-fang-hppb-1": 0.7030467618209677,
    "polaris/adme-fang-perm-1": 0.7782570641619255,
    "polaris/adme-fang-rclint-1": 0.6977989870637715,
    "polaris/adme-fang-hclint-1": 0.6819491480051566,
    "tdcommons/lipophilicity-astrazeneca": 0.45583846613339013,
    "tdcommons/ppbr-az": 8.392007630813952,
    "tdcommons/clearance-hepatocyte-az": 0.30759207038454234,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6311510659134058,
    "tdcommons/half-life-obach": 0.15559431056850465,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.4137288188613576,
    "tdcommons/clearance-microsome-az": 0.6122548075506901,
    "tdcommons/dili": 0.8643478260869566,
    "tdcommons/bioavailability-ma": 0.5723312271366809,
    "tdcommons/vdss-lombardo": 0.2539101274169481,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6273734177215189,
    "tdcommons/pgp-broccatelli": 0.9132231404958677,
    "tdcommons/caco2-wang": 0.4277113168979855,
    "tdcommons/herg": 0.7901325478645067,
    "tdcommons/bbb-martins": 0.8771106941838649,
    "tdcommons/ames": 0.8301317824903561,
    "tdcommons/ld50-zhu": 0.5906501094085116
}
```
