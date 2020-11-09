import paho.mqtt.client as mqtt
from random import randint
from time import sleep

broker_url = "localhost"
broker_port = 1883

client = mqtt.Client()
client.connect(broker_url, broker_port)

try:
    while True:
        peso = randint(0,49) + (randint(0,99)/100)
        quantidade = round(peso / 0.10)
        send = f"{peso}|{quantidade}"

        print(peso)
        print(quantidade)

        client.publish(topic="medicao", payload=send, qos=0, retain=False)

        sleep(1) 

except KeyboardInterrupt:
    print("\nCtrl+C pressionado, encerrando aplicacao e saindo...")

