#!/usr/bin/env python3
import time
from smbus2 import SMBus
import bme280

I2C_BUS = 1
BME280_ADDR = 0x76  # เปลี่ยนเป็น 0x77 ถ้า i2cdetect เห็น 77
INTERVAL_SEC = 2

def main():
    # โหลด calibration params ครั้งเดียว
    with SMBus(I2C_BUS) as bus:
        calibration_params = bme280.load_calibration_params(bus, BME280_ADDR)

    print("Reading BME280 via I2C...")
    print(f"I2C bus={I2C_BUS}, addr=0x{BME280_ADDR:02x}")

    while True:
        with SMBus(I2C_BUS) as bus:
            data = bme280.sample(bus, BME280_ADDR, calibration_params)

        temp_c = float(data.temperature)
        humid = float(data.humidity)
        press_hpa = float(data.pressure)

        print(f"Temp: {temp_c:6.2f} °C | Humid: {humid:6.2f} %RH | Pressure: {press_hpa:7.2f} hPa")
        time.sleep(INTERVAL_SEC)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped.")
