# Import the necessary modules
import shutil
import glob

# Set the source and destination folders
src = r"/Users/m1/Desktop"
screenshot = r"/Users/m1/Desktop/ScreenShots//"
png = r"/Users/m1/Desktop/images//"
documents = r"/Users/m1/Desktop/Documents//"
developer = r"/Users/m1/Desktop/Developer//"

# Set the patterns to search for screenshots, PNG images, and documents
ss = src + "/Screenshot*"
doc0 = src + "/*.pdf"
doc1 = src + "/*.PDF"
doc2 = src + "/*.docx"
doc3 = src + "/*.DOCX"
doc4 = src + "/*.doc"
doc5 = src + "/*.DOC"
doc6 = src + "/*.txt"
doc7 = src + "/*.TXT"
image0 = src + "/*.png"
image00 = src + "/*.PNG"
image1 = src + "/*.jpg"
image2 = src + "/*.JPG"
image3 = src + "/*.jpeg"
image4 = src + "/*.JPEG"
dev0 = src + "/*.py"

# Define functions to move screenshots, PNG images, and documents to their respective folders
def mv_screenshot():
    for files in glob.iglob(ss):
        shutil.move(files, screenshot)
def mv_images():
    for files in glob.iglob(image0):
        shutil.move(files, png)
    for files in glob.iglob(image00):
        shutil.move(files, png)
    for files in glob.iglob(image1):
        shutil.move(files,png)
    for files in glob.iglob(image2):
        shutil.move(files, png)
    for files in glob.iglob(image3):
        shutil.move(files, png)
    for files in glob.iglob(image4):
        shutil.move(files, png)
def mv_docs():
    for files in glob.iglob(doc0):
        shutil.move(files, documents)
    for files in glob.iglob(doc1):
        shutil.move(files, documents)
    for files in glob.iglob(doc2):
        shutil.move(files, documents)
    for files in glob.iglob(doc3):
        shutil.move(files, documents)
    for files in glob.iglob(doc4):
        shutil.move(files, documents)
    for files in glob.iglob(doc5):
        shutil.move(files, documents)
    for files in glob.iglob(doc6):
        shutil.move(files, documents)
    for files in glob.iglob(doc7):
        shutil.move(files, documents)
def mv_dev():
    for files in glob.iglob(dev0):
        shutil.move(files, developer)
        print('Moved the following items(s):', files)

# Call the functions to move the files
print(mv_screenshot())
print(mv_images())
print(mv_docs())
print(mv_dev())
