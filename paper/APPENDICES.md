# Appendices: Neuro-Linguistic Signatures of Dark-Pattern Microcopy

This document contains supplementary materials for the research paper.

---

## Appendix A: Computational Linguistics Model (CLM) Settings
The linguistic analysis was performed using the following parameters:
- **Lexical Density Formula:** (Total Content Words / Total Words) × 100
- **Sentiment Scoring:** VADER (Valence Aware Dictionary and sEntiment Reasoner)
- **Complexity Index:** Weighted combination of sentence length, passive voice frequency, and cognitive verb density.

## Appendix B: Neuro-Physiological Instrumentation
- **fNIRS Device:** Artinis Brite24 (24 channels, 758nm & 845nm wavelengths).
- **EEG System:** 32-channel dry-electrode (Standard 10-20 system).
- **Sampling Rate:** fNIRS: 10Hz | EEG: 500Hz.
- **Preprocessing Pipeline:** Band-pass filter (0.01–0.2 Hz for fNIRS), Artifact removal via ICA.

## Appendix C: Detailed Statistical Tables
For full Tukey HSD post-hoc comparisons, please refer to the files in the `/analysis` folder:
- `anova_all_features_results.csv`
- `tukey_all_features_results.csv`

## Appendix D: NASA Task Load Index (NASA-TLX)
Participants were evaluated on 6 dimensions post-stimulus:
1. **Mental Demand:** How much mental and perceptual activity was required?
2. **Temporal Demand:** How much time pressure did you feel?
3. **Performance:** How successful were you in accomplishing the task?
4. **Effort:** How hard did you have to work?
5. **Frustration:** How insecure, discouraged, or annoyed did you feel?

## Appendix E: Microcopy Stimuli Samples (N=360)
The full dataset is available in `/data/dark_patterns_microcopy_360_enriched.csv`.
- **Sample Pattern (Confirmshaming):** "No thanks, I prefer paying full price."
- **Sample Pattern (Fake Urgency):** "Only 2 items left - order in 02:45!"
