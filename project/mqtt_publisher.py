import paho.mqtt.client as mqtt
from random import uniform
from time import sleep

BROKER_URL = "localhost"
BROKER_PORT = 1883
TOPIC = "medicao"

def generate_payload():
    """
    Gera um payload aleatório com peso e quantidade.
    """
    weight = round(uniform(0, 50), 2)  # Peso com 2 casas decimais
    amount = round(weight / 0.10)
    return f"{weight}|{amount}"

def main():
    client = mqtt.Client()
    client.connect(BROKER_URL, BROKER_PORT)
    
    try:
        while True:
            payload = generate_payload()
            print(f"Enviando: {payload}")
            client.publish(topic=TOPIC, payload=payload, qos=0, retain=False)
            sleep(1)
    except KeyboardInterrupt:
        print("\nEncerrando o publicador MQTT.")

if __name__ == "__main__":
    main()
