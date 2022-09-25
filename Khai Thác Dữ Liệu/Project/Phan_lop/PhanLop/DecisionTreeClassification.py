###https://stackabuse.com/decision-trees-in-python-with-scikit-learn/
## DecisiontreeForClassification
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv("data/bill_authentication.csv")
dataset.shape
dataset.head()
X = dataset.drop('Class', axis=1)
y = dataset['Class']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)
## Evaluating the algorithm\
print("Evaluating model")
y_pred = classifier.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
