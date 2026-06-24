# Predicting Food Insecurity Risk from Conflict Dynamics in South Sudan

*A comparative machine learning and deep learning approach for humanitarian early-warning systems.*

---

# Project Overview

Food insecurity remains one of the most pressing humanitarian challenges in South Sudan, where prolonged armed conflict continues to disrupt livelihoods, agricultural production, and access to essential resources. Humanitarian organizations rely on periodic food security assessments to guide emergency interventions; however, these assessments often provide limited lead time for proactive response.

This project investigates whether **historical conflict event data can be used to predict county-level food security crises one month in advance**. Using conflict records from the **Armed Conflict Location & Event Data (ACLED)** project and food security classifications from **FEWS NET / IPC**, a complete machine learning pipeline was developed to compare traditional machine learning models with deep learning approaches for humanitarian forecasting.

Rather than replacing existing humanitarian assessments, the project demonstrates how conflict data can serve as an additional early-warning signal to support more timely, evidence-based decision-making.

---

# Research Question

> **Can county-level conflict event data predict the likelihood of a food security crisis one month in advance?**

---

# Mission Alignment

This project supports the broader goal of improving humanitarian decision-making and promoting sustainable development in conflict-affected regions. By identifying patterns that precede food insecurity, the developed models demonstrate how machine learning can assist governments, humanitarian organizations, and peacebuilding agencies in prioritizing interventions before conditions deteriorate.

---

# Project Objectives

The project was designed to:

* Develop an end-to-end machine learning pipeline for conflict-driven food security forecasting.
* Compare the performance of classical machine learning models and deep learning architectures.
* Evaluate model performance using metrics appropriate for imbalanced classification problems.
* Investigate how feature engineering, class balancing, regularization, and temporal forecasting windows influence predictive performance.
* Assess the practical applicability of machine learning for humanitarian early-warning systems.

---

# Repository Structure

```text
.
├── data/
│   ├── raw/
│   └── README.md
│
├── notebooks/
│   └── main_analysis.ipynb
│
├── src/
│   ├── data_loading.py
│   ├── preprocessing.py
│   └── __init__.py
│
├── docs/
│   ├── experiment_log.md
│   └── report_outline.md
│
├── reports/
│   └── figures/
│
├── scripts/
│   └── build_notebook.py
│
├── requirements.txt
└── README.md
```

---

# Dataset

Two publicly available datasets were integrated.

### ACLED (Armed Conflict Location & Event Data)

Provides detailed records of conflict events including:

* event type
* fatalities
* actors involved
* event date
* county location

Conflict events were aggregated into monthly county-level features.

### FEWS NET / IPC

Provides county-level food security assessments using the Integrated Food Security Phase Classification (IPC).

The binary prediction target was defined as:

* **IPC Phase < 3 → No Crisis**
* **IPC Phase ≥ 3 → Crisis**

This threshold reflects internationally recognised humanitarian intervention criteria.

---

# Methodology

The notebook implements a complete reproducible machine learning workflow:

1. Data loading and validation
2. Exploratory data analysis
3. Data cleaning and county harmonisation
4. Feature engineering
5. Chronological train–test split
6. Classical machine learning experiments
7. Deep learning experiments
8. Hyperparameter optimisation
9. Model evaluation
10. Comparative analysis and conclusions

To preserve the temporal nature of the forecasting problem, all experiments used a **chronological split**, training on **2017–2022** data and evaluating on **2023–2025** observations.

---

# Models Evaluated

## Classical Machine Learning

* Logistic Regression
* Random Forest
* Balanced Random Forest
* Gradient Boosting

## Deep Learning

* Sequential Neural Network
* Regularized Sequential Neural Network
* Functional API Neural Network
* Functional API with Two-Month Forecast Horizon

---

# Evaluation Strategy

The modelling dataset is highly imbalanced (approximately **87.7% Crisis** and **12.3% No Crisis**).

For this reason, **ROC-AUC was used as the primary evaluation metric**, since it measures a model's ability to distinguish between crisis and non-crisis observations across all decision thresholds.

The following supporting metrics were also reported:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion matrices
* Learning curves
* ROC curves

---

# Key Findings

The experiments demonstrated several important findings.

* Baseline Logistic Regression and Random Forest models achieved high overall accuracy (~88–89%) but largely predicted the majority crisis class.
* Introducing class weighting substantially improved minority-class detection, making the Balanced Random Forest the strongest classical machine learning model.
* The Regularized Sequential Neural Network achieved the strongest overall generalization, maintaining a validation ROC-AUC of approximately **0.80** while reducing overfitting through Batch Normalization, Dropout, and Early Stopping.
* Increasing architectural complexity through the Functional API did not improve predictive performance.
* Extending the forecasting horizon from one month to two months reduced predictive accuracy, indicating that recent conflict events provide the strongest predictive signal.

Overall, the experiments showed that **careful feature engineering, class balancing, and regularization contributed more to model performance than increasing model complexity alone.**

---

# Reproducing the Project

Clone the repository and install the project dependencies.

```bash
git clone <https://github.com/SLICKMAN-TYRUS/south-sudan-conflict-food-security-ml.git>

cd <south-sudan-conflict-food-security-ml>

python -m venv venv

source venv/bin/activate

# Windows
# venv\Scripts\activate

pip install -r requirements.txt
```

Run the notebook from a fresh environment.

```bash
jupyter notebook notebooks/main_analysis.ipynb
```

Execute every notebook cell from top to bottom.

Random seeds are fixed (`SEED = 42`) for Python, NumPy, and TensorFlow to maximise reproducibility.

---

# Repository Deliverables

* Final Jupyter Notebook
* Written Research Report
* Experiment Log
* Supporting Figures
* Presentation Video
* Source Code

---

# References

## Datasets

* Armed Conflict Location & Event Data (ACLED): https://acleddata.com
* FEWS NET: https://fews.net

---

# Links

**GitHub Repository**

> *(https://github.com/SLICKMAN-TYRUS/south-sudan-conflict-food-security-ml.git)*

**Presentation Video**

> *(https://drive.google.com/drive/folders/1DUYqIahGVkO0ylwS6aLjE9tTVxMb84Ye?usp=sharing)*



# Acknowledgements

This project was completed as part of the **Introduction to Machine Learning** course. Publicly available conflict and food security datasets were used exclusively for academic purposes. All preprocessing, feature engineering, model development, experimentation, analysis, and interpretation were conducted by the author.
