# Programmed by Piboy314
# A youtube info and downloader
import getpass, sys, os

from pytube import YouTube
from colorama import init, Fore, Style
from pathlib import Path

# Define initial variables
username = getpass.getuser()
downloads_path = str(Path.home() / "Downloads")

# Callback functions
def on_complete(stream, filepath):
    print("Download complete!")
    print(filepath)

def on_progress(stream, chunk, bytes_remaining):
    progress_string = f"{100 - round(bytes_remaining / stream.filesize * 100, 2)}% complete"
    print(progress_string)

init()

# Create video object
link = input("Enter video link (Don't forget https://): ")
if link == "rickroll":
    link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
elif link == "rickroll4k":
    link = "https://www.youtube.com/watch?v=o-YBDTqX_ZU"

video_object = YouTube(link,
    on_complete_callback = on_complete,
    on_progress_callback = on_progress
)

# Print info
print(Fore.RED + f"Title:  {Style.RESET_ALL}{video_object.title}")
print(Fore.RED + f"Length: {Style.RESET_ALL}{round(video_object.length / 60, 2)} minutes")
print(Fore.RED + f"Views:  {Style.RESET_ALL}{round(video_object.views / 1000000, 2)} million")
print(Fore.RED + f"Author: {Style.RESET_ALL}{video_object.author}")

# Download
print(
    Fore.RED + "Download: " +
    Fore.GREEN + "(b)est " + Style.RESET_ALL + "| " +
    Fore.YELLOW + "(w)orst " + Style.RESET_ALL + "| " +
    Fore.BLUE + "(a)udio " + Style.RESET_ALL + "| " +
    "(e)xit"
 )
download_choice = input(f"{username} $ ")

if download_choice == "b":
        if os.path.exists(str(video_object.title) + str(downloads_path)):
            print("File already exists in downloads")
        print("Downloading full quality video")
        video_object.streams.get_highest_resolution().download(downloads_path)

if download_choice == "w":
        print("Downloading low quality video")
        video_object.streams.get_lowest_resolution().download(downloads_path)

if download_choice == "a":
        print("Downloading audio")
        video_object.streams.get_audio_only().download(downloads_path)

if download_choice == "e":
        print("Exiting")
        sys.exit()

