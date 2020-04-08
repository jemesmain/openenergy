
""" LoPy LoRaWAN Nano Gateway configuration options """

import machine
import ubinascii

WIFI_MAC = ubinascii.hexlify(machine.unique_id()).upper()
# Set  the Gateway ID to be the first 3 bytes of MAC address + 'FFFE' + last 3 bytes of MAC address for ttn
#GATEWAY_ID = WIFI_MAC[:6] + "FFFE" + WIFI_MAC[6:12]

# Set  the Gateway ID to be the first 3 bytes of MAC address + 'FFEE' + last 3 bytes of MAC address for chirpstack
GATEWAY_ID = WIFI_MAC[:6] + "FFEE" + WIFI_MAC[6:12]

#The thing network
#SERVER = 'router.eu.thethings.network'
#PORT = 1700

#chirpstack gateway en local
#SERVER = '192.168.1.101'
#PORT = 1700


#chirpstack gateway via www 
SERVER = 'machine.my_server.com'
PORT = 1700


#server de temps
NTP = "pool.ntp.org"
NTP_PERIOD_S = 3600

#wifi home_settings/bavg _settings/androidAP_settings(partage de connexion internet) settings
#pour tester trois réseau il faut mettre i=3 dans main.py (juste avant for net in nets)
#seront testé par main.py avec la ligne for net in nets... (nets etant le nom des réseau découvert)
SSID = ('wifi ssid 1','wifi ssid 2')
PWD = ('A43','64A')


# for EU868
LORA_FREQUENCY = 868100000
LORA_GW_DR = "SF7BW125" # DR_5
LORA_NODE_DR = 5

# for US915
# LORA_FREQUENCY = 903900000
# LORA_GW_DR = "SF7BW125" # DR_3
# LORA_NODE_DR = 3
