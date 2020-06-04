from calEvent import CalEvent
import datetime


def main():
    #obtain user input for desc and start date
    desc = input("Hey! Please enter a description of the event that you want to schedule!")
    theNewEvenet  = CalEvent(desc)

    # validate and add the start date
    start_date = input("Please enter the start date (YYYY-MM-DD): ")
    theNewEvenet.validate_and_add(start_date, "start")

    print(theNewEvenet.start_date, theNewEvenet.desc)
if __name__ == '__main__':
    main()