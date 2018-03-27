from ruuvitag_sensor.ruuvitag import RuuviTag
import time
import os
import sys
import subprocess as sp
from tracker.tracker_mock import MockSensor
from signal import signal, SIGPIPE, SIG_DFL 

SENSOR_MAC = 'C3:D4:CC:7C:6C:2E'
LOCK = "tracker.lock"

def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)
    
    return reduce(lambda x,y:x+y, lst)

def toStr(s):
    return s and chr(atoi(s[:2], base=16)) + toStr(s[2:]) or ''

def recreate_file(filename="tracker_log.csv"):
    try:
        os.remove(filename)
    except OSError:
        pass

    with open(filename, "w+") as f:
        f.write("timestamp,acceleration,pressure,temperature,humidity\n")

def main(sensor, measurement):
    signal(SIGPIPE,SIG_DFL) 

    state = sensor.update()
    state = sensor.state
    data = ""
    try:
        with open("tracker_log.csv", "a") as f:
            state["timestamp"] = time.time()
            data = "{},{},{},{},{}".format(
                state["timestamp"],
                state["acceleration"],
                state["pressure"],
                state["temperature"],
                state["humidity"]
            )
            f.write(data + "\n")
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
    if args.mock:
        sensor = RuuviTag(SENSOR_MAC)
    else:
        sensor = MockSensor()

    recreate_file()
    main(sensor, args.measurement)