from sklearn.cluster.bicluster import SpectralCoclustering
from Whiskies import load_whiskies

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

whiskies = load_whiskies()
flavours = whiskies.iloc[:, 2:14]
corr_whiskies = pd.DataFrame.corr(flavours.transpose())

model = SpectralCoclustering(n_clusters=6, random_state=0)
model.fit(corr_whiskies)

whiskies['Group'] = pd.Series(model.row_labels_, index=whiskies.index)
whiskies = whiskies.ix[np.argsort(model.row_labels_)]
whiskies = whiskies.reset_index(drop=True)

correlations = pd.DataFrame.corr(whiskies.iloc[:,2:14].transpose())
correlations = np.array(correlations)

plt.figure(figsize=(14,7))
plt.subplot(121)
plt.pcolor(corr_whiskies)
plt.title("Original Correlation Matrix")
plt.axis("tight")

plt.subplot(122)
plt.pcolor(correlations)
plt.title("Rearranged Correlation Matrix")
plt.axis("tight")
plt.savefig("Graphs to Show Correlation Matrices.pdf")
