import requests
import os

def fetch_deezer_album_data(deezer_album_id):
    deezer_api_key = os.environ.get('DEEZER_API_KEY')

    if deezer_api_key is None:
        raise ValueError("DEEZER_API_KEY environment variable is not set.")

    # Deezer API endpoint for album info
    endpoint = f"https://api.deezer.com/album/{deezer_album_id}"
    params = {
        'output': 'json',
        'access_token': deezer_api_key,
    }

    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()  # Check for HTTP request errors

        album_data = response.json()
        return album_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Deezer album info: {str(e)}")
        return None

def extract_album_metadata(album_data):
    if not album_data:
        return None  # Handle the case where album_data is not available

    # Extract album name
    album_name = album_data.get('title', 'Unknown Album')

    # Extract artist name (assuming a single artist, you may adjust this for multiple artists)
    artist_name = album_data.get('artist', {}).get('name', 'Unknown Artist')

    # Extract album art URL (you can use this URL to download album art)
    album_art_url = album_data.get('cover', '')

    # Extract tracklisting
    tracks = album_data.get('tracks', {}).get('data', [])

    tracklisting = []
    for track in tracks:
        track_title = track.get('title', 'Unknown Track')
        track_duration = track.get('duration', 0)  # Duration in seconds
        track_artists = [artist.get('name', 'Unknown Artist') for artist in track.get('contributors', [])]
        
        # Additional metadata fields you may want to extract:
        track_number = track.get('track_position', 0)
        release_date = album_data.get('release_date', 'Unknown')
        genre = album_data.get('genre_id', 'Unknown Genre')

        tracklisting.append({
            'title': track_title,
            'duration': track_duration,
            'artists': track_artists,
            'track_position': track_number,
            'release_date': release_date,
            'genre_id': genre,
        })

    # Return the extracted metadata
    return {
        'album_name': album_name,
        'artist_name': artist_name,
        'album_art_url': album_art_url,
        'tracklisting': tracklisting,
    }
