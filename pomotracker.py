import time

# Constants (Seconds)
TESTTIME = 5        # 5 Seconds
WORKTIME = 1500     # 25 Minutes
SHORTBREAK = 300    # 5 Minutes
LONGBREAK = 600     # 10 Minutes

# countdown counts down from given runTime
def countdown(runTime):
    while runTime:
        mins, secs = divmod(runTime, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end="\r")
        time.sleep(1)
        runTime -= 1
    print("Time up!")

# scheduler runs the specified timing approach. Maybe configurable one day, but these are pretty standard for pomodoro applications 
def scheduler(timerType):
    if timerType == "test":
        print("Running a test")
        countdown(TESTTIME)
    elif timerType == "shortBreak":
        countdown(SHORTBREAK)
    elif timerType == "longBreak":
        countdown(LONGBREAK)
    elif timerType == "standard":
        countdown(WORKTIME)
        countdown(SHORTBREAK)
        countdown(WORKTIME)
        countdown(SHORTBREAK)
        countdown(WORKTIME)
        countdown(SHORTBREAK)
        countdown(WORKTIME)
        countdown(LONGBREAK)

# Pomotracker will allow for categorization and lead into data saving (and loading?)
# def pomotracker():

def main():
    reply = ""
    while reply.lower() != "q":
        timerType = ""
        print("(S)tandard Cycle, Short (b)reak, (l)ong Break, (t)est, or (q)uit:")
        reply = input("Please enter a selection >> ")
        if reply.lower() == "s":
            timerType = "standard"
        elif reply.lower() == "b":
            timerType = "shortBreak"
        elif reply.lower() == "l":
            timerType = "longBreak"
        elif reply.lower() == "t":
            timerType = "test"
        scheduler(timerType)
    exit()


if __name__ == "__main__":
    main()