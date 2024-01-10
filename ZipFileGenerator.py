import os
import zipfile

class ZipFileGenerator:
       
    def createCbzFile(self, dir, permDir):
        # Zip up files ino cbz files 
        newFileName = os.path.join(permDir, os.path.basename(dir) + ".cbz")
        cbz = zipfile.ZipFile(newFileName, "w", compression=zipfile.ZIP_STORED)
        for file in os.listdir(dir):
            cbz.write(os.path.join(dir, file), file)   
        cbz.close()

