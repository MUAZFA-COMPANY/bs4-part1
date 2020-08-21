import requests
import bs4

html_doc = requests.get("https://www.detik.com/tag/din-syamsuddin", params={'tag_from': 'wp_tagpopuler'})

soup = bs4.BeautifulSoup(html_doc.text, features='html.parser')

popular_area = soup.find(attrs={'class': 'list media_rows list-berita'})

urls = popular_area.find_all('a')

for url in urls:
    print(url['href'])
    print(url.find(attrs={'class': 'ratiobox_content lqd'}).find('img')['title'])
