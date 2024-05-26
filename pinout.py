from machine import Pin, ADC
led = Pin("LED", Pin.OUT)

slider1 = ADC(Pin("GP26"))

slider2 = ADC(Pin("GP27"))

slider3 = ADC(Pin("GP28"))

slider4 = ADC(Pin("GP28"))

mute1 = Pin("GP0", Pin.IN)
mute2 = Pin("GP1", Pin.IN)
mute3 = Pin("GP2", Pin.IN)
mute4 = Pin("GP3", Pin.IN)