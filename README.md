# Predicting User Vulnerability to Deceptive Interface Design Using Multimodal Neural and Behavioral Modeling

<p align="center">
  <img src="ga.png" alt="Graphical Abstract" width="800">
</p>

<p align="center">
  <b>Graphical Abstract:</b> A neuroergonomic framework integrating multimodal signals to predict user vulnerability to deceptive interface designs.
</p>

---

## 📌 Overview

This repository contains the official implementation, datasets, and analysis for the research submitted to the *International Journal of Human-Computer Studies (IJHCS)*.

While previous research, such as our work on neuro-linguistic signatures, focused on the linguistic impact of dark patterns, this study advances the field by developing a **predictive multimodal framework**. We investigate how the fusion of neural and behavioral data can identify the “tipping point” of user vulnerability, where deceptive interface designs lead to forced compliance.

## 🧠 Core Methodology

This project moves beyond unimodal analysis by implementing a high-dimensional fusion of:

- **Neural Indicators:** High-temporal-resolution EEG and high-spatial-resolution fNIRS, measuring cognitive load and affective pressure
- **Behavioral Measures:** Precise eye-tracking metrics, including gaze, fixation, and saccades
- **Linguistic Features:** Analysis of manipulative microcopy and deceptive framing
- **Advanced Modeling:** A deep learning pipeline designed to predict vulnerability states

---

## 🚀 Key Research Contributions

- **Multimodal Fusion Framework:** Integration of EEG, fNIRS, and eye-tracking to create a holistic map of user vulnerability
- **Vulnerability Prediction:** Moving from describing dark patterns to predicting user susceptibility using neural markers
- **Explainable AI (XAI):** Implementation of SHAP (*SHapley Additive exPlanations*) to reveal the neural markers, such as frontal theta oscillations, that drive model predictions
- **Bridging Disciplines:** An interdisciplinary approach combining HCI, NeuroIS, computational linguistics, and digital ethics

---

## 📊 Visualizations & Results

### 📉 Neuro-Cognitive Analysis

The following figure illustrates the neuro-cognitive indices and the predictive accuracy of the multimodal model:

<p align="center">
  <img src="radar_neuro_cognitive_indices.png" alt="Radar Plot" width="500">
</p>

<p align="center">
  <i>Figure 1: Radar plot demonstrating the distribution of neuro-cognitive indices across different deceptive interface categories.</i>
</p>

---

## 📂 Repository Structure
```text
├── data/                         # Processed datasets for multimodal analysis
│   ├── raw/                      # Original signal recordings
│   └── processed/                # Feature-extracted CSVs (EEG, fNIRS, Gaze)
├── src/                          # Source code for the pipeline
│   ├── preprocessing/            # ICA, band-pass filtering, and artifact removal
│   ├── feature_extraction/       # PSD, entropy, and linguistic features
│   └── models/                   # Deep learning architectures and XAI (SHAP)
├── results/                      # Final outputs
│   └── figures/                  # All figures used in the manuscript (including ga.png)
└── main.py                       # Execution entry point for prediction and evaluation
