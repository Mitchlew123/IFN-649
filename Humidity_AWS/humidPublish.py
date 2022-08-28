import paho.mqtt.publish as publish
import serial
import time
import string
IP_ADDR = "204.236.175.9"
print("Done")


ser = serial.Serial("/dev/rfcomm1", 9600)
ser.write(str.encode('Start\r\n'))

while True:
        if ser.in_waiting > 0:
                rawserial = ser.readline()
                cookedserial = rawserial.decode('utf-8').strip('\r\n')
                humidity = cookedserial[0:16]
                print ("Sending humidity to AWS")
                publish.single("humid", humidity, hostname=IP_ADDR)
