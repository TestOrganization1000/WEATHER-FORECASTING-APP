print("Hello World")

class Weather:
    def __init__(self, temperature):
        self.temperature = temperature
        
weather = Weather(30)

print(weather.temperature)