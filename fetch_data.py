import requests
from bs4 import BeautifulSoup
import time

RATE = .25
base_url = 'https://apod.nasa.gov/apod/' 
archive_url = base_url + 'archivepix.html'

def _get(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    return soup

def cache_page(filename, page):
    #do this later
    with open('cache/{filename}'.format(filename)) as f:
        pass

def get_archive_links():
    soup = _get(archive_url)
    b = soup.findAll('b')
    raw_links = b[1].findAll('a')
    links = []
    for link in raw_links: 
        links.append(link.get('href'))
    return links

def get_dailylink_text(link):
    soup = _get(base_url + link)
    ps = soup.findAll('p')
    for p in ps:
        raw_text = p.get_text().strip().split()
        if len(raw_text) != 0 and raw_text[0] == 'Explanation:':
            text = p.get_text()
    processed_text = text.replace('Explanation:', '').replace('\n', '').strip()
    return processed_text 



if __name__ == "__main__":
    links = get_archive_links()
    for link in links:
        time.sleep(RATE)
        print(get_dailylink_text(link))
        break