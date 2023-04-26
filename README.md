# Micropython Utilities

## What is it?

Micropython Utilities is a small package for usage with Raspberry Pi Pico W. (It can be used with Pico, Pico H, and ESP32, but it can need some tweaks)

## Usage

1. Clone the repository (Choose one version of setup)

Minimal setup

```sh
git clone https://github.com/Quar15/micropython-utilities.git -b utilities --single-branch
```

Full setup

```sh
git clone https://github.com/Quar15/micropython-utilities.git
```

2. Copy `utilities` folder to Pico storage

1. Now you can use it as normal package

```python
from utilities.conifg import *
from utilities.file_manager import *
from utilities.led import *
from utilities.simple_request import *
from utilities.threads import *
from utilities.wifi import *
```

`NOTE`: Import only those variables and/or functions that you need to avoid unexpected errors

## File contents

> Examples folder

All files inside `examples` folder are exemplary usage of utilities package

> Utilities folder

| Filename | Status | Description |
| :-- | :-- | :-- |
| `config.py` | ✅ | Configuration variables used inside library |
| `file_manager.py` | ✅ | Saving and reading file |
| `led.py` | ✅ | Setting, toggling LED and blinking (using second thread)|
| `simple_request.py` | 🚧 | GET, POST, PUT, DELETE request|
| `threads.py` | 🚧 | Thread manager |
| `wifi.py` | 🚧 | Wi-fi connection, AP setup |

Legend
- ✅ - it is done and ok to use it without concerns
- 🚧 - it is NOT done yet and can be unstable