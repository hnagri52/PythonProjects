from dotenv import load_dotenv
import os
import json
import requests
import re
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





        data = json.dumps({})
        headers = {
            "Content-Type":"application/json"
        }
        res = requests.post(URL, data=data, headers=headers)


    def get_details(self):
        to_send = input("Enter the email of the zoom participants, separated by a comma").split(",")
        for email in to_send:
            self.check(email)
        return to_send

    def check(self, email):
        #regex for email
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (re.search(regex, email)):
            pass
        else:
            raise ValueError(f'Invalid email provided: {email}')