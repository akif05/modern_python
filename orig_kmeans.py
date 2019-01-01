from typing import Iterable, Tuple, Sequence, Dict, List
from collections import defaultdict
from random import sample
from functools import partial
from math import fsum, sqrt
from pprint import pprint

# Define that Point is a Tuple[int, ...]
Point = Tuple[int, ...]
Centroid = Point

def mean(data: Iterable[float]) -> float:
    data = list(data)
    return fsum(data) / len(data)

def dist(p: Point, q: Point, fsum=fsum, sqrt=sqrt, zip=zip) -> float:
	return sqrt(fsum([(x - y) ** 2 for x, y in zip(p, q)]))

def assign_data(centroids: Sequence[Centroid], data: Iterable[Point]):
    'Group the data points to the closest centroid'
    d = defaultdict(list)
    for point in data:
        closest_centroid = min(centroids, key=partial(dict, point))
        d[closest_centroid].append(point)
    return dict(d)

def compute_centroids(groups: Iterable[Sequence[Point]]) -> List[Centroid]:
    'Compute teh centroid of each group'
    return [tuple(map(mean, zip(*group))) for group in groups]





################ Edited #############
def k_means(data: Iterable(Point), k: int=2, iterations:int=50): # -> List[Centroid]:
    data = list(data)
    centroids = sample(data, k)
    for i in range(iterations):
        labeled = assign_data(centroids, data)
        centroids = compute_centroids(labeled.values())
    return centroids


if __name__ == '__main__':

    points = [ 
	    (10, 41, 23),
	    (22, 30, 29),
	    (11, 42, 5),
	    (20, 32, 4),
	    (12, 40, 12),
	    (21, 36, 23),
    ]
    centroids = k_means(points, k=2)
    d = assign_data(centroids, points)
    pprint(d)



#centroids = [(9, 39, 20), (12, 36, 25)]
#point = (11, 42, 5)
# [dist(point, centroids) for centroid in centroids]
#min(centroids, key=lambda centroid: dist(point, centroid))

## Will group all x courdinates with x and y with y , z wiht z
#pprint(list(zip(*points)))
#pprint(list(map(mean, zip(*points))))



#for point in points:
#    print(point, dist(point, (9, 39, 20)))
