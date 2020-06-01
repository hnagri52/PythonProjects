from calEvent import CalEvent

def main():
    desc = input("Hey! Please enter a description of the event that you want to schedule!")
    theNewEvenet  = CalEvent(desc)

    print(theNewEvenet.desc)


if __name__ == '__main__':
    main()