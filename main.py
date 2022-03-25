import requests
import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, image = cam.read()
    cv2.imshow('image',image)
    k = cv2.waitkey(1)
    if k != 1:
        break

jisoo = open("jisoo.jpeg","rb")

server = "http://192.168.100.17:8000/api/upload"
response = requests.post(server, files={"file":jisoo})
print(response)
