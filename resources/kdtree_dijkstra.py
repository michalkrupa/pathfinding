
from collections import defaultdict
import heapq
from scipy.spatial import KDTree
import math

def calculate_shortest_path_using_djikstras_kdtree(points, k=10):
    """
    Dijkstra's algorithm using a KD-tree to limit neighbors (approximate shortest path).
    points: List of [x, y] coordinates
    k: Number of nearest neighbors to connect in the graph
    """
    points = [tuple(p) for p in points]
    tree = KDTree(points)
    graph = defaultdict(list)

    # Build graph using k-nearest neighbors
    for i, pt in enumerate(points):
        dists, indices = tree.query(pt, k + 1)  # k+1 because query includes the point itself
        for dist, idx in zip(dists[1:], indices[1:]):
            neighbor = points[idx]
            graph[pt].append((neighbor, dist))

    start = points[0]
    end = points[-1]

    # Dijkstra's algorithm
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        if node == end:
            return cost, path
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))

    return float('inf'), None
