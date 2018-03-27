from ruuvitag_sensor.ruuvitag import RuuviTag

sensor = RuuviTag('C3:D4:CC:7C:6C:2E')

# update state from the device
state = sensor.update()

# get latest state (does not get it from the device)
state = sensor.state

print(state)
