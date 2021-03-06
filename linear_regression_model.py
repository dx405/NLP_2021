import json
import numpy as np
import tf_idf
import sys
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder, MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier

Y, X, mlb = tf_idf()

# split into training and testing 
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=.20)

# train linear regression model
reg = OneVsRestClassifier(LinearRegression()).fit(x_train, y_train)

# performing prediction on dataset
y_pred = reg.predict(x_test)

# return classification report and accuracy score
print(classification_report(y_test, y_pred))
print('Accuracy:', accuracy_score(y_test, y_pred))

y_pred_label = mlb.inverse_transform(y_pred)
y_test_label = mlb.inverse_transform(y_test)

with open('label_results.txt', 'w+') as out:
	for i in range(len(y_pred_label)):
		out.write(f'Predicted: {y_pred_label[i]}\tActual: {y_test_label[i]}\n')
