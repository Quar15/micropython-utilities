from machine import Pin
import time
from utilities.interrupt import setup_interrupt_pin

INPUT_PIN_1 = 15
INPUT_PIN_2 = 14


def interrupt_f(pin):
    print("@INFO: Interrupt called")
    while pin.value(): continue
        
    time.sleep_ms(50)
    

def interrupt_f_unprotected(pin):
    print("@INFO: Interrupt unprotected called")


setup_interrupt_pin(INPUT_PIN_1, interrupt_f)
setup_interrupt_pin(INPUT_PIN_2, interrupt_f_unprotected)

for i in range(10):
    print("Working...")
    time.sleep(1)

