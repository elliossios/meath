import binascii

class Measurement:
    def __init__(self, time, lat, lon, measurement, measurement_name):
        self.time = time
        self.lat = lat
        self.lon = lon
        self.measurement = measurement
        self.measurement_name = measurement_name

    def to_string(self):
        return "{},{},{},{}".format(
            self.time,
            self.lat, 
            self.lon, 
            self.measurement
        )
    
    def to_csv_row(self):
        return "{},{},{},{},{}\n".format(
            self.time,
            self.lat,
            self.lon,
            self.measurement_name, 
            self.measurement
        ) 
    
    def to_hex(self):
        data = self.to_string()
        return binascii.hexlify(data.encode('utf-8'))
    
    def __str__(self):
        return self.to_string()
