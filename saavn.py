import requests
from bs4 import BeautifulSoup
from youtube import getLink
import os

# to get the list of songs on a page 
def getSongs(url):
	data = requests.get(url)
	soup = BeautifulSoup(data.text, 'html.parser')
	playlistName = soup.find('title').text.split(',')[0]
	songs = {}
	for song in soup.find_all('p', attrs={'class':'song-name ellip'}):
		title, albumName = song.text.split('\n')[0:2]
		songs[title] = {}
		songs[title]['album'] = albumName
	return songs,playlistName

url = input('> Enter link: ')
songs,playlistName = getSongs(url)
os.system('mkdir "%s"' %(playlistName))
os.system('cd ' + playlistName)
for song, details in songs.items():
	print("Downloading " + song)
	temp = song.split('(')[0]
	os.system('youtube-dl --extract-audio --audio-format mp3 -q -o ' +  "name.%(ext)s " + getLink(song))
	os.rename('name.mp3', '%s.mp3' %(temp))
	os.system('mv "%s.mp3" "%s"' %(temp,playlistName))