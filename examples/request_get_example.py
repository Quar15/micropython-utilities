from utilities.wifi import connect_to_wifi
from utilities.simple_request import Request

def main():
    is_connected, ipconfig = connect_to_wifi()

    if not is_connected:
        return

    data = Request.get("http://api.open-notify.org/astros.json").json()
    number = data['number']
    for i in range(number):
        print(data['people'][i]['name'])

if __name__ == "__main__":
    main()
