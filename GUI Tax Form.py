from breezypythongui import EasyFrame

class TaxCalculator(EasyFrame):
    """Income tax"""
    def __init__(self):
        EasyFrame.__init__(self, title = "Tax Calculator")
  
        # Income
        self.addLabel(text = "Gross Income",
                      row = 0, column = 0)
        self.incomeField = self.addFloatField(value = 0.0,
                                              row = 0,
                                              column = 1)
 
        # Dependents
        self.addLabel(text = "Dependents",
                      row = 1, column = 0)
        self.depField = self.addIntegerField(value = 0, row = 1, column = 1)

        # The command button
        self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.computeTax)
 
        # Tax
        self.addLabel(text = "Total tax",
                      row = 4, column = 0)
        self.taxField = self.addFloatField(value = 0.0, row = 4, column = 1, precision = 2)
  
    # The event handler method for the button
    def computeTax(self):
        
        income = self.incomeField.getNumber()
        numDependents = self.depField.getNumber()
        exemptionAmount = self.exeField.getNumber()
        tax = (income - numDependents * exemptionAmount) * .15
        self.taxField.setNumber(tax)

def main():
     TaxCalculator().mainloop()

if __name__=="__main__":
    main()
