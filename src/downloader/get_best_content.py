import subprocess
import sys
# https://ytdlp.org/guides/yt-dlp-format-selection

# Example call- python3 src/downloader/get_best_content.py "https://www.youtube.com/watch?v=v-IsUoDdeuY" "*00:00-0:15"

def get_best_content(link, timestamp = "*00:00-inf"):
    print("Fetching MP4", link)
    
    # Example yt-dlp command
    subprocess.run(['yt-dlp', f'{link}', 
                    "-f", "bv*+ba/b", # Best audio, best video where available
                    "-o", "outputs/%(title)s.%(ext)s",
                    "-S", "vcodec:h264,res,acodec:m4a", # deprioritize webm formats
                    "--download-sections", f"{timestamp}"])

    return

if __name__ == "__main__":
    try:
        get_best_content(sys.argv[1], sys.argv[2])
    except:
        get_best_content(sys.argv[1])
