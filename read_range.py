import os
import PyPDF2
import pyttsx3

def change_voice(engine, language, gender='female'):
    for voice in engine.getProperty('voices'):
        if language.lower() in voice.name.lower():
            engine.setProperty('voice', voice.id)

def read_pdf_from_range():
    result = [y for x in os.walk('./input/') for y in x[2]]

    for index, book_name in enumerate(result):
        print(index + 1, book_name)

    book_choice = int(input('select a book: '))
    book_name = result[book_choice - 1]

    page_range = input('page range: ')
    range_arr = page_range.split(',')
    start_page = int(range_arr[0])
    end_page = int(range_arr[1]) + 1
    print(f'start page: {start_page}')
    print(f'end page: {end_page}')

    file = open(f'./input/{book_name}', 'rb')
    pdf = PyPDF2.PdfFileReader(file)
    totalPages = pdf.numPages
    print(f'total pages: {totalPages}')

    engine = pyttsx3.init()
    engine.setProperty('rate', engine.getProperty('rate') - 30)
    change_voice(engine, 'english')

    for i in range(start_page, end_page):
        page = pdf.getPage(i)
        txt = page.extractText()
        engine.say(txt)
        engine.runAndWait()

    file.close()

    engine.say('this is the end of chapter, goodbye~')
    engine.runAndWait()
    print('this is the end of chapter, goodbye~')

if __name__ == '__main__':
    read_pdf_from_range()
