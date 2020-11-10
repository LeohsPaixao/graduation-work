import paho.mqtt.client as mqtt
from random import randint
from time import sleep

broker_url = "localhost"
broker_port = 1883

client = mqtt.Client()
client.connect(broker_url, broker_port)

try:
    peso = 100.00
    while True:
        limite = randint(0, 30)
        print("limite: ", limite)
        if peso <= limite:
            reposicao = randint(0, 100)
            while peso + reposicao > 100.00:
                reposicao = randint(0, 100.00)
                
            peso += reposicao

        quantidade = float(round(peso /(1/50)))

        for i in range(5):

            client.publish(topic="medicao/peso", payload=peso, qos=0, retain=False)
            client.publish(topic="medicao/quantidade", payload=quantidade, qos=0, retain=False)
            

            print("Peso: " , peso)
            print("Quantidade: " , quantidade)

            sleep(3)
        peso -= randint(2.00, 15.00)

except KeyboardInterrupt:
    print("\nCtrl+C pressionado, encerrando aplicacao e saindo...")
