# Complete project details at https://RandomNerdTutorials.com

try:
  import usocket as socket
except:
  import socket

import network

import esp
esp.osdebug(0)

import gc
gc.collect()

ssid = 'pajeromini'
password = ''

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

while ap.active() == False:
  pass

print('Connection setup successful')
print(ap.ifconfig())