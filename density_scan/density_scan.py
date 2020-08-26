from queue import MyQueue
from scipy.spatial import distance
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# create dscan class
class DensityScan:

    def __init__(self, data, eps, minpts):
        self.data = data  # point to input data
        self.eps = eps  # point to input epsilon
        self.minpts = minpts  # point to input minimum points
        self.noise_point = 0  # set noise point marker to 0
        self.unassigned_point = 0  # set unassigned point marker to 0
        self.core_point = -1  # set core point marker to -1
        self.edge_point = -2  # set edge point marker to -2

    def neighbors(self, point_index):
        neighbor_points = []  # create empty list for neighboring points
        for i in range(len(self.data)):  # iterate through length of data
            if distance.euclidean(self.data[i], self.data[point_index]) <= self.eps:  # use euclidean method to check distance of neighbors
                neighbor_points.append(i)
        return neighbor_points

    def scanner(self):
        # allocate memory for labels using list of 0s
        labels = [self.unassigned_point] * len(self.data)
        points = []
        cores = []
        other_points = []

        # find the neighbors for all points
        [points.append(self.neighbors(i)) for i in range(len(self.data))]

        # find core, edge, and noise points
        # [labels[i] = self.core_point and cores.append(i) if len(points[i]) >= self.minpts else other_points.append(i) for i in range(len(points))]

        for i in range(len(points)):
            if (len(points[i]) >= self.minpts):
                labels[i] = self.core_point
                cores.append(i)
            else:
                other_points.append(i)

        for i in other_points:
            for j in points[i]:
                if j in cores:
                    labels[i] = self.edge_point

                    break
        
        # start clustering
        cluster = 1

        # use queue for neighboring core points; find neighbors' neighbors
        for i in range(len(labels)):
            myqueue = MyQueue()
            if (labels[i] == self.core_point):
                labels[i] = cluster
                for x in points[i]:
                    if (labels[x] == self.core_point):
                        myqueue.enqueue(x)
                        labels[x] = cluster
                    elif (labels[x] == self.edge_point):
                        labels[x] = cluster

                # stop when all points checked
                while myqueue.__len__() > 0:
                    neighbors = points[myqueue.dequeue()]
                    for y in neighbors:
                        if (labels[y] == self.core_point):
                            labels[y] = cluster
                            myqueue.enqueue(y)
                        if (labels[y] == self.edge_point):
                            labels[y] = cluster

                cluster += 1
        return labels, cluster

    # method for plotting results
    def plotscan(self, labels, clusters):
        num_points = len(self.data)
        colors = ['green', 'brown', 'red', 'purple', 'orange', 'blue', 'yellow']
        for i in range(clusters):
            if (i == 0):
                # plot noise as yellow
                size=50
                color = 'k'
            elif (i == 1):
                size = 150
                color = 'r'
            else:
                size=150
                color = 'y'
            x1 = []
            y1 = []
            for j in range(num_points):
                if labels[j] == i:
                    x1.append(self.data[j, 0])
                    y1.append(self.data[j, 1])
            plt.scatter(x1, y1, s=size, c=color, alpha=1, marker='.', edgecolor='k')

if __name__ == "__main__":

    iris_df = pd.read_csv("iris.data")
    # print(iris_df.head())
    # print(iris_df.columns)
    train = iris_df[["sep_length", "sep_width", "pet_length", "pet_width"]].values
    # print(train)
    eps = 0.6
    minpt = 5

    dscan = DensityScan(train, eps, minpt)
    labels, clusters = dscan.scanner()
    print(f"Number of clusters found: {str(clusters-1)}" )
    outliers = labels.count(0)
    print(f"Number of outliers found: {str(outliers)} \n")
    dscan.plotscan(labels, clusters)
    plt.show()
        