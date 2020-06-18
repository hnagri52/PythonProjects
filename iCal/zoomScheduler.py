from dotenv import load_dotenv
import os
import json
import requests
import re
from icalendar import Calendar, Event
import pytz
import datetime

load_dotenv()


class ZoomScheduler:
    #TODO: JWT generation should come dynamically, not have a default in the .env file
    def __init__(self):
        self.zoom_key = os.getenv("ZOOM_API_KEY")
        self.email = os.getenv("ZOOM_EMAIL")
        self.JWT = os.getenv("ZOOM_JWT")
    def send_invite(self, creation_details):
        URL = f"https://api.zoom.us/v2/users/{self.email}/meetings?access_token={self.JWT}"

        emails = self.get_details()
        data = {"myEmail" : self.email,
                "send_emails" : emails,
                "start" : creation_details["start_date"],
                "end" : creation_details["end_date"],
                "desc" : creation_details["desc"]
                }

        data = json.dumps(data, indent=4, sort_keys=True, default=str)
        headers = {
            "Content-Type":"application/json"
        }
        res = requests.post(URL, data=data, headers=headers)


        print(creation_details["start_date"])

        cal = Calendar()
        self.make_ical(data)

        print(res.content)


    def get_details(self):
        to_send = input("Enter the email of the zoom participants, separated by a comma: ").split(",")
        emails = []
        for email in to_send:
            emails = self.check(email)
        return to_send

    def check(self, email):
        #regex for email
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (re.search(regex, email.strip())):
            return email.strip()
        else:
            raise ValueError(f'Invalid email provided: {email}')

    def make_ical(self,data):
        event = Event()
        event.add('summary', data["desc"])
        event.add("dtstart", datetime(data["start_date"].year, data["start_date"].month, data["start_date"].day, 8,0,0, tzinfo=pytz.utc))
        event.add('dtend', datetime(data["end_date"].year, data["end_date"].month, data["end_date"].day, 8,0,0, tzinfo=pytz.utc))