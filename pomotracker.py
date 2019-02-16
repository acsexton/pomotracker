import time

# Constants (Seconds)
TESTTIME = 5
WORKTIME = 1500    
SHORTBREAK = 300
LONGBREAK = 600

def pomotimer(runTime):
    while runTime:
        mins, secs = divmod(runTime, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end="\r")
        time.sleep(1)
        runTime -= 1
    print("Time up!")

def main():
    while True:
        pomotimer(TESTTIME)

if __name__ == "__main__":
    main()