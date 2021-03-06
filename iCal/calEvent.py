from datetime import datetime
from zoomScheduler import ZoomScheduler

class CalEvent:
    def __init__(self, desc=""):
        self.desc = desc


    def validate_and_add(self, date_text, date_type):
        try:
             datetime_obj = datetime.fromisoformat(date_text)
             if(isinstance(datetime_obj, datetime)):
                self.add_date(datetime_obj, date_type)
        except:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD HH:MM")

    def add_date(self, date, type):
        if(type=="start"):
            self.start_date = date
        else:
            self.end_date = date


    def schedule_meeting(self, details):
        newMeeting = ZoomScheduler()
        newMeeting.send_invite(details)


