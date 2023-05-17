import numpy as np
import os
from pydub import AudioSegment
from pydub.playback import play

def play_playlist(playlist):
    original_playlist = playlist[:]  # Make a copy of the original playlist
    while True:
        np.random.shuffle(playlist)  # Shuffle the playlist
        # Playlist loop
        for i, song in enumerate(playlist):
            # Get the file name from the path
            file_name = os.path.basename(song[0])
            # Print the current song
            print("Now playing:", file_name)
            
            # Play the song
            play(song[1])
            
            # Check if it's the last song
            if i == len(playlist) - 1:
                # Ask for user input (skip, replay, reshuffle, or exit)
                user_input = input("'r' to replay, 'm' to reshuffle, or 'e' to exit: ")
                
                # Check user input for skip, replay, reshuffle, or exit
                if user_input == 's':
                    continue  # Skip to the next song
                elif user_input == 'r':
                    playlist = original_playlist[:]  # Reset playlist to original order
                    break  # Replay the same order
                elif user_input == 'm':
                    continue  # Start playing the reshuffled playlist
                elif user_input == 'e':
                    return  # Exit the program
            else:
                # Ask for user input (skip or continue)
                user_input = input("Press 's' to skip to the next song, or 'c' to continue: ")
                
                # Check user input for skip or continue
                if user_input == 's':
                    continue  # Skip to the next song
                elif user_input == 'c':
                    playlist = playlist[i+1:]  # Continue playing from the next song
                    break  # Continue playing from the next song

# Function to get the list of audio files from a folder
def get_audio_files_from_folder(folder_path):
    audio_files = []
    supported_formats = [".wav", ".mp3", ".flac", ".ogg", ".aac"]  # Add more formats if needed
    for file in os.listdir(folder_path):
        if file.lower().endswith(tuple(supported_formats)):
            file_path = os.path.join(folder_path, file)
            audio_files.append((file_path, AudioSegment.from_file(file_path)))
    return audio_files

# Define the folder path containing the songs
folder_path = '/home/kushwanth/Downloads/songs/dodo'

# Get the list of audio files from the folder
playlist = get_audio_files_from_folder(folder_path)

# Shuffle the original playlist
np.random.shuffle(playlist)

# Play the playlist
play_playlist(playlist)

