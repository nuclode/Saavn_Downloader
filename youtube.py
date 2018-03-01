import os
import requests
from bs4 import BeautifulSoup

# to get link of youtube songs
def getLink(name):
	url = 'https://www.youtube.com/results?search_query=' + str('+'.join(name.split()))
	data = requests.get(url)
	soup = BeautifulSoup(data.text, 'html.parser')
	for song in soup.find_all('a'):
		if '/watch' in song.get('href'):
			return "https://www.youtube.com" + song.get('href')
