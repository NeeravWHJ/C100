class Atm :
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balanceenquiry(self):
        print("Your Balance is $100")

    def withdraw(self,amount):
        new_amount = 100-amount
        print("You withdrawed : " + str(amount) + "Your remaining balance is : " + str(new_amount))

def main():
        name = input("Hello! What is your name : ")
        print("Hello " + name)
        cardnumber = input("Insert your card number : ")
        pin = input("Enter your pin : ")
        user = Atm(cardnumber,pin)

        print("Choose your activity")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        activity = int(input("Enter activity choice : "))

        if(activity == 1):
            user.balanceenquiry()
        elif(activity == 2):
            amount = int(input("Enter the amount : "))
            user.withdraw(amount)
        else:
            print("Enter a valid amount")        

main()

        