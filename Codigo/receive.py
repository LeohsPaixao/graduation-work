import paho.mqtt.client as mqtt
from connectsave import *

broker_url = "localhost"
broker_port = 1883

# def clean(dirty_message):
#     dirty_message = str(dirty_message)
#     clean_message = ""

#     for letter in dirty_message:
#         if letter not in("b'"):
#             clean_message+= letter 

#     print(f"Mensagem Completa = {clean_message}")
#     return clean_message

# def separator(clean_message):
#     list_clean_message = clean_message.split("|")
#     weight = float(list_clean_message[0])
#     amount = int(list_clean_message[1])
#     return weight, amount

def on_message(client, userdata, msg):

    print(str(msg.payload))
    # clean_message = clean(str(msg.payload))
    # weight, amount = separator(clean_message)
    # print(f"Peso = {weight}")
    # print(f"Quantidade = {amount}")
    # save(weight, amount)
    
while True:

    client = mqtt.Client()
    client.connect(broker_url, broker_port)
    client.subscribe("medicao")
    client.on_message = on_message

    client.loop_forever()
