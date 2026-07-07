# Predicting User Vulnerability to Deceptive Interface Design Using Multimodal Neural and Behavioral Modeling

<!-- Graphical abstract centered -->
<p align="center">
  <img src="ga.png" alt="Graphical Abstract" width="800">
</p>

<p align="center">
  <b>Graphical Abstract:</b> A neuroergonomic framework integrating multimodal signals to predict user vulnerability to deceptive interface designs.
</p>

---

## 📌 Overview

This repository contains the official implementation, datasets, and analysis for the research submitted to the *International Journal of Human-Computer Studies (IJHCS)*.

This work investigates the cognitive and neural signatures of deceptive interface designs (dark patterns). By fusing high-temporal-resolution EEG, high-spatial-resolution fNIRS, and behavioral eye-tracking, we provide an objective predictive model to quantify user vulnerability and "forced compliance" in digital environments.

### 🚀 Key Research Contributions

- **Multimodal Fusion:** Integration of neural and behavioral signals to map subconscious cognitive strain.
- **Predictive Modeling:** A deep learning pipeline capable of classifying vulnerability states.
- **Explainable AI (XAI):** Implementation of SHAP to identify the specific neural markers, such as frontal theta oscillations, that drive the model's predictions.
- **Empirical Validation:** Rigorous statistical analysis of linguistic complexity and its correlation with neural fatigue.

---

## 📊 Key Visualizations & Results

### 🧠 Neuro-Cognitive & Linguistic Analysis

The following figures demonstrate the relationship between manipulative microcopy and the resulting cognitive impact:

<p align="center">
  <img src="figure1_linguistic_feature_profiles.png" alt="Linguistic Profiles" width="500">
  <br><i>Figure 1: Linguistic feature profiles across dark-pattern types.</i>
</p>

<p align="center">
  <img src="radar_neuro_cognitive_indices.png" alt="Radar Plot" width="500">
  <br><i>Figure 2: Radar plot demonstrating the distribution of neuro-cognitive indices.</i>
</p>

### 📈 Statistical Highlights

Our analysis revealed significant differences across dark-pattern types (p < .001), demonstrating that manipulative language directly triggers measurable neural responses.

| Feature | F-statistic | p-value | Significance |
| :--- | :---: | :---: | :---: |
| Cognitive Load (fNIRS) | 35.62 | < .001 | * |
| Neural Fatigue (EEG) | 19.87 | < .005 |  |
| Linguistic Complexity | 42.18 | < .001 | * |

**Key Insight:** Our findings indicate that "Confirmshaming" and "Trick Questions" trigger significantly higher frontal theta power, representing a peak in inhibitory control effort and cognitive dissonance.

---

## 📂 Repository Structure
```text
├── data/                    # Dataset containing 360+ microcopy samples
│   ├── raw/                 # Original signal recordings
│   └── processed/           # Feature-extracted CSVs (EEG, fNIRS, Gaze)
├── analysis/                # Statistical scripts and outputs (ANOVA, Tukey, Regression)
├── src/                     # Core source code
│   ├── preprocessing/       # ICA, filtering, and artifact removal
│   ├── feature_extraction/  # PSD, entropy, and linguistic features
│   └── models/              # Deep learning architectures and XAI (SHAP)
├── paper/                   # Research documentation and appendices
└── main.py                  # Execution entry point for prediction and evaluation
