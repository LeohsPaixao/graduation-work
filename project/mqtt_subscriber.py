import paho.mqtt.client as mqtt
from connectsave import save_measurement

BROKER_URL = "localhost"
BROKER_PORT = 1883
TOPIC = "medicao"

def process_message(message):
    """
    Processa a mensagem recebida, extrai peso e quantidade, e salva no InfluxDB.
    """
    try:
        weight, amount = map(float, message.decode().split("|"))
        print(f"Peso: {weight}, Quantidade: {amount}")
        save_measurement(weight, amount)
    except (ValueError, AttributeError) as e:
        print(f"Erro ao processar mensagem: {message}, Detalhes: {e}")

def on_message(client, userdata, msg):
    print(f"Mensagem recebida no tópico {msg.topic}: {msg.payload}")
    process_message(msg.payload)

def main():
    client = mqtt.Client()
    client.connect(BROKER_URL, BROKER_PORT)
    client.subscribe(TOPIC)
    client.on_message = on_message
    
    print(f"Conectado ao broker MQTT em {BROKER_URL}:{BROKER_PORT}, ouvindo o tópico '{TOPIC}'...")
    client.loop_forever()

if __name__ == "__main__":
    main()
