import os
import pyttsx3


book_text = ''
with open(os.path.join(os.getcwd(), 'output', 'Clean_Code.pdf.txt'), 'rt', encoding='utf-8') as file:
    book_text += file.read()

print(book_text)

# initialize
engine = pyttsx3.init()

# rate setting
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 30)

# run engine
# engine.say("你好, 我是python")
# engine.say(text)
# text = 'Bruce大大早點下班回家陪嫂子!'
engine.save_to_file(book_text, './clean_code.mp3')
engine.runAndWait()
