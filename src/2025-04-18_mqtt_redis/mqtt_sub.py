import paho.mqtt.client as mqtt
import time

broker = 'localhost'
port = 1883
topics = [("a", 0), ("b", 0), ("c", 0)]  # (토픽 이름, QoS)

message_count = 0
start_time = time.time()

i = 2**14

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topics)

def on_message(client, userdata, msg):
    global message_count, start_time, i
    message_count += 1
    
    if ((message_count&i)!=0):
        now = time.time()
        print(f"[Received] msg_cnt({message_count}) spend time({now-start_time})")
        message_count = 0
        start_time = now

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)
client.loop_forever()