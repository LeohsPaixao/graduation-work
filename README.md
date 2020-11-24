# TG
Repositório de Trabalho de Graduação.

Integração de Sensores de Carga e Tecnologia Iot.

Componentes utilizados:
- 2x Célula de Carga Meia Ponte Wheatstone;
- 1x Módulo Semiconductor HX711;
- 1x ESP8266 NodeMCU V3 (12-E).

Software utilizados:
- Telegraf;
https://dl.influxdata.com/telegraf/releases/telegraf-1.16.1_windows_amd64.zip

- SGBD InfluxBD;
https://dl.influxdata.com/influxdb/releases/influxdb-1.8.3_windows_amd64.zip

- Grafana;
https://grafana.com/grafana/download?platform=windows

- Broker Mosquistto.
https://mosquitto.org/download/

O objetivo deste trabalho foi desenvolver um sistema para monitorar os materiais de uma linha de produção usando 
tecnologia IoT.Atualmente o processo de monitoramento e reposição de peças depende de serviços manuais. Para isso
foram utilizados células de carga, microcontrolador, Broker MQTT, Telegraf, InfluxDB e Grafana. Foi implementado
em um workflow que tinha a função de coletar os dados do sensor, armazenar em um banco de dados e visualizar na 
forma de peso e quantidade. Com essas solução desenvolvida espera contribuir na área de logística, na reposição e
controle dos materiais.
