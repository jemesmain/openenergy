""" LoPy LoRaWAN Nano Gateway example usage """

import config
#pycom to use rgbled to tell if network is ok
import pycom
import time

from nanogateway import NanoGateway
import machine
from network import WLAN
#WLAN().mac()
#Result is in 6-byte format, not the usual MAC address with 6 hexadecimal bytes separated by ':'. To convert, use
#import ubinascii
#mac_adress = ubinascii.hexlify(WLAN().mac(),':').decode()
#print('mac adress lopy-gateway')
#print(mac_adress)

#choix du wifi
WIFI_SSID='no known wifi reachable'
#scan des wifi disponnible
wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan()
#wifi home/bavg _settings settings
#SSID = ('my settings one ','my settings two')
#PWD = ('A43','64A')
i=0
#i jusqu'a 3 car on veut essayer de connecté un des trois réseau connu de config.py
for i in range (3):
    for net in nets:
        #print (nets)
        print (net.ssid)
        print (config.SSID[i])
        if net.ssid ==config.SSID[i] :
            WIFI_SSID=config.SSID[i]
            WIFI_PASS=config.PWD[i]
            #wlan.connect(net.ssid, auth=(net.sec,PWD[i] ), timeout=5000)
            #while not wlan.isconnected():
                #machine.idle()
                #('lopy-green is connected to')
                #print(SSID[i])
            #break
    i+=1
print('gateway trying to connect to wifi')
print(WIFI_SSID)

if __name__ == '__main__':
    nanogw = NanoGateway(
        id=config.GATEWAY_ID,
        frequency=config.LORA_FREQUENCY,
        datarate=config.LORA_GW_DR,
        ssid=WIFI_SSID,
        password=WIFI_PASS,
        server=config.SERVER,
        port=config.PORT,
        ntp_server=config.NTP,
        ntp_period=config.NTP_PERIOD_S
        )

    nanogw.start()
    pycom.heartbeat(False)
    pycom.rgbled(0x007f00) #green color
    time.sleep(5)
    pycom.heartbeat(True)
    nanogw._log('You may now press ENTER to enter the REPL')
    input()
