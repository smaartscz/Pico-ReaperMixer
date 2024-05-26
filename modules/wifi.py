import network
import modules.colors as colors
from pinout import led
import configuration
from time import sleep



def connect():
    """
    Connect to wifi
    """
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(configuration.ssid, configuration.password)
    while wlan.isconnected() == False:
        print(colors.yellow + 'Waiting for connection...' + colors.reset)
        led.toggle()
        sleep(1)
    led.off()
    print(colors.green + f"Successfully connected to Wifi:{wlan.ifconfig()}" + colors.reset)