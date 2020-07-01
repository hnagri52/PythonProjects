from dotenv import load_dotenv
import json
import requests
import re
from icalendar import Calendar, Event
import tempfile, os
import pytz
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import COMMASPACE, formatdate
from datetime import datetime
from os.path import basename

load_dotenv()


class ZoomScheduler:
    #TODO: JWT generation should come dynamically, not have a default in the .env file
    def __init__(self):
        self.zoom_key = os.getenv("ZOOM_API_KEY")
        self.email = os.getenv("ZOOM_EMAIL")
        self.JWT = os.getenv("ZOOM_JWT")
        self.smtp_email = os.getenv("SMTP_EMAIL")
        self.smtp_pass = os.getenv("SMTP_PWD")


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

        cal = Calendar()
        cal.add_component(self.make_ical(data, res.content))
        dir = self.write_temp_dir()
        #make the send email fct call
        self.send_mail(dir, self.smtp_email, data["send_emails"], )

        #TODO:// create a functoin to send the email, the file is located in dir @ dir/invite.ics -->LINK: https://stackoverflow.com/questions/3362600/how-to-send-email-attachments

        # print(res.content)


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

    def make_ical(self,data, zoom_details):
        event = Event()
        data = json.loads(data)
        zoom_data = json.loads(zoom_details)
        #TODO: so have 1 event which sends meeting icals to attendees, and 1 for host

        #For host
        total_desc = data["desc"] + "\n" + "Link to start meeting: " + zoom_data["start_url"]
        event.add("summary", total_desc)
        event.add("dtstart", datetime.strptime(data["start"], '%Y-%m-%d %H:%M:%S'))
        event.add('dtend', datetime.strptime(data["end"], '%Y-%m-%d %H:%M:%S'))
        # event.add("")
        for email in data["send_emails"]:
            event.add("attendee", f"MAILTO:${email}")
        #https://icalendar.readthedocs.io/en/latest/usage.html


        return event
        print(data)
        print(zoom_data)

    def write_temp_dir(self, cal):
        directory = tempfile.mkdtemp()
        f = open(os.path.join(directory, 'invite.ics'), 'wb')
        f.write(cal.to_ical())
        f.close()
        return directory


    def send_mail(self, directory,send_from, send_to, subject, text, files=None,
              server="127.0.0.1" ):
        assert isinstance(send_to, list)
        #TODO: TWEAK
        # msg = MIMEMultipart()
        # msg['From'] = send_from
        # msg['To'] = COMMASPACE.join(send_to)
        # msg['Date'] = formatdate(localtime=True)
        # msg['Subject'] = subject
        #
        # msg.attach(MIMEText(text))
        #
        # for f in files or []:
        #     with open(f, "rb") as fil:
        #         part = MIMEApplication(
        #             fil.read(),
        #             Name=basename(f)
        #         )
        #     # After the file is closed
        #     part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        #     msg.attach(part)
        #
        # smtp = smtplib.SMTP(server)
        # smtp.sendmail(send_from, send_to, msg.as_string())
        # smtp.close()

        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders

        fromaddr = "EMAIL address of the sender"
        toaddr = "EMAIL address of the receiver"

        # instance of MIMEMultipart
        msg = MIMEMultipart()

        # storing the senders email address
        msg['From'] = send_from

        # storing the receivers email address
        msg['To'] = COMMASPACE.join(send_to)

        # storing the subject
        msg['Subject'] = subject

        # string to store the body of the mail
        body = text

        # attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # open the file to be sent
        filename = "invite.ics"
        attachment = open(os.path.join(directory, filename), "rb")

        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
        p.set_payload((attachment).read())

        # encode into base64
        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # attach the instance 'p' to instance 'msg'
        msg.attach(p)

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(send_from, self.smtp_pass)

        # Converts the Multipart msg into a string
        text = msg.as_string()

        # sending the mail
        s.sendmail(send_from, toaddr, text)

        # terminating the session
        s.quit()




{'desc': '2000-02-03 12:12', 'end': '2000-02-03 12:12:00', 'myEmail': 'hznagri@uwaterloo.ca', 'send_emails': ['qw@wq.ca'], 'start': '2000-02-03 12:12:00'}
{'uuid': 'wcXGlu9NQ3SjJRmZ9fgSMQ==', 'id': 83785232253, 'host_id': '-xFmmXU3TrKLt1qM8u_F0w', 'topic': 'Zoom Meeting', 'type': 2, 'status': 'waiting', 'start_time': '2020-06-26T01:16:40Z', 'duration': 60, 'timezone': 'America/Los_Angeles', 'created_at': '2020-06-26T01:16:40Z', 'start_url': 'https://us02web.zoom.us/s/83785232253?zak=eyJ6bV9za20iOiJ6bV9vMm0iLCJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJjbGllbnQiLCJ1aWQiOiIteEZtbVhVM1RyS0x0MXFNOHVfRjB3IiwiaXNzIjoid2ViIiwic3R5IjoxMDAsIndjZCI6InVzMDIiLCJjbHQiOjAsInN0ayI6IkxIMHQ5c2hfSTNVekpONHEtVnBhTzJJVDQ0UzNvQmd1MXlmMDdhRjFlS1UuQmdVZ1IwRkJNMUoxZEdsNFZVTnJObkZUT1N0M1NEUXZiREJNVkc1VmJ6VnhObmxBWW1ReU1EWTJPVGd4TWpJMFlXSTVNRGMyTnprM1l6WXdNamMxT1dJM1lqUmtaV00wTWpFeFpURTBZVGsxWXpCaE1qVXdZakpoTVRabVpESXdNalpqTXdBTU0wTkNRWFZ2YVZsVE0zTTlBQVIxY3pBeSIsImV4cCI6MTU5MzE0MTQwMCwiaWF0IjoxNTkzMTM0MjAwLCJhaWQiOiJ2elgwa3BqY1NRbWpVNXVvdDlLeDZBIiwiY2lkIjoiIn0.l-JHF3U0FMLprd67TvJOpo0KpNAcxnWY3T40Inmkm9I', 'join_url': 'https://us02web.zoom.us/j/83785232253?pwd=REQxSUxXQlY1WnB0TlQvZk1YTzhvdz09', 'password': '9Gj26D', 'h323_password': '943391', 'pstn_password': '943391', 'encrypted_password': 'REQxSUxXQlY1WnB0TlQvZk1YTzhvdz09', 'settings': {'host_video': False, 'participant_video': False, 'cn_meeting': False, 'in_meeting': False, 'join_before_host': False, 'mute_upon_entry': False, 'watermark': False, 'use_pmi': False, 'approval_type': 2, 'audio': 'voip', 'auto_recording': 'none', 'enforce_login': False, 'enforce_login_domains': '', 'alternative_hosts': '', 'close_registration': False, 'registrants_confirmation_email': True, 'waiting_room': True, 'registrants_email_notification': True, 'meeting_authentication': False}}
