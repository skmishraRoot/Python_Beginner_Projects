# for this to work make sure you download python and pytube

# imports
from pytube import YouTube
from pathlib import Path


# getting the home dir path and adding downloads at the end to get absolute downloads folder path
downloads_path = str(Path.home() / "Downloads")

# Path where file get saved
save_path = downloads_path

# Taking input of link from user
link = input('Enter your link here: ')

# checking the link using try and except block
try:
    yt = YouTube(link)
except:
    print('Enter a correct link.')

# Print video title
print("Title: ", yt.title)

# Taking input to check what file type program need to download.
download_type = input('For audio file enter "a" and for video file enter "v": ')

# checking for audio = 'a'
if download_type.lower() == 'a':
    # using try and except block checking the heights quality possible for download
    try:
        print('Downloading in audio format.')
        audio_file = yt.streams.get_by_itag(251)
    except:
        print('Downloading in audio format.')
        audio_file = yt.streams.get_by_itag(250)
    try:
        print('Download under progress wait a while and check downloads folder on your computer.')
        audio_file.download(save_path)
        print('Download complete enjoy your download.')
    except:
        # if program unable to download it wills how this
        print('Unable to download some error happened')

# checking for video = 'v'
elif download_type.lower() == 'v':
    #  # using try and except block checking the heights quality possible for download
    try:
        print('Downloading in 720p resolution.')
        download = yt.streams.get_by_itag(22)
    except:
        print('Downloading in 360p resolution.')
        download = yt.streams.get_by_itag(18)

    # downloading video
    try:
        print('Download under progress wait a while and check downloads folder on your computer.')
        download.download(save_path)
        print('Download complete enjoy your download.')
    except:
        # if program unable to download it wills how this
        print('Unable to download some error happened')

# if program fails to download it will prompt this
else:
    print('Unable to download.Try again.')

