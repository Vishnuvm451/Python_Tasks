# OOP Project: Bank Account Management System
# Scenario: A bank wants to develop a simple account management system where customers can create bank accounts, deposit money, withdraw money, and check their balances.

# This project combines three important OOP concepts:
# 1. Abstraction – Define rules that every bank account must follow.
# 2. Encapsulation – Protect account balance using private attributes, getters, and setters.
# 3. Inheritance – Create different types of bank accounts using a common parent class.
# 1. Project Requirements

# Task 1: Abstraction
# Create an abstract class called BankAccount.
# - It should have an abstract method called calculate_interest().
# - Every child class must implement this method.
# - The BankAccount class should not allow objects to be created directly.
# Task 2: Encapsulation
# Inside the BankAccount class, create these attributes:
# - account_holder – Public attribute.
# - _account_type – Protected attribute.
# - __balance – Private attribute.
# Implement:
# - A getter using @property to retrieve the balance.
# - A setter using @balance.setter to update the balance.
# - The setter must not allow negative balances.
# Task 3: Inheritance
# Create two child classes:

# 1. SavingsAccount
# - Inherit from BankAccount.
# - Set the account type to "Savings".
# - Implement calculate_interest() with a 5% annual interest rate.
# 2. CurrentAccount
# - Inherit from BankAccount.
# - Set the account type to "Current".
# - Implement calculate_interest() with a 2% annual interest rate.
# Both child classes must use super() to initialize their parent class.
# Task 4: Banking Operations
# The parent class should contain the following methods:
# - deposit(amount) – Add money to the account.
# - withdraw(amount) – Deduct money from the account if sufficient balance is available.
# - display_details() – Display account holder, account type, and current balance.
# Use the balance setter whenever the balance is updated.

# 2. Expected Output
# For testing, create the following accounts:
# - Customer 1: Ashbi, Savings Account, Initial balance ₹10,000.
# - Customer 2: Rahul, Current Account, Initial balance ₹20,000.
# Perform these operations:
# 1. Deposit ₹5,000 into Ashbi's account.
# 2. Withdraw ₹2,000 from Ashbi's account.
# 3. Deposit ₹3,000 into Rahul's account.
# 4. Withdraw ₹5,000 from Rahul's account.
# 5. Display both account details.
# 6. Calculate and display the annual interest for both accounts.	



# Deposit successful: Rs.5000
# Withdrawal successful: Rs.2000

# Deposit successful: Rs.3000
# Withdrawal successful: Rs.5000

# ---------- ACCOUNT DETAILS ----------

# Account Holder: Ashbi
# Account Type: Savings
# Balance: Rs.13000

# Account Holder: Rahul
# Account Type: Current
# Balance: Rs.18000

# ---------- ANNUAL INTEREST ----------

# Ashbi's Annual Interest: Rs.650.0
# Rahul's Annual Interest: Rs.360.0

#----------------------------------------------------------------------------------



from abc import ABC,abstractmethod

class BankAccount(ABC):

    def __init__(self,account_holder,account_type,balance):
        self.account_holder = account_holder
        self._account_type = account_type
        self.__balance = balance


    @abstractmethod
    def calculate_interest(self,account_holder,account_type,balance):
        pass


    @property
    def balance(self):
        return self.__balance


    @balance.setter
    def bank_balance(self,new_amt):
        if new_amt<0:
            raise "Amount cannot be Negative"
        
        self.__balance = new_amt

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return

        self.__balance += amount
        print(f"Deposited Amount: {amount}")


    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return

        if amount > self.__balance:
            print("Insufficient Balance")
            return

        self.__balance - amount
        print(f"Withdrawn Amount: {amount}")


class SavingsAccount(BankAccount):

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    
    def acc_type_change(self,acc_type_new):
        if acc_type_new == '' :
            raise 'Account type cannot be empty'
        
        self._account_type = acc_type_new

    def calculate_interest(self):
        # super().__init__(account_holder,account_type,balance)
        annual_interest = self.balance * (5/100)
        print(f'Ashbi Annual Interest (5%): {annual_interest}')

    def account_details(self):
        print('Account Holder :',self.account_holder)
        print('Account Type : ',self._account_type)
        print('Balance :',self.balance)
    

class CurrentAccount(BankAccount):

    @property
    def account_type(self):
        return self._account_type
    def bank_bal(self):
        return self.__balance

    @account_type.setter
    
    def acc_type_change(self,acc_type_new):
        if acc_type_new == '' :
            raise 'Account type cannot be empty'
        
        self._account_type = acc_type_new

    def calculate_interest(self):
        # super().__init__(account_holder,account_type,balance)
        annual_interest = self.balance * (2/100)
        print(f'Rahul Annual Interest (2%): {annual_interest}')


    def account_details(self):
        
        print('Account Holder :',self.account_holder)
        print('Account Type : ',self._account_type)
        print('Balance :',self.balance)


cust_1 = SavingsAccount('ashbi','savings',10000)
cust_2 = CurrentAccount('rahul','current',20000)

print(' ')
cust_1.deposit(5000)
cust_1.withdraw(2000)
print(' ')
cust_2.deposit(5000)
cust_2.withdraw(2000)
print(' ')
print(' ---------- ACCOUNT DETAILS ----------')
cust_1.account_details()
cust_2.account_details()
print(' ')
print('---------- ANNUAL INTEREST ----------')
cust_1.calculate_interest()
cust_2.calculate_interest()



# 2. Expected Output
# For testing, create the following accounts:
# - Customer 1: Ashbi, Savings Account, Initial balance ₹10,000.
# - Customer 2: Rahul, Current Account, Initial balance ₹20,000.


# Perform these operations:
# 1. Deposit ₹5,000 into Ashbi's account.
# 2. Withdraw ₹2,000 from Ashbi's account.
# 3. Deposit ₹3,000 into Rahul's account.
# 4. Withdraw ₹5,000 from Rahul's account.
# 5. Display both account details.
# 6. Calculate and display the annual interest for both accounts.	



# Deposit successful: Rs.5000
# Withdrawal successful: Rs.2000

# Deposit successful: Rs.3000
# Withdrawal successful: Rs.5000

# ---------- ACCOUNT DETAILS ----------

# Account Holder: Ashbi
# Account Type: Savings
# Balance: Rs.13000

# Account Holder: Rahul
# Account Type: Current
# Balance: Rs.18000

# ---------- ANNUAL INTEREST ----------

# Ashbi's Annual Interest: Rs.650.0
# Rahul's Annual Interest: Rs.360.0

#----------------------------------------------------------------------------------