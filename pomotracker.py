import time

# Constants (Seconds)
TESTTIME = 5        # 5 Seconds
WORKTIME = 1500     # 25 Minutes
SHORTBREAK = 300    # 5 Minutes
LONGBREAK = 600     # 10 Minutes

# Pomotimer counts down from given runTime
def pomotimer(runTime):
    while runTime:
        mins, secs = divmod(runTime, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end="\r")
        time.sleep(1)
        runTime -= 1
    print("Time up!")

def workLoop(workType):
    if workType == "test":
        print("Running a tst")
        pomotimer(TESTTIME)
    elif workType == "shortBreak":
        pomotimer(SHORTBREAK)
    elif workType == "longBreak":
        pomotimer(LONGBREAK)
    elif workType == "standard":
        pomotimer(WORKTIME)
        pomotimer(SHORTBREAK)
        pomotimer(WORKTIME)
        pomotimer(SHORTBREAK)
        pomotimer(WORKTIME)
        pomotimer(SHORTBREAK)
        pomotimer(WORKTIME)
        pomotimer(LONGBREAK)

# Pomotracker will allow for categorization and lead into data saving (and loading?)
# def pomotracker():

def main():
    reply = ""
    while reply.lower() != "q":
        workType = ""
        reply = input("Press S to start a standard cycle >> ")
        if reply.lower() == "s":
            workType = "standard"
        elif reply.lower() == "b":
            workType = "shortBreak"
        elif reply.lower() == "l":
            workType = "longBreak"
        elif reply.lower() == "t":
            workType = "test"
        workLoop(workType)
    exit()


if __name__ == "__main__":
    main()