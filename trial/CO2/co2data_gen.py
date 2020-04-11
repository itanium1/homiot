from CO2Meter import *
import time
sensor = CO2Meter("/dev/hidraw0")
while True:
    time.sleep(2)
    are=sensor.get_data()
    print(are['co2'])