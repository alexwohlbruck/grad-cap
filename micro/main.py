from machine import Pin
from time import sleep_ms

center = Pin(27, Pin.OUT)
left = Pin(25, Pin.OUT)
right = Pin(32, Pin.OUT)
button = Pin(33, Pin.IN, Pin.PULL_UP)
builtin = Pin(2, Pin.OUT)

effect = 1
effects = range(4)

def on_button(val):
    global effect
    global effects
    
    # Switch to next effect
    effect = (effect + 1) % len(effects)
    
    for blink in range(effect):
        builtin.value(1)
        sleep_ms(100)
        builtin.value(0)
        sleep_ms(100)
    

def set(lcr):
    l,c,r = lcr
    left.value(l)
    center.value(c)
    right.value(r)

def wait(duration=500):
    sleep_ms(duration)

def solid():
    set((1,1,1))

def off():
    set((0,0,0))
    sleep_ms(100)

def chase(d):
    set((1,0,0))
    wait(d)
    set((0,1,0))
    wait(d)
    set((0,0,1))
    wait(d)

def typewrite(d):
    off()
    wait(d)
    set((1,0,0))
    wait(d)
    set((1,1,0))
    wait(d)
    solid()
    wait(d * 2)

def sides_center(d):
    set((0,1,0))
    wait(d)
    set((1,0,1))
    wait(d)
    set((0,1,0))
    wait(d)

button.irq(trigger=Pin.IRQ_FALLING, handler=on_button)

while True:        
    if effect == 0:
        off()
    elif effect == 1:
        solid()
    elif effect == 2:
        typewrite(500)
    elif effect == 3:
        chase(100)
        sides_center(100)
