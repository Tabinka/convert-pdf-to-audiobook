from text_to_speech import speak
import PyPDF2

all_content = ""
pdf_file = open('sample.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
filename = pdf_file.name[:-4]
for x in range(number_of_pages):
    page = read_pdf.getPage(x)
    page_content = page.extractText()
    all_content = all_content + page_content
speak(all_content, "en", save=True, file=f"{filename}.mp3")
