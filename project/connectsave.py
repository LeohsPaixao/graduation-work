from influxdb import InfluxDBClient

def save_measurement(weight, amount, host='localhost', port=8086, database='medicao'):
    """
    Salva uma medição no banco de dados InfluxDB.
    """
    client = InfluxDBClient(host=host, port=port)
    client.switch_database(database)
    
    data_point = [
        {
            "measurement": "carga",
            "tags": {"region": "br"},
            "fields": {"weight": weight, "amount": amount},
        }
    ]
    
    print(f"Enviando dados para o InfluxDB: {data_point}")
    client.write_points(data_point)
