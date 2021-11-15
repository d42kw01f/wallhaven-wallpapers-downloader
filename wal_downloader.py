import re
import requests
from bs4 import BeautifulSoup
from requests.api import head 
from tqdm.auto import tqdm
import lxml

def scrapingtheweb(theLink):
    header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'}
    r = requests.get(theLink, headers=header)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        wal_url = soup.find('img', id='wallpaper')
        return wal_url['src']

def main():
    number_url = int(input('How many urls are there: '))
    print("Enter all the urls here: ")
    urls = []
    for inputs in range(number_url):
        url = input()
        urls.append(url)
    for i in tqdm(urls):
        try:
            the_url = scrapingtheweb(i)
            theimg = requests.get(the_url)
            file_name = the_url.split('/')[-1]
            with open(file_name, 'wb') as file:
                file.write(theimg.content)
                file.close()
        except:
            continue


main()