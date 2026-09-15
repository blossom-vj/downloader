import subprocess
import sys
from get_best_content import get_best_content 
import pandas as pd

# Example call- python3 src/downloader/batch_download_files.py "src/inputs/example-files.csv"

def parse_timestamps(data):
    # Parse timestamps

    data["start"] = data["start"].fillna("0:00").astype(str).radd("*")
    data["end"] = data["end"].fillna("inf").astype(str).radd("-")
    data["range"] = data["start"] + data["end"]

    return data

def batch_download(csv):
    # Batch download from CSV

    data = pd.read_csv(csv)

    # Ensure that correct variables are present
    try:
        data[['link','start','end']]
    except Exception as e:
        print(e)

    data = parse_timestamps(data)

    # Loop through videos
    for video in data.itertuples(index=True):
        # Get best available formats, prioritizing h.264
        get_best_content(video.link, video.range)

    return

if __name__ == "__main__":

    # 1 argument - csv location
    batch_download(sys.argv[1])