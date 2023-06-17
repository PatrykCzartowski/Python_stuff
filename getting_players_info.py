import requests
from bs4 import BeautifulSoup

def get_players_info():
    url = "https://www.premierleague.com/players"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        #print(soup)
        lista_pilkarzy = soup.find_all("a", class_="playerName")
        lista_pozycji = soup.find_all("td", class_="hide-s")
        name = []
        for pilkarz in lista_pilkarzy:
            name.append(pilkarz.text.strip())
        i = 0
        position = []
        country = []
        while i < len(lista_pozycji):
            if i%2 == 0 and i != 0:
                position.append(lista_pozycji[i].text.strip())
            else:
                country.append(lista_pozycji[i].text.strip()) 
            i+=1

        position.append(country[0])
        country.pop(0)

        for i in range(len(position)):
            print((name[i],position[i],country[i]))
    else:
        print("Wystąpił błąd podczas pobierania danych.")

get_players_info()
