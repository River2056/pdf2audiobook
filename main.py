import os
import PyPDF2
import pyttsx3

# create necessary folders
output_dir = os._exists('./output/')
if not output_dir:
    os.mkdir('./output/')

result = [y for x in os.walk('./input/') for y in x[2]]

for index, book_name in enumerate(result):
    print(index + 1, book_name)

book_choice = int(input('select a book: '))
book_name = result[book_choice - 1]

file = open(f'./input/{book_name}', 'rb')
pdf = PyPDF2.PdfFileReader(file)
totalPages = pdf.numPages
print(f'total pages: {totalPages}')

book_text = ''
for i in range(totalPages):
    page = pdf.getPage(i)
    txt = page.extractText()
    book_text += txt + '\n'

file.close()
output_file = open(f'./output/{book_name}.txt', 'a', encoding='utf-8')
output_file.write(book_text)
output_file.close()

