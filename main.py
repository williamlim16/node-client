import requests
import cv2
import paho.mqtt.client as mqtt
import time
import datetime


def on_message(client, userdata, message):
    print("received message:", str(message.payload.decode("utf-8")))


"""
MQTT init
"""
mqttBroker = "192.168.100.17"
client = mqtt.Client("TS001")
client.connect(mqttBroker)

"""
Accessing camera
"""
cam = cv2.VideoCapture(-1)
ret, image = cam.read()
if ret:
    cv2.imshow('snap', image)
    cv2.waitKey(0)
    cv2.destroyWindow('snap')
    cv2.imwrite('/home/pi/skripsi/node-client/image.jpg', image)
cam.release()

"""
Subscribe to corresponding topic
"""
client.loop_start()
client.subscribe("TS001")
client.on_message = on_message

"""
Opening and sending image via HTTP
"""
image = open("image.jpg", "rb")
server = "http://192.168.100.17:8000/api/upload"
data = {'trashcan': 'TS001',
        'image': round(time.time()*1000)}
response = requests.post(server, files={"file": image}, data=data)
time.sleep(30)
client.loop_stop()
print(response)
