

#!/usr/bin/python

from ruuvitag_sensor.ruuvi import RuuviTagSensor

def handle_data(found_data):
    print('MAC ' + found_data[0])
    print(found_data[1])

RuuviTagSensor.get_datas(handle_data)
