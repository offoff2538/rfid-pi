import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
col=[26,19,13,6]
row=[21,20,16,7]
for x in row:
	GPIO.setup(x, GPIO.IN, pull_up_down=GPIO.PUD_UP)
for y in col:
	GPIO.setup(y,GPIO.OUT)
	GPIO.output(y,0)
keypad=[
					[1,2,3,"A"],
					[4,5,6,"B"],
					[7,8,9,"C"],
					["E",0,"F","D"]
					]
k=''
cc=0
a=0
def button_pressed(channel):
	global keypad,cc,k
	a=1
	while a:
		for x in range(4):
			GPIO.output(col[x],0)
			for y in range (4):
				if GPIO.input(row[y])==0:
					while  GPIO.input(row[y])==0:
						pass
					k+=str(keypad[y][x])
					cc+=1
					a=0
					print str(keypad[y][x])
					time.sleep(1)
			GPIO.output(col[x],1) 
GPIO.add_event_detect(21, GPIO.RISING, callback=button_pressed,
bouncetime=300)
GPIO.add_event_detect(20, GPIO.RISING, callback=button_pressed,
bouncetime=300)
GPIO.add_event_detect(16, GPIO.RISING, callback=button_pressed,
bouncetime=300)
GPIO.add_event_detect(7, GPIO.RISING, callback=button_pressed,
bouncetime=300)
import time
import Adafruit_SSD1306
from PIL import Image,ImageDraw,ImageFont
RST = 1
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
import datetime
import binascii
import sys
import Adafruit_PN532 as PN532
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
while 1:
	now = datetime.datetime.now()
	now2 =now.strftime("%H:%M")
	now1=now.strftime("%d/%m/%Y")
	if cc==5:
		if k=="12345":
			width = disp.width
			height = disp.height  
			image = Image.new('1', (width, height))
			draw = ImageDraw.Draw(image)
			font = ImageFont.truetype('VCR_OSD_MONO_1.001.ttf',22)
			draw.text((0,0), 'Antman',font=font, fill=1)
			disp.image(image)
			disp.display()
			k=''
			cc=0
			with open("December.txt", "a") as text_file:
				text_file.write("Code:12345  Name:Antman  Date: %s Time: %s\n" % (now1,now2))
		elif k=="67890":
			width = disp.width
			height = disp.height  
			image = Image.new('1', (width, height))
			draw = ImageDraw.Draw(image)
			font = ImageFont.truetype('VCR_OSD_MONO_1.001.ttf',22)
			draw.text((0,0), 'Ironman',font=font, fill=1)
			disp.image(image)
			disp.display()
			k=''
			cc=0
			with open("December.txt", "a") as text_file:
				text_file.write("Code:67890  Name:Ironman  Date: %s Time: %s\n" % (now1,now2))
		else:
			width = disp.width
			height = disp.height  
			image = Image.new('1', (width, height))
			draw = ImageDraw.Draw(image)
			font = ImageFont.truetype('VCR_OSD_MONO_1.001.ttf',18)
			draw.text((0,0), 'Access Denied',font=font, fill=1)
			disp.image(image)
			disp.display()
			k=''
			cc=0
	uid = pn532.read_passive_target()
	# Try again if no card is available.
	if uid is None:
		continue
	uid_str = str(binascii.hexlify(uid))
	if uid_str=="4fbe4729":
			width = disp.width
			height = disp.height  
			image = Image.new('1', (width, height))
			draw = ImageDraw.Draw(image)
			font = ImageFont.truetype('VCR_OSD_MONO_1.001.ttf',22)
			draw.text((0,0), 'Spiderman',font=font, fill=1)
			print ('Found card with UID:0x{}'.format(uid_str))
			disp.image(image)
			disp.display()
			k=''
			cc=0
			with open("December.txt", "a") as text_file:
				text_file.write("Code:0x4fbe4729 Name:Spiderman  Date: %s Time: %s\n" % (now1,now2))
	elif uid_str=="e235315b":
			width = disp.width
			height = disp.height  
			image = Image.new('1', (width, height))
			draw = ImageDraw.Draw(image)
			font = ImageFont.truetype('VCR_OSD_MONO_1.001.ttf',22)
			draw.text((0,0), 'Superman',font=font, fill=1)
			print ('Found card with UID:0x{}'.format(uid_str))
			disp.image(image)
			disp.display()
			k=''
			cc=0
			with open("December.txt", "a") as text_file:
				text_file.write("Code:0xe235315b  Name:Superman  Date: %s Time: %s\n" % (now1,now2))
	else:
		width = disp.width
		height = disp.height  
		image = Image.new('1', (width, height))
		draw = ImageDraw.Draw(image)
		font = ImageFont.truetype('VCR_OSD_MONO_1.001.ttf',18)
		draw.text((0,0), 'Access denied',font=font, fill=1)
		print ('Found card with UID:0x{}'.format(uid_str))
		disp.image(image)
		disp.display()
		k=''
		cc=0
