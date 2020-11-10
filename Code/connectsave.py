from influxdb import InfluxDBClient

# Conexão com o Banco de Dados InfluxDB
# def save(weight, amount):
#     db = InfluxDBClient(host='localhost', port=8086) 
#     db.switch_database('medicao')  

#     json_body = [
#         {
#             "measurement": "leo",
#             "tags": {
#                 "region": "br"
#             },
#             "fields":{
#                 "weight": weight,
#                 "amount": amount
#             }
#         }
#     ]
#     print(f'json = { json_body}')
#     db.write_points(json_body)
