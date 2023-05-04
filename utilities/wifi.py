import network, rp2
import time
from utilities.config import WIFI_SSID, WIFI_PWD, MAX_RETRIES, WIFI_COUNTRY

def connect_to_wifi(ssid: str = WIFI_SSID, pwd: str = WIFI_PWD, retries: int = MAX_RETRIES):
    rp2.country(WIFI_COUNTRY)
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, pwd)

    retries = 0

    while not station.isconnected() and retries < MAX_RETRIES:
        time.sleep(5)
        retries += 1

    return station.isconnected(), station.ifconfig()


def turn_off_wifi():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(False)
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)


def get_available_AP():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    return wlan.scan()


def print_available_AP():
    aps = get_available_AP()
    print(f"@INFO: Available APs [{len(aps)}]")
    for ap in aps:
        print(ap)
