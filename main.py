import server.update_map as update_map
import server.update_hotel as update_hotel
from server.flask_app import app
import time
import threading
import os

running = True

def periodically_update_data():
    while running:
        current_time = int(time.time())
        if current_time % 3600 == 0:
            time_tuple = time.localtime(time.time())
            print("Updating Covid-19 data and hotel data: {}/{}/{} {}:{}".format(time_tuple[0], time_tuple[1], time_tuple[2], time_tuple[3], time_tuple[4]))
            update_map.main()
            update_hotel.main()

def run_flask():
    app.run(host='0.0.0.0', debug=False)

def run_vue():
    os.system("npm run serve")

if not os.path.exists("node_modules"):
    print("Installing neccessary components...")
    os.system("npm install")
try:
    thread1 = threading.Thread(target=periodically_update_data)
    thread2 = threading.Thread(target=run_flask)
    thread3 = threading.Thread(target=run_vue)
    thread1.start()
    thread2.start()
    thread3.start()
except:
    running = False
    raise