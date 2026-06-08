class Student:
    def __init__(self,name,student_no,course):
        self.name = name
        self.student_no = student_no
        self.course = course

    def study(self,unit):
        print(f"{self.name} studies {unit}")

    def sleeps(self,time):
        print(f"{self.name} sleeps at {time}")

    def eats(self,food):
        print(f"{self.name} eats {food}")

    def get_details(self):
        print("User details")
        print(f"Name:{self.name} - Student No:{self.student_no} - Course:{self.course}")
        print("---------------------------------")


#object 1
student1 = Student("Jack","S101","Computer Science")
print(type(student1))
print(student1)
student1.get_details()
student1.study("Web Development")
student1.sleeps("10pm")
student1.eats("apples")


#object 2
student2 = Student("Jane","S102","Data Science")
print(type(student2))
student2.get_details()
student2.study("OOP")
student2.sleeps("11pm")
student2.eats("cake")


# TASK
# TASK1
class BankAccount:
    def __init__(self, account_number, owner_name, balance, date_opened):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.date_opened = date_opened

# TASK2

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds")

    def check_balance(self):
        print(f"Balance: {self.balance}")

    def display_info(self):
        print(f"Account: {self.account_number}, Owner: {self.owner_name}, Balance: {self.balance}, Opened: {self.date_opened}")

    def close_account(self):
        self.balance = 0
        print(f"Account {self.account_number} closed. Balance set to 0.")


# TASK3
acc1 = BankAccount("A101", "Alice", 500, "2024-01-10")
acc2 = BankAccount("A102", "Bob", 1000, "2024-02-15")

# ACC1
acc1.deposit(200)
acc1.withdraw(100)
acc1.check_balance()
acc1.display_info()
acc1.close_account()

# ACC2
acc2.deposit(50)
acc2.withdraw(300)
acc2.check_balance()
acc2.display_info()
acc2.close_account()
