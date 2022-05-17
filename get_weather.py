

import requests
import datetime

url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/16.158/lat/58.5812/data.json"


hej = requests.get(url)

resp = hej.json()
#
import pprint

#pprint.pprint(resp)
#print(resp)

a = resp["timeSeries"]

#pprint.pprint(a)

date_fmt = "%Y-%m-%dT%H:%M:%SZ"

now = datetime.datetime.now()
print(now.date)
print("NOW", now)

def parse_entry(entry):
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
    return report
    
    
for entry in a:
    valid_time = entry["validTime"]
    #print(valid_time)

    a = datetime.datetime.strptime(valid_time, date_fmt)
    #print(a)
    
    if a.date() != now.date():
        continue
    if a.hour != 8:
        continue

    entry = parse_entry(entry)

    print(valid_time)
    print(entry)
    

