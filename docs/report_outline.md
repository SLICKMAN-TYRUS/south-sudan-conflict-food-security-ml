# Research Report Blueprint

**Target Length:** 3,500–5,000 words (excluding references, captions, appendices)

**Citation Style:** IEEE

**Writing Style:** Formal academic prose with clear transitions between sections. Avoid excessive bullet points. Interpret results rather than simply reporting them, and write in a natural, analytical voice.

---

# 1. Introduction (500–700 words)

### Purpose

Introduce the humanitarian problem, justify its significance using evidence, and present the research question, objectives, and project contribution.

### Include

* Background on conflict-driven food insecurity in South Sudan, supported by recent humanitarian reports and peer-reviewed literature.
* Explain why timely prediction is important for humanitarian planning and resource allocation.
* State the mission alignment and practical motivation for the study.
* Introduce the research question:

> *Can county-level conflict event data predict the likelihood of a food security crisis one month in advance?*

* Present the project objectives.
* Briefly summarize the machine learning pipeline and the comparison between classical machine learning and deep learning approaches.
* End with a short overview of the report structure.

---

# 2. Literature Review (700–900 words)

### Purpose

Critically evaluate previous research and identify the knowledge gap addressed by this project.

### Organize into thematic subsections

### 2.1 Conflict and Food Security

Discuss how conflict disrupts agricultural production, markets, livelihoods, and population displacement.

Compare findings from multiple studies rather than describing them individually.

---

### 2.2 Humanitarian Early Warning Systems

Review existing food security forecasting approaches.

Discuss their strengths and limitations.

Explain why predictive modelling can complement existing IPC assessments.

---

### 2.3 Machine Learning for Humanitarian Forecasting

Review applications of

* Logistic Regression
* Random Forest
* Gradient Boosting
* Neural Networks

Compare their reported strengths and weaknesses.

Discuss interpretability versus predictive performance.

---

### 2.4 Research Gap

Conclude by identifying the gap addressed by this project.

For example:

* limited comparison of ML versus DL on South Sudan food security prediction,
* limited use of conflict events as predictive features,
* insufficient evaluation using appropriate metrics for imbalanced datasets.

End the section by explaining how the present study addresses these limitations.

---

# 3. Methodology (900–1,100 words)

### Purpose

Describe every step of the modelling pipeline in sufficient detail for reproducibility.

Organize into the following subsections.

---

## 3.1 Study Design

Provide a brief overview of the complete workflow.

Include a pipeline figure.

---

## 3.2 Datasets

Describe

### ACLED

* source
* variables
* temporal coverage
* why it is appropriate

### IPC / FEWS NET

* IPC phases
* county-level assessments
* why selected

Justify integrating both datasets.

---

## 3.3 Data Preprocessing

Explain every preprocessing decision.

Include:

* county name harmonization
* correction of all three county naming inconsistencies
* handling of the six temporal gaps
* removal of incomplete observations
* filtering strategy (`filter_ipc`)
* missing value treatment
* handling of `population_best`
* duplicate removal
* feature scaling
* encoding strategy

Justify each decision.

---

## 3.4 Feature Engineering

Explain

* monthly aggregation
* conflict counts
* fatalities
* event diversity
* violence against civilians
* lag variables
* one-month forecasting horizon
* target variable definition
* why IPC ≥ 3 was selected

Discuss why these variables are theoretically meaningful.

---

## 3.5 Experimental Design

Explain why a chronological train-test split was used instead of a random split.

Discuss reproducibility measures.

Include:

* random seeds
* software versions
* TensorFlow
* Scikit-learn

---

## 3.6 Machine Learning Models

Describe

### Logistic Regression

Purpose

Advantages

Limitations

---

### Random Forest

Theory

Hyperparameters

Why selected

---

### Balanced Random Forest

Explain class weighting

Trade-offs

---

### Gradient Boosting

Explain boosting

Expected advantages

---

### Sequential Neural Network

Architecture

Activation functions

Loss function

Optimizer

---

### Regularized Sequential Network

Explain

* Batch Normalization
* Dropout
* Early Stopping

---

### Functional API

Explain why feature branches were investigated.

---

### Two-Month Lag Experiment

Explain the motivation for testing longer forecasting windows.

---

# 4. Results (700–900 words)

### Purpose

Present the experiments objectively before interpretation.

Structure

---

## Classical ML Results

Describe

Experiment 1

Experiment 2

Experiment 3

Experiment 4

Refer directly to

Table 1

Discuss

* Accuracy
* Precision
* Recall
* F1
* ROC-AUC

---

## Deep Learning Results

Describe

Experiment 5

Experiment 6

Experiment 7

Experiment 8

Discuss

* convergence
* validation loss
* validation ROC-AUC
* Early Stopping behaviour

---

## Comparative Analysis

Include the experiment comparison table.

State clearly that

**ROC-AUC is the primary evaluation metric because of class imbalance.**

Explain why the Regularized Sequential Network and Balanced Random Forest were selected as the strongest models.

---

# 5. Discussion (600–800 words)

### Purpose

Interpret the findings rather than repeating the results.

Include

---

## Learning Curves

Interpret divergence between training and validation curves.

Discuss overfitting.

---

## Confusion Matrices

Identify

* true positives
* false negatives
* false positives

Discuss humanitarian implications.

---

## ROC Curves

Interpret discrimination ability.

Explain why ROC-AUC was prioritized.

---

## Bias–Variance Trade-off

Compare

* Logistic Regression
* Random Forest
* Deep Learning

Discuss complexity versus generalization.

---

## Dataset Limitations

Discuss

* class imbalance
* reporting delays in ACLED
* county harmonization challenges
* missing temporal records
* exclusion of climatic variables
* exclusion of market prices
* exclusion of humanitarian assistance indicators

---

## Future Improvements

Recommend

* additional environmental predictors
* socioeconomic variables
* temporal deep learning architectures
* cost-sensitive learning
* probability calibration
* explainable AI techniques

Each recommendation should be justified.

---

# 6. Conclusion (300–400 words)

Summarize the research question.

Answer it directly.

Summarize the main findings.

State the best-performing models.

Reconnect the findings to the humanitarian mission.

Explain the broader contribution of machine learning to humanitarian early-warning systems.

End with future research directions.

---

# Figures

Integrate naturally within the discussion.

Include

* Pipeline diagram
* Class distribution
* Learning curves
* ROC curves
* Confusion matrices

Every figure should be referenced and interpreted within the surrounding text.

---

# Tables

Include

* Dataset summary
* Feature descriptions
* Hyperparameter summary
* Experiment comparison
* Final model comparison

Discuss every table within the text.

---

# References

Use at least 10–15 high-quality academic sources.

Prioritize

* peer-reviewed journal articles,
* conference papers,
* technical manuals,
* authoritative humanitarian reports.

Use IEEE citation style consistently throughout.

---

# Appendix

Include

* GitHub repository link
* Demo video link
* Reproducibility information
* Software versions and dependencies
