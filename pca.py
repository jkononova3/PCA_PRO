

# Simulate some random "weight" vs. "height" data.
import numpy as np
import pandas as pd

rng = np.random.RandomState(1)
X = np.dot(rng.rand(2, 2), rng.randn(2, 200)).T

height = X[:,0]+65
weight = X[:,1]+120

data = pd.DataFrame({"height": height, "weight": weight})

# You can use `data.head()` to see the columns of the data frame.
# Recall `data["height"]` and `data["weight"]` will access those two columns:
data.head()


import sklearn.decomposition
pca = sklearn.decomposition.PCA()
pca.fit(data[["height","weight"]])

pc_magnitudes = pca.explained_variance_
pcs = pca.components_
print("PC 1 - magnitude: %s"%pc_magnitudes[0])
print("PC 1: %s"%pcs[0])
print("PC 2 - magnitude: %s"%pc_magnitudes[1])
print("PC 2: %s"%pcs[1])