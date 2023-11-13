import tkinter as tk
from download_module import download_music, get_downloaded_file_path 
from retrieve_metadata import fetch_deezer_album_data, extract_album_metadata # Import necessary functions
from embed_module import embed_metadata

root = tk.Tk()
root.title("Generation DL")

# Label
label = tk.Label(root, text="Enter YouTube Link:")
label.pack()

# Entry widget for the YouTube link
youtube_link_entry = tk.Entry(root, width=40)
youtube_link_entry.pack()

from tkinter import ttk

# Create a notebook for tabbed interface
notebook = ttk.Notebook(root)
notebook.pack()

# Create a tab for settings
settings_tab = ttk.Frame(notebook)
notebook.add(settings_tab, text="Settings")

# Audio Quality Label and Combobox
audio_quality_label = tk.Label(settings_tab, text="Audio Quality:")
audio_quality_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

audio_quality_combobox = ttk.Combobox(settings_tab, values=["best", "worst", "128k", "256k"])
audio_quality_combobox.grid(row=0, column=1, padx=10, pady=5)
audio_quality_combobox.set("best")  # Set the default value

# Output Format Label and Radiobuttons
output_format_label = tk.Label(settings_tab, text="Output Format:")
output_format_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

output_format_var = tk.StringVar()
output_format_var.set("wav")  # Set the default format

wav_radio = tk.Radiobutton(settings_tab, text="WAV", variable=output_format_var, value="wav")
mp3_radio = tk.Radiobutton(settings_tab, text="MP3", variable=output_format_var, value="mp3")
aac_radio = tk.Radiobutton(settings_tab, text="AAC", variable=output_format_var, value="aac")  # Add AAC option

wav_radio.grid(row=1, column=1, padx=10, pady=5, sticky="w")
mp3_radio.grid(row=1, column=2, padx=10, pady=5, sticky="w")
aac_radio.grid(row=1, column=3, padx=10, pady=5, sticky="w") 


def download_music_gui():
    youtube_link = youtube_link_entry.get()  # Get the entered YouTube link
    audio_quality = audio_quality_combobox.get()  # Get selected audio quality
    output_format = output_format_var.get()  # Get selected output format

    # Call your download function here, passing the user inputs
    result = download_music(youtube_link, audio_quality, output_format)
    audio_file_path = get_downloaded_file_path(youtube_link, audio_quality, output_format)
    deezer_album_id = fetch_deezer_album_data(youtube_link)

    if deezer_album_id is None:
        result_label.config(text="Deezer Album ID not found.")
        return
    
    # Fetch album metadata using the Deezer Album ID
    metadata = extract_album_metadata(deezer_album_id)
    embed_metadata(audio_file_path, metadata, output_format)
    # Update the result label with the download result and album metadata
    result_label.config(text=result)

download_button = tk.Button(root, text="Download", command=download_music_gui)  # Connect to download_music_gui
download_button.pack()

result_label = tk.Label(root, text="", fg="green")  # Create an empty label
result_label.pack()

root.mainloop()
