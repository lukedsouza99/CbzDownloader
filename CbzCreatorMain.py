import os
import shutil
from config import directory, baseUrl, tailUrl
from MetadataGenerator import MetadataGenerator
from ZipFileGenerator import ZipFileGenerator
from ComicIssueDownloader import ComicIssueDownloader
import logging

class CbzCreatorMain:

    def __init__(self, title):
        logging.basicConfig(level=logging.INFO)
        self.PATH = directory
        self.baseUrl = baseUrl
        self.tailUrl = tailUrl
        self.newPermDir = os.path.join(self.PATH, title)
        os.mkdir(self.newPermDir)


    def downloadSingleIssue(self, link, series, year, issue, publisher, includeYearInMetaTitle):

        # Create temp directory to save pictures to
        newDir = os.path.join(self.PATH, f"{series} {issue} ({year})")
        os.mkdir(newDir)

        # Downloads individual pngs of pages of a comic issue
        logging.info(f"Downloading: {series} ({year}) #{issue}")
        ComicIssueDownloader().downloadSingleIssue(newDir, link, series, issue, year)
        logging.info("Download complete")

        # Create metadata for the cbz
        logging.info(f"Creating metadata for: {series} ({year} #{issue})")
        MetadataGenerator().withSeries(series).withIssue(issue).withYear(year).withPublisher(publisher).withIncludeYearInMeteaTitle(includeYearInMetaTitle).createMetadataXml(newDir)
        logging.info("Metadata generation complete")

        # Zip up files into cbz files
        logging.info(f"Zipping up: {series} ({year} #{issue})")
        ZipFileGenerator().createCbzFile(newDir, self.newPermDir)
        logging.info(f".CBR created successfully")

        # Delete temp directory
        shutil.rmtree(newDir)
    

    def downloadSeries(self, link, series, year, publisher, includeYearInMetaTitle, onlyIssues):

        # Give it link to page with all issues and extract links
        linksToSingleIssues = ComicIssueDownloader().extractSingleIssueLinksFromMainSeries(link, self.baseUrl, self.tailUrl, onlyIssues)

        # loop through links and save each issue cbr into a single folder full of issue cbrs
        for issueNumber, singleIssueLink in enumerate(linksToSingleIssues):
            singleIssueNumber = str(issueNumber + 1)
            self.downloadSingleIssue(singleIssueLink, series, year, singleIssueNumber, publisher, includeYearInMetaTitle)



if __name__ == '__main__':
    
    link = input("Link:")
    series = input("Series Name:")
    year = input("Year:")
    issue = input("Issue:")
    publisher = input("Publisher:")
    downloadSingleIssue = bool(int(input("downloadSingleIssue:")))
    onlyIssues = bool(int(input("OnlyIssues:")))
    includeYearInMetaTitle = bool(int(input("include year in metadata title:")))
    CbzCreatorMain().downloadSingleIssue(link, series, year, issue, publisher, includeYearInMetaTitle) if downloadSingleIssue == True else CbzCreatorMain().downloadSeries(link, series, year, publisher, includeYearInMetaTitle, onlyIssues)



