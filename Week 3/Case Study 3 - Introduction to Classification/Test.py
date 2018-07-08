from Prediction import *
from DataGeneration import *
from IrisClassifier import *

def test_prediction_grid():
    (points, outcomes) = generate_synthetic_data(50)
    (xx, yy, predict_grid) = make_prediction_grid(points, outcomes, (-3, 4, -3, 4), 0.1, 5)
    plot_prediction_grid(xx, yy, predict_grid, outcomes[:70])

def test_iris_classifier():
    predictors, outcomes = load_iris_dataset()
    sk_predictions = get_sk_learn_kNN_predictions(predictors, outcomes, 5)
    my_predictions = get_my_kNN_predictions(predictors, outcomes, 5)
    compare_predictions(my_predictions, sk_predictions, outcomes)
