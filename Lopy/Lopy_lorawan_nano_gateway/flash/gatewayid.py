from network import WLAN
import binascii
wl = WLAN()
#chirpstack config FFEE
binascii.hexlify(wl.mac())[:6] + 'FFEE' + binascii.hexlify(wl.mac())[6:]
#TTN config FFFE
#binascii.hexlify(wl.mac())[:6] + 'FFFE' + binascii.hexlify(wl.mac())[6:]
