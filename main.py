from pytube import Playlist
import youtube_dl
import sys

print("#####################################################")
print("#        Youtube playlist to MP3  downloader         #")
print("#####################################################")

try:
    url = input("Please enter the url of the playlist you wish to download: ")
    #url = "https://www.youtube.com/playlist?list=PLpPVD1gS2eSFturasjuoJxAp0Hl2RxI4n"
    pl = Playlist(url)
    pl_length = pl.length
    print('Number of videos in playlist: ' + str(pl.length))
except Exception:
    sys.exit("The playlist could not be downloaded!!!\nPlease check the playlist url ina browser!!!")

# Uncomment the below line to customize download directory
# filepath = input("Please enter the filepath of the directory where this script is located:\n")
filepath = "downloads"
# get linked list of links in the playlist
for video_url in pl.video_urls[:pl_length]:
    try:
        # print(url)
        video_info = youtube_dl.YoutubeDL().extract_info(
            url = video_url, download = False
        )
        filename = f"{video_info['title']}.mp3"
        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': filepath + '/' + filename,
        }

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
            print("Download complete... {}".format(filename))
    except Exception:
        print("Couldn\'t download the audio!!! \n Moving onto the next file!!!")
