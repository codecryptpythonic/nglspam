import requests
import threading
import time
import os
import random
import string

os.system('cls' if os.name == 'nt' else 'clear')

def logo():
    print("""####################
Made by codecryptpythonic

Use it for fun!
####################
    """)

logo()

def deviceid():
    return "".join(random.choice("0123456789abcdefghijklmnopqrstuvwxyz-") for i in range(36))

def send_request(user, q):
    h = "https://ngl.link/api/submit"
    message = f"{q}"
    data = {
        "username": user,
        "question": message,
        "deviceId": deviceid(),
    }
    try:
        k = requests.post(h, data=data).text
        print("Sent request!")
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(0.5)

user = input("Enter your username: ")
q = input("Enter your message: ")
idd = int(input("How many times do you want to send requests: "))

threads = []
for i in range(1, idd + 1):
    thread = threading.Thread(target=send_request, args=(user, q))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
