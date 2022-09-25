###https://stackabuse.com/decision-trees-in-python-with-scikit-learn/
## DecisiontreeForClassification
import pandas as pd
dataset = pd.read_csv("data/csv_result-iris.csv")
print(dataset.shape)
print(dataset.head())
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
### testing
print("testing")
dataset = pd.read_csv("data/csv_result-iris_test.csv")
X_test = dataset
y_pred = classifier.predict(X_test)
A=X_test.to_numpy()
print("Gan lop")
for i in range (len(y_pred)):
    print(A[i],y_pred[i])

