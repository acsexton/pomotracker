## Temple Bell by Mike Koenig (via http://soundbible.com/1496-Japanese-Temple-Bell-Small.html)
# under Attribution 3.0 (https://creativecommons.org/licenses/by/3.0/us/)

import time
from playsound import playsound
from enum import Enum

# Default Times in seconds
SECONDS_5 = 5
MINUTES_5 = 300  # 5 Minutes
MINUTES_15 = 900  # 15 Minutes
MINUTES_25 = 1500  # 25 Minutes

# Sound Files
BREAK_SOUND = 'temple_bell.mp3'


class Timers(Enum):
    # Default work time, number of work cycles/shortbreaks between long breaks
    TESTER = [SECONDS_5, 1]
    BREAK_SHORT = [MINUTES_5, 1]
    BREAK_LONG = [MINUTES_15, 1]
    WORK_CYCLE = [MINUTES_25, 3]


def timer_complete(sound=BREAK_SOUND):
    playsound(sound)
    print("\nTime up!\n")


class Timer:
    def __init__(self, seconds):
        self.seconds = seconds

    def tick(self):
        mins, secs = divmod(self.seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(time_format, end="\r")
        time.sleep(1)
        self.seconds -= 1

    def countdown(self):
        while self.has_time():
            self.tick()
        timer_complete()

    def has_time(self):
        return self.seconds != 0


class PomoTracker:

    # TODO: Vary number of cycles?
    # TODO: Counting out and printing number of works/breaks/cycles
    # TODO: interrupt/skip current countdown, set next manually?

    def __init__(self, timer_type):
        default_work_index = 0
        work_cycles_index = 1

        self.timer_type = timer_type
        self.work_time = timer_type.value[default_work_index]
        self.work_cycles = timer_type.value[work_cycles_index]

    def get_to_work(self):
        input("Press enter to start work...")
        work_timer = Timer(self.work_time)
        work_timer.countdown()

    def take_short_break(self):
        input("Press enter to start a short break...")
        short_break_timer = Timer(MINUTES_5)
        short_break_timer.countdown()

    def take_long_break(self):
        input("Press enter to start a long break...")
        long_break_timer = Timer(MINUTES_15)
        long_break_timer.countdown()

    def run_cycles(self):
        while self.work_cycles > 0:
            self.get_to_work()
            self.take_short_break()
            self.work_cycles -= 1
        self.take_long_break()


def main():
    timer_type = None
    print("(S)tandard Cycle, Short (b)reak," +
          " (l)ong Break, (t)est, or (q)uit:")
    reply = input("Please enter a selection >> ")
    if reply.lower() == "s":
        timer_type = Timers.WORK_CYCLE
    elif reply.lower() == "b":
        timer_type = Timers.BREAK_SHORT
    elif reply.lower() == "l":
        timer_type = Timers.BREAK_LONG
    elif reply.lower() == "t":
        timer_type = Timers.TESTER
    else:
        exit(1)
    pomo_tracker = PomoTracker(timer_type)
    pomo_tracker.run_cycles()
    # TODO: CSV saving/loading
    # TODO: Reporting, categories and cycles per that category?


if __name__ == "__main__":
    main()
