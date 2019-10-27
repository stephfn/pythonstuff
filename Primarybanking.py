
# Python program to create Bankaccount class 
# Your program will create an object of each type (CheckingAccount & SavingsAccount)
# You will need to run the program twice.  Once with the account balance of $100 and once with the account balance of $25.
#  Since the second run of the program will have a balance lower than the minimum balance
# a message should be output letting the user know that their account is below the minimum balance
class Bank_Account:
	# attributes= account number & balance
	# Functions= withdrawal, deposit, getbalance
	
    def __init__(self, checkingbalance=100, account=123456, savingsbalance=60):
        self.balance=checkingbalance
        self.account=account
        print("Welcome to Online Banking")
        print("\n Your account number is:",                             account)
        print("\n Your checking account balance is:        $",checkingbalance, "USD")
        print("\n Your savings account balance is:          $",savingsbalance, "USD")
        
    def deposit(self): 
        amount=float(input("\n Enter amount to be deposited into Checking: ")) 
        self.balance += amount
        print("\n Amount Deposited....................:+$ ",amount,"USD")

    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn from Checking: ")) 
        if self.balance>=amount: 
            self.balance-=amount
             
            print("\n You Withdrew........................:-$ ", amount,"USD") 
        else: 
            print("\n Insufficient balance  ")
             
  
    def display(self): 
        print("\n Net Available Checking Balance................:$ ",self.balance,"USD")

		
class Checking(Bank_Account):
	#Represents attributes of the child class checking account.
	# attributes =(fees$5 & min balance), Functions(deductfees, checkminbal)
	def __init__(self, balance=100):
		
		#Initialize attributes of parent class
		
		super().__init__(balance)


class InterestSavings(Bank_Account):
	#Represents aspects of a savings account
	# attributes = interest rate, functions=add interest rate
	def __init__(self, balance=60, rate=0):
		self.balance = 100
		self.rate = 0.02
	def add_interest(self):
		self.balance * self._rate
		
	
 
   
# creating an object of class 
s = Checking()
s = InterestSavings()

# Calling functions with that class object 
s.deposit() 
s.withdraw() 
s.display() 


