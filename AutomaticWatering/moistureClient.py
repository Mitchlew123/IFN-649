import serial
import paho.mqtt.client as mqtt
IP_ADDR = "54.183.6.241"

def on_connect(client, userdata, flags, rc): # func for making connection
	print("Connected to MQTT")
	print("Connection returned result: " + str(rc) )
	client.subscribe("humid")

def on_message(client, userdata, msg): # Func for Sending msg
	ser.write(msg.payload)
	message = msg.payload
	message = message.decode()
ser = serial.Serial("/dev/rfcomm1", 9600)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(IP_ADDR, 1883, 60)

client.loop_forever()
