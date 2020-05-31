from __future__ import unicode_literals
import youtube_dl

class MyLogger(object):
    def debug(self, msg):
        print (msg)
        pass

    def warning(self, msg):
        print (msg)
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading')


ydl_opts = {
    'nooverwrites' : True,
    'ignoreerrors' : True,
    'format': 'bestaudio/best',
    'logger': MyLogger(),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'progress_hooks': [my_hook],
    'outtmpl' : 'D://Music/DOWNLOADS/Sets/%(title)s.%(ext)s'
}
print("Inserisci link da scaricare")
link = input()
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
    print("Inserire un altro link o scrivere exit per uscire")
    link = input()
    while link!="exit":
        ydl.download([link])
        print("Inserire un altro link o scrivere exit per uscire")
        link = input()
        
    