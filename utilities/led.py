import machine
import time
import _thread
from utilities.threads import SECOND_THREAD_LOCK

BLINKER_LOCK = _thread.allocate_lock()
BLINK_DELAY = .5

def set_LED_state(state: bool, pin = "LED", led = None):
    if led == None: led = machine.Pin(pin, machine.Pin.OUT)
    led.on() if state else led.off()


def toggle_LED_state(pin = "LED", led = None):
    if led == None: led = machine.Pin(pin, machine.Pin.OUT)
    led.off() if led.value() else led.on()


def blink_loop(pin = "LED", exit_state: bool = True):
    led = machine.Pin(pin, machine.Pin.OUT)
    while not BLINKER_LOCK.locked():
        toggle_LED_state(pin, led)
        time.sleep(BLINK_DELAY)
    set_LED_state(exit_state, pin, led)
    SECOND_THREAD_LOCK.release()
    return


def start_blinking(pin = "LED", exit_state: bool = True):
    if BLINKER_LOCK.locked():
        print(f"@ERROR: BLINKER_LOCK ({BLINKER_LOCK.locked()}) is locked!")
        return False

    SECOND_THREAD_LOCK.acquire()
    _thread.start_new_thread(blink_loop, (pin, exit_state, ))
    return True


def stop_blinking():
    BLINKER_LOCK.acquire()
    time.sleep(BLINK_DELAY + 0.1)
    BLINKER_LOCK.release()