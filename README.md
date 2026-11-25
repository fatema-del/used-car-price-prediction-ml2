https://used-car-price-prediction-ml2-nqpgjvqntpxtnrnaamsbsn.streamlit.app/

## Project Overview
This project uses machine learning to analyze used car data. Our goal is to predict used car prices and classify cars into different price categories based on their features.

## Project Objectives
- Predict used car prices using Linear Regression.
- Classify used cars into Low, Medium, and High price categories using Decision Tree Classification.
- Evaluate both models using different performance metrics.
- Use cross-validation and Grid Search to test model performance.

## Dataset
We used a cleaned used car dataset containing information about vehicles, such as year, manufacturer, model, condition, fuel type, transmission, odometer, car age, and other features.

Due to the large file size, the dataset is hosted on Google Drive instead of being uploaded directly to GitHub.

[Download the Dataset](https://drive.google.com/file/d/1a2KoBE-C8xiIY4LYQ3ZhvCgKLI8k-GhP/view?usp=sharing)

## Machine Learning Models

### Linear Regression
Linear Regression was used to predict the numerical price of used cars. The model was evaluated using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R².

### Decision Tree Classifier
A Decision Tree Classifier was used to classify cars into three price categories:

- **Low:** Below $7,500
- **Medium:** $7,500 to less than $16,800
- **High:** $16,800 or above

The classification model was evaluated using Accuracy, Precision, Recall, and F1-score.

## Model Tuning
Grid Search with cross-validation was used to test different model parameters and select the best settings.

### Linear Regression
- Best parameter: `fit_intercept=False`
- Best CV MAE: `5771.38`

### Decision Tree
- Criterion: `gini`
- Maximum depth: `10`
- Minimum samples per leaf: `5`
- Best CV Accuracy: `0.7125`

## Tools and Technologies
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Google Colab

## Project Files
- **Google Colab Notebook (.ipynb):** Includes the code, data preparation, model building, evaluation, and tuning.
- **Cleaned Dataset (.csv):** Available through the Google Drive link above.
- **Project Report (.docx):** Contains the project explanation, methodology, model results, screenshots, and conclusions.

## Conclusion
In this project, we used Linear Regression and Decision Tree Classification to analyze used car data. We evaluated both models and used Grid Search to test their parameters. This project helped us understand how machine learning can be applied to used car price prediction and classification.
