import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

DEGREE_SYMBOL = u'\N{DEGREE SIGN}'

def plot_all_migrations(bird_data: pd.DataFrame):
    bird_names = pd.unique(bird_data.bird_name)
    plt.figure(figsize=(7,7))
    for name in bird_names:
        index = bird_data.bird_name == name
        x, y = bird_data.longitude[index], bird_data.latitude[index]
        plt.plot(x, y, ".", label=name)
    plt.title("Plot to Show Migration of Birds Over Half Hour Intervals")
    plt.xlabel("Longitude (" + DEGREE_SYMBOL + ")")
    plt.ylabel("Latitude (" + DEGREE_SYMBOL + ")")
    plt.legend(loc="lower right")
    plt.savefig("Migration of Plot of All Birds.pdf")

bird_data = pd.read_csv("bird_tracking.csv")
plot_all_migrations(bird_data)
