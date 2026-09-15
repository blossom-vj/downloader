import subprocess
import sys

# Example call- python3 src/downloader/get_mp4.py "https://www.youtube.com/watch?v=v-IsUoDdeuY" "*00:00-0:15"

def get_mp4(link, timestamp = "*00:00-inf"):
    print("Fetching MP4", link)
    
    # Example yt-dlp command
    subprocess.run(['yt-dlp', f'{link}', 
                    "-f", "mp4",
                    "-o", "src/outputs/%(title)s.%(ext)s",
                    "--download-sections", f"{timestamp}"])

    return

if __name__ == "__main__":
    try:
        get_mp4(sys.argv[1], sys.argv[2])
    except:
        get_mp4(sys.argv[1])
