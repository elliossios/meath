from ruuvitag_sensor.ruuvitag import RuuviTag
import time
import os

sensor = RuuviTag('C3:D4:CC:7C:6C:2E')

while True:
    state = sensor.update()
    state = sensor.state

    with open("tracker_log.csv", "a") as f:
        f.write("{},{},{},{}\n".format(
            state["acceleration"],
            state["pressure"],
            state["temperature"],
            state["humidity"]
        ))
    time.sleep(1)