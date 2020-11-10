import paho.mqtt.client as mqtt
from random import randint
from time import sleep

broker_url = "localhost"
broker_port = 1883

client = mqtt.Client()
client.connect(broker_url, broker_port)

try:
    peso = 50.00
    while True:
        limite = randint(0, 25)
        print("limite: ", limite)
        if peso <= limite:
            reposicao = randint(0, 50)
            while peso + reposicao > 50.00:
                reposicao = randint(0, 50.00)
                
            peso += reposicao

        quantidade = float(round(peso / 0.10))

        for i in range(5):

            client.publish(topic="medicao/peso", payload=peso, qos=0, retain=False)
            client.publish(topic="medicao/quantidade", payload=quantidade, qos=0, retain=False)
            

            print("Peso: " , peso)
            print("Quantidade: " , quantidade)

            sleep(3)
        peso -= float(randint(1.00, 5.00))

except KeyboardInterrupt:
    print("\nCtrl+C pressionado, encerrando aplicacao e saindo...")

