from load_coordinates import load_coordinates_from_csv
from pathfinder import calculate_shortest_path
from kdtree_dijkstra import calculate_shortest_path_using_djikstras_kdtree
coordinates = load_coordinates_from_csv('./test_data.csv')

if __name__ == "__main__":
    (shortest_path, walk) = calculate_shortest_path(coordinates)
    print(shortest_path)
    (shortest_path_2, walk_2) = calculate_shortest_path_using_djikstras_kdtree(coordinates)
    print(shortest_path_2)