#importing libraries
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

#Reading data csv file
data_1 = pd.read_csv(sys.argv[1]) 
data = data_1.drop('Category', axis = 1)

#Setting the labels
labels = data_1['Category']  

#Getting date for training data in the right format
data['Dates'] = pd.to_datetime(data['Dates'])
data['Year'] = data['Dates'].dt.year
data['Month'] = data['Dates'].dt.month
data['Date'] = data['Dates'].dt.day
data['Hour'] = data['Dates'].dt.hour
data['Minute'] = data['Dates'].dt.minute

#Filling in possible missing values
data['X'] = data['X'].fillna(data['X'].mean())
data['Y'] = data['Y'].fillna(data['Y'].mean())

#Scaling X, Y, Hour
scaler = StandardScaler()
numeric_variables = scaler.fit_transform(data[['X','Y','Hour']])

#One-hot encoding
categorical_variables = pd.get_dummies(data[['DayOfWeek','PdDistrict','Resolution']])

#X and y
X = np.concatenate((numeric_variables,categorical_variables.as_matrix()), axis = 1)
y = labels.as_matrix() 

#Reading the test data
test_data = pd.read_csv(sys.argv[2])
test_ID = test_data[['Id']]

#Getting dates for test set
test_data['Dates'] = pd.to_datetime(test_data['Dates'])
test_data['Year'] = test_data['Dates'].dt.year
test_data['Month'] = test_data['Dates'].dt.month
test_data['Date'] = test_data['Dates'].dt.day
test_data['Hour'] = test_data['Dates'].dt.hour
test_data['Minute'] = test_data['Dates'].dt.minute

#Filling in possible missing values
test_data['X'] = test_data['X'].fillna(test_data['X'].mean())
test_data['Y'] = test_data['Y'].fillna(test_data['Y'].mean())

#Scaling X, Y, Hour
numeric_variables_2 = scaler.fit_transform(test_data[['X','Y','Hour']])

#One-hot encoding
categorical_variables_2 = pd.get_dummies(test_data[['DayOfWeek','PdDistrict','Resolution']])

#X_test
X_test = np.concatenate((numeric_variables_2,categorical_variables_2.as_matrix()),axis = 1)

#Fitting classifier
clf = LogisticRegression()
clf.fit(X, y)

#Getting predictions as probabilities
y_pred = clf.predict_proba(X_test)

#Saving probabilities
test_data = test_data.reindex(columns=['Id','ARSON', 'ASSAULT', 'BAD CHECKS', 'BRIBERY', 'BURGLARY', 'DISORDERLY CONDUCT', 'DRIVING UNDER THE INFLUENCE', 'DRUG/NARCOTIC', 'DRUNKENNESS', 'EMBEZZLEMENT', 'EXTORTION', 'FAMILY OFFENSES', 'FORGERY/COUNTERFEITING', 'FRAUD', 'GAMBLING', 'KIDNAPPING', 'LARCENY/THEFT', 'LIQUOR LAWS', 'LOITERING', 'MISSING PERSON', 'NON-CRIMINAL', 'OTHER OFFENSES', 'PORNOGRAPHY/OBSCENE MAT', 'PROSTITUTION', 'RECOVERED VEHICLE', 'ROBBERY', 'RUNAWAY', 'SECONDARY CODES', 'SEX OFFENSES FORCIBLE', 'SEX OFFENSES NON FORCIBLE', 'STOLEN PROPERTY', 'SUICIDE', 'SUSPICIOUS OCC', 'TREA', 'TRESPASS', 'VANDALISM', 'VEHICLE THEFT', 'WARRANTS', 'WEAPON LAWS'])  
test_data[['ARSON', 'ASSAULT', 'BAD CHECKS', 'BRIBERY', 'BURGLARY', 'DISORDERLY CONDUCT', 'DRIVING UNDER THE INFLUENCE', 'DRUG/NARCOTIC', 'DRUNKENNESS', 'EMBEZZLEMENT', 'EXTORTION', 'FAMILY OFFENSES', 'FORGERY/COUNTERFEITING', 'FRAUD', 'GAMBLING', 'KIDNAPPING', 'LARCENY/THEFT', 'LIQUOR LAWS', 'LOITERING', 'MISSING PERSON', 'NON-CRIMINAL', 'OTHER OFFENSES', 'PORNOGRAPHY/OBSCENE MAT', 'PROSTITUTION', 'RECOVERED VEHICLE', 'ROBBERY', 'RUNAWAY', 'SECONDARY CODES', 'SEX OFFENSES FORCIBLE', 'SEX OFFENSES NON FORCIBLE', 'STOLEN PROPERTY', 'SUICIDE', 'SUSPICIOUS OCC', 'TREA', 'TRESPASS', 'VANDALISM', 'VEHICLE THEFT', 'WARRANTS', 'WEAPON LAWS']]  = y_pred
test_data[['Id']] = test_ID

#Writing into the file
test_data.to_csv('2014A3TS0215G_final.csv',index=False)