import paho.mqtt.client as mqtt
from connectsave import *

broker_url = "localhost"
broker_port = 1883

def on_message(client, userdata, msg):

    print(str(msg.payload))
    
while True:

    client = mqtt.Client()
    client.connect(broker_url, broker_port)
    client.subscribe("medicao/peso")
    client.subscribe("medicao/quantidade")
    client.on_message = on_message

    client.loop_forever()
