import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __copy__(self):
        return Point(self.x, self.y)

    def euclidean_distance(self, other):
        return np.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Cluster:
    centroid = None
    points = None

    def __init__(self, centroid=None, points=None, color=None):
        if centroid is None:
            self.centroid = Point(0, 0)
        else:
            self.centroid = centroid

        if points is None:
            self.points = []
        else:
            self.points = points

        if color is None:
            self.color = np.random.rand(3, )
        else:
            self.color = color

    def __eq__(self, other):
        if len(self.points) != len(other.points):
            return False
        for i in range(len(self.points)):
            if self.points[i] != other.points[i]:
                return False
        if self.centroid != other.centroid:
            return False
        return True

    def __copy__(self):
        new_cluster = Cluster()
        new_cluster.centroid = self.centroid.__copy__()
        new_cluster.points = self.points.copy()
        new_cluster.color = self.color.copy()
        return new_cluster

    def add_point(self, point):
        self.points.append(point)

    def remove_points(self):
        self.points = []

    def get_coords(self):
        x = y = []
        for point in self.points:
            x.append(point.x)
            y.append(point.y)
        return x, y

    def calculate_centroid(self):
        x = y = 0
        for point in self.points:
            x += point.x
            y += point.y
        n = len(self.points)
        self.centroid = Point(x / n, y / n)
        return self.centroid


class State:
    def __init__(self, clusters):
        self.clusters = clusters

    def __eq__(self, other):
        if len(self.clusters) != len(other.clusters):
            return False
        for i in range(len(self.clusters)):
            if self.clusters[i] != other.clusters[i]:
                return False
        return True

    def draw_state(self, plot):
        for cluster in self.clusters:
            x = []
            y = []
            for point in cluster.points:
                x.append(point.x)
                y.append(point.y)
            plot.scatter(x, y, color=cluster.color, s=20)
            plot.scatter(cluster.centroid.x, cluster.centroid.y, color='black', s=100, marker='*')

