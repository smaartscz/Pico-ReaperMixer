import modules.wifi as wifi
import modules.colors as colors
import modules.tracks as tracks

async def start():
    print(colors.red + "Starting boot sequence!" + colors.reset)
    print(colors.red + "Connecting to Wifi.." + colors.reset)
    wifi.connect()
    await tracks.assaign_inputs_to_trackno()
