from Prediction import *
from DataGeneration import *

(points, outcomes) = generate_synthetic_data(50)
(xx, yy, predict_grid) = make_prediction_grid(points, outcomes, (-3, 4, -3, 4), 0.1, 5)
plot_prediction_grid(xx, yy, predict_grid, outcomes[:70])
