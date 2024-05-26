import uasyncio
from modules.ReaperAPI import ReaperAPI
import startup
import modules.colors as colors
import modules.check_input as check_input
import modules.colors as colors
import modules.ssd1306 as ssd1306

reaper_ip = "http://192.168.1.219:8080"

reaper = ReaperAPI(reaper_ip)

async def main():
    """
    Main loop\n
    Loop is responsible for calling functions to check slider or mute buttons updates.
    """
    
    await startup.start()
    try:
        print(colors.red + "Main application is running. Checking for slider or mute button update." + colors.reset)
        while True:
            slider_task = uasyncio.create_task(check_input.sliders())
            mute_task = uasyncio.create_task(check_input.mute())
            await uasyncio.gather(slider_task, mute_task)
    except KeyboardInterrupt:
        print(colors.red + "Program interrupted by user. Cleaning up..." + colors.reset)
        await reaper.close()
        print(colors.green + "Cleanup complete. Exiting program." + colors.reset)
        return

if __name__ == "__main__":
    try:
        uasyncio.run(main())
    except KeyboardInterrupt:
        print(colors.red + "Program interrupted by user. Exiting..." + colors.reset)