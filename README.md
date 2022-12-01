# ESP-WROOM-32 4MB

# TODO
    1. Add websocket
    2. Test CAN on a car
    
# Create virtual environment and activate (for testing and intelisense)
    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt

# RUN INSTALL.SH (bash install.sh)
    download the firmware: https://github.com/nos86/micropython/releases/tag/esp32-can-driver-v2 (Find release)
    check: http://domoticx.com/esp8266-esptool-bootloader-communicatie/

# MICROPYTHON SERVER
    microdot-->github search

# Install the required packages
    pip install esptool.py
    pip install adafruit-ampy
# HELP
    esptool.py --help
    ampy --help

# FLASH ESP: 
    esptool.py --port /dev/tty.usbserial-0001 erase_flash
# UPLOAD FIRMWARE: 
    esptool.py --port /dev/tty.usbserial-0001 write_flash 0x1000 firmware.bin
# PUT FILES: 
    ampy --port /dev/tty.usbserial-0001 put boot.py 
    ampy --port /dev/tty.usbserial-0001 put main.py 
    ampu -- ****** all files and folders

# create a REPL terminal
    screen /dev/tty.usbserial-0001 115200
