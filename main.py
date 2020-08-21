import bs4
import requests

url = 'https://www.jadwalsholat.org/adzan/monthly.php?id=232'
contents = requests.get(url)

response = bs4.BeautifulSoup(contents.text, features="html.parser")
data = response.find_all('tr', 'table_highlight')
data = data[0]

sholat = {}
i = 0
for d in data:
    if i == 0:
        sholat['tanggal'] = d.get_text()
    elif i == 2:
        sholat['subuh'] = d.get_text()
    elif i == 2:
        sholat['duhur'] = d.get_text()
    elif i == 4:
        sholat['ashar'] = d.get_text()
    elif i == 5:
        sholat['maghrib'] = d.get_text()
    elif i == 6:
        sholat['isya'] = d.get_text()
    i += 1

print(sholat['isya'])
