

import requests
import datetime

class WeatherApi:
    def __init__(self):
        self.url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{lon}/lat/{lat}/data.json"

        self.time_series = None
        self.date_fmt = "%Y-%m-%dT%H:%M:%SZ"

        self.now = datetime.datetime.now()
        self.now = datetime.datetime(2022, 5, 20, 1, 1)

    def get_weather(self, lon: float, lat: float) -> bool:
        full_url = self.url.format(lon=lon, lat=lat)
        response = requests.get(full_url)
        if response.status_code != 200:
            print("Failed with request")
            print(response.status_code)
            print(response.text)
            return False

        response_json = response.json()
        self.time_series = response_json["timeSeries"]

        return True

    def parse_timeseries(self):
        for entry in self.time_series:
            if not self.is_valid_time(entry):
                continue
            return self.get_report(entry)

        print("No valid entry")
        return None

    def is_valid_time(self, entry: dict):
        valid_time = entry["validTime"]
        formatted_time = datetime.datetime.strptime(valid_time, self.date_fmt)
        if formatted_time.date() != self.now.date():
            return False
        if formatted_time.hour != 8:
            return False
        return True
            

    def get_report(self, entry):
        """Parse one single entry of the timeseries."""
        report = {}
        for param in entry["parameters"]:
            value = param["values"][0]

            if param["name"] == "t":
                report["temperature"] = value
            if param["name"] == "ws":
                report["wind_speed"] = value
            if param["name"] == "pmean":
                report["rain"] = value
        return self.format_report(report)

    def format_report(self, report):
        return f"Temperature: {report['temperature']}, rain: {report['rain']} with wind speed: {report['wind_speed']}"
