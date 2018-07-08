import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from Prediction import make_prediction_grid, plot_prediction_grid
from NearestNeighbours import knn_predict

def load_iris_dataset() -> tuple:
    iris = datasets.load_iris()
    predictors = iris['data'][:,0:2]
    outcomes = iris['target']
    return (predictors, outcomes)

def plot_iris_data(predictors: np.array, outcomes: np.array) -> None:
    plt.plot(predictors[outcomes==0][:,0], predictors[outcomes==0][:,1], "ro")
    plt.plot(predictors[outcomes==1][:,0], predictors[outcomes==1][:,1], "go")
    plt.plot(predictors[outcomes==2][:,0], predictors[outcomes==2][:,1], "bo")
    plt.savefig("Iris Colour Indicators.pdf")

def get_sk_learn_kNN_predictions(predictors: np.array, outcomes: np.array, k: int = 5) -> np.array:
    kNN = KNeighborsClassifier(n_neighbors = k)
    kNN.fit(predictors, outcomes)
    sk_predictions = kNN.predict(predictors)
    return sk_predictions

def get_my_kNN_predictions(predictors: np.array, outcomes: np.array, k: int = 5) -> np.array:
    my_predictions = np.array([knn_predict(p, predictors, outcomes, k) for p in predictors])
    return my_predictions

def compare_predictions(my_predictions: np.array, sk_predictions: np.array, outcomes: np.array) -> None:
    print("Similarity between my predictions and sklearn predictions: " + str(100 * np.mean(sk_predictions == my_predictions)))
    print("Similarity between my predictions and actual outcomes: " + str(100 * np.mean(my_predictions == outcomes)))
    print("Similarity between sklearn predictions and actual outcomes: " + str(100 * np.mean(sk_predictions == outcomes)))
