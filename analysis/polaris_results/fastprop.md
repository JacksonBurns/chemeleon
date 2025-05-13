# Descriptor MLP Results
timestamp: 2025-04-29 02:03:40.816836
## Random Seed 42

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.634433 |
|  1 | test       | CLS_RET        | roc_auc     | 0.840714 |
|  2 | test       | CLS_RET        | mcc         | 0.266557 |
|  3 | test       | CLS_RET        | accuracy    | 0.849057 |
|  4 | test       | CLS_RET        | f1          | 0.272727 |
|  5 | test       | CLS_RET        | cohen_kappa | 0.215541 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 822.5      |
|  1 | test       | RET            | mean_absolute_error |  21.9797   |
|  2 | test       | RET            | pearsonr            |   0.576737 |
|  3 | test       | RET            | explained_var       |   0.329512 |
|  4 | test       | RET            | spearmanr           |   0.571227 |
|  5 | test       | RET            | r2                  |   0.307313 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.483658 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.75677  |
|  2 | test       | CLS_KIT        | mcc         | 0.218701 |
|  3 | test       | CLS_KIT        | accuracy    | 0.801724 |
|  4 | test       | CLS_KIT        | f1          | 0.30303  |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.202153 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | mean_squared_error  | 1009.68     |
|  1 | test       | KIT            | mean_absolute_error |   25.6487   |
|  2 | test       | KIT            | pearsonr            |    0.445213 |
|  3 | test       | KIT            | explained_var       |    0.168244 |
|  4 | test       | KIT            | spearmanr           |    0.42032  |
|  5 | test       | KIT            | r2                  |    0.163258 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 561.686    |
|  1 | test       | EGFR           | mean_absolute_error |  18.6954   |
|  2 | test       | EGFR           | pearsonr            |   0.559434 |
|  3 | test       | EGFR           | explained_var       |   0.309873 |
|  4 | test       | EGFR           | spearmanr           |   0.317169 |
|  5 | test       | EGFR           | r2                  |   0.302918 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.357987 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.40975  |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.586616 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.343467 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.475695 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.339725 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.4391   |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.471991 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.752482 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.505955 |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.82087  |
|  5 | test       | LOG_RPPB       | r2                  | 0.505787 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.233505 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.421878 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.846636 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.701461 |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.856903 |
|  5 | test       | LOG_HPPB       | r2                  | 0.614449 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.216888 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.356276 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.749812 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.562195 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.747893 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.562189 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.313167 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.444431 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.668994 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.445882 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.667493 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.445274 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.234436 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.381739 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.645224 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.398216 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.669958 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.39642  |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.550494 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.76612 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.338182 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.67832 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.348983 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.38175 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.544154 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  |    0.91 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.682408 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.515669 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.599797 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.924154 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.28448 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.849632 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.901423 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  |  0.8419 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.609437 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.634433064559178,
    "polaris/pkis2-ret-wt-reg-v2": 822.5000476439109,
    "polaris/pkis2-kit-wt-cls-v2": 0.48365776087492673,
    "polaris/pkis2-kit-wt-reg-v2": 1009.6837656446122,
    "polaris/pkis2-egfr-wt-reg-v2": 561.6864792544841,
    "polaris/adme-fang-solu-1": 0.5866155015957892,
    "polaris/adme-fang-rppb-1": 0.7524815976915824,
    "polaris/adme-fang-hppb-1": 0.8466364925604364,
    "polaris/adme-fang-perm-1": 0.749812092808102,
    "polaris/adme-fang-rclint-1": 0.6689941010586801,
    "polaris/adme-fang-hclint-1": 0.6452242176194555,
    "tdcommons/lipophilicity-astrazeneca": 0.5504940575872148,
    "tdcommons/ppbr-az": 8.766118995243408,
    "tdcommons/clearance-hepatocyte-az": 0.3381819840968773,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6783196065152546,
    "tdcommons/half-life-obach": 0.3489832151631764,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.38174971855565254,
    "tdcommons/clearance-microsome-az": 0.5441541748144705,
    "tdcommons/dili": 0.91,
    "tdcommons/bioavailability-ma": 0.6824077153308946,
    "tdcommons/vdss-lombardo": 0.5156685955766196,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5997965641952984,
    "tdcommons/pgp-broccatelli": 0.9241535590509198,
    "tdcommons/caco2-wang": 0.284479731069326,
    "tdcommons/herg": 0.8496318114874816,
    "tdcommons/bbb-martins": 0.9014227642276423,
    "tdcommons/ames": 0.8419001742740214,
    "tdcommons/ld50-zhu": 0.6094365377477767
}
```
## Random Seed 117

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.659285 |
|  1 | test       | CLS_RET        | roc_auc     | 0.879709 |
|  2 | test       | CLS_RET        | mcc         | 0.453107 |
|  3 | test       | CLS_RET        | accuracy    | 0.877358 |
|  4 | test       | CLS_RET        | f1          | 0.380952 |
|  5 | test       | CLS_RET        | cohen_kappa | 0.34067  |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 752.283    |
|  1 | test       | RET            | mean_absolute_error |  20.5789   |
|  2 | test       | RET            | pearsonr            |   0.622371 |
|  3 | test       | RET            | explained_var       |   0.386534 |
|  4 | test       | RET            | spearmanr           |   0.627947 |
|  5 | test       | RET            | r2                  |   0.366448 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.438832 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.745164 |
|  2 | test       | CLS_KIT        | mcc         | 0.246387 |
|  3 | test       | CLS_KIT        | accuracy    | 0.801724 |
|  4 | test       | CLS_KIT        | f1          | 0.342857 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.235092 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | KIT            | mean_squared_error  | 1031.48     |
|  1 | test       | KIT            | mean_absolute_error |   25.482    |
|  2 | test       | KIT            | pearsonr            |    0.446951 |
|  3 | test       | KIT            | explained_var       |    0.1537   |
|  4 | test       | KIT            | spearmanr           |    0.421544 |
|  5 | test       | KIT            | r2                  |    0.145195 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 511.199    |
|  1 | test       | EGFR           | mean_absolute_error |  18.0993   |
|  2 | test       | EGFR           | pearsonr            |   0.61194  |
|  3 | test       | EGFR           | explained_var       |   0.37375  |
|  4 | test       | EGFR           | spearmanr           |   0.318681 |
|  5 | test       | EGFR           | r2                  |   0.365575 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.360191 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.416918 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.583697 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.339759 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.484383 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.335661 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.325038 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.411402 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.823436 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.637619 |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.847826 |
|  5 | test       | LOG_RPPB       | r2                  | 0.634165 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.30948  |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.501832 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.785331 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.579612 |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.759722 |
|  5 | test       | LOG_HPPB       | r2                  | 0.489002 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.22138  |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.360233 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.744691 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.553138 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.739643 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.553123 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.30221  |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.42962  |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.683436 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.464947 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.685663 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.464683 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.231565 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.377    |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.648983 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.40546  |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.672463 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.403813 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.533609 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.47792 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.327811 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.680503 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.279265 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.381371 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.496948 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.904783 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.63984 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.540753 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.596632 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.91389 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.302933 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.832253 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.913579 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.843518 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.64841 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6592849474427518,
    "polaris/pkis2-ret-wt-reg-v2": 752.2830033703634,
    "polaris/pkis2-kit-wt-cls-v2": 0.43883222496546376,
    "polaris/pkis2-kit-wt-reg-v2": 1031.4798659775242,
    "polaris/pkis2-egfr-wt-reg-v2": 511.1993329038103,
    "polaris/adme-fang-solu-1": 0.5836965562479778,
    "polaris/adme-fang-rppb-1": 0.8234363138787124,
    "polaris/adme-fang-hppb-1": 0.7853310470239419,
    "polaris/adme-fang-perm-1": 0.7446911697084346,
    "polaris/adme-fang-rclint-1": 0.6834356185236604,
    "polaris/adme-fang-hclint-1": 0.6489828208363397,
    "tdcommons/lipophilicity-astrazeneca": 0.5336093098265784,
    "tdcommons/ppbr-az": 8.477919699134896,
    "tdcommons/clearance-hepatocyte-az": 0.3278109077713852,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6805029819309203,
    "tdcommons/half-life-obach": 0.27926486624613855,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3813706859417536,
    "tdcommons/clearance-microsome-az": 0.4969482639250949,
    "tdcommons/dili": 0.9047826086956522,
    "tdcommons/bioavailability-ma": 0.6398403724642501,
    "tdcommons/vdss-lombardo": 0.5407531091740178,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5966320072332731,
    "tdcommons/pgp-broccatelli": 0.9138896294321515,
    "tdcommons/caco2-wang": 0.3029325581849655,
    "tdcommons/herg": 0.8322533136966126,
    "tdcommons/bbb-martins": 0.913578799249531,
    "tdcommons/ames": 0.8435175938436235,
    "tdcommons/ld50-zhu": 0.6484098774331832
}
```
## Random Seed 709

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.611109 |
|  1 | test       | CLS_RET        | roc_auc     | 0.857898 |
|  2 | test       | CLS_RET        | mcc         | 0.266557 |
|  3 | test       | CLS_RET        | accuracy    | 0.849057 |
|  4 | test       | CLS_RET        | f1          | 0.272727 |
|  5 | test       | CLS_RET        | cohen_kappa | 0.215541 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 853.174    |
|  1 | test       | RET            | mean_absolute_error |  22.1062   |
|  2 | test       | RET            | pearsonr            |   0.560695 |
|  3 | test       | RET            | explained_var       |   0.31263  |
|  4 | test       | RET            | spearmanr           |   0.603024 |
|  5 | test       | RET            | r2                  |   0.28148  |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.467767 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.755319 |
|  2 | test       | CLS_KIT        | mcc         | 0.218701 |
|  3 | test       | CLS_KIT        | accuracy    | 0.801724 |
|  4 | test       | CLS_KIT        | f1          | 0.30303  |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.202153 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_squared_error  | 966.288    |
|  1 | test       | KIT            | mean_absolute_error |  24.6991   |
|  2 | test       | KIT            | pearsonr            |   0.476524 |
|  3 | test       | KIT            | explained_var       |   0.204849 |
|  4 | test       | KIT            | spearmanr           |   0.461556 |
|  5 | test       | KIT            | r2                  |   0.19922  |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 510.569    |
|  1 | test       | EGFR           | mean_absolute_error |  17.9502   |
|  2 | test       | EGFR           | pearsonr            |   0.612203 |
|  3 | test       | EGFR           | explained_var       |   0.372962 |
|  4 | test       | EGFR           | spearmanr           |   0.335811 |
|  5 | test       | EGFR           | r2                  |   0.366357 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.382441 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.428245 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.548578 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.298819 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.454484 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.294623 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.351544 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.430415 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.815248 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.605441 |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.845217 |
|  5 | test       | LOG_RPPB       | r2                  | 0.604332 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.311617 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.513691 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.780446 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.570081 |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.81473  |
|  5 | test       | LOG_HPPB       | r2                  | 0.485473 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.227926 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.361984 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.736547 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.540637 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.734597 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.539908 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.300449 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.428665 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.685128 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.46891  |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.689552 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.467802 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.230572 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.380956 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.641758 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.407037 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.661496 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.406369 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.550162 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  8.4425 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.379186 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.690576 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.296136 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.312685 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr |  0.5349 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.886522 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.603592 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.522128 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.591433 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.92522 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.275029 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.823711 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.91483 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.851587 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.638441 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6111087631652372,
    "polaris/pkis2-ret-wt-reg-v2": 853.1739460940686,
    "polaris/pkis2-kit-wt-cls-v2": 0.4677672988549707,
    "polaris/pkis2-kit-wt-reg-v2": 966.2882995782583,
    "polaris/pkis2-egfr-wt-reg-v2": 510.56916627469593,
    "polaris/adme-fang-solu-1": 0.5485783628872404,
    "polaris/adme-fang-rppb-1": 0.8152480403725656,
    "polaris/adme-fang-hppb-1": 0.7804464622490165,
    "polaris/adme-fang-perm-1": 0.7365469065828796,
    "polaris/adme-fang-rclint-1": 0.6851278224711912,
    "polaris/adme-fang-hclint-1": 0.6417578777330453,
    "tdcommons/lipophilicity-astrazeneca": 0.5501623697564716,
    "tdcommons/ppbr-az": 8.442498672567242,
    "tdcommons/clearance-hepatocyte-az": 0.3791857307971865,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6905762892677276,
    "tdcommons/half-life-obach": 0.2961359066694225,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.3126853749471482,
    "tdcommons/clearance-microsome-az": 0.5348996733716542,
    "tdcommons/dili": 0.8865217391304347,
    "tdcommons/bioavailability-ma": 0.6035916195543731,
    "tdcommons/vdss-lombardo": 0.5221281671346515,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.5914330922242313,
    "tdcommons/pgp-broccatelli": 0.9252199413489736,
    "tdcommons/caco2-wang": 0.27502936638384823,
    "tdcommons/herg": 0.8237113402061856,
    "tdcommons/bbb-martins": 0.9148295809881175,
    "tdcommons/ames": 0.8515870684759835,
    "tdcommons/ld50-zhu": 0.6384410723478449
}
```
## Random Seed 1701

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.443833 |
|  1 | test       | CLS_RET        | roc_auc     | 0.796431 |
|  2 | test       | CLS_RET        | mcc         | 0        |
|  3 | test       | CLS_RET        | accuracy    | 0.839623 |
|  4 | test       | CLS_RET        | f1          | 0        |
|  5 | test       | CLS_RET        | cohen_kappa | 0        |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 795.13     |
|  1 | test       | RET            | mean_absolute_error |  21.4411   |
|  2 | test       | RET            | pearsonr            |   0.589062 |
|  3 | test       | RET            | explained_var       |   0.346982 |
|  4 | test       | RET            | spearmanr           |   0.58893  |
|  5 | test       | RET            | r2                  |   0.330363 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.495573 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.772727 |
|  2 | test       | CLS_KIT        | mcc         | 0.225784 |
|  3 | test       | CLS_KIT        | accuracy    | 0.793103 |
|  4 | test       | CLS_KIT        | f1          | 0.333333 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.217978 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_squared_error  | 964.653    |
|  1 | test       | KIT            | mean_absolute_error |  24.0988   |
|  2 | test       | KIT            | pearsonr            |   0.494547 |
|  3 | test       | KIT            | explained_var       |   0.213922 |
|  4 | test       | KIT            | spearmanr           |   0.465785 |
|  5 | test       | KIT            | r2                  |   0.200575 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 585.943    |
|  1 | test       | EGFR           | mean_absolute_error |  19.0369   |
|  2 | test       | EGFR           | pearsonr            |   0.529421 |
|  3 | test       | EGFR           | explained_var       |   0.279157 |
|  4 | test       | EGFR           | spearmanr           |   0.256412 |
|  5 | test       | EGFR           | r2                  |   0.272815 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.381749 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.433968 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.54629  |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.298419 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.444799 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.295898 |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.450754 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.511809 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.748231 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.493443 |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.751304 |
|  5 | test       | LOG_RPPB       | r2                  | 0.492669 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.227221 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.419362 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.838238 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.674398 |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.851249 |
|  5 | test       | LOG_HPPB       | r2                  | 0.624824 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.217689 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.352027 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.749728 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.56117  |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.752496 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.560572 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.303266 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.437166 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.680435 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.46286  |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.675385 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.462811 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.227403 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.371084 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.65453  |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.415898 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.684044 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.414527 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.554748 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.21279 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.383427 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.602108 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.102281 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.358189 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.528328 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.882609 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.62288 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.452852 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.610873 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.919355 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.277743 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.843152 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.91823 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.846314 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.644551 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.44383307588392185,
    "polaris/pkis2-ret-wt-reg-v2": 795.1300875648799,
    "polaris/pkis2-kit-wt-cls-v2": 0.49557259940773923,
    "polaris/pkis2-kit-wt-reg-v2": 964.6530951079977,
    "polaris/pkis2-egfr-wt-reg-v2": 585.9431030189237,
    "polaris/adme-fang-solu-1": 0.5462900721945965,
    "polaris/adme-fang-rppb-1": 0.7482305340604205,
    "polaris/adme-fang-hppb-1": 0.8382378122379444,
    "polaris/adme-fang-perm-1": 0.7497276420801129,
    "polaris/adme-fang-rclint-1": 0.6804349902060638,
    "polaris/adme-fang-hclint-1": 0.6545303217655917,
    "tdcommons/lipophilicity-astrazeneca": 0.5547479983170827,
    "tdcommons/ppbr-az": 8.212785119345023,
    "tdcommons/clearance-hepatocyte-az": 0.3834271645392779,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.6021082373587222,
    "tdcommons/half-life-obach": 0.10228113989160104,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.35818866208083505,
    "tdcommons/clearance-microsome-az": 0.528328352426961,
    "tdcommons/dili": 0.8826086956521739,
    "tdcommons/bioavailability-ma": 0.6228799467908214,
    "tdcommons/vdss-lombardo": 0.4528523032574587,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6108725135623869,
    "tdcommons/pgp-broccatelli": 0.9193548387096775,
    "tdcommons/caco2-wang": 0.2777430246384004,
    "tdcommons/herg": 0.8431516936671576,
    "tdcommons/bbb-martins": 0.9182301438399,
    "tdcommons/ames": 0.846313810726664,
    "tdcommons/ld50-zhu": 0.6445508438834319
}
```
## Random Seed 9001

