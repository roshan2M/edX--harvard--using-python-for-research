import numpy as np
import matplotlib.pyplot as plt

from matplotlib.colors import ListedColormap
from NearestNeighbours import knn_predict

def make_prediction_grid(predictors: np.array, outcomes: np.array, limits: tuple, h: float, k: int) -> tuple:
    """
    Classify each point in the prediction grid.
    """
    (x_min, x_max, y_min, y_max) = limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)

    prediction_grid = np.zeros(xx.shape, dtype=int)
    for i,x in enumerate(xs):
        for j,y in enumerate(ys):
            p = np.array([x, y])
            prediction_grid[j][i] = int(knn_predict(p, predictors, outcomes, k))

    return (xx, yy, prediction_grid)

def plot_prediction_grid (xx: np.array, yy: np.array, prediction_grid: np.array, outcomes: np.array) -> None:
    """
    Plot kNN predictions for every point on the grid.
    """
    background_colormap = ListedColormap(["hotpink","lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap(["red","blue","green"])
    plt.figure(figsize=(10,10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap=background_colormap, alpha=0.5)
    plt.scatter(prediction_grid[:,0], prediction_grid[:,1], c=outcomes, cmap=observation_colormap, s=50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))
    plt.savefig("Prediction Grid for Points on Grid")
