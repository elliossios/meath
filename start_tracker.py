import time
import os
import sys
import subprocess as sp
from tracker.mock_sensor import MockSensor
from tracker.geo_api import GeoApi
from tracker.models import Measurement
from signal import signal, SIGPIPE, SIG_DFL 

SENSOR_MAC = 'C3:D4:CC:7C:6C:2E'
LOGFILE = "tracker_log.csv"
GEO_SERVER = "http://localhost:5000"

def create_log_file(filename="tracker_log.csv"):
    with open(filename, "w+") as f:
        f.write("timestamp,lat,long,measurement,value\n")

def write_to_csv(data: Measurement):
    with open(LOGFILE, "a") as f:
        f.write(data.to_csv_row())

def run(sensor, measurement):
    signal(SIGPIPE,SIG_DFL) 
    geo_api = GeoApi(GEO_SERVER)
    loc = geo_api.get_location()

    _ = sensor.update()
    state = sensor.state

    try: 
        data = Measurement(time.time(), loc["lat"], loc["long"],
                            state[measurement], measurement)
        write_to_csv(data)
        print(data.to_hex())
    except KeyError as e:
        print(e)

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description='Tracker config.')
    parser.add_argument('--mock', action='store_false')
    parser.add_argument('--measurement', required=True)
    args = parser.parse_args()

    # Check if we want to mock the sensor because we are not running on HiKey
    if args.mock:
        from ruuvitag_sensor.ruuvitag import RuuviTag
        sensor = RuuviTag(SENSOR_MAC)
    else:
        sensor = MockSensor()

    if not os.path.exists(LOGFILE):
        create_log_file()
    run(sensor, args.measurement)