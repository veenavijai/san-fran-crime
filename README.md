## San Francisco Crime Classification

This repo documents my final project as part of the Machine Learning course (BITS F464) offered in BITS Pilani, Goa by Dr. Ashwin Srinivasan in Spring 2018.

**Problem Description**

From 1934 to 1963, San Francisco was infamous for housing some of the world's most notorious criminals on the inescapable island of Alcatraz.

Today, the city is known more for its tech scene than its criminal past. But, with rising wealth inequality, housing shortages, and a proliferation of expensive digital toys riding BART to work, there is no scarcity of crime in the city by the bay.

From Sunset to SOMA, and Marina to Excelsior, this competition's dataset provides nearly 12 years of crime reports from across all of San Francisco's neighborhoods. Given time and location, you must predict the category of crime that occurred.

**Dataset**

This dataset contains incidents derived from SFPD Crime Incident Reporting system. The data ranges from 1/1/2003 to 5/13/2015. The training set and test set rotate every week, meaning week 1,3,5,7... belong to test set, week 2,4,6,8 belong to training set.

Dates - timestamp of the crime incident
Category - category of the crime incident . This is the target variable you are going to predict.
DayOfWeek - the day of the week
PdDistrict - name of the Police Department District
Resolution - how the crime incident was resolved
Address - the approximate street address of the crime incident 
X - Longitude
Y - Latitude

The training set can be downloaded [here.](https://drive.google.com/open?id=1Qs_LlKzqkAR2PMAUUQpuDslhjfs-hWtr) The validation data that we used is called Test.csv on the repo. 

Note: Both the training and test datasets are different from the [Kaggle dataset.](https://www.kaggle.com/c/sf-crime)

**Evaluation Metric**

Multi-class log loss, implemented by [sklearn's function](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html). Our final submission, Submission.py in this repo, achieved a log loss of 2.21.

**Experiments for Feature Selection**

We chose X, Y, Hour

**Final Code**

The training and test .csv files were given as two arguments in the command line.

We obtained the date in the correct format using to_datetime() from pandas.

We imputed missing values of X and Y by filling in the mean. 

We used the StandardScaler() to convert our numeric variables, X, Y, and Hour, to zero-mean and unit variance.

In order to use the categorical variables, we one-hot encoded DayOfWeek, PdDistrict, and Resolution with get_dummies() from pandas.

The numerical variables and one-hot encodings were then concatenated.

Similarly, for the test data, the date was converted to the correct format, missing values for X, Y, and Hour were filled in with the mean values, and scaled with the StandardScaler() fitted to the training data. After one-hot encoding, both the numeric and categorical variables were concatenated.

We chose the LogisticRegression() classifier from sklearn and used its predict_proba() function to save the predictions as probabilities.

At the end, Submission.py saves the results in a .csv file.

**Team Members**

Sujith S Pai\
Veena Vijai
