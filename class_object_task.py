
def finance_manager():
    name = input('Enter your Fullname: \n')
    print(f'****** Welcome {name} To Your Personal Finance Manager ******')
    income = input('What is your monthly income: \n')


class Budget:
    name = []
    balance = {}

    def __init__(self, budget_name, balance):
        self.budget_name = budget_name
        self.balance = balance
        self.budget_balance()

    def budget_balance(self):
        Budget.balance[self.budget_name] = self.balance
        return Budget.balance

    def deposit(self, deposit):
        self.balance += deposit
        self.budget_balance()
        return self.balance

    def withdrawal(self, withdraw):
        if withdraw < self.balance:
            self.balance -= withdraw
            self.budget_balance()
            return self.balance
        else:
            print("Insufficient Funds")

    def transfer_balance(self, other, amount):
        if amount <= self.balance:
            other.deposit(amount)
            self.withdrawal(amount)

        else:
            print("Insufficient Balance")

    def __repr__(self):
        return f"Available {self.budget_name} balance is {self.balance}"


