from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=m1147UUT31A')
print(yt.title)
# for i in yt.streams:
#     print(i)

download1=yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
print(download1.url)