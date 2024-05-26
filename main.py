import uasyncio
from modules.ReaperAPI import ReaperAPI
import startup
import modules.colors as colors
import modules.check_input as check_input
import modules.colors as colors
import modules.ssd1306 as ssd1306


reaper = ReaperAPI("http://192.168.1.219:8080")


async def api_worker():    
    try:
        return
 
    finally:
        #print(colors.red + "API worker has completed."+ colors.reset)´
        
        await reaper.close()

async def main():
    await startup.start()
    while True:
        slider_task = uasyncio.create_task(check_input.sliders())
        mute_task = uasyncio.create_task(check_input.mute())
        api_worker_task = uasyncio.create_task(api_worker())

        #print(colors.red + "Main application is running..." + colors.reset)
        await uasyncio.gather(api_worker_task, slider_task, mute_task)
        #await uasyncio.gather(api_worker_task, mute_task)

if __name__ == "__main__":
    uasyncio.run(main())
