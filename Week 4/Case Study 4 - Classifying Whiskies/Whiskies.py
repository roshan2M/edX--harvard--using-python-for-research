import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_whiskies() -> pd.DataFrame:
    whiskies = pd.read_csv("whiskies.txt")
    whiskies["Region"] = pd.read_csv("regions.txt")
    return whiskies

def load_correlation_matrix(corr_flavours: pd.DataFrame, file_name: str) -> None:
    plt.figure(figsize=(10,10))
    plt.pcolor(corr_flavours)
    plt.axis("tight")
    plt.colorbar()
    plt.savefig(file_name)

whiskies = load_whiskies()
flavours = whiskies.iloc[:, 2:14]
corr_flavours = pd.DataFrame.corr(flavours)
load_correlation_matrix(corr_flavours, "Graph to Show Pearson's Coefficient Between Flavours of Whiskies.pdf")

corr_whisky = pd.DataFrame.corr(flavours.transpose())
load_correlation_matrix(corr_whisky, "Graph to Show Pearson's Coefficient Between Distilleries of Whiskies.pdf")
