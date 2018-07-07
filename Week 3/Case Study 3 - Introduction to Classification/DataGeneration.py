import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt

def generate_synthetic_data(n: int = 50) -> tuple:
    """
    Creates two sets of points from bivariate normal distributions.
    """
    points = np.concatenate((ss.norm(0, 1).rvs((n, 2)), ss.norm(1, 1).rvs((n, 2))), axis=0)
    outcomes = np.concatenate((np.repeat(0, n), np.repeat(1, n)))
    return (points, outcomes)

def plot_synthetic_data(points: np.array, n: int) -> None:
    """
    Plots given points on a graph, classified by the a number n that splits
    the dataset.
    """
    plt.figure()
    plt.plot(points[:n,0], points[:n,1], "ro")
    plt.plot(points[n:,0], points[n:,1], "bo")
    plt.title("Random Points Generated from Normal Distributions")
    plt.xlabel("Normally Distributed x-Coordinates")
    plt.ylabel("Normally Distributed y-Coordinates")
    plt.savefig("Normal Distribution Data Generation.pdf")
