import uasyncio
from modules.ReaperAPI import ReaperAPI
import startup
import modules.colors as colors
import time
import modules.wifi as wifi
import modules.colors as colors
from machine import Pin, SPI
import modules.ssd1306 as ssd1306


reaper = ReaperAPI("http://192.168.1.219:8080")

print(colors.red + "Connecting to Wifi.." + colors.reset)
wifi.connect()


async def api_worker():    
    try:
        # Initialize communication
        print(colors.red + "Starting communication with REAPER API..." + colors.reset)
        tracks_info = await startup.get_tracks_name()
 
    finally:
        await reaper.close()

if __name__ == "__main__":
    print(colors.red + "Main application is running..." + colors.reset)
    uasyncio.run(api_worker())
    print(colors.red + "API worker has completed."+ colors.reset)
