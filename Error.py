from breezypythongui import EasyFrame
import math

def computeSqrt(self):
    EasyFrame.__intit__(self)
    """Inputs the integer, computers the square root,
    and outputs the result. Handles input errors
    by displaying a message box."""
    try:
        number = self.inputField.getNumber()
        result = math.sqrt(number)
        self.outputField.setNumber(result)
    except ValueError:
        self.messageBox(title = "ERROR",
                        message = "Input must be an integer >= 0")

def main():
    computeSqrt().mainloop()

if __name__=="__main__":
    main()
