import os
from pytube import YouTube


URLS_LIST_FILE = "urls.txt"
MUSIC_OUTPUT_PATH = "./music"


urls_to_fetch = []

with open(URLS_LIST_FILE, "r") as urls:
    for url in urls:
        urls_to_fetch.append((url.strip()))

for video_url in urls_to_fetch:
    yt = YouTube(video_url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=MUSIC_OUTPUT_PATH)
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)
    print(yt.title + " foi baixado com sucesso!")