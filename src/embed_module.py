import os
from pydub import AudioSegment
import eyed3

def embed_metadata(audio_file, metadata, output_format):
    if output_format == "mp3":
        embed_metadata_mp3(audio_file, metadata)
    elif output_format in ["flac", "ogg"]:
        # Handle other formats that support embedding here
        pass
    else:
        raise ValueError(f"Embedding metadata for {output_format} is not supported.")

def embed_metadata_mp3(audio_file, metadata):
    audiofile = eyed3.load(audio_file)

    if audiofile is None:
        raise ValueError("Failed to load the audio file.")

    # Set album name
    audiofile.tag.album = metadata['album_name']

    # Set artist name
    audiofile.tag.artist = metadata['artist_name']

    # Embed tracklisting
    for i, track in enumerate(metadata['tracklisting'], start=1):
        audiofile.tag.track_num = i
        audiofile.tag.title = track['title']
        audiofile.tag.album_artist = ', '.join(track['artists'])

    audiofile.tag.save()

