## Scrapes GoodRead's top quotes, saving to quotes.txt

from bs4 import BeautifulSoup
import requests

base_url = 'https://www.goodreads.com/quotes?page='
url = lambda page: base_url + str(page)

quotes = []

for page in range(1,101):
    r = requests.get(url(page))
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'html.parser')
    quotes += [
        str(quote).split('\n  <br/>  ―\n', 1)[0][30:].replace('<br/>', '').replace('<br>', '')
        for quote
        in soup(class_='quoteText')]
    print(page)

with open('quotes.txt', 'w') as f:
    f.write('\n'.join(quotes))
