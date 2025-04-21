import redis
import time

r = redis.Redis(host='localhost', port=6379, db=0)

#messages_per_second = 3000
#interval = 1.0 / messages_per_second
count=0
message = f"message {count}"

try:
    while True:
        r.publish("a", message)
        count+= 1
except KeyboardInterrupt:
    print("Publishing stopped.")