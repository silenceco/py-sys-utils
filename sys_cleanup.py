import os
import shutil
import pathlib
from datetime import datetime

def get_dir_size(path: str) -> float:
    """Calculates directory size in Megabytes."""
    total_size = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return round(total_size / (1024 * 1024), 2)

def log_status(message: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

if __name__ == "__main__":
    current_dir = os.getcwd()
    log_status(f"Scanning directory: {current_dir}")
    size_mb = get_dir_size(current_dir)
    log_status(f"Total directory size: {size_mb} MB")
