import rumps
import time

class LunchTimer(rumps.App):

    @rumps.clicked("Start Timer")
    def sayhi(self, _):
        time.sleep(3)
        rumps.notification("Timer Complete", "Time to clock back in!", "It has been 29 minutes, get ready to clock in!")

if __name__ == "__main__":
    app = LunchTimer("Lunch Timer", icon='./timer.png')
    # Icon made by Freepik (https://www.flaticon.com/authors/freepik) from Flaticon (https://www.flaticon.com/)
    app.run()

