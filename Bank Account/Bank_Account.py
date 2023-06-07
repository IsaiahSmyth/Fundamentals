class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
      self.int_rate = int_rate
      self.balance = balance
      
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
      self.balance = self.balance + amount
        # your code here
    def withdraw(self, amount):
      self.amount = self.amount - amount
        # your code here
    def display_account_info(self):
      print("Your balance is: " + str(self.balance))
        # your code here
    def yield_interest(self):
      self.balance = self.balance * self.int_rate
        # your code here

# Create a BankAccount class with the attributes interest rate and balance

# Add a deposit method to the BankAccount class

# Add a withdraw method to the BankAccount class

# Add a display_account_info method to the BankAccount class

# Add a yield_interest method to the BankAccount class

# Create 2 accounts
class Account1:
  def __int__(self, int_rate, balance):
    self.int_rate = int_rate
    self.balance = balance
  def deposit(self, amount):
    self.balance = self.balance + amount
  def withdraw(self, amount):
    self.amount = self.amount - amount
  def display_account_info(self):
    print("Your balance is: " + str(self.balance))
  def yield_interest(self):
    self.balance = self.balance * self.int_rate
  
class Account2:
  def __int__(self, int_rate, balance):
    self.int_rate = int_rate
    self.balance = balance
  def deposit(self, amount):
    self.deposit = self.balance + amount
  def withdraw(self, withdraw):
    self.withdraw = self.balance - withdraw
  def display_account_info(self):
    print("Your balance is: " + str(self.balance))
  def yield_interest(self):
    self.balance = self.balance * self.int_rate

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
    Account1.deposit(500)
    Account1.deposit(500)
    Account1.deposit(500)
    Account1.withdraw(500)

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
    Account2.deposit(500)
    Account2.deposit(500)
    Account2.withdraw(500)
    Account2.withdraw(500)
    Account2.withdraw(500)
    Account2.withdraw(500)

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info in a nice format!  
    print(Account1.display_account_info())
    print(Account2.display_account_info())
    