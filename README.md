# Parkinson's Disease Detection

This project focuses on detecting Parkinson's Disease using machine learning techniques. Parkinson's Disease is a neurodegenerative disorder that affects movement and often includes tremors. Early and accurate detection can help in managing and treating the disease effectively. This repository provides an implementation of various machine learning models to classify and predict the presence of Parkinson's Disease using a dataset containing biomedical voice measurements.

## Introduction

Parkinson's Disease affects millions of people worldwide. The challenge in detecting Parkinson's lies in the overlapping symptoms with other diseases and the lack of early diagnostic tools. This project aims to use machine learning algorithms to provide a more accurate diagnosis of Parkinson's by analyzing various biomedical features extracted from voice recordings.

## Dataset

The dataset used in this project contains biomedical voice measurements from 31 people, 23 with Parkinson's and 8 healthy individuals. The attributes in the dataset include several measures of variation in fundamental frequency, measures of variation in amplitude, and nonlinear dynamic complexity measures.

### Features

Some of the key features in the dataset are:

- MDVP: Fo(Hz) - Average vocal fundamental frequency
- MDVP: Fhi(Hz) - Maximum vocal fundamental frequency
- MDVP: Flo(Hz) - Minimum vocal fundamental frequency
- MDVP: Jitter(%), Jitter(Abs), RAP, PPQ, DDP - Several measures of variation in fundamental frequency
- MDVP: Shimmer, Shimmer(dB), APQ3, APQ5, APQ, DDA - Several measures of variation in amplitude
- NHR, HNR - Two measures of ratio of noise to tonal components in the voice

## Methodology

The project involves the following steps:

1. **Data Preprocessing**: Cleaning the data, handling missing values, and scaling the features.
2. **Exploratory Data Analysis (EDA)**: Visualizing the data to understand the distribution of various features.
3. **Feature Engineering**: Selecting the most relevant features that help in the classification of Parkinson's Disease.
4. **Model Training**: Applying various machine learning models, such as Support Vector Machines (SVM), Random Forest, XGBoost, and Neural Networks.
5. **Model Evaluation**: Evaluating the models based on accuracy, precision, recall, F1-score, and confusion matrix.

## Dependencies

To run this project, you'll need the following libraries:

- Python 3.7+
- NumPy
- Pandas
- Scikit-Learn
- Matplotlib
- Seaborn

Install the dependencies using pip:

```bash
pip install numpy pandas scikit-learn matplotlib seaborn
```

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/arhanbasu/Parkinsons_detect.git
   cd Parkinsons_detect
   ```

2. Run the Jupyter Notebook to see the implementation of various models and their performance:

   ```bash
   jupyter notebook Parkinsons_Detection.ipynb
   ```

3. You can modify the code to experiment with different models or parameters.

## Results

The performance of the models is evaluated using various metrics. Here are some of the results:

- **Support Vector Machine (SVM)**: Achieved an accuracy of 95%.
- **Random Forest Classifier**: Achieved an accuracy of 93%.
- **XGBoost Classifier**: Achieved an accuracy of 96%.

The models show promising results in predicting Parkinson's Disease using the provided dataset. Further improvements can be made by fine-tuning the parameters and using advanced deep learning models.
