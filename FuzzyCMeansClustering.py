import numpy as np


class fuzzy_c():
    def __init__(self, mu, centers, points, k, maxiter, mu_ij, classes, distances):
        self.mu_ij = mu
        self.centers = centers
        self.pts = points
        self.k = k
        self.maxiter = maxiter
        self.mui_ij = mu_ij
        self.classes = classes
        self.distances = distances

    def c_i_calculation(self, mu, points):
        total = 0
        point_total = 0
        for row in mu:
            for cell in row:
                point_total = + cell
                for z in points:
                    total += cell * points
        return total

    def compute_l2_distance(self, points, centers):
        return np.linalg.norm(points - centers, axis=1)

    def forward(self):
        for i in range(self.maxiter):
            for i,c in enumerate(self.centers):
                self.distances[:, i] = self.compute_l2_distance(self.pts, c)

    def backward(self):
        for i,j in enumerate(self, self.centers):
            self.centers[i] = self.c_i_calculation(self.mu_ij, self.pts)
        return self.centers

    def initialize_clusters(self, points, k):
        return points[np.random.randint(points.shape[0], size=k)]


    def normalized_cluster_distance(self, point, current_center, cluster_list, fuzzifier):
        total = 0
        for k in cluster_list:
            total += (point - current_center) / (point - cluster_list[k]) ** (2 / (fuzzifier - 1))
        return total

    def mu_ij_calculation(self, points, centers, fuzzifier):
        for i, j in self.mu_ij:
            for x in points:
                self.mu_ij[i, j] = 1 / self.normalized_cluster_distance(points[x], centers[i], centers, fuzzifier)