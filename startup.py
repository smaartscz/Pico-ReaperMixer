from modules.ReaperAPI import ReaperAPI
import asyncio
import modules.colors as colors
import re
reaper = ReaperAPI("http://192.168.1.219:8080")

tracks_info = {}
keys = [
    "tracknumber",
    "trackname",
    "trackflags",
    "volume",
    "pan",
    "last_meter_peak",
    "last_meter_pos",
    "width/pan2",
    "panmode",
    "sendcnt",
    "recvcnt",
    "hwoutcnt",
    "color"
]

async def get_tracks_name():
    tracks = await reaper.get_tracks()
    tracks_max = int(tracks.split()[1])

    for track in range(0, tracks_max):
        print(colors.yellow + f"Processing track {track}" + colors.reset)
        values = await reaper.get_track_info(track)
        # Regular expression to match the track name properly
        match = re.match(r'TRACK\s+(\d+)\s+(.+?)\s+(\d+)\s+([0-9.]+)\s+([0-9.]+)\s+([-0-9]+)\s+([-0-9]+)\s+([0-9.]+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)', values)
        if match:
            values = match.groups()
            if len(values) == len(keys):
               tracks_info[track] = dict(zip(keys, values))
            else:
                print(colors.red + f"Warning: Mismatch in number of values and keys for track {track}" + colors.reset)
                tracks_info[track] = {}

        print(colors.green + f"Track {track} processed" + colors.reset)
    print(colors.green + f"All {tracks_max} tracks processed" + colors.reset)
    return tracks_info