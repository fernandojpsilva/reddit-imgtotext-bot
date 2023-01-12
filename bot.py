import praw
import cv2
import pytesseract
from urllib.request import urlopen
import numpy as np

client_id = ""
client_secret = ""
username = ""
password = ""
user_agent = "<console:ImgToText:1.0>"
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

subreddit = reddit.subreddit("soccer")


def url_to_image(url):
    req = urlopen(url)
    image = np.asarray(bytearray(req.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    print("*******************************")
    print(url)
    return image


def process_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    noise = cv2.medianBlur(gray, 3)
    thresh = cv2.threshold(noise, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    return thresh


for post in subreddit.hot(limit=10):
    if ('.jpg' or '.png') in post.url:
        img_decoded = url_to_image(post.url)
        img_processed = process_image(img_decoded)
        print(post.title)
        #cv2.imshow('image', img_decoded)
        config = ('-l eng — oem 3 — psm 3')
        text = pytesseract.image_to_string(img_processed, config=config)
        print(text)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
