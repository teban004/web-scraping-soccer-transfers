import requests
from bs4 import BeautifulSoup

#get the data from the website
data = requests.get('https://espndeportes.espn.com/futbol/transferencias')

#load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

#get data simply by looking for each <tr>
data =[]
for table in soup.find('table', {'class': 'Table'}):
    for tr in table.find_all('tr'):
        td = tr.find_all('td', {'class': 'Table__TD'})
        if( len(td)>0 ):
            fecha = td[0].text.strip()
            jugador = td[1].text.strip()
            equipoAnterior = td[2].find_all('span')[1].text.strip()
            equipoNuevo = td[4].find_all('span')[1].text.strip()
            print(fecha + "\t| " + jugador + " \t| " + equipoAnterior + " => " + equipoNuevo)

        
