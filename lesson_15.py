
# Task 1. Create a class Product with properties name, price, and quantity.
#  Create a child class Book that inherits from Product and adds a property author and a method called read.

class Product:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

class Book(Product):
    def __init__(self, name, price, quantity, author) -> None:
        super().__init__(name, price, quantity)
        self.author = author
    
    def read(self):
        return f'Let\'s read the book by the author {self.author} called {self.name}'

# Task 2. Create a class Restaurant with properties name, cuisine, and menu. 
# The menu property should be a dictionary with keys being the dish name and values being the price. 
# Create a child class FastFood that inherits from Restaurant and adds a property drive_thru 
# (a boolean indicating whether the restaurant has a drive-thru or not) 
# and a method called order which takes in the dish name and quantity and returns the total cost of the order. 
# The method should also update the menu dictionary to subtract the ordered quantity from the available quantity. 
# If the dish is not available or if the requested quantity is greater than the available quantity, 
# the method should return a message indicating that the order cannot be fulfilled.

class Restaurant:
    def __init__(self, name: str, cuisine: str, menu: dict[str, dict[str, int]]) -> None:
        self._name = name
        self._cuisine = cuisine
        self._menu = menu


# Поменять проверку на None в методе order
class FastFood(Restaurant):
    def __init__(self, name: str, cuisine: str, menu: dict[str, dict[str, int]], drive_thru: bool) -> None:
        super().__init__(name, cuisine, menu)
        self.__drive_thru = drive_thru

    def order(self, dish_name, quantity):
        if (dish_name not in self._menu) or quantity > self._menu[dish_name]['quantity']:
            return 'The order cannot be fulfilled'
        else:
            self._menu[dish_name]['quantity'] -= quantity
            total_price = self._menu[dish_name]['price'] * quantity
            return total_price

menu =  {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

rest1 = FastFood('Name', 'Italiano', menu, False)
# print(rest1._FastFood__drive_thru)

# A Bank

class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number
    
    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance
    
    def get_account_number(self):
        return self._account_number
    
    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'

# A. Using the Account class as a base class, write two derived classes called SavingsAccount and CurrentAccount. 
# A SavingsAccount object, in addition to the attributes of an Account object, should have an interest attribute 
# and a method which adds interest to the account. A CurrentAccount object, in addition to the attributes of an Account object, 
# should have an overdraft limit attribute.

class SavingsAccount(Account): 
    def __init__(self, balance, account_number, interest):
        super().__init__(balance, account_number)
        self._interest = interest
    
    def add_interest(self):
        self._balance *= 1 + self._interest / 100

    def __str__(self):
        return 'Savings ' + super().__str__()
        

class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self.overdraft_limit = overdraft_limit

    def __str__(self):
        return 'Current ' + super().__str__()

# B. Now create a Bank class, an object of which contains an array of Account objects. 
# Accounts in the array could be instances of the Account class, the SavingsAccount class, or the CurrentAccount class. 
# Create some test accounts (some of each type).

# C. Write an update method in the Bank class. It iterates through each account, updating it in the following ways: 
# Savings accounts get interest added (via the method you already wrote); CurrentAccounts get a letter sent if they are in overdraft. 
# (use print to 'send' the letter).

# D. The Bank class requires methods for opening and closing accounts, and for paying a dividend into each account.

class Bank:
    def __init__(self, acc_arr: list[Account] = []) -> None:
        self._acc_arr = acc_arr

    def open_account(self, account):
        self._acc_arr.append(account)

    def close_account(self, account):
        self._acc_arr.remove(account)

    def paying_dividend(self, account, dividend_value):
        # print(account.get_balance())
        account.deposit(dividend_value)
        # print(account.get_balance())

    def __str__(self) -> str:
        string = 'Account list: \n'
        for account in self._acc_arr:
            string += str(account)  + '\n'
        return string
    
    def update(self):
        for account in self._acc_arr:
            if "add_interest" in account.__dir__():
                account.add_interest()
            elif "Current" in str(account):
                if account._balance > account.overdraft_limit:
                    return 'Overdraft' 

            


bank1 = Bank()
bank1.open_account(Account(300, 123))
bank1.open_account(Account(500, 127))
bank1.open_account(Account(300000, 124))
bank1.open_account(Account(50, 120))
bank1.open_account(Account.create_account(333))
bank1.open_account(CurrentAccount(44444, 444, 10))
bank1.open_account(SavingsAccount(5555, 555, 10))
# print(bank1.paying_dividend(Account(300, 123), 300))




































