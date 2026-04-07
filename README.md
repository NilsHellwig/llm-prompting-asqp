# Do we still need Human Annotators? Prompting LLMs for ASQP

<div align="center">

Accepted at **XLLM 2025** (1st Joint Workshop on LLMs and Structure Modeling) · Vienna, Austria

[![Paper](https://img.shields.io/badge/Paper_Download-ACL_Anthology-blue?style=for-the-badge&logo=googlescholar)](https://aclanthology.org/2025.xllm-1.15/)
[![Correspondence](https://img.shields.io/badge/Contact-Nils%20Hellwig-darkred?style=for-the-badge&logo=minutemailer)](mailto:nils-constantin.hellwig@ur.de)

---

**Nils Constantin Hellwig¹* · Jakob Fehle¹ · Udo Kruschwitz² · Christian Wolff¹**

¹Media Informatics Group, University of Regensburg, Germany  
²Information Science Group, University of Regensburg, Germany

*✉ Correspondence to: [nils-constantin.hellwig@ur.de](mailto:nils-constantin.hellwig@ur.de)*  
`{nils-constantin.hellwig, jakob.fehle, udo.kruschwitz, christian.wolff}@ur.de`

---

</div>

> **Abstract:** Aspect sentiment quad prediction (ASQP) facilitates a detailed understanding of opinions expressed in a text by identifying the opinion term, aspect term, aspect category and sentiment polarity for each opinion. However, annotating a full set of training examples to fine-tune models for ASQP is a resource-intensive process. In this study, we explore the capabilities of large language models (LLMs) for zero- and few-shot learning on the ASQP task across five diverse datasets. We report F1 scores almost up to par with those obtained with state-of-the-art fine-tuned models and exceeding previously reported zero- and few-shot performance. In the 20-shot setting on the Rest16 restaurant domain dataset, LLMs achieved an F1 score of 51.54, compared to 60.39 by the best-performing fine-tuned method MVP. Additionally, we report the performance of LLMs in target aspect sentiment detection (TASD), where the F1 scores were close to fine-tuned models, achieving 68.93 on Rest16 in the 30-shot setting, compared to 72.76 with MVP. While human annotators remain essential for achieving optimal performance, LLMs can reduce the need for extensive manual annotation in ASQP tasks.

---

## 🚀 Overview

This repository contains the official implementation of the paper **"Do we still need Human Annotators? Prompting Large Language Models for Aspect Sentiment Quad Prediction"**. We investigate the performance of Large Language Models (LLMs) in Zero-Shot and Few-Shot scenarios for complex Aspect-Based Sentiment Analysis (ABSA) tasks.

### Key Features
- **LLM Prompting Framework**: Scripts for evaluating LLMs on ASQP and TASD.
- **Multi-task Support**: Implementation for Target Aspect Sentiment Detection (TASD) and Aspect Sentiment Quad Prediction (ASQP).
- **Comprehensive Benchmarking**: Evaluation across five diverse datasets including a new airline review ASQP dataset.
- **Few-Shot Analysis**: Systematic study of performance from 0 to 50 annotated examples.
- **Self-Consistency**: Investigation of self-consistency prompting strategies.

## 📁 Repository Structure

- `classifier/`: Implementation of different classification strategies and model-specific wrappers.
- `datasets/`: Data for ASQP and TASD tasks (Rest15, Rest16, Hotels, Coursera, etc.).
- `fs_examples/`: Few-shot examples used for in-context learning.
- `generations/`: Output directory for LLM-generated predictions and baselines.
- `prompt/`: Template files for different prompting strategies.
- `study/`: Main execution scripts for the experimental studies (zero-shot, few-shot, etc.).
- `dataloader.py`, `promptloader.py`: Utilities for loading data and prompts.
- `evaluation.py`, `validator.py`: Scripts for calculating metrics and validating outputs.
- `llm.py`: Interface for interacting with Large Language Models.

## 🛠️ Setup & Usage

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nilshellwig/llm-prompting-asqp.git
   cd llm-prompting-asqp
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Experiments

To replicate the zero-shot experiments:
```bash
python study/01_zeroshot.py
```

To run the baseline evaluations:
```bash
python study/00_baselines.py
```

## 📜 Citation

```bibtex
@inproceedings{hellwig-etal-2025-still,
    title = "Do we still need Human Annotators? Prompting Large Language Models for Aspect Sentiment Quad Prediction",
    author = "Hellwig, Nils Constantin  and
      Fehle, Jakob  and
      Kruschwitz, Udo  and
      Wolff, Christian",
    editor = "Fei, Hao  and
      Tu, Kewei  and
      Zhang, Yuhui  and
      Hu, Xiang  and
      Han, Wenjuan  and
      Jia, Zixia  and
      Zheng, Zilong  and
      Cao, Yixin  and
      Zhang, Meishan  and
      Lu, Wei  and
      Siddharth, N.  and
      {\O}vrelid, Lilja  and
      Xue, Nianwen  and
      Zhang, Yue",
    booktitle = "Proceedings of the 1st Joint Workshop on Large Language Models and Structure Modeling (XLLM 2025)",
    month = aug,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.xllm-1.15/",
    doi = "10.18653/v1/2025.xllm-1.15",
    pages = "153--172",
    ISBN = "979-8-89176-286-2",
    abstract = "Aspect sentiment quad prediction (ASQP) facilitates a detailed understanding of opinions expressed in a text by identifying the opinion term, aspect term, aspect category and sentiment polarity for each opinion. However, annotating a full set of training examples to fine-tune models for ASQP is a resource-intensive process. In this study, we explore the capabilities of large language models (LLMs) for zero- and few-shot learning on the ASQP task across five diverse datasets. We report F1 scores almost up to par with those obtained with state-of-the-art fine-tuned models and exceeding previously reported zero- and few-shot performance. In the 20-shot setting on the Rest16 restaurant domain dataset, LLMs achieved an F1 score of 51.54, compared to 60.39 by the best-performing fine-tuned method MVP. Additionally, we report the performance of LLMs in target aspect sentiment detection (TASD), where the F1 scores were close to fine-tuned models, achieving 68.93 on Rest16 in the 30-shot setting, compared to 72.76 with MVP. While human annotators remain essential for achieving optimal performance, LLMs can reduce the need for extensive manual annotation in ASQP tasks."
}
```

