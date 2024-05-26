import pinout
import modules.tracks as tracks
import modules.colors as colors
import uasyncio
# sliders_value = {
#     'slider1_value' : 0.0,
#     "slider2_value" : 0.0,
#     "slider3_value" : 0.0,
#     "slider4_value" : 0.0
# }
# sliders_previous_value = {
#     'slider1_value' : 0.0,
#     "slider2_value" : 0.0,
#     "slider3_value" : 0.0,
#     "slider4_value" : 0.0
# }

# buttons_value = {
#     'mute1_value' : False,
#     "mute2_value" : False,
#     "mute3_value" : False,
#     "mute4_value" : False
# }
# buttons_previous_value = {
#     'mute1_value' : False,
#     "mute2_value" : False,
#     "mute3_value" : False,
#     "mute4_value" : False
# }



async def check_sliders():
    """
    Check if any slider updated it's value. \n

    Calls:\n
    tracks.get_mapped_tracks()\n
    tracks.update_track()\n

    """
    map = await tracks.get_mapped_tracks()

    try:
        for track in map:
            slider_index = int(track["slider"]) - 1

            if slider_index >= len(pinout.sliders):
                print(colors.red + f"Slider index {slider_index} out of range for track {track['name']}" + colors.reset)
                continue

            # Read the slider value from the corresponding pin
            new_slider_value = pinout.sliders[slider_index].read_u16() / 65535.0
        
            if new_slider_value != track["slider_value"]:
                print(colors.blue + f"Slider for {track['name']} changed from {track['slider_value']} to {new_slider_value}" + colors.reset)
                track["slider_previous"] = track["slider_value"]
                track["slider_value"] = new_slider_value
                await tracks.update_track(track['tracknumber'], "Slider", new_slider_value)
    except Exception as e:
        print(colors.red + f"Error: {e}" + colors.reset)



# async def check_sliders():
#     #print(colors.yellow + "Checking Sliders" + colors.reset)
#     sliders_previous_value = sliders_value.copy()
#     slider1_value = slider1.read_u16()
#     slider1_normalized = slider1_value/65535.0
#     sliders_value["slider1_value"] = slider1_normalized

#     slider2_value = slider2.read_u16()
#     slider2_normalized = slider2_value/65535.0
#     sliders_value["slider2_value"] = slider2_normalized

#     slider3_value = slider3.read_u16()
#     slider3_normalized = slider3_value/65535.0
#     sliders_value["slider3_value"] = slider3_normalized

#     slider4_value = slider4.read_u16()
#     slider4_normalized = slider4_value/65535.0
#     sliders_value["slider4_value"] = slider4_normalized
#     return sliders_value, sliders_previous_value




# async def check_buttons():
#     #print(colors.yellow + "Checking Buttons" + colors.reset)
#     buttons_previous_value = buttons_value.copy()
#     buttons_value["mute1_value"] = bool(mute1.value()) 
#     buttons_value["mute2_value"] = bool(mute2.value()) 
#     buttons_value["mute3_value"] = bool(mute3.value()) 
#     buttons_value["mute4_value"] = bool(mute4.value()) 
#     return buttons_value, buttons_previous_value