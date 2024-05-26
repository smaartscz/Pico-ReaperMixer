"""
DEFINE PHYSICAL INPUTS AND OUTPUTS:

TEMPLATE:
mute1 = Pin("GP0", Pin.IN) for input pin. Replace GP0 with correct pin based on PicoW/Pico pinout. Don't forget to add your new variable(in this case it's mute1) into mute = []
"""

from machine import Pin, ADC
led = Pin("LED", Pin.OUT)

slider1 = ADC(Pin("GP26"))
slider2 = ADC(Pin("GP27"))
slider3 = ADC(Pin("GP28"))
slider4 = ADC(Pin("GP28"))
sliders = [slider1, slider2, slider3, slider4]

mute1 = Pin("GP0", Pin.IN)
mute2 = Pin("GP1", Pin.IN)
mute3 = Pin("GP2", Pin.IN)
mute4 = Pin("GP3", Pin.IN)
mute = [mute1, mute2, mute3, mute4]