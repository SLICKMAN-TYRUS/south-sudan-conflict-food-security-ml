# Written Report Checklist

Target: 3,500–5,000 words (excluding references, captions, appendices).
Style: IEEE citations, prose throughout (no excessive bullet points), your
authentic voice. AI-detected content must stay below 20%.

## Sections

- [ ] **Introduction** — problem statement with cited evidence (not just asserted),
      mission alignment, overview of approach
- [ ] **Literature Review** — 10+ scholarly sources, IEEE in-text citations,
      sources *compared critically* against each other (not just summarised
      one after another), gaps in existing work that your project addresses
- [ ] **Methodology**
  - [ ] Both datasets described and justified with attribution
  - [ ] Every preprocessing decision explained: county-name fixes (all 3),
        the 6 documented gaps, filter_ipc rationale, lag window choice,
        population_best handling, target variable definition and threshold
  - [ ] Model architectures described with justification for design choices
  - [ ] Chronological split explained and justified (why not random)
- [ ] **Results** — experiment table referenced in text, all 8 experiments
      described with metrics, figures integrated (not just pasted)
- [ ] **Discussion**
  - [ ] Learning curves interpreted (specific divergence patterns cited)
  - [ ] Confusion matrices interpreted (which classes confused and why)
  - [ ] ROC/AUC discussion tied to class balance and application context
  - [ ] Bias-variance tradeoff discussed across model types
  - [ ] Dataset limitations (date gap, county mismatches, ACLED underreporting
        in remote areas, 2017+ restriction)
  - [ ] Proposed improvements with specific justification
- [ ] **Conclusion** — findings summarised, explicit tie to mission
      (does conflict data provide early-warning signal?), future work
- [ ] **References** — IEEE format, complete list, 10+ sources
- [ ] Links to GitHub and demo video in the report
- [ ] No plagiarism, no excessive AI-generated text
- [ ] Read it aloud once — does it sound like you explaining your reasoning?

## Suggested sources to find and cite (IEEE format)

1. Maystadt, J-F. & Ecker, O. (2014) — conflict and food security linkages
2. Maxwell, D. et al. (2020) — IPC methodology and humanitarian thresholds
3. Hegre, H. et al. (ViEWS project) — ML for conflict forecasting
4. Raleigh, C. et al. (2010) — introducing ACLED methodology
5. Von Uexkull, N. et al. (2016) — civil conflict and food security
6. Buhaug, H. et al. — climate, conflict, food in Sub-Saharan Africa
7. Hochreiter & Schmidhuber (1997) — LSTM (for DL architecture justification)
8. Breiman, L. (2001) — Random Forests
9. IPC Global Partners (2021) — IPC technical manual v3.1 (cite the threshold)
10. Peters, K. et al. — humanitarian early warning systems
