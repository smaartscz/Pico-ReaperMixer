import uasyncio
from modules.ReaperAPI import ReaperAPI
import modules.colors as colors
import time
import modules.wifi as wifi
import modules.colors as colors

print(colors.red + "Connecting to Wifi.." + colors.reset)
wifi.connect()

async def api_worker():
    reaper = ReaperAPI("http://192.168.1.219:8080")
    
    try:
        # Initialize communication
        print(colors.red + "Starting communication with REAPER API..." + colors.reset)
        
        # Test transport state
        transport_info = await reaper.get_transport()
        print(colors.green + f"Transport info: {transport_info}")
        
        track_info = await reaper.get_track_info(5)
        print(colors.green + f"Track Info: {track_info}")
        
        await reaper.mute(5, -1)
        await reaper.mute(5, -1)
        num = 0.0
        while num <= 1.0:
            print(colors.yellow + f"Current volume is: {num}" + colors.reset)
            await reaper.set_volume(5,num)
            num += 0.01
            time.sleep(0.1)
    finally:
        await reaper.close()

if __name__ == "__main__":
    print(colors.red + "Main application is running..." + colors.reset)
    uasyncio.run(api_worker())
    print(colors.red + "API worker has completed."+ colors.reset)
