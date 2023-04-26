import time
from utilities.led import start_blinking, stop_blinking

def test_loop():
    start_blinking()
    print("Started blinking...")
    time.sleep(5)
    stop_blinking()
    print("Stopped blinking...")

print("@INFO: START")
test_loop()
time.sleep(5)
test_loop()
time.sleep(5)
print("@INFO: END")