import time


# Default Times (Seconds)
TESTTIME = 5        # 5 Seconds
WORKTIME = 1500     # 25 Minutes
SHORTBREAK = 300    # 5 Minutes
LONGBREAK = 600     # 10 Minutes


# countdown counts down from given runTime, plays a terminal bell, and then waits for user input before starting the next countdown
def countdown(runTime):
    while runTime:
        mins, secs = divmod(runTime, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end="\r")
        time.sleep(1)
        runTime -= 1
    print('\a') # Terminal bell // TODO: bell sound effect? 
    print("\nTime up!\n")
    input("Press Enter to Continue >> ")
    # TODO: Print next time length?
    # TODO: Gentle nag with simpler bell effect until enter pressed?


# scheduler runs the specified timing approach. Maybe configurable one
# day, but these are pretty standard for pomodoro applications
def scheduler(timerType):
    if timerType == "test":
        tests = 2
        while tests > 0:
            print("Running a test")
            countdown(TESTTIME)
            tests -= 1
    elif timerType == "shortBreak":
        countdown(SHORTBREAK)
    elif timerType == "longBreak":
        countdown(LONGBREAK)
    elif timerType == "standard":
        # TODO: number of shortbreaks before long break as parameter?
        shortbreaks = 4
        while shortbreaks > 0:
            countdown(WORKTIME)
            countdown(SHORTBREAK)
            shortbreaks -= 1
        countdown(LONGBREAK)        
        # TODO: Math schedule with gentle nudge halfway through worktime, but
        # does not stop timer?
        # TODO: Counting out and printing number of works/breaks/cycles
        # TODO: interrupt/skip current countdown, set next manually?


# Pomotracker will allow for categorization and lead into data saving (and
# loading?)
# def pomotracker():
# TODO: Figure out categorizing and counting cycles per that category
# TODO: Figure out file saving/loading
# TODO: Reporting? or just csv file and leave up to spreadsheet geekery?


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
        # TODO: Repeat previous timerType? Q to quit?
    exit()


if __name__ == "__main__":
    main()