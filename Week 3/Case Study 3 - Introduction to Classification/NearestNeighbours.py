import numpy as np

from Distance import distance, majority_vote

def find_nearest_neighbours(p: np.array, points: np.array, k: int = 5) -> np.array:
    """
    Find the k nearest neighbours of point p in points and return them.
    """
    distances = np.zeros(points.shape[0])
    for i in range(len(points)):
        distances[i] = distance(p, points[i])
    indices = np.argsort(distances)
    return indices[:k]

def knn_predict(p: np.array, points: np.array, outcomes: np.array, k: int = 5):
    """
    Finds the k nearest neighbours of point p in points, and returns the class
    that most of those k nearest neighbours belong to.
    """
    k_nearest_indices = find_nearest_neighbours(p, points, k)
    majority_vote(outcomes[k_nearest_indices])
