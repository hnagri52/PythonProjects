from dotenv import load_dotenv
import os
import requests
load_dotenv()


class ZoomScheduler:
    def __init__(self):
        self.zoom_key = os.getenv("ZOOM_API_KEY")
        self.email = os.getenv("ZOOM_EMAIL")
    def send_invite(self, creation_details):
        URL = f"https://api.zoom.us/v2/users/{self.email}/meetings"
        headers = {"Content-Type":"application/json", "Authorization": f"Bearer ${self.zoom_key}"}
        res = requests.post(URL, headers=headers)
        print(res)
        print(creation_details)
