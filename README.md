# Predicting Food Insecurity Risk from Conflict Dynamics in South Sudan

Summative project for Introduction to Machine Learning, applying classical ML
and deep learning to predict food insecurity crises from armed conflict patterns.

## Problem Statement

South Sudan faces recurring, overlapping crises of armed conflict and food
insecurity. This project investigates whether county-level conflict event data
(ACLED) can anticipate food security outcomes (FEWS NET IPC classifications),
supporting earlier, more targeted humanitarian and peacebuilding response.

## Mission Alignment

This project supports the goal of fostering enduring peace and sustainable
development in South Sudan and Africa at large — examining whether conflict
indicators provide meaningful early-warning signal for food insecurity, and
informing where peacebuilding and humanitarian response should be prioritised.

## Repository Structure

```
.
├── data/
│   ├── raw/                        # ACLED and FEWS NET CSVs (add yours here)
│   └── README.md                   # Data dictionary, sources, known issues
├── notebooks/
│   └── main_analysis.ipynb         # Full pipeline: EDA → preprocessing → models → evaluation
├── src/
│   ├── __init__.py
│   ├── data_loading.py             # CSV loaders
│   └── preprocessing.py            # Cleaning, aggregation, merge logic
├── docs/
│   ├── experiment_log.md           # Running log of all experiments (rubric requirement)
│   └── report_outline.md           # Written report checklist
├── reports/
│   └── figures/                    # Exported plots for the written report
├── scripts/
│   └── build_notebook.py           # Regenerates main_analysis.ipynb from scratch
├── requirements.txt
└── README.md
```

## Setup

```bash
python -m venv venv
source venv/bin/activate            # Windows: venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook notebooks/main_analysis.ipynb
```

## Data Sources

- **ACLED** — Armed Conflict Location & Event Data Project, South Sudan.
  https://acleddata.com
- **FEWS NET** — Famine Early Warning Systems Network, IPC classifications.
  https://fews.net

See `data/README.md` for full attribution, filter settings, and known issues.

## Deliverables

- Written report: [link]
- Demo video: [link]
- GitHub repository: [link]

## Reproducibility

- Random seed `SEED = 42` set in the notebook setup cell for numpy, Python
  `random`, and TensorFlow.
- Raw data committed to `data/raw/` so the notebook runs without credentials.
- Run all cells top-to-bottom from a fresh kernel before submitting.