### `polaris/pkis2-ret-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.66591  |
|  1 | test       | CLS_RET        | roc_auc     | 0.85922  |
|  2 | test       | CLS_RET        | mcc         | 0.504899 |
|  3 | test       | CLS_RET        | accuracy    | 0.886792 |
|  4 | test       | CLS_RET        | f1          | 0.5      |
|  5 | test       | CLS_RET        | cohen_kappa | 0.448395 |


### `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_squared_error  | 782.444    |
|  1 | test       | RET            | mean_absolute_error |  21.4517   |
|  2 | test       | RET            | pearsonr            |   0.599664 |
|  3 | test       | RET            | explained_var       |   0.357976 |
|  4 | test       | RET            | spearmanr           |   0.594145 |
|  5 | test       | RET            | r2                  |   0.341047 |


### `polaris/pkis2-kit-wt-cls-v2`

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.441419 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.776112 |
|  2 | test       | CLS_KIT        | mcc         | 0.172599 |
|  3 | test       | CLS_KIT        | accuracy    | 0.767241 |
|  4 | test       | CLS_KIT        | f1          | 0.307692 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.170551 |


### `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_squared_error  | 965.019    |
|  1 | test       | KIT            | mean_absolute_error |  24.9938   |
|  2 | test       | KIT            | pearsonr            |   0.470918 |
|  3 | test       | KIT            | explained_var       |   0.203611 |
|  4 | test       | KIT            | spearmanr           |   0.473977 |
|  5 | test       | KIT            | r2                  |   0.200272 |


