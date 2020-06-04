import datetime


class CalEvent:
    def __init__(self, desc=""):
        self.desc = desc

    def validate_and_add(self, date_text, date_type):
        try:
             datetime_obj = datetime.date.fromisoformat(date_text)
             if(isinstance(datetime_obj, datetime.date)):
                self.add_date(datetime_obj, date_type)
        except:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    def add_date(self, date, type):
        if(type=="start"):
            self.start_date = date
        else:
            self.end_date = date

