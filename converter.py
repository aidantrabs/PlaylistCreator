from flask import Flask, render_template, request, redirect, url_for
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

    # If post request sent 
    if request.method == 'POST':

        # Form information
        playlistName = request.form['playlistName']
        songURL = request.form['songURL']
        songName = request.form['songName']

        # Check if playlist name is not empty
        if playlistName != "":
            try:
                os.mkdir(os.path.expanduser('~') + '\\Desktop\\' + playlistName)
            except(FileExistsError):
                error_message = 'This playlist folder already exists!'

        # Use youtube-dl to download song at specific file path 
        subprocess.call(['youtube-dl', '-o', songName + ".mp3",
        "--extract-audio", "--audio-format", "mp3", songURL])

        # Move song files to playlist folder
        os.system('move ' + songName + ".mp3 " + os.path.expanduser('~') + '\\Desktop\\' + playlistName)

    # Return html page
    return render_template('index.html', playlistName=playlistName, songName=songName)

if __name__ == "__main__":
    app.run(debug = True)
