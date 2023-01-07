import pytube

class YouTubeDownloader:
    def __init__(self, url, output_path, quality):
        self.url = url
        self.output_path = output_path
        self.quality = quality

    def download_video(self):
        yt = pytube.YouTube(self.url)
        video = yt.streams.filter(resolution=self.quality).first()
        video.download(self.output_path)

    def download_playlist(self):
        yt = pytube.Playlist(self.url)
        for video in yt.videos:
            video = video.streams.filter(resolution=self.quality).first()
            video.download(self.output_path)
    
    def validate_url(self):
        try:
            yt = pytube.YouTube(self.url)
            return True
        except:
            return False
