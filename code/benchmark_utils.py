
from datetime import datetime

def benchmark_algorithm(func, *args, label="Algorithm"):
    print(f"Running {label}...")
    start_time = datetime.now()
    result = func(*args)
    end_time = datetime.now()
    duration = end_time - start_time
    print(f"{label} completed in {duration.total_seconds():.4f} seconds.")
    return result, duration.total_seconds()
