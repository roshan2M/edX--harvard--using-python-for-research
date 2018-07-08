import numpy as np
import pandas as pd

whiskies = pd.read_csv("whiskies.txt")
whiskies["Region"] = pd.read_csv("regions.txt")

print(whiskies)
