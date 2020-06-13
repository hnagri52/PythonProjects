from dotenv import load_dotenv
import os
import json
import requests
load_dotenv()


class ZoomScheduler:
    #TODO: JWT generation should come dynamically, not have a default in the .env file
    def __init__(self):
        self.zoom_key = os.getenv("ZOOM_API_KEY")
        self.email = os.getenv("ZOOM_EMAIL")
        self.JWT = os.getenv("ZOOM_JWT")
    def send_invite(self, creation_details):
        URL = f"https://api.zoom.us/v2/users/{self.email}/meetings?access_token={self.JWT}"
        print(URL)
        data = json.dumps({})
        headers = {
            "Content-Type":"application/json"
        }
        res = requests.post(URL, data=data, headers=headers)
        print(res.content)

