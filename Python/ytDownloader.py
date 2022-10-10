#Python program to download youtube videos
#Disclamer: Please respect youtube policies

from pytube import YouTube

path = input("Enter the local directory to download: ")
link = input("Enter link of video: ")

yt_video = YouTube(link)

yt_video.streams.get_highest_resolution().download(path)

print("Video Downloaded Sucessfully!! ",yt_video.title)