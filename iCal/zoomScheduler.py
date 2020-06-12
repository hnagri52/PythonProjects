from dotenv import load_dotenv
import os
load_dotenv()


class ZoomScheduler:
    def __init__(self):
        self.zoom_key = os.getenv("ZOOM_KEY")

    def send_invite(self, creation_details):
        print(self.zoom_key)
        print(creation_details)
