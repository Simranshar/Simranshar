import PyPDF2
a= PyPDF2.PdfFileReader('E:/sample/pri.pdf')
#print(a.getDocumentInfo())
str=" "
for i in range(0,3):
    str+=a.getPage(i).extractText()
with open("pri.txt","w",encoding='utf-8') as f:
    f.write(str)
'''pdfFileObj = open('E:/sample/animal.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(2)

# extracting text from page
print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()'''
