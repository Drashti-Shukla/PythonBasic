# Implement a Python class for a basic banking system with methods for deposit, withdrawal, and checking the balance.
class Banking:
    def _int_(self, accountable, initial_balance):
        self.account_holder = accountable
        self.balance = initial_balance

    def deposit(self, amt):
        if amt > 0:
            self.balance += amt
            return f"Deposit of ${amt} successful. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdrawal(self, amt):
        if 0 < amt <= self.balance:
            self.balance -= amt
            return f"Withdrawal of ${amt} successful. New balance: ${self.balance}"
        else:
            return "Invalid Withdrawal amount."

    def check_bal(self):
        return f"Current balance for {self.account_holder}: ${self.balance}"


acc = Banking('abc',500)
print(acc.check_bal())
print(acc.deposit(200))
print(acc.withdrawal(50))
