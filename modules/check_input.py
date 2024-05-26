import pinout
from modules import tracks, colors


async def sliders():
    """
    Check if any slider updated its value.\n
    
    Calls:\n
    tracks.get_mapped_tracks()\n
    tracks.update_track()\n
    """
    map = await tracks.get_mapped_tracks()

    try:
        for track in map:
            slider_index = int(track["slider"]) - 1

            # Check if slider is mapped correctly
            if slider_index >= len(pinout.sliders):
                print(colors.red + f"Slider index {slider_index} out of range for track {track['name']}" + colors.reset)
                continue

            # Read the slider value from the corresponding pin
            raw_value = pinout.sliders[slider_index].read_u16()
            scaled_value = round((raw_value / 65535.0) * 1000)
            reaper_value = scaled_value/1000
            new_slider_value = reaper_value
        
            if abs(new_slider_value - track["slider_value"]) >= 0.005:
                # Adjust accordingly if we are close to 0 or 1.0
                if new_slider_value <= 0.005:
                    new_slider_value = 0.0
                elif new_slider_value >= 0.995:
                    new_slider_value = 1.0

                print(colors.blue + f"Slider for {track['name']} changed from {track['slider_value']} to {new_slider_value}" + colors.reset)
                track["slider_previous"] = track["slider_value"]
                track["slider_value"] = new_slider_value
                await tracks.update_track(track['tracknumber'], "slider", new_slider_value)
                return
    except Exception as e:
        print(colors.red + f"Error: {e}" + colors.reset)

async def mute():
    """
    Check if any mute button updated its value.\n
    Calls:\n
    tracks.get_mapped_tracks()\n
    tracks.update_track()\n
    """
    map = await tracks.get_mapped_tracks()

    try:
        for track in map:
            mute_index = int(track["mute"]) - 1

            # Check if mute button is mapped correctly
            if mute_index >= len(pinout.mute):
                print(colors.red + f"mute index {mute_index} out of range for track {track['name']}" + colors.reset)
                continue

            # Read the mute value from the corresponding pin
            current_mute_value = pinout.mute[mute_index].value()
            previous_mute_value = track.get("mute_previous", False)

            # Check for rising edge (transition from not pressed to pressed)
            if current_mute_value and not previous_mute_value:
                # Toggle the mute value
                new_mute_value = not track["mute_value"]

                print(colors.blue + f"Mute for {track['name']} toggled to {new_mute_value}" + colors.reset)
                track["mute_previous"] = current_mute_value
                track["mute_value"] = new_mute_value
                await tracks.update_track(track["tracknumber"], "mute", '-1')
            else:
                # Update the previous state without toggling
                track["mute_previous"] = current_mute_value

    except Exception as e:
        print(colors.red + f"Error: {e}" + colors.reset)
