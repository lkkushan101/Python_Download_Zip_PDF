from zipfile import ZipFile
import requests
import PyPDF2

url = 'http://web.utk.edu/~archinfo/EcoDesign/escurriculum/PDF/Part_A.zip'
fileName = 'sample.zip'
req = requests.get(url)
file = open(fileName, 'wb')
for chunk in req.iter_content(100000):
    file.write(chunk)
file.close()
archive = ZipFile(fileName, 'r')
imgfile = archive.extract('Part_A.pdf')
pdfFileObject = open('Part_A.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
count = pdfReader.numPages
for i in range(count):
    page = pdfReader.getPage(i)
    print(page.extractText())
    if page.extractText().find('ENERGY SCHEMING'):
        print('Text found...')

