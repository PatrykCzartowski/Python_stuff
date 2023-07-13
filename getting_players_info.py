import requests
from bs4 import BeautifulSoup

def get_players_info():
    url = "https://www.premierleague.com/players"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        players = soup.find_all("a", class_="playerName")
        positions = soup.find_all("td", class_="hide-s")
        
        name = []
        for player in players:
            name.append(player.text.strip())
            
        i = 0
        position = []
        country = []
        while i < len(positions):
            if i%2 == 0 and i != 0:
                position.append(positions[i].text.strip())
            else:
                country.append(positions[i].text.strip()) 
            i+=1

        position.append(country[0])
        country.pop(0)

        for i in range(len(position)):
            print((name[i],position[i],country[i]))
    else:
        print("An error occurred while downloading data.")

get_players_info()

