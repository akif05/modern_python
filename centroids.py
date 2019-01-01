from pprint import pprint
from math import fsum, sqrt
from typing import Iterable, Tuple
from collections import defaultdict

# Define that Point is a Tuple[int, ...]
Point = Tuple[int, ...]

points = [ 
	(10, 41, 23),
	(22, 30, 29),
	(11, 42, 5),
	(20, 32, 4),
	(12, 40, 12),
	(21, 36, 23),
]

def dist(p: Point, q: Point, fsum=fsum, sqrt=sqrt, zip=zip) -> float:
	return sqrt(fsum([(x - y) ** 2 for x, y in zip(p, q)]))

def assign_data(centroids, data):
	d = defaultdict(list)
	for point in data:
		closest_centroid
		d[closest_centroid].append(point)
	return d

for point in points:
	print(point, dist(point, (9, 39, 20)))

centroids = [(9, 39, 20), (12, 36, 25)]
point = (11, 42, 5)

# [dist(point, centroids) for centroid in centroids]

min(centroids, key=lambda centroid: dist(point, centroid))
