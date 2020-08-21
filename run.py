import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/detik-populer')
def detik_populer():
    html_doc = requests.get("https://www.detik.com/tag/din-syamsuddin", params={'tag_from': 'wp_tagpopuler'})

    soup = BeautifulSoup(html_doc.text, features='html.parser')

    popular_area = soup.find(attrs={'class': 'list media_rows list-berita'})

    urls = popular_area.find_all('a')

    return render_template('index.html', urls=urls)


if __name__ == '__main__':
    app.run(debug=True)
