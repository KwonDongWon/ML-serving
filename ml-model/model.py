"""
iris data logistic regression modeling
"""
import pickle

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

iris = load_iris()  # sample data load
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1 / 3, random_state=0)

model = LogisticRegression()
model.fit(X_train, y_train)
model.score(X_test, y_test)

pickle.dump(model, open('model.pkl', 'wb'))

model = pickle.load(open('model.pkl', 'rb'))


