from abc import ABC, abstractmethod

class car(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ",amount)
        @abstractmethod #will allow amount to be passed no matter the type of data is in it
        def payment(self,amount):
            pass

class DebitCardPayment(car):
#defining how to implement the payment function from its parent paySlip class
    def payment(self, amount):
        print("Your purchase amount of {} exceeded your $100 limit.".format(amount))

obj = DebitCardPayment()
obj.paySlip("$400")
obj.payment("$400")
