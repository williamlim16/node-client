import paho.mqtt.client as mqtt
import time

def on_message(client,userdata,message):
    print("received message:", str(message.payload.decode("utf-8")))

mqttBroker = "192.168.100.17"
client = mqtt.Client("node")

# client.connect(host=mqttBroker, port=1883,keepalive=60)
client.connect(mqttBroker)

client.loop_start()
client.subscribe("TESTING2")
client.on_message = on_message

time.sleep(30)
client.loop_stop()