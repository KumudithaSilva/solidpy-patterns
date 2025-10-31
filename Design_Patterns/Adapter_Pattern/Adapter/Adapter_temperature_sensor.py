class CelsiusTemperatureSensor:
    def __init__(self):
        self._temperature = 25

    def set_temperature(self, temperature):
        self._temperature = temperature

    def get_temperature_celsius(self):
        return self._temperature


class FahrenheitTemperatureSensor:
    def __init__(self):
        self._temperature = 77

    def set_temperature(self, temperature):
        self._temperature = temperature

    def get_temperature_fahrenheit(self):
        return self._temperature


# TODO: Complete the TemperatureSensorAdapter class
class TemperatureSensorAdapter:
    def __init__(self, sensor):
        self.sensor = sensor

    def set_temperature(self, temperature):
        self.sensor.set_temperature(temperature)

    def get_temperature_celsius(self):
        return (self.sensor.get_temperature_fahrenheit() - 32) * 5 / 9


def display_temperature(sensor):
    print(f"Temperature: {sensor.get_temperature_celsius():.2f} °C")



if __name__ == "__main__":
    celsius_sensor = CelsiusTemperatureSensor()
    fahrenheit_sensor = FahrenheitTemperatureSensor()

    # TODO: Create an instance of the TemperatureSensorAdapter
    adapter = TemperatureSensorAdapter(fahrenheit_sensor)

    display_temperature(celsius_sensor)
    if adapter:
        display_temperature(adapter)
