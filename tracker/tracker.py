from ruuvitag_sensor.ruuvitag import RuuviTag

sensor = RuuviTag('D3:7E:10:F4:95:6D')

# update state from the device
state = sensor.update()

# get latest state (does not get it from the device)
state = sensor.state

print(state)
