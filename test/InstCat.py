from instabot import Bot
import os
import shutil
from PIL import Image
import urllib3

insta_username = ''
insta_password = ''

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


def upload_post():
    bot = Bot()
    bot.login(username=insta_username, password=insta_password)
    bot.upload_photo("new_pic.png", caption="Just another cat")
    bot.get_you_medias()


clean_up()

url = 'https://thiscatdoesnotexist.com/'
http = urllib3.PoolManager()
file = http.request('GET', url).data
with open('new_pic.png','wb')as img:
    img.write(file)

bot = Bot()
bot.login(username=insta_username, password=insta_password)
bot.upload_photo("new_pic.png", caption="Just another cat")
bot.logout()
