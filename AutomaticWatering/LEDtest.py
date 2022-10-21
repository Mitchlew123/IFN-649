import paho.mqtt.publish as publish
IP_ADDR = "54.183.6.241"
publish.single("humid", " START", hostname=IP_ADDR)
print("Done")
