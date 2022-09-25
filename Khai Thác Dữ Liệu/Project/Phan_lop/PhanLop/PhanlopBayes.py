# Import scikit-learn dataset library
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
# Load dataset
wine = datasets.load_wine()
print(wine)
# print the names of the 13 features
print("Features: ", wine.feature_names)

# print the label type of wine(class_0, class_1, class_2)
print("Labels: ", wine.target_names)

# print data(feature)shape-- co 178 dong du lieu va co 13 cot feature
print("data(feature)shape")
print(wine.data.shape)
# print the wine data features (top 5 records)
print(wine.data[0:5])

# Import train_test_split function
# from sklearn.cross_validation import train_test_split

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3, random_state=109) #70% training and 30% test
# Model Generation
# After splitting, you will generate a random forest model on the training set and perform prediction on test set features.
#Import Gaussian Naive Bayes model

#Create a Gaussian Classifier
gnb = GaussianNB()

#Train the model using the training sets
gnb.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = gnb.predict(X_test)

# Evaluating Model
# After model generation, check the accuracy using actual and predicted values.
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
# POWERED BY DATACAMP WORKSPACE
# COPY CODE
# ('Accuracy:', 0.90740740740740744)