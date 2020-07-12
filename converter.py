
from flask import Flask, render_template, request
import os
import subprocess

app = Flask(__name__)

# Index app route
@app.route('/', methods=['POST', 'GET'])
def createPlaylist():

    # Initialize local variables
    playlistName = ''
    songURL = ' '
    songName = ' '
    error_message = ''

    # If form request sent (button pressed)
    if request.method == 'POST':

        # Get form information
        playlistName = request.form.get('playlistName')
        songURL = request.form.get('songURL')
        songName = request.form.get('songName')

        # Check if playlist name is not empty
        if playlistName != "":
            try:
                os.mkdir(os.path.expanduser('~') + '\\Desktop\\' + playlistName)
            except(FileExistsError):
                error_message = 'This playlist folder already exists!'

        # Use youtube-dl to download song at specific file path 
        subprocess.call(['youtube-dl', '-o', os.path.expanduser('~') + '\\Desktop\\' + songName + ".mp3",
        "--extract-audio", "--audio-format", "mp3", songURL])

    # Return html page
    return render_template('index.html', playlistName=playlistName, songName=songName)

if __name__ == "__main__":
    app.run(debug = True)


