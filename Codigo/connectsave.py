from influxdb import InfluxDBClient

# Conexão com o Banco de Dados InfluxDB
def save(weight, amount):
    db = InfluxDBClient(host='localhost', port=8086) 
    db.switch_database('example')  

    json_body = [
        {
            "measurement": "carga",
            "tags": {
                "region": "br"
            },
            "fields":{
                "weight": weight,
                "amount": amount
            }
        }
    ]
    print(f'json = { json_body}')
    db.write_points(json_body)
