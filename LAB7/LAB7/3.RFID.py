import binascii
import sys
import Adafruit_PN532 as PN532
u=0
l=0
x=0
import time
import Adafruit_SSD1306
from PIL import Image,ImageDraw,ImageFont
RST = 1
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
import datetime
CS   = 8
MOSI = 10
MISO = 9
SCLK = 11
pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
pn532.begin()
ic, ver, rev, support = pn532.get_firmware_version()
print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))
pn532.SAM_configuration()
print('Waiting for MiFare card...')
while True:
    uid = pn532.read_passive_target()
    if uid is None:
        continue
    print('Found card with UID: 0x{0}'.format(binascii.hexlify(uid)))
    
