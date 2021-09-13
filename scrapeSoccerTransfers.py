import requests
from bs4 import BeautifulSoup

#get the data from the website
data = requests.get('https://espndeportes.espn.com/futbol/transferencias')

#load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

#get data simply by looking for each <tr>
for tr in soup.find_all('tr'):
    for td in tr.find_all('td'):
        print(td.text)


