# downloader
This project allows a user to input a list of videos and loop through them with `yt-dlp` using a `.csv` input file.

Example acceptable input:

| link                                        | start | end  | note                                              |
|---------------------------------------------|-------|------|---------------------------------------------------|
| https://www.youtube.com/watch?v=VvqOvToCoi8 | 0:00  | 0:23 | Heather happy birthday                            |
| https://www.youtube.com/watch?v=9q9SNspy2FU | 0:25   |      | Baby monkey riding backwards on a pig baby monkey |
| https://www.youtube.com/watch?v=IEpHswmkisQ |       |      | Balegdeh                                          |

This should work for any site that is compatible with `yt-dlp`.

## Requirements
Ensure you have `uv` installed, `git` installed and configured to your PATH variables.

## Clone this repository
From the command line:
```
# Step 1: clone repository
git clone https://github.com/blossom-vj/downloader

# Step 2: navigate to downloader
cd downloader

# Step 3: sync environment from .toml file
uv sync

# Step 4: activate environment
source .venv/bin/activate
```
You should now be able to run the code.

## Functionality
From the command line:
```
# Get best available audio and video for one link, preferring mp4.
python3 src/downloader/get_best_content.py "https://www.youtube.com/watch?v=v-IsUoDdeuY" "*00:00-0:15"

# Go through entire provided list.
python3 src/downloader/batch_download_files.py "src/inputs/example-files.csv"
```
