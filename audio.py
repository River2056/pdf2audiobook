import pyttsx3

# initialize
engine = pyttsx3.init()

# rate setting
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 30)

# run engine
# engine.say("你好, 我是python")
# engine.say(text)
text = 'Bruce大大早點下班回家陪嫂子!'
engine.save_to_file(text, './test.mp3')
engine.runAndWait()
