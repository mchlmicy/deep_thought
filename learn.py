# data
from data import features, labels

# machine learning
from sklearn import tree


classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(features, labels)