### `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_squared_error  | 574.487    |
|  1 | test       | EGFR           | mean_absolute_error |  18.5672   |
|  2 | test       | EGFR           | pearsonr            |   0.547643 |
|  3 | test       | EGFR           | explained_var       |   0.290257 |
|  4 | test       | EGFR           | spearmanr           |   0.292963 |
|  5 | test       | EGFR           | r2                  |   0.287032 |


### `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.385034 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.438289 |
|  2 | test       | LOG_SOLUBILITY | pearsonr            | 0.540951 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.292599 |
|  4 | test       | LOG_SOLUBILITY | spearmanr           | 0.439093 |
|  5 | test       | LOG_SOLUBILITY | r2                  | 0.28984  |


### `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_squared_error  | 0.30793  |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.427651 |
|  2 | test       | LOG_RPPB       | pearsonr            | 0.837617 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.654042 |
|  4 | test       | LOG_RPPB       | spearmanr           | 0.84     |
|  5 | test       | LOG_RPPB       | r2                  | 0.653421 |


### `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | mean_squared_error  | 0.265237 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.466113 |
|  2 | test       | LOG_HPPB       | pearsonr            | 0.798975 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.592553 |
|  4 | test       | LOG_HPPB       | spearmanr           | 0.794866 |
|  5 | test       | LOG_HPPB       | r2                  | 0.562054 |


