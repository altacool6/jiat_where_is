import redis
import time

i = 2**14
r = redis.Redis(host='localhost', port=6379, db=0)
pubsub = r.pubsub()
pubsub.subscribe('a','b','c')

message_count = 0
start_time = time.time()

# print("Subscribed to test_channel")

for message in pubsub.listen():
    if message['type'] != 'message':
        continue

    message_count+=1
    
    if ((message_count&i)!=0):
        now = time.time()
        print(f"[Received] {message_count} messages/sec {message['data']}, spend time({now-start_time})")
        message_count = 0
        start_time = now