#Source:
#https://github.com/tuya/tuya-iot-python-sdk

import time
import logging
from tuya_connector import TuyaOpenAPI, TUYA_LOGGER

ACCESS_ID = "ruyrak7f8cc3ryxg7akw"
ACCESS_KEY = "2559577a59664f51bd6bdc7de209d8b7"
API_ENDPOINT = "https://openapi.tuyaus.com"

#Device_id
DEVICE_ID ="eb591c3b52dfa828d32fvc"



# Debug log
TUYA_LOGGER.setLevel(logging.DEBUG)

# Inicia a OpenAPI e conecta
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

# Chamada (call) APIs  Tuya
# Pega as informações do dispositivo
response = openapi.get("/v1.0/iot-03/devices/{}".format(DEVICE_ID))

# Obtenha o conjunto de instruções do dispositivo
response = openapi.get("/v1.0/iot-03/devices/{}/functions".format(DEVICE_ID))

# Liga Lampada
commands = {'commands': [{'code': 'switch_led', 'value': True}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)


# Mudar a Cor(H = cor, S = Saturação, V = Intensidade)
#vermelho = 0
#amarelo = 58
#verde = 123
#agua = 174
#azul = 237
#roxo = 274
#rosa = 301
commands = {'commands': [{'code': 'colour_data_v2', 'value': '{\"h\":120,\"s\":1000,\"v\":10}'}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)






# Desliga Lampada
#time.sleep(3)
#commands = {'commands': [{'code': 'switch_led', 'value': False}]}
#openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)


# Obtenha o status de um único dispositivo
response = openapi.get("/v1.0/iot-03/devices/{}/status".format(DEVICE_ID))