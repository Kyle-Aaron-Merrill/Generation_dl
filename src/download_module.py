from youtube_dl import YoutubeDL
import os

def download_music(youtube_link, audio_quality, output_format):
    # Define download options based on user inputs
    ydl_opts = {
        'format': audio_quality,
        'outtmpl': f'downloads/%(title)s.{output_format}',  # Output folder and file format
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            # Download the video/audio based on the YouTube link
            info_dict = ydl.extract_info(youtube_link)
            # Return a success message
            return "Downloaded successfully: " + info_dict['title']
        except Exception as e:
            # Handle download errors and return an error message
            return "Error during download: " + str(e)

def get_downloaded_file_path(youtube_link, audio_quality, output_format):
    # Define download options based on user inputs
    ydl_opts = {
        'format': audio_quality,
        'outtmpl': f'downloads/%(title)s.{output_format}',  # Output folder and file format
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            # Download the video/audio based on the YouTube link
            info_dict = ydl.extract_info(youtube_link)
            # Get the path of the downloaded file
            downloaded_file_path = os.path.abspath(ydl.prepare_filename(info_dict))
            # Return the path of the downloaded file
            return downloaded_file_path
        except Exception as e:
            # Handle download errors and return None if there's an issue
            return None
