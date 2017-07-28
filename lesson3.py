from lesson3.io.Reader import Reader
from lesson3.algorithm.EularDistance import distance as eularDistance
import matplotlib.pyplot as plt
import os
import numpy as np
from lesson3.algorithm.KMeans import KMeans as KMeans


reader = Reader()
path = os.getcwd()
path += "/kmeansPoints.txt"
print(path)
lines = reader.read(path, float)
dataSet = np.mat(lines)
# print(dataSet)

kMeans = KMeans(dataSet=dataSet, eularDistance=eularDistance, k=5)
kMeans.randomCent()