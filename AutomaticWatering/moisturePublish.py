import paho.mqtt.publish as publish
import serial
import time
import string
IP_ADDR = "54.183.6.241"
print("Done")


ser = serial.Serial("/dev/rfcomm1", 9600)
ser.write(str.encode('Start\r\n'))

while True:
        if ser.in_waiting > 0:
                rawserial = ser.readline()
                cookedserial = rawserial.decode('utf-8').strip('\r\n')
                humidity = cookedserial
                print(cookedserial)
                print ("Sending humidity to AWS")
                publish.single("humid", humidity, hostname=IP_ADDR)
