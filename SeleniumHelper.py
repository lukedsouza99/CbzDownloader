from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from WebScraper import WebScraper

# Returns HTML after javascript to be used with BeautifulSoup for the given link.
# SeleniumGetHTML.SeleniumGetHTML(link).get()
class SeleniumHelper:
    
    #Get HTML from website
    def getHTML(self, link):
        options = Options()
        options.headless = True
        options.add_argument("--log-level=3")
        driver = webdriver.Chrome(options=options)
        driver.get(link)
        time.sleep(3)
        html = driver.page_source
        driver.quit()
        return html

    # Get soup object from HTML using WebScraper class
    def getSoupFromLink(self, link):
        return WebScraper().getSoupFromSeleniumSource(self.getHTML(link))
        
