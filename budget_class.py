class Budget:
    def __init__(self, **kwargs):
        self.categories = kwargs

    def __repr__(self):
        return f"Available balance per category {self.categories}"

    def check_balance(self, category):
        return self.categories[category]

    def _rename_key_(self, category, new_name):
        self.categories[new_name] = self.categories.pop(category)

    def add_category(self, **kwargs):
        self.categories.update(kwargs)

    def deposit(self, deposit_amount, category):
        self.categories[category] += deposit_amount

    def withdraw(self, withdrawal_amount, category):
        if withdrawal_amount <= self.categories[category]:
            self.categories[category] -= withdrawal_amount

        else:
            print("Insufficient Funds")

    def transfer(self, amount, category_to_debit, category_to_credit):
        if amount <= self.categories[category_to_debit]:
            self.withdraw(amount, category_to_debit)
            self.deposit(amount, category_to_credit)

        else:
            print("Insufficient Balance")

    def inter_budget_transfer(self, other, amount, category_to_debit, category_to_credit):
        if amount <= self.categories[category_to_debit]:
            self.withdraw(amount, category_to_debit)
            other.deposit(amount, category_to_credit)

        else:
            print("Insufficient Balance")


def add_cat_to_budget(budget_name):
    try:
        category = input("Enter the name of the category eg Food:\n")
        amount = float(input("How much would you like to allocate:\n"))
        budget_name.add_category(category=amount)
        budget_name._rename_key_('category', category)

    except ValueError:
        print("Please Enter A Valid Number \n")


def cat_creator():
    try:
        category = input("Enter the name of the category eg 'Food', 'transport':\n")
        amount = float(input("How much would you like to allocate:\n"))
        budget_name = Budget(category=amount)
        budget_name._rename_key_('category', category)

        return budget_name

    except ValueError:
        print("Please Enter A Valid Number \n")
        cat_caller()


def cat_loop(budget_name):
    b = budget_name
    try:

        res = input('\nWould you like to add another category? yes[1] or no[2]\n')

        if res == '1':
            add_cat_to_budget(b)
            cat_loop(b)

        elif res == '2':
            print("You have successfully created your budget!")
            print(b)
            # return budget_name

        else:
            print('You have selected an invalid option, enter 1 [yes] or 2 [no] ')
            cat_loop(b)

    except ValueError:
        print("Please Enter A Valid Number \n")
        cat_loop(b)

    return b

def cat_caller():
    budget_name = cat_creator()
    print(budget_name)
    budget_name = cat_loop(budget_name)

    return budget_name


def deposit_operation(budget):
    try:
        category = input("Enter category:\n")
        amount = int(input("Enter amount to deposit:\n"))
        budget.deposit(amount, category)
        print(f'Successful!, Available {category} balance is ${budget.check_balance(category)}')
        response(budget)

    except ValueError:
        print("Please Enter A Valid Number \n")
        deposit_operation(budget)

    except KeyError:
        print("The category you have selected does not exist\n")
        deposit_operation(budget)


def withdrawal_operation(budget):
    try:
        category = input("Enter category:\n")
        amount = int(input("Enter amount to withdraw:\n"))
        budget.withdraw(amount, category)
        print(f'Successful!, Available {category} balance is ${budget.check_balance(category)}')
        response(budget)

    except ValueError:
        print("Please Enter A Valid Number \n")
        withdrawal_operation(budget)

    except KeyError:
        print("The category you have entered does not exist\n")
        withdrawal_operation(budget)


def inter_cat_transfer(budget):
    try:
        amount = int(input("Enter amount to transfer:\n"))
        category_to_debit = input("Enter category to debit:\n")
        category_to_credit = input("Enter category to credit:\n")
        budget.transfer(amount, category_to_debit, category_to_credit)
        print(budget)
        response(budget)

    except ValueError:
        print("Please Enter A Valid Number \n")
        inter_cat_transfer(budget)

    except KeyError:
        print("The category you have entered does not exist\n")
        inter_cat_transfer(budget)


def category_balance(budget):
    try:
        category = input("Enter category:\n")
        print(f"Available {category} balance is ${budget.check_balance(category)}")
        response(budget)

    except KeyError:
        print("The category you have entered does not exist\n")
        category_balance(budget)


def add_category(budget):
    add_cat_to_budget(budget)
    response(budget)

def budget_balance(budget):
    print(budget)
    response(budget)

def response(budget):
    print("\nWould You Like To Perform Another Transaction?")

    try:
        res = int(input(" 1 (Yes) or 2 (No): \n"))
        if res == 1:
            operations(budget)
        if res == 2:
            print("Enjoy The Rest Of Your Day!")
            exit()
        else:
            print("You Have Selected An Invalid Option, Try Again")
            response(budget)

    except ValueError:
        print("You Have Entered An Invalid Number")
        response(budget)


def operations(budget):
    print("The following options are available for managing your Budget:\n"
          "[1] Deposit Into A Category\n"
          "[2] Withdraw From A Category\n"
          "[3] Inter Category Transfer\n"
          "[4] Check Category Balance\n"
          "[5] Check Budget Balance\n"
          "[6] Add a new Category To The Budget\n"
          "[7] Exit\n"
          )

    try:
        option = int(input("Please Select An Option: \n"))

        if option == 1:
            deposit_operation(budget)

        elif option == 2:
            withdrawal_operation(budget)

        elif option == 3:
            inter_cat_transfer(budget)

        elif option == 4:
            category_balance(budget)

        elif option == 5:
            budget_balance(budget)

        elif option == 6:
            add_category(budget)

        elif option == 7:
            print(f"Goodbye")

        else:
            print("Invalid Option Selected, Please Try Again \n")
            operations(budget)

    except ValueError:
        print("You Have Entered An InValid Number, Try Again \n")


def budget_planner():
    name = input("What is your fullname?\n")
    print(f'Welcome {name} to your Budget manager\n')
    print("What categories would like to budget for?")
    budget = cat_caller()
    operations(budget)


if __name__ == '__main__':
    budget_planner()
