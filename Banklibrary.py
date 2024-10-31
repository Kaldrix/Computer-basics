class BankAccount: #Defining the class
    def __init__(self, account_number):
        self.account_number = account_number #Introducing the self atribute of the account
        self.balance =0 #Assinging the balance 0 by default  


    def deposit(self, amount): #This defines the deposit action with its exceptions
        if amount > 0:
            self.balance=self.balance + amount
            print(f"You´ve deposited {amount}€")

        else:
            print("You can´t deposit negative numbers or 0. What are you doing?.")
            exit()

    def withdraw(self, amount): #Same, but with the action withdraw
        if amount > self.balance:
            print("Nope. You can´t extract more than what you have. For security reasons, the flow has been stopped")
            exit()

        if amount <= 0:
            print("That´s the same as doing nothing...")

        else:
            self.balance=self.balance - amount
            print(f"You´ve withdrown{amount}€")

    def get_balance(self): #Although I don´t think this is neccesary, it was asked so I did it.
        return self.balance

    def __str__(self): #Same as with the get_balance function
        return f"Account Number= #{self.account_number} Balance={self.balance}€"


