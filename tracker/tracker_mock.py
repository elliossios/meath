class MockSensor:
    def __init__(self, *args, **kwargs):
        self.state={'acceleration': 1056.1287800263754, 
                        'pressure': 1011.46, 
                        'temperature': 23.23, 
                        'acceleration_y': 16, 
                        'acceleration_x': -4, 
                        'battery': 3199, 
                        'acceleration_z': 1056, 
                        'humidity': 35.5}
    
    def update(self):
        return None
