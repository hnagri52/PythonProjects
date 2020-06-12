from calEvent import CalEvent
import datetime


def main():
    #obtain user input for desc and start date
    desc = input("Hey! Please enter a description of the event that you want to schedule!")
    theNewEvenet  = CalEvent(desc)

    # validate and add the start date
    start_date = input("Please enter the start date (YYYY-MM-DD): ")
    theNewEvenet.validate_and_add(start_date, "start")

    # validate and add the end date
    end_date = input("Please enter the end date (YYYY-MM-DD): ")
    theNewEvenet.validate_and_add(end_date, "end")
    the_deets = {"start_date": theNewEvenet.start_date,
                "desc": theNewEvenet.desc,
                "end_date": theNewEvenet.end_date}
    theNewEvenet.schedule_meeting(the_deets)


if __name__ == '__main__':
    main()