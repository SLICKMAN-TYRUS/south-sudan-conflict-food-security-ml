# Experiment Log

Fill this in as you go — do not reconstruct from memory at the end.
The rubric grades this table on: model/approach, hyperparameters/settings,
dataset split, evaluation metrics, and observations/insights — and whether
each run visibly builds on what the previous one taught you.

Minimum 7 runs to hit the top rubric band (9 pts).

| # | Approach | Key hyperparameters | Train period | Test period | Accuracy | Precision | Recall | F1 | AUC-ROC | Observations & insights |
|---|----------|---------------------|--------------|-------------|----------|-----------|--------|----|---------|--------------------------|
| 1 | Logistic Regression | C=1.0, max_iter=1000 | 2017–2022 | 2023–2025 | | | | | | Baseline. Note any class imbalance issues here. |
| 2 | Random Forest | n_estimators=100, default depth | 2017–2022 | 2023–2025 | | | | | | Compare to LR baseline — does non-linearity help? |
| 3 | Random Forest (tuned) | max_depth=10, class_weight=balanced | 2017–2022 | 2023–2025 | | | | | | Does balancing class weight fix recall for minority class? |
| 4 | Gradient Boosting | n_estimators=200, lr=0.05 | 2017–2022 | 2023–2025 | | | | | | Best classical ML? Note if overfitting vs RF. |
| 5 | Sequential MLP | 64→32, ReLU, no regularisation | 2017–2022 | 2023–2025 | | | | | | First DL run. Watch training vs val loss gap. |
| 6 | Sequential MLP (regularised) | Dropout=0.3, BatchNorm, same arch | 2017–2022 | 2023–2025 | | | | | | Does regularisation close the train/val gap from Exp 5? |
| 7 | Functional API (multi-branch) | Conflict branch + state embedding branch | 2017–2022 | 2023–2025 | | | | | | Does separating conflict and geographic features help? |
| 8 | Best DL arch, lag=2 months | Same as best of Exp 5–7, lag_months=2 | 2017–2022 | 2023–2025 | | | | | | Does a longer lag window improve prediction? |

---

## What makes a strong "Observations & insights" entry

**Weak:** "Accuracy improved to 0.81."

**Strong:** "Increasing max_depth from 5 to 10 raised training accuracy from
0.83 to 0.91 but widened the train/validation gap from 0.03 to 0.12,
indicating the deeper tree is memorising county-specific conflict patterns
rather than learning generalisable signals. This motivates the class_weight
and depth constraints tested in Experiment 3."

The second kind is what the rubric means by "critical insights into why
results changed" — not just restating the number.
