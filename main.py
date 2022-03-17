

class func():
    def __init__(self):

        
        try:
            account_code = input("please enter your account code: ")
            account_code = int(account_code)
        except Exception:
            print("Please enter your values correctly")
            func()
        try:
            name = input("Enter your UserName: ")
            name = str(name)
        except Exception:
            print("Please enter your values correctly")
            func()
        try:
            account_num = input("Enter your Account Number: ")
            account_num = int(account_num)
        except Exception:
            print("Please enter your values correctly")
            func()
        
        password = input("Please enter your Password: ")
            # passward can int or str
        


        self.balance = 5000

        def withdraw():
            try:
                m = input("How much money do you want to withdraw: ")
                m = int(m)
            except Exception:
                print("Please submit a valid value")
                withdraw()
            self.balance = self.balance - m
            print(f"You have withdraw ${ m }\n Your remaining balance is {self.balance}")
            with open('data.txt', 'a+') as data:
                data.write(f"You have withdraw ${ m } \n")
            return ano_run()


        def deposit():
            try:
                m = input("How much money do you want to deposit: ")
                m = int(m)
            except Exception:
                print("Please submit a valid value")
                deposit()

            self.balance = self.balance + m
            print(f"You have deposit ${ m }\n Your current balance is {self.balance}")
            with open('data.txt', 'a+') as data:
                data.write(f"You have deposit ${ m } \n")
            return ano_run()


        if name == "john" and account_num == 54321 and password == "master" and account_code == 1:
            def ano_run():
                i = input("What do you want to do \n 1. Withdraw \n 2. Deposit\n=>")
                i = i.lower()
                if i == "withdraw":
                    withdraw()
                elif i == "deposit":
                    deposit()
                elif name == "exit" or account_num or "exit" or password == "exit" or account_code == "exit":
                    while True:
                        break
                else:
                    ano_run()
            ano_run()
    
        else:
            print("Try again")
            func()

func()













































