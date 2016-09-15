# Perceptron
from random import choice
from numpy import array, dot, random
import matplotlib.pyplot as plt
import pandas as pd



def csvImporter():
   data = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
   return data


def dataHandler(data):
    data.drop(data.columns[[2, 3]],inplace=True, axis=1)
    data.replace({'Iris-setosa': '0'},inplace=True, regex=True)
    data.replace({'Iris-virginica': '1'},inplace=True, regex=True)
    print(data)

step_function = lambda x: 0 if x < 0 else 1

dataHandler(csvImporter())
# Training data set
training = [
    (array([0, 0, 1]), 0),
    (array([0, 1, 1]), 1),
    (array([1, 0, 1]), 1),
    (array([1, 1, 1]), 1), ]

w = [-1,0,0]
errors = []

eta = 0.2

# iterations
n = 100

for i in range(n):
    x, expected = choice(training)
    result = dot(w, x)
    error = expected - step_function(result)
    errors.append(error)
    # Delta + input
    w += eta * error * x
    plt.plot(w)

print("X \t\t x*w \t\t result")

for x, _ in training:
    result = dot(x, w)
    print("{}\t: {}->\t{}".format(x[:2], float("{0:.2f}".format(result)), step_function(result)))

print (errors);
plt.show()
