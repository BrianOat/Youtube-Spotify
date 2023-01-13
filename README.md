# Youtube-Spotify
This program utilizes VLC Media Player, a free and open source cross-platform multimedia player, to download youtube videos, and convert them to .mp3 to upload them to your spotify local files folder.



Prerequisites before laucnhing the program:
1. You must have VLC Media Player
download link: https://www.videolan.org/vlc/download-windows.html

2. You must have chromedriver
download link: https://chromedriver.chromium.org/downloads

3. You must have activated Spotify Local Files and have added a source folder
more info: https://support.spotify.com/us/article/local-files/

4. Open VLC Media Player, go to media, then convert/save, then click add, select a random file, then make sure u select Audio - Mp3 which is under settings, next to profile, then you can exit/cancel and now this option will remain selected on vlc. This is a required step because reformatting the downloaded video to .mp3 is necessary to view it on spotify, and it was not possible to have the python program select the option when running. Only need to do this once, unless you change it.

5. Follow the directions on comments at the top of main.py to correctly specify your directories



Some things that can go wrong:
1. If VLC Media Player is not playing a youtube video, it might be due to the youtube.luac file, download the latest version here: https://github.com/videolan/vlc/blob/master/share/lua/playlist/youtube.lua
Replace the current luac file in your vlc directory with this one.

2. Make sure your chrome driver supports your chrome version, you can check you chrome version by going into chrome, click the 3 dots on top right corner, then go to settings, and scroll down and click About Chrome, there you will find your chrome version
