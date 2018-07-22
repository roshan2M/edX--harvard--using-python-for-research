import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
import numpy as np

def format_time_stamp(time_string: str) -> dt.datetime:
    return dt.datetime.strptime(time_string[:-3], "%Y-%m-%d %H:%M:%S")

def get_time_stamps(time_strings: pd.DataFrame, format_str) -> list:
    time_stamps = []
    for time in time_strings:
        time_stamps.append(format_str(time))
    return time_stamps

def get_time_deltas(times: pd.DataFrame, delta: int = 1) -> np.array:
    elapsed_time = [time - times[0] for time in times]
    return np.array(elapsed_time) / dt.timedelta(days=delta)

def save_time_delta(times: np.array) -> None:
    plt.plot(times)
    plt.title("Graph to Show Observation Number against Elapsed Time")
    plt.xlabel("Observation Number")
    plt.ylabel("Elapsed Time (Days)")
    plt.savefig("Plot of Observations of Bird Times")

bird_data = pd.read_csv("bird_tracking.csv")
time_stamps = get_time_stamps(bird_data.date_time, format_time_stamp)
bird_data["time_stamp"] = pd.Series(time_stamps, index=bird_data.index)

times = bird_data.time_stamp[bird_data.bird_name == "Eric"]
time_delta = get_time_deltas(times, 1)
save_time_delta(time_delta)
