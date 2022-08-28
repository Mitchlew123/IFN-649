import paho.mqtt.publish as publish
IP_ADDR = "204.236.175.9"
publish.single("light_switch", " LED_OFF", hostname=IP_ADDR)
print("Done")
