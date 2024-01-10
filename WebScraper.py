from bs4 import BeautifulSoup
import requests

# Returns web scraper ("soup" object) for the given link.
# ws.WebScraper(link).get()
class WebScraper:

    #Get web scraper
    def getSoupFromLink(self, link):
        url = requests.get(link)
        return BeautifulSoup(url.text, 'html.parser')


    def getSoupFromSeleniumSource(self, html):
        return BeautifulSoup(html, 'html.parser')
