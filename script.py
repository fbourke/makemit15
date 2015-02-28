import mraa, serial
from time import sleep

motorPin = mraa.Gpio(3)
motorPin.dir(mraa.DIR_OUT)
motorPin.write(1)

ser = serial.Serial('/dev/ttyMFD1', 115200)
sleep(0.5)
ser.write("\xA5\x21")
while True:
	while ser.inWaiting() > 0:
		data = ser.read()
		print(data)
	while ser.inWaiting() == 0:
		ser.write("\xA5\x52")

