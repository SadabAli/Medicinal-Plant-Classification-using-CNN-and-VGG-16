# 🌿 Medicinal-Plant-Classification-using-CNN-and-VGG-16

This project focuses on classifying 30 different medicinal plants using deep learning models (Custom CNN and VGG-16) and explains the model predictions using XAI (Explainable AI). This work was accepted and presented at the **1st International Conference on Machine Intelligence and Data Science** (Springer) held at **CUTM, Paralakhemundi**.

---

## 📌 Table of Contents

- [About the Project](#about-the-project)
- [Dataset](#dataset)
- [Models Used](#models-used)
- [Explainable AI (XAI)](#explainable-ai-xai)
- [Project Results](#project-results)
- [How to Clone](#how-to-clone)
- [Installation](#installation)
- [How to Run the Project](#how-to-run-the-project)
- [Acknowledgements](#acknowledgements)

---

## 🔬 About the Project

The aim of this project is to identify medicinal plants using leaf images by applying image classification techniques. Deep learning is used to automate plant identification for applications in agriculture, healthcare, and education.

---

## 📁 Dataset

- The dataset contains **30 classes** of medicinal plant leaf images.
- Some of the classes:  
  `Tulsi, Neem, Guava, Mint, Curry, Jasmine, Jackfruit, Sandalwood, Pomegranate`, etc.
- Each class contains multiple images with variations in lighting, background, and angles.
- Images were preprocessed with **resizing**, **normalization**, and **augmentation**.

---

## 🧠 Models Used

### 1. Custom CNN
- A self-built CNN model with convolutional, pooling, and dense layers.
- Achieved around **85% accuracy**.

### 2. VGG-16 (Transfer Learning)
- Pretrained model fine-tuned for our dataset.
- Achieved around **99% accuracy**.
- Faster convergence and better generalization than custom CNN.

---

## 💡 Explainable AI (XAI)

To improve the transparency and trust of our deep learning model, we implemented Explainable AI techniques.

### 🔍 Techniques Used:

#### ✅ Grad-CAM (Gradient-weighted Class Activation Mapping)
- Highlights important regions in the image that the model focused on while making a prediction.
- Helps verify whether the model is learning relevant features like leaf texture, shape, and edges.
- Provides heatmaps to visually explain the classification result.

#### ✅ LIME (Local Interpretable Model-agnostic Explanations)
- Offers local visual explanations by perturbing parts of the image and observing the model's output.
- Identifies the top superpixels (regions) that influenced the model’s decision.
- Useful in understanding which specific parts of the leaf image were important for classification.
- Builds trust by showing human-understandable visual reasons behind predictions.

These XAI methods help researchers, botanists, and users interpret deep learning predictions more effectively, making the system more transparent and reliable.

---

## 📊 Project Results

| Model      | Accuracy | Strengths                          |
|------------|----------|----------------------------------|
| CNN        | ~85%     | Simpler, interpretable architecture |
| VGG-16     | ~99%     | High accuracy, pretrained features  |
| XAI (Grad-CAM / LIME) | - | Visual explanations for decisions |

- Accuracy and loss curves are plotted for both models.
- Confusion matrices are used to analyze class-wise performance.

---

## 🛠 How to Clone

```bash
git clone https://github.com/SadabAli/Medicinal-Plant-Classification-using-CNN-and-VGG-16.git
cd Medicinal-Plant-Classification-using-CNN-and-VGG-16
```
## ⚙️ Installation
Make sure you have Python 3.8+ installed.

1. Create a virtual environment (optional but recommended)
```
python -m venv env
```
2. Activate the virtual environment
On Windows:
```
.\env\Scripts\activate
```
On Linux/MacOS:
```
source env/bin/activate
```
3. Install dependencies
```
pip install -r requirements.txt
```
## 🚀 How to Run the Project
Run the main application Scripts
```
python medical_plant.py
```
Open the web app
After running the script, open your browser and go to:
```
http://127.0.0.1:5000/
```

## Acknowledgements
Presented at 1st International Conference on Machine Intelligence and Data Science (Springer), CUTM Bhubaneswar.

Special thanks to the Faculty of Engineering and Technology, CUTM for continuous support.

Inspired by the goal of making AI useful in real-world problems like medicinal plant identification.
