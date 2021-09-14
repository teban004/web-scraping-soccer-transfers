import requests
from bs4 import BeautifulSoup

#get the data from the website
data = requests.get('https://espndeportes.espn.com/futbol/transferencias')

#load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

#get data simply by looking for each <tr>
data =[]
for table in soup.find('table', {'class': 'Table'}):
    for tr in table.find_all('tr', { 'class': 'Table__TR'}):
        values = [td.text for td in tr.find_all('td')]
        data.append(values)

print(data)
