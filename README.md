# ESP-WROOM-32 4MB
# Create virtual environment and activate (for testing and intelisense)
python3 -m venv venv<br />
. venv/bin/activate<br /><br />
pip install -r requirements.txt<br />

# RUN INSTALL.SH (bash install.sh)
download the firmware: https://github.com/nos86/micropython/releases/tag/esp32-can-driver-v2 (Find release)<br />
check: http://domoticx.com/esp8266-esptool-bootloader-communicatie/<br />

# SERVER: microdot-->github

# Install the required packages
pip install esptool.py<br />
pip install adafruit-ampy<br />
# HELP
    esptool.py --help<br />
    ampy --help<br />

# FLASH ESP: esptool.py --port /dev/tty.usbserial-0001 erase_flash
# UPLOAD FIRMWARE: esptool.py --port /dev/tty.usbserial-0001 write_flash 0x1000 firmware.bin
# PUT FILES: 
    ampy --port /dev/tty.usbserial-0001 put boot.py <br />
    ampy --port /dev/tty.usbserial-0001 put main.py <br />
    ampu -- ****** all files and folders<br />

# create a REPL terminal
    screen /dev/tty.usbserial-0001 115200
