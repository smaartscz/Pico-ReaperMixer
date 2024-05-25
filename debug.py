from modules.ReaperAPI import ReaperAPI
import modules.colors as colors
reaper = ReaperAPI("http://localhost:8080")

# Initialize communication
print("Starting communication with REAPER API...")
    
# Test transport state
transport_info = reaper.get_transport()
print(colors.green +f"Transport info: {transport_info}")
track_info = reaper.get_track_info(5)
print(colors.green + f"Track Info: {track_info}")
reaper.mute(5, -1)
reaper.mute(5, -1)