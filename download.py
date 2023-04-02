import os
from pytube import YouTube

# Input the YouTube video URL
url = input("Enter the YouTube video URL: ")

# Create the folder to save the video
folder_name = input("Enter the folder name to save the video: ")
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Download the video
yt = YouTube(url)
stream = yt.streams.first()
stream.download(output_path=folder_name)

print("Video downloaded successfully!")
