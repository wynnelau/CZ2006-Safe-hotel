import update_map
import update_hotel
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

if not os.path.exists("node_modules"):
    os.system("npm install")
try:
    thread = threading.Thread(target=periodically_update_data)
    thread.start()
    os.system("npm run serve")
except:
    running = False
    raise