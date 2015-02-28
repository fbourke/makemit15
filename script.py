import mraa, serial

motorPin = mraa.Gpio(3)
motorPin.dir(mraa.DIR_OUT)
motorPin.write(1)

ser = serial.Serial('/dev/ttyMFD1', 115200)
ser.write("\xA5\x21")
data = ser.read(5)
print(data)
