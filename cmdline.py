import platform
import os
import pytube
from youtube import YouTubeDownloader


def main():
    banner = """
         __   __ _____  ____  _      ___        ____                          _                    _             
         \ \ / /|_   _|/ ___|| |    |_ _|      |  _ \   ___ __      __ _ __  | |  ___    __ _   __| |  ___  _ __ 
          \ V /   | | | |    | |     | | _____ | | | | / _ \\ \ /\ / /| '_ \ | | / _ \  / _` | / _` | / _ \| '__|
           | |    | | | |___ | |___  | ||_____|| |_| || (_) |\ V  V / | | | || || (_) || (_| || (_| ||  __/| |   
           |_|    |_|  \____||_____||___|      |____/  \___/  \_/\_/  |_| |_||_| \___/  \__,_| \__,_| \___||_|   
         
        -- by @hendurhance
    """
    print(banner)
    type_msg = "Enter type of download:\n"
    type_msg += "  [1] Single video\n"
    type_msg += "  [2] Playlist\n"
    type_msg += "Enter your choice: "
    type = input(type_msg)
    while type not in ["1", "2"]:
        print("Invalid choice. Please enter a valid choice.")
        type = input(type_msg)

    url = input("Enter the URL of the YouTube video or playlist: ")
    downloader = YouTubeDownloader(url, "", "")
    while not downloader.validate_url():
        print("Invalid URL. Please enter a valid URL.")
        url = input("Enter the URL of the YouTube video or playlist: ")
        downloader = YouTubeDownloader(url, "", "")
    yt = pytube.YouTube(url)
    available_qualities = []
    for stream in yt.streams:
        if stream.resolution not in available_qualities:
            available_qualities.append(stream.resolution)
    print("Available qualities: ", available_qualities)
    quality_msg = "Enter the quality of the downloaded video(s) (e.g. 1080p, 720p, 480p, 360p): "
    quality = input(quality_msg)
    while quality not in available_qualities:
        print("Invalid quality. Please enter a valid quality.")
        quality = input(quality_msg)
    output_path = input(
        "Enter the output path for the downloaded video(s) (leave empty for default folder): ")
    if output_path == "":
        if platform.system() == "Windows":
            output_path = os.path.join(
                os.getenv("HOMEDRIVE"), os.getenv("HOMEPATH"), "Downloads")
        else:
            output_path = os.path.join(os.getenv("HOME"), "Downloads")

    downloader = YouTubeDownloader(url, output_path, quality)
    if type == "1":
        yt = pytube.YouTube(url)
        video = yt.streams.filter(resolution=quality).first()
        try:
            video.download(output_path)
        except KeyboardInterrupt:
            print("Download cancelled.")
    else:
        try:
            playlist = yt.streams.filter(resolution=quality).all()
            for video in playlist:
                video.download(output_path)
        except KeyboardInterrupt:
            print("Download cancelled.")

if __name__ == "__main__":
    main()
