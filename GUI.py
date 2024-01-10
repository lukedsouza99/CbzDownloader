from tkinter import *
from CbzCreatorMain import CbzCreatorMain

class ComicGUI:

    def __init__(self):
        
        self.win = Tk()
        self.win.geometry("500x650")

        self.downloadLabel=Label(self.win, text='Download Link')

        self.radio = BooleanVar()
        self.radio.set(True)

        self.issueRadio = Radiobutton(self.win, text = "issue", variable = self.radio, value = True)
        self.seriesRadio = Radiobutton(self.win, text = "series", variable = self.radio, value = False)

        self.radio2 = BooleanVar()
        self.radio2.set(False)

        self.onlyIssueRadio = Radiobutton(self.win, text = "single issues only", variable = self.radio2, value = True)
        self.everythinRadio = Radiobutton(self.win, text = "everything", variable = self.radio2, value = False)

        self.radio3 = BooleanVar()
        self.radio3.set(False)

        self.noYearInMetadataTitle = Radiobutton(self.win, text = "Don't include year in meta title", variable = self.radio3, value = False)
        self.yesYearInMetadataTitle = Radiobutton(self.win, text = "Include year in meta title", variable = self.radio3, value = True)


        self.seriesLabel=Label(self.win, text='Series')
        self.yearLabel=Label(self.win, text='Year')
        self.issueLabel=Label(self.win, text='Issue')
        self.publisherLabel=Label(self.win, text='Publisher')
        
        self.downloadEntry=Entry()
        self.seriesEntry=Entry()
        self.yearEntry=Entry()
        self.issueEntry=Entry()
        self.publisherEntry=Entry()
        
        self.btn1 = Button(self.win, text='Enter', command = self.enterValues)
        self.btn2 = Button(self.win, text = "Exit", command = self.win.destroy)

        self.downloadLabel.place(x=100, y=50)
        self.downloadEntry.place(x=200, y=50)

        self.issueRadio.place(x = 150, y = 100)
        self.seriesRadio.place(x = 260, y = 100)

        self.everythinRadio.place(x = 150, y = 150)
        self.onlyIssueRadio.place(x = 260, y = 150)

        self.noYearInMetadataTitle.place(x=100, y=200)
        self.yesYearInMetadataTitle.place(x=300, y=200)

        self.seriesLabel.place(x=100, y=250)
        self.seriesEntry.place(x=200, y=250)
        self.yearLabel.place(x=100, y=300)
        self.yearEntry.place(x=200, y=300)
        self.issueLabel.place(x=100, y=350)
        self.issueEntry.place(x=200, y=350)
        self.publisherLabel.place(x=100, y=400)
        self.publisherEntry.place(x=200, y=400)
        self.btn1.place(x = 200, y= 450)
        self.btn2.place(x=203, y=490)



    def createGUI(self):
        self.win.mainloop()
    
    def enterValues(self):
        values = {"DownloadSingleIssue":self.radio.get(), "Series": self.seriesEntry.get(), "Year": self.yearEntry.get(), "Issue": self.issueEntry.get(), "Publisher": self.publisherEntry.get(), "IncludeYearInMetaTitle":self.radio3.get()}
        print(values)
        title = values["Series"] + " " + "(" + values["Year"] + ")"        
        CbzCreatorMain(title).downloadSingleIssue(self.downloadEntry.get(), values["Series"], values["Year"], values["Issue"], values["Publisher"], values["IncludeYearInMetaTitle"]) if values["DownloadSingleIssue"] == True else CbzCreatorMain(title).downloadSeries(self.downloadEntry.get(), values["Series"], values["Year"], values["Publisher"], values["IncludeYearInMetaTitle"], self.radio2.get())
        print("Completed")

if __name__ == '__main__':
    ComicGUI().createGUI()