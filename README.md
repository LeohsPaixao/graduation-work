# TG
Repositório de Trabalho de Graduação.

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

O Trabalho foi feito totalmente feito no Sistema Operacional Windows, com isso possuindo
algumas limitações. Inicialmente as células de carga é responsavel por realizar a medida
da sua grandeza, o valor da sua ressitencia é convertido por um conversor A/D, o Módulo
HX711, e o sinal resulante deste conversor é enviado para o NodeMCU. O Microcontrolador
NodeMCU recebe toda a Programação necessária para realizar a interface entre os dados
coletados e o computador ou notebook. No InfluxBD, possui um database para armazenar
os dados coletados e a Ferramenta Grafana é utilizado para a exibição dos Dados.
  
