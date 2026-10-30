from abc import ABC, abstractmethod

# Abstract class
class Payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


# First subclass
class CreditCardPayment(Payment):

    def process_payment(self, amount):
        print(f"Payment of ₹{amount} processed using Credit Card.")


# Second subclass
class UPIPayment(Payment):

    def process_payment(self, amount):
        print(f"Payment of ₹{amount} processed using UPI.")


# Test all classes
credit = CreditCardPayment()
upi = UPIPayment()

credit.process_payment(1000)
upi.process_payment(500)