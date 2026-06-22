# Predicting Food Insecurity Risk from Conflict Dynamics in South Sudan

Summative project for [Module Name], applying classical machine learning and
deep learning approaches to a real-world problem in South Sudan.

## Problem Statement

[Write 2–3 sentences here summarizing your problem statement — expand fully
in your written report's introduction. Starting point: South Sudan faces
recurring, overlapping crises of armed conflict and food insecurity. This
project explores whether county-level conflict event data (ACLED) can help
anticipate food security outcomes (FEWS NET IPC classifications), as a step
toward earlier, more targeted humanitarian and peacebuilding response.]

## Mission Alignment

This project supports the goal of fostering enduring peace and sustainable
development in South Sudan and Africa at large, by examining whether
conflict indicators provide meaningful early-warning signal for food
insecurity — informing where peacebuilding and humanitarian response might
be prioritized.

## Repository Structure

```
.
├── data/
│   ├── raw/                    # Original ACLED and FEWS NET downloads
│   └── README.md               # Data dictionary, sources, access dates
├── notebooks/
│   └── main_analysis.ipynb     # Full pipeline: EDA, preprocessing, models, evaluation
├── src/
│   ├── data_loading.py         # CSV loaders
│   └── preprocessing.py        # County standardization, aggregation, merge logic
├── docs/
│   ├── experiment_log.md       # Running log of all experiments (rubric requirement)
│   └── report_outline.md       # Checklist for the written report's required sections
├── reports/
│   └── figures/                # Exported plots for use in the written report
├── requirements.txt
└── README.md
```

## Setup

```bash
git clone <your-repo-url>
cd south-sudan-conflict-foodsecurity-ml
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook notebooks/main_analysis.ipynb
```

## Data Sources

- **ACLED** (Armed Conflict Location & Event Data Project) — South Sudan,
  event-level conflict data. https://acleddata.com
- **FEWS NET** (Famine Early Warning Systems Network) — South Sudan, IPC
  food security phase classifications. https://fews.net

Full attribution, filter settings, and known data issues: see
[`data/README.md`](data/README.md).

## Deliverables

- Written report: [link]
- Demo video: [link]
- This repository: [link]

## Reproducibility Notes

- Random seeds are set in the notebook's setup cell (`SEED = 42`) for numpy,
  Python's `random`, and TensorFlow.
- Raw data is committed to this repo (`data/raw/`) so the notebook runs
  without needing ACLED/FEWS NET credentials.
- Run all cells top-to-bottom from a fresh kernel before submitting, to
  confirm there are no hidden state dependencies.
