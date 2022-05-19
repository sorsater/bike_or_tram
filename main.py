from get_weather import WeatherApi
from pusher import Pusher

def main():
    w_api = WeatherApi()
    pusher = Pusher()

    res = w_api.get_weather(lon=16.158, lat=58.5812)
    if not res:
        return
    report = w_api.parse_timeseries()
    pusher.push_message(report)


if __name__ == "__main__":
    main()