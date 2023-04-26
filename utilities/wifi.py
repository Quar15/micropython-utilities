import network
import time
from utilities.config import WIFI_SSID, WIFI_PWD, MAX_RETRIES

def connect_to_wifi(ssid: str = WIFI_SSID, pwd: str = WIFI_PWD, retries: int = MAX_RETRIES):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, pwd)

    while not station.isconnected() and retries < MAX_RETRIES:
        time.sleep(5)

    return station.isconnected(), station.ifconfig()