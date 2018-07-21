import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_bird_speed_histogram(speeds: pd.DataFrame, bird_name: str):
    speeds.plot(kind="hist", range=[0,30])
    plt.title("Histogram to Track the Speeds of Bird " + bird_name + ".pdf")
    plt.xlabel("2D Speed (m/s)")
    plt.ylabel("Frequency")
    plt.savefig("Histogram of Bird Speeds.pdf")

bird_data = pd.read_csv("bird_tracking.csv")
plot_bird_speed_histogram(bird_data.speed_2d, "Eric")
