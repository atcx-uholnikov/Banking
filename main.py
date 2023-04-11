"""
Parent Class - User:
- Holds details about the user
- Has a functions to show user details

Child Class - Bank:
- Stores the info about the account balance
- Stores details about the amount
- Allows to deposits.withdraw.balance_info
"""

#Parent Class
class Client():

    # Holds details about the Client
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    #Functions to show Client details
    def client_details(self):
        print("Personal Details")
        print("")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

#Child Class
class Bank(Client):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender) #avoids to repeat lines of code (lines №№ 17-19)
        self.balance = 0

    #Put some amount to an account (balance)
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f"Accont balance has been updated: $ {self.balance}")

    #Spend some amount from an account (balance)
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print(f"Insufficient Funds. Your balance is: $ {self.balance}")
        else:
            self.balance = self.balance - self.amount
            print(f"Your balance has been updated after a withdraw: $ {self.balance}")

    #Sows Client`s info and a balance
    def balance_info(self):
        self.client_details()
        print(f"The balance is: $ {self.balance}")

if __name__ == "__main__":
    #Creating new Client using Client class
    person1 = Client("Gene", 36, "Male")
    person1.client_details()

    #Creating new Client using Bank class (becouse Bank it`s child class of Client)
    person2 = Bank("Gail", 35, "female")
    person2.client_details()

    #Put some amount on the account
    person2.deposit(20)
    person2.deposit(40)
    person2.deposit(26)

    #Spend some amount from the account
    person2.withdraw(10)

    #Show the Client`s info and current balance
    person2.balance_info()