### `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.224208 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.367235 |
|  2 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.73998  |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.547414 |
|  4 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.744148 |
|  5 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.547413 |


### `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.302884 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.434263 |
|  2 | test       | LOG_RLM_CLint  | pearsonr            | 0.686578 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.466742 |
|  4 | test       | LOG_RLM_CLint  | spearmanr           | 0.688579 |
|  5 | test       | LOG_RLM_CLint  | r2                  | 0.463488 |


### `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.228231 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.372919 |
|  2 | test       | LOG_HLM_CLint  | pearsonr            | 0.658202 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.412504 |
|  4 | test       | LOG_HLM_CLint  | spearmanr           | 0.681554 |
|  5 | test       | LOG_HLM_CLint  | r2                  | 0.412397 |


### `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.526586 |


### `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  8.1464 |


### `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.33694 |


### `tdcommons/cyp2d6-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.594729 |


### `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.249111 |


### `tdcommons/cyp2c9-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.445102 |


### `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.53072 |


### `tdcommons/dili`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.886522 |


### `tdcommons/bioavailability-ma`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.619887 |


### `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.487928 |


### `tdcommons/cyp3a4-substrate-carbonmangels`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.622401 |


### `tdcommons/pgp-broccatelli`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.924953 |


### `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.309463 |


