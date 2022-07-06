import youtube_downloader
import file_converter

links = youtube_downloader.input_links()
for link in links:
    print("Downloading...")
    filename = youtube_downloader.download_video(link, 'low')
    print("Converting...")
    file_converter.convert_to_mp3(filename)