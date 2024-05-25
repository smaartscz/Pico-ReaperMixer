import network
import modules.colors as colors
from machine import Pin
from modules.do_not_share import ssid, password
from time import sleep

pin = Pin("LED", Pin.OUT)

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print(colors.yellow + 'Waiting for connection...' + colors.reset)
        pin.toggle()
        sleep(1)
    pin.off()
    print(colors.green + f"Successfully connected to Wifi:{wlan.ifconfig()}" + colors.reset)