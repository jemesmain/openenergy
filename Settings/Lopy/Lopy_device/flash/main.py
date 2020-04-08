""" OTAA Node example compatible with the LoPy Nano Gateway """

from network import LoRa
import socket
import binascii
import struct
import time
import config

# initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)


# create an OTA authentication params
#setting found in ttn device / name of device with activation method OTAA
#ttn dev_eui 70B3D54995E574C6
#const char *appEui = "70B3D59BA0000114";
#const char *appKey = "65240933ADE876AB9AD5990DB003B6E9";

#ttn configuration
#print('ttn config')
#dev_eui = binascii.unhexlify('70B3D54985E573F7'.replace(' ','')) # these settings can be found from TTN
#app_eui = binascii.unhexlify('70B3D59CC0000004'.replace(' ','')) # these settings can be found from TTN
#app_key = binascii.unhexlify('65240932ADE876AB9AD5990DB004C2E9'.replace(' ','')) # these settings can be found from TTN

#chirpstack configuration
print('chirpstack config')
dev_eui = binascii.unhexlify('db2b4bbc2cf73c6'.replace(' ','')) # these settings can be found from Chirpstack
app_eui = binascii.unhexlify('db2b4bbc2cf743c6'.replace(' ','')) # these settings can be found from Chirpstack
app_key = binascii.unhexlify('f5d90236196aef9d6d39c690b5b8a317'.replace(' ','')) # these settings can be found from Chirpstack

# set the 3 default channels to the same frequency (must be before sending the OTAA join request)
lora.add_channel(0, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=5)
lora.add_channel(1, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=5)
lora.add_channel(2, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=5)

# join a network using OTAA
lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0, dr=config.LORA_NODE_DR)

# wait until the module has joined the network
i=1
while not lora.has_joined():
    time.sleep(2.5)
    print('Not joined yet...')
    print(i)
    i+=1

print('device connected')
# remove all the non-default channels
for i in range(3, 16):
    lora.remove_channel(i)

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, config.LORA_NODE_DR)

# make the socket blocking
s.setblocking(False)

time.sleep(5.0)

for i in range (60):
    #envoi des information toutes les 2 minutes donc pendant 2h
    value = 22.5
    # Nombre mis dans un tableau de flottants et on l'affiche avec formattage
    myArrayOfFloat = bytes(struct.pack("f", value))
    print('myArrayOfFloat')
    print(myArrayOfFloat)
    print([ "0x%02x" % item for item in myArrayOfFloat ])
    #s.send(b'0001' + myArrayOfFloat)
    s.send(myArrayOfFloat)
    # send some data ("hello")
    #s.send(bytes([0x48, 0x65, 0x6C, 0x6C, 0x6F]))
    #print('hello is sent')
    # send some data ("h")
    #s.send(bytes([0x48]))
    #print('h is sent')
    # send some data ("20.5")
    #s.send(bytes([0x32, 0x30, 0x2e, 0x35]))
    #print('20.5 is sent')

    #s.send(b'PKT #' + myArrayOfFloat)
    #s.send(b'PKT #' + bytes([i]))
    time.sleep(118)
    rx, port = s.recvfrom(256)
    if rx:
        print('Received: {}, on port: {}'.format(rx, port))
    time.sleep(2)
