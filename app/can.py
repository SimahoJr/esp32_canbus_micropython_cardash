# Display driver from https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py
# Web server : https://github.com/jczic/MicroWebSrv
# https://github.com/hmaerki/micropython/tree/master/canbus_example
# https://github.com/nos86/micropython/blob/esp32-can-driver/examples/esp32_can.py
# https://github.com/nos86/micropython/blob/esp32-can-driver/docs/library/machine.CAN.rst
# Access point https://randomnerdtutorials.com/micropython-esp32-esp8266-access-point-ap/

from machine import CAN
import time

def sendAndCheck(dev, name, id, expectedLP = True):
    dev.clear_tx_queue()
    dev.clear_rx_queue()
    dev.send([], id)
    time.sleep_ms(100)
    if dev.any() == expectedLP:
        print("{}: OK".format(name))
        if expectedLP:
            hey = dev.recv()
            return True
        return False
    else:
        print("{}: FAILED".format(name))
        return False

dev = CAN(0,
    extframe=False, 
    mode=CAN.SILENT_LOOPBACK, 
    baudrate=500, 
    tx_io=17,rx_io=16, auto_restart=False)

#Test send/receive message
print("Loopback Test: no filter - STD")
sendAndCheck(dev, "No filter", 0x100, True)

#Set filter1
print("Loopback Test: one filter - STD")
dev.setfilter(0, CAN.FILTER_ADDRESS, [0x101, 0])
sendAndCheck(dev, "Passing Message", 0x101, True)
sendAndCheck(dev, "Blocked Message", 0x100, False)

#Set filter2
print("Loopback Test: second filter - STD")
dev.setfilter(0, CAN.FILTER_ADDRESS, [0x102, 0])
sendAndCheck(dev, "Passing Message - Bank 1", 0x102, True)
sendAndCheck(dev, "Passing Message - Bank 0", 0x101, True)
sendAndCheck(dev, "Blocked Message", 0x100, False)

#Remove filter
print("Loopback Test: clear filter - STD")
dev.clearfilter()
sendAndCheck(dev, "Passing Message - Bank 1", 0x102, True)
sendAndCheck(dev, "Passing Message - Bank 0", 0x101, True)
sendAndCheck(dev, "Passing any Message", 0x100, True)

#Move to Extended
dev = CAN(0,
    extframe=True, 
    mode=CAN.SILENT_LOOPBACK, 
    baudrate=500, 
    tx_io=17,rx_io=16, auto_restart=False)

#Test send/receive message
print("Loopback Test: no filter - Extd")
sendAndCheck(dev, "No filter", 0x100, True)

#Set filter1
print("Loopback Test: one filter - Extd")
dev.setfilter(0, CAN.FILTER_ADDRESS, [0x101, 0])
sendAndCheck(dev, "Passing Message", 0x101, True)
sendAndCheck(dev, "Blocked Message", 0x100, False)

#Remove filter
print("Loopback Test: clear filter - Extd")
dev.clearfilter()
sendAndCheck(dev, "Passing Message - Bank 0", 0x101, True)
sendAndCheck(dev, "Passing any Message", 0x100, True)