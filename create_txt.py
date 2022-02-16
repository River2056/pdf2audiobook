import os
import PyPDF2
import pyttsx3

def create_txt():
    # create necessary folders
    output_dir = os.path.exists(os.path.join(os.getcwd(), 'output'))
    if not output_dir:
        os.mkdir('./output/')

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

    book_text = ''
    for i in range(start_page, end_page):
        page = pdf.getPage(i)
        txt = page.extractText()
        book_text += txt + '\n'

    file.close()
    output_file = open(f'./output/{book_name}.txt', 'a', encoding='utf-8')
    output_file.write(book_text)
    output_file.close()

if __name__ == '__main__':
    create_txt()
