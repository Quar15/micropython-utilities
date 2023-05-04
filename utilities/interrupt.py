from machine import Pin

def setup_interrupt_pin(pin_n: int, f, pin_mode = Pin.PULL_DOWN, trigger = Pin.IRQ_RISING):
    pin = Pin(pin_n, Pin.IN, pin_mode)
    return pin, pin.irq(trigger=trigger, handler=f)

