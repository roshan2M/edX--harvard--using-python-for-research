import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
import numpy as np

def format_time_stamp(time_string: str) -> dt.datetime:
    return dt.datetime.strptime(time_string[:-3], "%Y-%m-%d %H:%M:%S")

def get_time_stamps(time_strings: pd.DataFrame, format_str) -> np.array:
    time_stamps = []
    for time in time_strings:
        time_stamps.append(format_str(time))
    return np.array(time_stamps)

def get_time_deltas(times: pd.DataFrame, delta: int = 1) -> np.array:
    elapsed_time = np.array([time - times[0] for time in times])
    return elapsed_time / dt.timedelta(days=delta)

def get_mean_speeds(elapsed_days: np.array, speeds: np.array) -> np.array:
    next_day = 1
    indices = []
    daily_mean_speeds = []
    for (index, time) in enumerate(elapsed_days):
        if time < next_day:
            indices.append(index)
        else:
            daily_mean_speeds.append(np.mean(speeds[indices]))
            next_day += 1
            indices = []
    return np.array(daily_mean_speeds)

def save_time_delta(times: np.array) -> None:
    plt.plot(times)
    plt.title("Graph to Show Observation against Elapsed Time")
    plt.xlabel("Observation Number")
    plt.ylabel("Elapsed Time (Days)")
    plt.savefig("Plot of Observations of Bird Times")

def save_daily_mean_speeds(mean_speeds: np.array):
    plt.figure(figsize=(8,6))
    plt.plot(mean_speeds)
    plt.title("Graph to Show Daily Mean Speed of Bird")
    plt.xlabel("Day Number")
    plt.ylabel("Mean Speed of Bird (m/s)")
    plt.savefig("Mean Speeds of a Bird.pdf")

bird_data = pd.read_csv("bird_tracking.csv")
time_stamps = get_time_stamps(bird_data.date_time, format_time_stamp)
bird_data["time_stamp"] = pd.Series(time_stamps, index=bird_data.index)

times = bird_data.time_stamp[bird_data.bird_name == "Eric"]
time_delta = get_time_deltas(times, 1)
save_time_delta(time_delta)

daily_mean_speeds = get_mean_speeds(time_delta, np.array(bird_data.speed_2d))
save_daily_mean_speeds(daily_mean_speeds)
