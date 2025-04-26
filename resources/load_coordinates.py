
import pandas as pd

def load_coordinates_from_csv(csv_path):
    df = pd.read_csv(csv_path)
    return df[["x", "y"]].values.tolist()
