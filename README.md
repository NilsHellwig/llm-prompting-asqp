# Code: Do we still need Human Annotators? Prompting Large Language Models for Aspect Sentiment Quad Prediction

This repository contains the code, data, and results for the paper:

## 📄 Paper Abstract

Aspect sentiment quad prediction (ASQP) enables a detailed understanding of opinions expressed in a text by extracting four elements: the opinion term, aspect term, aspect category, and sentiment polarity for each opinion. However, creating annotated datasets to fine-tune ASQP models is resource-intensive.

In this study, we explore the capabilities of large language models (LLMs) for zero- and few-shot learning on the ASQP task across five diverse datasets. We report F1 scores nearly matching those of state-of-the-art fine-tuned models, and exceeding previously reported zero- and few-shot results. For example, in the 20-shot setting on the Rest16 restaurant domain dataset, LLMs achieved an F1 of **51.54**, compared to **60.39** by the fine-tuned MVP method. On the target aspect sentiment detection (TASD) task, LLMs achieved **68.93** on Rest16 in the 30-shot setting, compared to **72.76** with MVP.

Our findings suggest that while human annotators remain essential for top-tier performance, LLMs can meaningfully reduce the need for extensive manual annotation in ASQP tasks.

## ✨ Highlights

- Evaluated LLMs on ASQP and TASD across **five datasets**.
- Tested **0 to 50-shot** settings.
- Introduced a **new airline review ASQP dataset**.
- Compared zero-/few-shot LLMs against fine-tuned small language models (SLMs).
- Investigated **self-consistency prompting**.

## 📊 Research Questions

- **RQ1:** How does varying the number of few-shot examples (0–50) impact ASQP performance?
- **RQ2:** How do LLMs compare to fine-tuned SLMs on ASQP?
- **RQ3:** Does self-consistency prompting improve LLM performance on ASQP?

## 📦 Installation

```bash
pip install -r requirements.txt # install packages
python study/01_zeroshot.py # run all prompting conditions
```

## Authors

| Name                  | Group                  | Institution             | Location         | Email                                      |
|-----------------------|------------------------|-------------------------|------------------|-------------------------------------------|
| Nils Constantin Hellwig | Media Informatics Group | University of Regensburg | Regensburg, Germany | [nils-constantin.hellwig@ur.de](mailto:nils-constantin.hellwig@ur.de) |
| Jakob Fehle          | Media Informatics Group | University of Regensburg | Regensburg, Germany | [jakob.fehle@ur.de](mailto:jakob.fehle@ur.de) |
| Udo Kruschwitz       | Information Science Group | University of Regensburg | Regensburg, Germany | [udo.kruschwitz@ur.de](mailto:udo.kruschwitz@ur.de) |
| Christian Wolff      | Media Informatics Group | University of Regensburg | Regensburg, Germany | [christian.wolff@ur.de](mailto:christian.wolff@ur.de) |


## ✍ Citation

```tex
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

