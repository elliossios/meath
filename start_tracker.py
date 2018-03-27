from ruuvitag_sensor.ruuvitag import RuuviTag
import time
import os
import sys
import subprocess as sp
from tracker.tracker_mock import MockSensor
from signal import signal, SIGPIPE, SIG_DFL 

SENSOR_MAC = 'C3:D4:CC:7C:6C:2E'

def create_log_file(filename="tracker_log.csv"):
    try:
        os.remove(filename)
    except OSError:
        pass

    with open(filename, "w+") as f:
        f.write("timestamp,acceleration,pressure,temperature,humidity\n")

def write_to_csv(state):
    with open("tracker_log.csv", "a") as f:
        data = "{},{},{},{},{}".format(
            state["timestamp"],
            state["acceleration"],
            state["pressure"],
            state["temperature"],
            state["humidity"]
        )
        f.write(data + "\n")

def run(sensor, measurement):
    signal(SIGPIPE,SIG_DFL) 

    _ = sensor.update()
    state = sensor.state
    state["timestamp"] = time.time()

    try:
        #write_to_csv(state)
        data = "{},{}".format(
            state["timestamp"],
            state[measurement]
        )
        data = data.encode('utf-8')
        print(data.hex())
    except KeyError as e:
        print(e)

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description='Tracker config.')
    parser.add_argument('--mock', action='store_false')
    parser.add_argument('--measurement')
    args = parser.parse_args()

    # Check if we want to mock the sensor because we are not running on HiKey
    if args.mock:
        sensor = RuuviTag(SENSOR_MAC)
    else:
        sensor = MockSensor()

    create_log_file()
    run(sensor, args.measurement)