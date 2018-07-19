import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_whiskies() -> pd.DataFrame:
    whiskies = pd.read_csv("whiskies.txt")
    whiskies["Region"] = pd.read_csv("regions.txt")
    return whiskies

def plot_correlation_matrix(corr_matrix: pd.DataFrame, file_name: str) -> None:
    plt.figure(figsize=(10,10))
    plt.pcolor(corr_matrix)
    plt.axis("tight")
    plt.colorbar()
    plt.savefig(file_name)

def save_correlation_matrix(data: pd.DataFrame, file_name: str) -> None:
    corr_matrix = pd.DataFrame.corr(data)
    plot_correlation_matrix(corr_matrix, file_name)

whiskies = load_whiskies()
flavours = whiskies.iloc[:, 2:14]

save_correlation_matrix(flavours, "Graph to Show Pearson's Coefficient Between Flavours of Whiskies.pdf")
save_correlation_matrix(flavours.transpose(), "Graph to Show Pearson's Coefficient Between Distilleries of Whiskies.pdf")
