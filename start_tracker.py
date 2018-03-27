from ruuvitag_sensor.ruuvitag import RuuviTag
import time
import os
import sys
import subprocess as sp
from tracker.tracker_mock import MockSensor

SENSOR_MAC = 'C3:D4:CC:7C:6C:2E'
LOCK = "tracker.lock"

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
        f.write("timestamp,acceleration,pressure,temperature,humidity\n")

def main(sensor):
    create_lock()
    while True:
        state = sensor.update()
        state = sensor.state
        data = ""
        try:
            with open("tracker_log.csv", "a") as f:
                data = "{},{},{},{},{}".format(
                    time.time(),
                    state["acceleration"],
                    state["pressure"],
                    state["temperature"],
                    state["humidity"]
                )
                f.write(data + "\n")
                print(data)
        except KeyError as e:
            print("Data was missing a value ", e)
        time.sleep(1)

if __name__=="__main__":
    if os.path.exists(LOCK):
        print("Tracker already running!")
        sys.exit(1)
    
    stdoutdata = sp.getoutput("hcitool con")

    if SENSOR_MAC in stdoutdata.split():
        print("Bluetooth device is connected")
        sensor = RuuviTag(SENSOR_MAC)
    else:
        print("Using mock sensor")
        sensor = MockSensor()

    try:
        recreate_file()
        main(sensor)
    except KeyboardInterrupt as e:
        print("Tracking stopped")
        free_lock()