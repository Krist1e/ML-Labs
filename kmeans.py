from classes import *


def generate_points(num_of_points, min, max):
    points = []
    for i in range(num_of_points):
        x = np.random.randint(min, max)
        y = np.random.randint(min, max)
        points.append(Point(x, y))
    return points


def choose_centroids(num_of_centroids, points):
    centroids = np.random.choice(points, num_of_centroids)
    return centroids


def assort_points_into_clusters(clusters, points):
    for point in points:
        min_distance = float('INF')
        closest_cluster = None
        for cluster in clusters:
            distance = point.euclidean_distance(cluster.centroid)
            if distance < min_distance:
                min_distance = distance
                closest_cluster = cluster
        closest_cluster.add_point(point)


def calculate_next_state(state):
    clusters = [cluster.__copy__() for cluster in state.clusters]
    points = []
    for cluster in clusters:
        points.extend(cluster.points)
        cluster.remove_points()
    assort_points_into_clusters(clusters, points)
    for cluster in clusters:
        cluster.calculate_centroid()
    return State(clusters)


def kmeans_clustering(num_of_centroids, num_of_points, min, max):
    points = generate_points(num_of_points, min, max)
    centroids = choose_centroids(num_of_centroids, points)
    clusters = [Cluster(centroids[i]) for i in range(len(centroids))]
    clusters[0].points = points
    state = State(clusters)
    states = []
    new_state = calculate_next_state(state)
    while new_state != state:
        state = new_state
        states.append(state)
        new_state = calculate_next_state(state)
    return states
