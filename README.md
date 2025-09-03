# Salary Prediction with Linear Regression
Build my own LR model from scratch, just math

This project demonstrates a simple linear regression model to predict salary based on years of experience. The model is built from scratch using the gradient descent algorithm to find the line of best fit.

Overview
The goal of this project is to model the relationship between an employee's years of experience and their corresponding salary. This is achieved by implementing a linear regression algorithm that learns the optimal parameters (slope and intercept) from a given dataset.

Dataset
The dataset used for training is data.csv, which contains two columns:

YearsExperience: The number of years of experience.

Salary: The corresponding salary.

How it Works
The core of this project is the main.py script, which performs the following steps:

Data Loading: It loads the dataset from data.csv using the pandas library.

Gradient Descent: It implements the gradient descent algorithm to find the optimal values for the slope (m) and y-intercept (b) of the regression line. The algorithm iteratively adjusts these parameters to minimize the cost function (Mean Squared Error).

Visualization: After training, it uses matplotlib to generate a scatter plot of the data points and overlays the calculated line of best fit.

Results
After running the gradient descent algorithm, the final parameters for the regression line equation y = mx + b were found to be:

Slope (m): 12718.710861289686

Y-Intercept (b): 3904.0116323933953

The model predicts a starting salary of approximately $3,904 and an increase of about $12,719 for each additional year of experience.

The resulting plot shows how well the model fits the data is located in img folder.
