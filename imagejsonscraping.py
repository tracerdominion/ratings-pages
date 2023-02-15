from bs4 import BeautifulSoup, Comment
import requests
import re
from time import sleep

out = {}

soup = BeautifulSoup(requests.get('http://wiki.dominionstrategy.com/index.php/Allies').content,'html.parser')

for lists in soup.find_all('ul'):
    if "Bauble" in lists.text:
        for card in lists.find_all('a'):
            print(card['title'])
            cardsoup = BeautifulSoup(requests.get('http://wiki.dominionstrategy.com' + card['href']).content,'html.parser')
            if "This page is awaiting large-scale edits" in cardsoup.text:
                imagesoup = BeautifulSoup(requests.get('http://wiki.dominionstrategy.com' + cardsoup.find_all('table')[1].find('a')['href']).content,'html.parser')
            else:
                imagesoup = BeautifulSoup(requests.get('http://wiki.dominionstrategy.com' + cardsoup.find('table').find('a')['href']).content,'html.parser')
            if card['title'] not in ["Augurs", "Clashes", "Forts", "Odysseys", "Wizards"]:
                out[card['title']] = 'http://wiki.dominionstrategy.com' + imagesoup.find('a', {'class': "mw-thumbnail-link"})['href']
        break
        
print(out)