import requests
import os
from SeleniumHelper import SeleniumHelper

class ComicIssueDownloader:

    def downloadSingleIssue(self, dir, link, series, issue, year):

        # get soup from link
        soup = SeleniumHelper().getSoupFromLink(link)

        # extract image links
        images = soup.find("div", { "id" : "divImage" }).findChildren()

        # Create list of links to images
        linkToImages = []
        for image in images:
            linkToImage = image.get("src")
            if linkToImage != None: linkToImages.append(linkToImage)

        # Download pictures to the directory
        for number, pageLink in enumerate(linkToImages):
            response = requests.get(pageLink)
            if response.status_code:
                pageTitle = self.__formatPageName(series, issue, year, number + 1, ".png")
                with open(os.path.join(dir, pageTitle), 'wb') as fp:
                    fp.write(response.content)
    


    def extractSingleIssueLinksFromMainSeries(self, link, baseUrl, tailUrl, onlyIssues):
        
        # get soup from link
        soup = SeleniumHelper().getSoupFromLink(link)
        
        table = soup.find('table')

        issues = []

        for row in table.tbody.find_all('tr'):
            for row2 in row.find_all("td"):
                issue = row2.find('a')
                if issue != None : issues.append(baseUrl + issue['href'] + tailUrl)
        issues.reverse()

        if onlyIssues:
            filteredIssues = []
            for i in issues:
                if "Issue" in i:
                    filteredIssues.append(i)
            return filteredIssues
        
        return issues



    # Format comic page title
    def __formatPageName(self, seriesName, issueText, yearText, pageNumber, imageFormat):
        pageNumberString = "0" + str(pageNumber) if pageNumber < 10 else str(pageNumber)
        return (seriesName + " " + "(" + yearText + ")" + issueText + "-" + pageNumberString + imageFormat)