import xml.etree.ElementTree as ET
import os

class MetadataGenerator:

    series = ""
    year = ""
    publisher = ""
    issue = ""
    includeYearInMetaTitle = False

    def withSeries(self, seriesName):
        self.series = seriesName
        return self
    
    def withYear(self, yearName):
        self.year = yearName
        return self
    
    def withPublisher(self, publisherName):
        self.publisher = publisherName
        return self

    def withIssue(self, issueName):
        self.issue = issueName
        return self
    
    def withIncludeYearInMeteaTitle(self, includeYearInMetaTitle):
        self.includeYearInMetaTitle = includeYearInMetaTitle
        return self

    def createMetadataXml(self, dir):
        root = ET.Element("ComicInfo")
        series = ET.SubElement(root, "Series") 
        number = ET.SubElement(root, "Number")
        year = ET.SubElement(root, "Year")
        publisher = ET.SubElement(root, "Publisher")

        if self.includeYearInMetaTitle:
            series.text = (self.series + " (" + self.year + ")")
        else:
            series.text = self.series
        number.text = self.issue
        year.text = self.year
        publisher.text = self.publisher

        ET.ElementTree(root).write(os.path.join(dir, 'ComicInfo.xml'))

