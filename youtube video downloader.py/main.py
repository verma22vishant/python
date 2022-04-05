from pytube import YouTube

link = "https://youtu.be/JwxsPKuu_Fs"
# Link of  video that you have to download
youtube_1 = YouTube(link)

# print(youtube_1.title)
#print(youtube_1.thumbnail_url)

videos = youtube_1.streams.all()

#videos = youtube_1.streams.filter(only_audio=True)
vid = list(enumerate(videos))
for i in vid:
   print(i)
strm = int(input("enter : "))
videos[strm].download()
print('Successfully')

