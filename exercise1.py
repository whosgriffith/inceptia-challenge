import requests
import json


class GeoAPI:
    API_URL = "https://api.openweathermap.org/data/2.5/weather"
    API_KEY = "d81015613923e3e435231f2740d5610/b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"

    @classmethod
    def is_hot_in_pehuajo(cls):
        url = cls.API_URL + f"?lat={cls.LAT}&lon={cls.LON}&appid={cls.API_KEY}&units=metric"
        try:
            response = requests.get(url)
            current_weather = json.loads(response.content)
            current_temperature = current_weather['main']['temp']
        except Exception as Ex:
            print(Ex)
            return False

        if current_temperature > 28:
            return True

        return False


print(GeoAPI.is_hot_in_pehuajo())
