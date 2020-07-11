
from flask import Flask, render_template, request
import os
import subprocess

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def createPlaylist():
    playlistName = ''
    songURL = ' '
    songName = ' '

    if request.method == 'POST':

        playlistName = request.form.get('playlistName')

        songURL = request.form.get('songURL')

        songName = request.form.get('songName')

        subprocess.call(['youtube-dl', '-o', os.path.expanduser('~') + '\\Desktop\\' + songName + ".mp3",
        "--extract-audio", "--audio-format", "mp3", songURL])

        # os.mkdir(r'C:\Users\Aidan\Desktop\folder')
        
        # password = request.form.get('password')

    return render_template('index.html', playlistName=playlistName, songName=songName)

 

    

            

if __name__ == "__main__":
    app.run(debug = True)


# song_name = input("Please enter the name: ")
# song_url = input("Please enter the url: ")


