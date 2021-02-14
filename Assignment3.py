'''
#1,2
try:
    a = 1/0
except ZeroDivisionError:
    print("Divided By Zero is illegal")
#3
# this is wrong:
try :
    x = 1
# this is wrong:
    finally:
        print("finally")

#but this is acceptable
finally :
    print("finally")

#4
#all of them

#5
# if unwanted exception will occur it will caught it as well, while I want to handle a specific exception

#6
# IOError will caught every file error, ZeroDivisionError will caught the Zero division error as below
import io
try:
    a = 1 / 0
    my_file = open("no_file.txt")
except IOError:
    print("IO")
except ZeroDivisionError:
    print("Zero div error")


#7,8,9,10
import io
my_file = open("words.txt", "w+",encoding="utf-8")
my_file.write("יקי קמחי")
my_file.close()
my_file = open("words.txt", "r", encoding="utf-8")
print(my_file.read())

#11

from flask import Flask
import io

my_app = Flask(__name__)

@my_app.route("/content")
@my_app.route("/content/<file_name>")
def content(file_name = "REDME.txt"):
    file_name = io.open(file_name , 'r', encoding="utf-8")
    return file_name.read(), 200

@my_app.route("/register")
@my_app.route("/register/<file_name>")
def register(file_name = "reg_text.txt"):
    file_name = io.open(file_name , 'w+', encoding="utf-8")
    file_name.write("hello")
    return "<H1 id='welcome'>Success!!</H1>", 201

my_app.run(host='127.0.0.1', debug=True, port=5000)
'''
#Challange
from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (100, 30), color=(73, 109, 137))

fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
d = ImageDraw.Draw(img)
d.text((10, 10), "Hello world", font=fnt, fill=(255, 255, 0))

img.save('pil_text_font.png')