### `tdcommons/herg`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.826951 |


### `tdcommons/bbb-martins`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.918699 |


### `tdcommons/ames`

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.847334 |


### `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.63125 |


### Summary

```
results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": 0.6659097672170222,
    "polaris/pkis2-ret-wt-reg-v2": 782.4439412258906,
    "polaris/pkis2-kit-wt-cls-v2": 0.44141874074855986,
    "polaris/pkis2-kit-wt-reg-v2": 965.019213824296,
    "polaris/pkis2-egfr-wt-reg-v2": 574.4871100505289,
    "polaris/adme-fang-solu-1": 0.5409506824691828,
    "polaris/adme-fang-rppb-1": 0.8376174003049301,
    "polaris/adme-fang-hppb-1": 0.7989753821105372,
    "polaris/adme-fang-perm-1": 0.7399800198301233,
    "polaris/adme-fang-rclint-1": 0.6865780819039338,
    "polaris/adme-fang-hclint-1": 0.6582023046440604,
    "tdcommons/lipophilicity-astrazeneca": 0.5265855010918208,
    "tdcommons/ppbr-az": 8.146403841076683,
    "tdcommons/clearance-hepatocyte-az": 0.3369398409280782,
    "tdcommons/cyp2d6-substrate-carbonmangels": 0.5947285612286788,
    "tdcommons/half-life-obach": 0.24911065593053056,
    "tdcommons/cyp2c9-substrate-carbonmangels": 0.44510197721391337,
    "tdcommons/clearance-microsome-az": 0.5307195247150402,
    "tdcommons/dili": 0.8865217391304347,
    "tdcommons/bioavailability-ma": 0.6198869304955105,
    "tdcommons/vdss-lombardo": 0.4879282030889926,
    "tdcommons/cyp3a4-substrate-carbonmangels": 0.6224005424954792,
    "tdcommons/pgp-broccatelli": 0.9249533457744601,
    "tdcommons/caco2-wang": 0.3094632692442172,
    "tdcommons/herg": 0.8269513991163476,
    "tdcommons/bbb-martins": 0.9186991869918699,
    "tdcommons/ames": 0.8473339990992578,
    "tdcommons/ld50-zhu": 0.6312499563877896
}
```
