import paho.mqtt.client as mqtt
import time

broker = 'localhost'
port = 1883
topic = "a"

client = mqtt.Client()
client.connect(broker, port, 60)
client.loop_start()

count = 0
message = f"message {count}"

try:
    while True:
        client.publish(topic, message)
        count += 1
except KeyboardInterrupt:
    print("Publishing stopped.")
finally:
    client.loop_stop()
    client.disconnect()