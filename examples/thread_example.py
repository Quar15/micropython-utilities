import _thread
import time

from utilities.threads import start_thread

global_variable = "MAIN"

def second_thread():
    global global_variable
    print(f"[Second Thread] - {global_variable}")
    global_variable = "SECOND"
    print(f"[Second Thread] - {global_variable}")


start_thread(f=second_thread)
print(f"[Main Thread] - {global_variable}")
time.sleep(5)
print(f"[Main Thread] - {global_variable}")