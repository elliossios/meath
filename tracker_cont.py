from ruuvitag_sensor.ruuvitag import RuuviTag
import time

sensor = RuuviTag('C3:D4:CC:7C:6C:2E')

while True:
    state = sensor.update()
    state = sensor.state

    print(state)
    time.sleep(1)