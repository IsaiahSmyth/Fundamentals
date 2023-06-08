class user:
# Create a User class with an __init__ method
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# Add a make_deposit method to the User class that calls on it's bank account's instance methods.
    def make_deposit(self, amount):
        self.bank_account.deposit(amount)
    
# Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.
    def with_draw(self, amount):
        self.bank_account.with_draw(amount)

# Add a display_user_balance method to the User class that displays user's account balance
    def display_user_balance(self):
        print(f"{self.name}'s balance is {self.bank_account.balance}")

# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to
    def checking_account(self, amount):
        self.bank_account.checking_account.deposit(amount)
    def savings_account(self, amount):
        self.banck_account.savings_account.deposit(amount)

# SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.
    def transfer_money(self, amount, other_user):
        self.bank_account.withdraw(amount)
        self.bank_account.deposit(amount)