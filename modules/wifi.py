import network
import modules.colors as colors
from pinout import led
from modules.do_not_share import ssid, password
from time import sleep



def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print(colors.yellow + 'Waiting for connection...' + colors.reset)
        led.toggle()
        sleep(1)
    led.off()
    print(colors.green + f"Successfully connected to Wifi:{wlan.ifconfig()}" + colors.reset)