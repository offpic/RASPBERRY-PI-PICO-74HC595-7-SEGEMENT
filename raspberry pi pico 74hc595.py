from machine import Pin
import time

LAT = machine.Pin(0, machine.Pin.OUT)
CLK = machine.Pin(1, machine.Pin.OUT)
DAT = machine.Pin(2, machine.Pin.OUT)

glyph = [63,6,91,79,102,109,125,7,127,111,119,124,57,94,121,113] #kathode common
#glyph = [192,249,164,176,153,146,130,248,128,144] #anode common

def hc595_shift(dat):
        LAT(0)
        time.sleep_us(1)
        for bit in range(7, -1, -1):
            CLK(0)
            time.sleep_us(1)
            value = 1 & (dat >> bit)
            DAT(value)
            time.sleep_us(1)
            CLK(1)
            time.sleep_us(1)
        time.sleep_us(1)
        LAT(1)
        time.sleep_us(1)


         

while True:
    for i in range(0,13):
        hc595_shift(glyph[i+2])
        hc595_shift(glyph[i+1])
        hc595_shift(glyph[i])
        time.sleep_ms(1000)


