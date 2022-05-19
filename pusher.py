import http.client, urllib
import json

class Pusher:

    def __init__(self):
        self.conn = http.client.HTTPSConnection("api.pushover.net:443")
        self.credentials = json.load(open("credentials.json"))

    def push_message(self, message):
        self.conn.request("POST", "/1/messages.json",
        urllib.parse.urlencode({
            "token": self.credentials["APP_TOKEN"],
            "user": self.credentials["USER_TOKEN"]    ,
            "message": message,
        }), { "Content-type": "application/x-www-form-urlencoded" })
        self.conn.getresponse()
        