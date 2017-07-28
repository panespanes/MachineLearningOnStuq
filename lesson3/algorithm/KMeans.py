import numpy as np
import matplotlib.pyplot as plt


class KMeans(object):
    def __init__(self, dataSet, eularDistance, k=5):
        self.dataSet = dataSet
        self.k = k
        self.number = dataSet.shape[0]
        self.eularDistance = eularDistance

    def randomCent(self):
        columnNum = self.dataSet.shape[1]
        print("columnNum = ", columnNum)
        centroids = np.zeros([self.k, columnNum])
        limit = np.zeros([2,2])
        for j in range(columnNum):
            minJ = min(self.dataSet[:, j])
            print("minJ = ", minJ)
            maxJ = max(self.dataSet[:, j])
            print("maxJ = ", maxJ)
            centroids[:, j] = minJ + float(maxJ - minJ) * np.random.rand(1, self.k)
            # x-min, max
            limit[j,:] = [minJ, maxJ]
        print(centroids)
        distances = self.centDistance(centroids)
        print(distances)
        print(distances.shape)
        minResult = self.minDistance(distances, centroids)
        print("minResult = ")
        print(minResult)
        newCentroids = self.clusterDistance(minResult, distances)

        print("main centroids:")
        print(centroids)
        print("main newCentroids:")
        print(newCentroids)
        plt.subplot(311)
        plt.scatter(x=self.dataSet[:, 0].A, y=self.dataSet[:, 1].A)
        plt.subplot(312)
        plt.scatter(x=centroids[:, 0], y=centroids[:, 1])
        plt.subplot(313)
        plt.scatter(x=newCentroids[:, 0], y=newCentroids[:, 1])
        axes = plt.gca()
        axes.set_xlim(limit[0])
        axes.set_ylim(limit[1])
        plt.show()

    def centDistance(self, centroids):
        distances = np.zeros([self.number, self.k])
        for row in range(self.number):
            for column in range(self.k):
                distances[row, column] = self.eularDistance(self.dataSet[row], centroids[column])
        return distances

    def minDistance(self, distances, centroids):
        # 0和1. 1代表当前所属的聚类
        minResult = np.zeros(distances.shape)
        for i in range(distances.shape[0]):
            minI = min(distances[i, :])
            for j in range(distances.shape[1]):
                if minI == distances[i, j]:
                    minResult[i, j] = 1
                else:
                    minResult[i, j] = 0
        return minResult

    def clusterDistance(self, clusterResult, distances):  # shape[80, 5]
        centroids = np.zeros([self.k, self.dataSet.shape[1]]) # shape[5, 2]
        clusterMean = np.zeros(clusterResult.shape)
        clusterDistance = np.zeros(clusterResult.shape)
        clusterData = np.zeros([clusterResult.shape[0], self.dataSet.shape[1]])  # shape[80, 2] 单个聚类中的data

        # clusterMean = self.dataSet * clusterResult

        # distanceZero = np.zeros([self.number, 1]) #dataSet到(0,0)的距离
        # for row in range(self.number):
        #     distanceZero[row,0] = self.eularDistance(self.dataSet[row], (0,0))
        # clusterDistance = np.zeros([self.number, self.k]) #每一聚类下各点到(0,0)的距离
        # for cluster in range(clusterResult.shape[1]):
        #     # clusterDistance[:,cluster] = distanceZero.reshape([self.number,1]) * clusterResult[:,cluster:cluster+1]
        #     clusterDistance[:, cluster:cluster + 1] = distanceZero * clusterResult[:,cluster:cluster+1]
        # print("clusterDistance = ")
        # print(clusterDistance)
        # print("mean = ")
        # np.mean()
        for cluster in range(clusterResult.shape[1]):
            for row in range(clusterResult.shape[0]):
                if clusterResult[row, cluster] == 1:
                    clusterData[row] = self.dataSet[row]
                else:
                    clusterData[row] = np.zeros([1, self.dataSet.shape[1]])
            centroids[cluster] = np.mean(clusterData, axis=0)
        return centroids
