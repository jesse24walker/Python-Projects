
from breezypythongui import EasyFrame

class Bouncy(EasyFrame):
    """Income tax"""
    def __init__(self):
        EasyFrame.__init__(self, title = "Bouncing ball")
  
        # Height of ball-drop
        self.addLabel(text = "Enter the height from ball drop",
                      row = 0, column = 0)
        self.height = self.addIntegerField(value = 0, row = 0,
                                           column = 1, columnspan = 2)
 
        # First bouncing distance of ball
        self.addLabel(text = "Enter the height of ball bounce back first",
                      row = 1, column = 0)
        self.firstBounce = self.addIntegerField(value = 0, row = 1,
                                                column = 1, columnspan = 2)

        # Number of times ball bounced back
        self.addLabel(text = "Number of times ball bounced back",
                      row = 2, column = 0)
        self.numberOfTimes = self.addIntegerField(value = 0, row = 2,
                                                column = 1, columnspan = 2)
        # Button to calculate total distance
        self.addButton("Total Distance", row = 3, column = 0, command = self.calculate)

        # display total distance
        self.totalDistacne = self.addLabel(text = "", row = 4, column = 0)
  
    # The event handler method for the button
    def calculate(self):
        try:
            height = self.height.getNumber()
            bounceDist = self.firstBounce.getNumber()
            numOfTimes = self.numberOfTimes.getNumber()
            
            BouncingIndex = float(bounceDist) / float(height)
        except (ValueError, ZeroDivisionError):
            self.messageBox(title = "Error Message", message = "Invalid input")
            return

        distance = height + bounceDist
        for i in range(0, numOftimes - 1):
            bounceBackDist = bounceDist * BouncingIndex
            distance += bounceDist + bounceBackDist
            bounceDist = bounceBackDist
        text = "The total distance travelled by the ball is %.lf ft."&distance
        self.totalDistance["text"] = text

def main():
    Bouncy().mainloop()

if __name__=="__main__":
    main()
