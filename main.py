import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs


X, y = make_blobs(centers=3, n_samples=500, random_state=1)
fig, ax = plt.subplots(figsize=(4, 4))
ax.scatter(X[:, 0], X[:, 1], alpha=0.5)
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')


def initialize_clusters(points, k):
    return points[np.random.randint(points.shape[0], size=k)]


def compute_l2_distance(points, centers):
    return np.linalg.norm(points - centers, axis= 1)


def c_i_calculation(mu, points):
    total = 0
    point_total = 0
    for i, j in mu:
        point_total += mu[i,j]
        for z in points:
            total += mu[i, j]*points[z]


def normalized_cluster_distance(point, current_center, cluster_list, fuzzifier):
    total = 0
    for k in cluster_list:
        total += (point - current_center)/(point - cluster_list[k])**(2/(fuzzifier-1))
    return total


def mu_ij_calculation(points, centers, fuzzifier):
    for i, j in mu_ij:
        for x in points:
            mu_ij[i, j] = 1/normalized_cluster_distance(points[x], centers[i], centers, fuzzifier)
    return mu_ij


k = 3
maxiter = 50
centers = initialize_clusters(X, k)
mu_ij = np.zeros((k, len(X)))
classes = np.zeros(X.shape[0], dtype=np.float64)
distances = np.zeros([X.shape[0], k], dtype=np.float64)


class fuzzy_c():
    def __init__(self, mu, centers, points):
        self.mu_ij = mu
        self.centers = centers
        self.pts = points

    def forward(self):
        for i in range(maxiter):
            for i,c in enumerate(self.centers):
                distances[:, i] = compute_l2_distance(X, c)

    def backward(self):
        for i, j in self.centers:
            self.centers[i] = c_i_calculation(self.mu_ij, self.pts)
        return self.centers


fuzzy_classifier = fuzzy_c(mu_ij, centers, X)
fuzzy_classifier.forward()
print(fuzzy_classifier.backward())
