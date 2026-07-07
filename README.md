# Predicting User Vulnerability to Deceptive Interface Design Using Multimodal Neural and Behavioral Modeling

<!-- Graphical Abstract - Corrected path for Root README -->
<p align="center">
  <img src="paper/ga.png" alt="Graphical Abstract" width="800">
</p>

<p align="center">
  <b>Graphical Abstract:</b> A neuroergonomic framework integrating multimodal signals to predict user vulnerability to deceptive interface designs.
</p>

---

## 📌 Research Overview

This repository contains the implementation, datasets, and statistical analysis for our study on the cognitive and neural signatures of deceptive interface designs (dark patterns).

By fusing high-temporal-resolution EEG, high-spatial-resolution fNIRS, and behavioral eye-tracking, we develop a predictive model to quantify user vulnerability. Our framework identifies how specific dark patterns (e.g., Trick Questions, Confirmshaming) bypass conscious deliberation and trigger "forced compliance."

### 🚀 Key Technical Contributions

- **Multimodal Signal Fusion:** Integrated EEG (Theta/Alpha), fNIRS (HbO/HbR), and eye-tracking (fixation/saccades).
- **GRU-based Temporal Modeling:** A Gated Recurrent Unit (64 units, dropout 0.3) architecture optimized for neuro-temporal sequences.
- **Explainable AI (SHAP):** Identification of neural markers (frontal theta oscillations) driving vulnerability predictions.
- **Linguistic Normalization:** Analysis of microcopy features including negation density and syntactic complexity.

---

## 📊 Empirical Results (Verified Data)

### 🧠 Statistical Highlights (ANOVA)

Based on the experimental data ($N = 40$ participants, $360$ trials), we observed significant neural and behavioral differences across deceptive conditions ($p < .001$):

| Feature | F-statistic | p-value | Significance |
| :--- | :---: | :---: | :---: |
| Cognitive Load (fNIRS HbO) | 28.45 | < .001 | * |
| Neural Fatigue (EEG Theta) | 22.12 | < .001 | * |
| Linguistic Complexity | 31.08 | < .001 | * |
| Response Time (Behavioral) | 18.94 | < .005 |  |

💡 **Key Finding:** "Trick Questions" and "Confirmshaming" conditions exhibited the highest frontal theta power and P300 latency, indicating significant inhibitory control effort and cognitive dissonance.

---

## 🛠️ Methodology & Pipeline

### 1. Neuro-Signal Processing

- **EEG:** Band-pass filtering (1–40 Hz), ICA for artifact removal, and spectral power extraction (Theta/Alpha).
- **fNIRS:** Wavelet filtering for motion correction and conversion to HbO/HbR signals.

### 2. Model Architecture (GRU)

Our predictive pipeline utilizes a GRU temporal model:

- **Hidden Layers:** 64 units with Tanh activation.
- **Optimization:** Adam optimizer ($1 \times 10^{-3}$) with early stopping.
- **XAI:** SHAP values used to interpret the contribution of P300 amplitude and fixation duration.

---

## 📂 Repository Structure
```text
├── data/                    # Processed datasets (360 samples)
│   └── dark_patterns_microcopy_enriched.json
├── src/                     # Implementation code
│   ├── preprocessing/       # ICA and wavelet filtering
│   ├── models/              # GRU architecture & training
│   └── explainability/      # SHAP interpretation scripts
├── analysis/                # Statistical modeling (mixed-effects, ANOVA)
├── paper/                   # Appendices and high-resolution figures
└── main.py                  # Entry point for model evaluation
