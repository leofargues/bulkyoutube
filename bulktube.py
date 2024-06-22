from time import sleep
from tqdm import tqdm
from pytube import YouTube
from colorama import Fore, Back, Style
print(Style.RESET_ALL)
print(r"""
  ____        _ _ _______    _          
 |  _ \      | | |__   __|  | |         
 | |_) |_   _| | | _| |_   _| |__   ___ 
 |  _ <| | | | | |/ / | | | | '_ \ / _ \
 | |_) | |_| | |   <| | |_| | |_) |  __/
 |____/ \__,_|_|_|\_\_|\__,_|_.__/ \___|
                                                                                
""")
print("Welcome to BulkTube, a Youtube Downloader in python")
print("You can easely download multiple video at one time without Ad")
print("")
print("Select a folder name to save your videos")
path = input()
print("")
print("Write down here video url separated by , - When you have put all url's, just press enter without writing anything")
print("")
videolist = []
queue = 1
finished = 0
while finished == 0:
    url = input("Url : ")
    if 'youtube.com' in url:
        videolist.append(url)
    else:
        print("")
        finished = 1
print(videolist)
queue = len(videolist) 
queue = queue - queue - 1 
for i in tqdm(range(len(videolist))):
    url = videolist[queue]
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    stream.download(path)
    queue = queue + 1
print("")
print("Video's", Fore.GREEN + 'succesfully', Style.RESET_ALL, "downloaded at the path (", path, ")")
queue = len(videolist) 
queue = queue - queue - 1 
print("")
print("Video", Fore.RED + 'downloaded', Style.RESET_ALL + ":")
for i in range(len(videolist)):
    url = videolist[queue]
    video = YouTube(url)
    print(video.title)
    queue = queue + 1
