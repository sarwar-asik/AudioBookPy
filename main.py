import pyttsx3
import PyPDF2
book = open('oop.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
page = pdfReader.numPages
print(page)
friend = pyttsx3.init()
page=pdfReader.getPage(7)
text = page.extractText()
friend.say(text)
# friend.say("I am ready to speak  Now. Thank  Boltu")
friend.runAndWait()


