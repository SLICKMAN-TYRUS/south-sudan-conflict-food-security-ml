# Experiment Log

Track every model run here as you go — don't reconstruct this from memory
at the end. The rubric grades this table on whether it documents, for each
run: the model/approach, hyperparameters/settings, dataset split, evaluation
metrics, and your own observations/insights — and whether the progression
across experiments tells a coherent story (each run building on what the
last one taught you, not just repeating a few minor tweaks).

You need at least 7 systematically varied runs across your classical ML and
deep learning approaches combined to hit the top rubric band — more if some
turn out to be minor variations rather than meaningfully different.

| # | Approach | Key hyperparameters / settings | Train/test split | Accuracy | Precision | Recall | F1 | AUC | Observations / insights |
|---|----------|--------------------------------|-------------------|----------|-----------|--------|----|----|--------------------------|
| 1 | | | | | | | | | |
| 2 | | | | | | | | | |
| 3 | | | | | | | | | |
| 4 | | | | | | | | | |
| 5 | | | | | | | | | |
| 6 | | | | | | | | | |
| 7 | | | | | | | | | |

## Notes on what makes a strong "observations / insights" entry

Weak: "Accuracy improved to 0.81."
Strong: "Increasing max_depth from 5 to 10 raised training accuracy but
widened the train/validation gap from 0.03 to 0.11, indicating the extra
depth is overfitting to county-specific conflict patterns rather than
generalizing — suggests regularization or a shallower tree is worth testing
next, which run #5 follows up on."

The second kind is what the rubric means by "critical insights into why
results changed," not just restating the metric.
