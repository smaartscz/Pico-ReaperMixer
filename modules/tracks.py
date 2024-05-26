from modules.ReaperAPI import ReaperAPI
import re
import modules.colors as colors
import track_mapping

tracks_info = {}
reaper_tracks = ""
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
mapped_tracks = None

reaper = ReaperAPI("http://192.168.1.219:8080")

async def get_tracks_name():
    """
    Try to get Reaper tracks and store them inside dictionary called tracks_info.
    """
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



async def assaign_inputs_to_trackno():
    """
    Request track_list from get_tracks_name() and map them correctly based on track_mapping.mapping.\n
    Returns: Nothing
    """
    global mapped_tracks
    print(colors.red + "Starting API worker"+ colors.reset)
    # Initialize communication
    print(colors.red + "Starting communication with REAPER API..." + colors.reset)
    reaper_tracks = await get_tracks_name()
    mapping_list = track_mapping.mapping
    try:
        for track_id, track_info in reaper_tracks.items():
            
            track_name = track_info['trackname']
            print(colors.yellow + f"Processing mapping for track {track_name}" + colors.reset)
            for item in mapping_list:
                if item['reaper'].lower() == track_name.lower():
                    item['tracknumber'] = int(track_info['tracknumber'])
                    item['slider_value'] = track_info.get('slider_value', 0.0)
                    item['mute_value'] = track_info.get('mute_value', False)
                    break
            print(colors.green + f"Mapping for track {track_name} processed" + colors.reset)
        print(colors.green + f"All tracks successfully mapped!" + colors.reset)
        mapped_tracks = mapping_list
    except Exception as e:
        print(colors.red + f"Error: {e}" + colors.reset)

async def get_mapped_tracks():
    """
    Get mapped tracks. \n
    Returns:
    list: mapped_tracks(list)
    """
    global mapped_tracks
    if mapped_tracks == None:
        await assaign_inputs_to_trackno()
        return mapped_tracks
    else:
        return mapped_tracks


async def update_track(track, type, value):
    """
    Update track in Reaper DAW. \n
    Parameters: \n
    track (int): Track ID inside Reaper DAW\n
    type (str): Slider/Mute\n
    value (float): Value of slider or -1 if it's mute request.\n
    Returns:\n
    list: mapping
    """
    if type == 'slider':
        if track == 5:
            await reaper.set_volume(track, value)
            return
        return

    elif type == 'mute':
        await reaper.mute(track, value)
        return