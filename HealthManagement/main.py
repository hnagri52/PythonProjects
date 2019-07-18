from datetime import datetime as dt

def currentTime():
    """Logs the current time"""
    return str(dt.now())
patients = ["Hussein", "JY", "Ahmed"]
activities = ["Exercise", "Diet"]
running = "True"


while running == "True" or running == "T" or running == "t":
    print("Here is a list of all of the patients names we have records on: ")
    for name in patients:
        print(name)
    name = input("Enter the patient name, or add a patient: ")
    print("Here is a list of all of the activities we have records on: ")
    for activity in activities:
        print(activity)
    want = input("Enter the activity, or add an activity: ")
    if name not in patients:
        patients.append(name)
    if want not in activities:
        activities.append(want)
    with open(name + want + ".txt", "a+") as op:
        command = input("Would you like to read or add an activity? ")
        if (command == "read"):
            op.seek(0)
            ls = op.readlines()
            for line in ls:
                print(line)
        elif (command == "add"):
            text = input("Enter what you want to add? ")
            op.write(currentTime() + " " + text + "\n");
    running = input("Would you like to continue(True/False): ")

