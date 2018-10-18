import youtube_dl
import requests
from bs4 import BeautifulSoup as bs
import sys

ydl_video = {
    'format': 'mp4/bestvideo+bestaudio'
}
ydl_mp3 = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '10000',
    }]
}

try:
    download_type = int(input("1: video download 2: audio download : "))
    mode = int(input("1: download from seach result 2: download from url  : "))
except ValueError:
    sys.exit(0)

if download_type == 1:
    opt = ydl_video

else:
    opt = ydl_mp3

if mode == 1:
    keyword = input("input search keyword: ")
    response = requests.get('https://www.youtube.com/results?search_query=%s' % keyword)

    soup = bs(response.text, 'html.parser')
    titles = soup.find_all('h3', {'class': 'yt-lockup-title'})

    for i, title in enumerate(titles):
        uri = title.find('a')["href"]
        _title = title.find('a').text
        print(i, _title)

    selected = int(input("select number of video(audio) : "))
    url = "https://www.youtube.com" + titles[selected].find('a')["href"]
    print(url)

else:
    url = input("input youtube url : ")

ydl = youtube_dl.YoutubeDL(opt)
ydl.download([url])
