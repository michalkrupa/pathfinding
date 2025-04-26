from load_coordinates import load_coordinates_from_csv
from benchmark_utils import benchmark_algorithm
from kdtree_dijkstra import calculate_shortest_path_using_djikstras_kdtree
from pathfinder import calculate_shortest_path

if __name__ == "__main__":
    coordinates = load_coordinates_from_csv('./test_data.csv')

    (result, duration) = benchmark_algorithm(calculate_shortest_path_using_djikstras_kdtree, coordinates, label="Djikstras")

    (result, duration) = benchmark_algorithm(calculate_shortest_path, coordinates, label="Pathfinder")
