from ruuvitag_sensor.ruuvitag import RuuviTag
import time
import os
import sys

LOCK = "tracker.lock"

sensor = RuuviTag('C3:D4:CC:7C:6C:2E')

def create_lock():
    open(LOCK, "w+").close()

def free_lock():
    os.remove(LOCK)

def recreate_file(filename="tracker_log.csv"):
    try:
        os.remove(filename)
    except OSError:
        pass

    with open(filename, "w+") as f:
        f.write("acceleration,pressure,temperature,humidity\n")

def main():
    create_lock()
    while True:
        state = sensor.update()
        state = sensor.state

        try:
            with open("tracker_log.csv", "a") as f:
                f.write("{},{},{},{}\n".format(
                    state["acceleration"],
                    state["pressure"],
                    state["temperature"],
                    state["humidity"]
                ))
        except KeyError as e:
            print("Data was missing a value ", e)
        time.sleep(1)

if __name__=="__main__":
    if os.path.exists(LOCK):
        print("Tracker already running!")
        sys.exit(1)
    
    try:
        recreate_file()
        main()
    except KeyboardInterrupt as e:
        print("Tracking stopped")
        free_lock()