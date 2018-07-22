import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pandas as pd
import numpy as np

DEGREE_SYMBOL = u'\N{DEGREE SIGN}'

def plot_all_migrations(bird_data: pd.DataFrame) -> None:
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

def plot_cartopy_migrations(bird_data: pd.DataFrame) -> None:
    bird_names = pd.unique(bird_data.bird_name)
    proj = ccrs.Mercator()
    plt.figure(figsize=(10,10))
    ax = plt.axes(projection=proj)
    ax.set_extent((-25.0, 20.0, 52.0, 10.0))
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    for name in bird_names:
        index = bird_data.bird_name == name
        x, y = bird_data.longitude[index], bird_data.latitude[index]
        ax.plot(x, y, ".", transform=ccrs.Geodetic(), label=name)
    plt.title("Plot to Show Migration of Birds Over Half Hour Intervals")
    plt.legend(loc="upper left")
    plt.savefig("Bird Migration Map.pdf")

bird_data = pd.read_csv("bird_tracking.csv")
plot_all_migrations(bird_data)
plot_cartopy_migrations(bird_data)
