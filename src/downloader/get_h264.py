import subprocess
import sys

def get_h264(link):
    print(f"Fetching h264 {link}")
    
    # Example yt-dlp command
    subprocess.run(['yt-dlp', f'{link}', "-f", "(bv*[vcodec~='^((he|a)vc|h26[45])']+ba) / (bv*+ba/b)"])

    return

if __name__ == "__main__":
    get_h264(sys.argv[0])