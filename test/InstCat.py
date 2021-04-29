from myigbot import MyIGBot
import os
import shutil
from PIL import Image
import urllib3

insta_username = '_lazy_programmer_'
insta_password = '78RUIUne'

def clean_up():
    dir = "config"
    remove_me = "new_pic.png.REMOVE_ME"
    # checking whether config folder exists or not
    if os.path.exists(dir):
        try:
            # removing it because in 2021 it makes problems with new uploads
            shutil.rmtree(dir)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
    if os.path.exists(remove_me):
        src = os.path.realpath("new_pic.png")
        os.rename(remove_me, src)


clean_up()

url = 'https://thiscatdoesnotexist.com/'
http = urllib3.PoolManager()
file = http.request('GET', url).data
with open('new_pic.png','wb')as img:
    img.write(file)

bot = MyIGBot(insta_username, insta_password)
response = bot.upload_post("new_pic.png", caption="Just another cat")
print(response)
