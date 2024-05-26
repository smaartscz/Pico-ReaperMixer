from pinout import slider1, slider2, slider3, slider4, mute1, mute2, mute3, mute4
import modules.colors as colors
import uasyncio
sliders_value = {
    'slider1_value' : 0.0,
    "slider2_value" : 0.0,
    "slider3_value" : 0.0,
    "slider4_value" : 0.0
}
sliders_previous_value = {
    'slider1_value' : 0.0,
    "slider2_value" : 0.0,
    "slider3_value" : 0.0,
    "slider4_value" : 0.0
}

buttons_value = {
    'mute1_value' : False,
    "mute2_value" : False,
    "mute3_value" : False,
    "mute4_value" : False
}
buttons_previous_value = {
    'mute1_value' : False,
    "mute2_value" : False,
    "mute3_value" : False,
    "mute4_value" : False
}

async def check_sliders():
    #print(colors.yellow + "Checking Sliders" + colors.reset)
    sliders_previous_value = sliders_value.copy()
    slider1_value = slider1.read_u16()
    slider1_normalized = slider1_value/65535.0
    sliders_value["slider1_value"] = slider1_normalized

    slider2_value = slider2.read_u16()
    slider2_normalized = slider2_value/65535.0
    sliders_value["slider2_value"] = slider2_normalized

    slider3_value = slider3.read_u16()
    slider3_normalized = slider3_value/65535.0
    sliders_value["slider3_value"] = slider3_normalized

    slider4_value = slider4.read_u16()
    slider4_normalized = slider4_value/65535.0
    sliders_value["slider4_value"] = slider4_normalized
    print(sliders_value)
    return sliders_value, sliders_previous_value




async def check_buttons():
    #print(colors.yellow + "Checking Buttons" + colors.reset)
    buttons_previous_value = buttons_value.copy()
    buttons_value["mute1_value"] = bool(mute1.value()) 
    buttons_value["mute2_value"] = bool(mute2.value()) 
    buttons_value["mute3_value"] = bool(mute3.value()) 
    buttons_value["mute4_value"] = bool(mute4.value()) 
    return buttons_value, buttons_previous_value

