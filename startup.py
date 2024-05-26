from modules.ReaperAPI import ReaperAPI
import modules.wifi as wifi
import modules.colors as colors
import modules.tracks as tracks

reaper = ReaperAPI("http://192.168.1.219:8080")





async def start():
    print(colors.red + "Starting boot sequence!" + colors.reset)
    print(colors.red + "Connecting to Wifi.." + colors.reset)
    wifi.connect()
    await tracks.assaign_inputs_to_trackno()
