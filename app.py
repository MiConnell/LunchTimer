# Icons made by Freepik (https://www.flaticon.com/authors/freepik) from Flaticon (https://www.flaticon.com/)
import rumps
import time

class LunchTimer(rumps.App):

    @rumps.clicked("Start Timer")
    def sayhi(self, _):
        time.sleep(1770) # 29 minutes and 30 seconds
        rumps.notification("Timer Complete", None, "It has been 29 minutes, get ready to clock in!",icon='./complete.png')

if __name__ == "__main__":
    app = LunchTimer("Lunch Timer", icon='./timer.png')
    app.run()

