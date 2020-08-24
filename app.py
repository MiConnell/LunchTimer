import rumps
import time
import datetime

class LunchTimer(rumps.App):

    @rumps.clicked("Start Timer")
    def sayhi(self, _):
        time.sleep(3)
        rumps.notification("Timer Complete", "Time to clock back in!", "It has been 29 minutes, get ready!")

if __name__ == "__main__":
    LunchTimer("Awesome App").run()

