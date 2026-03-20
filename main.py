# 1 - bank account 
# 2 - deposit money 
# 3 - withdraw money 
# 4 - details 
# 5 - update details
# 6 - delete account 

import json
import random 
import string 
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exists")
    except Exception as err:
        print(f"an exception occures as {err}")
        
    @staticmethod
    def update():
        with open(Bank.database, 'w') as fs:
                fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)



    def CreateAccount(self):
        info = {
            "name" : input("enter your name - "),
            "age" : int(input("enter your age - ")),
            "email" : input("enter your email - "),
            "pin" : int(input("set your pin - ")),
            "accountNumber" : Bank.__accountgenerate(),
            "balance" : 0
        }
        if info['age'] < 18 or len(str(info['pin'])) != 4 :
            print("sorry you cannot create your account")
        else:
            print("account has been created successfuly")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number")
        Bank.data.append(info)
        Bank.update()
    

    def depositMoney(self):
        accNumber = input("enter your account number - ")
        pin = int(input("ente your pin - "))
        userData = [i for i in Bank.data if i['accountNumber'] == accNumber and i['pin'] == pin]
        if userData == False:
            print("sorry no data found")

        else:
            amount = int(input("how much amount do you want to deposit"))
            if amount > 10000:
                print("sorry amount too high deposit below 10000")
            else:
                userData[0]['balance'] += amount    
                Bank.update()
                print("Money successfuly deposited")



    def withdrawMoney(self):
        accNumber = input("enter your account number - ")
        pin = int(input("enter your pin - "))
        userData = [i for i in Bank.data if i['accountNumber'] == accNumber and i['pin'] == pin]
        if userData == False:
            print("sorry no data found")

        else:
            amount = int(input("how much amount do you want to withdraw"))
            if userData[0]['balance'] < amount:
                print("sorry you don't have that much balance")
            else:
                userData[0]['balance'] -= amount    
                Bank.update()
                print("Money successfuly withdrawn")            

    def checkDetails(self):
        accNumber = input("enter your account number - ")
        pin = int(input("enter your pin - "))
        userData = [i for i in Bank.data if i['accountNumber'] == accNumber and i['pin'] == pin]
        if userData == False:
            print("sorry no data found")

        else:
            for key,value  in userData[0].items():
                print(f"{key} : {value}")
            print("all details shown successfuly")


    def updateDetails(self):
        accNumber = input("enter your account number - ")
        pin = int(input("enter your pin - "))
        userData = [i for i in Bank.data if i['accountNumber'] == accNumber and i['pin'] == pin]
        if userData == False:
            print("sorry no data found")

        else:
            for key,value  in userData[0].items():
                print(f"{key} : {value}")
            key = input("enter the field to be updated - ")
            value = input("enter the updated value - ")
            userData[0][key] = value
            Bank.update()
            print("Successfuly updated")

    def deleteAccount():
        accNumber = input("enter your account number - ")
        pin = int(input("enter your pin - "))
        userData = [i for i in Bank.data if i['accountNumber'] == accNumber and i['pin'] == pin]
        reminder = input("are you sure you want to delete your account ? [yes/no]")
        if reminder == "yes":
            Bank.data.remove(userData[0])
            Bank.update()
            print("account deleted successfully")
        else:
            print("deletion cancelled")


user = Bank()
print("Press 1 for creating an account")
print("Press 2 for depositing money")
print("Press 3 for withdrawing money")
print("Press 4 for your details")
print("Press 5 for updating details")
print("Press 6 for deleting your account")

check = int(input("enter your response"))
if check == 1:
    user.CreateAccount()
elif check==2:
    user.depositMoney()
elif check==3:
    user.withdrawMoney()
elif check==4:
    user.checkDetails()
elif check==5:
    user.updateDetails()
elif check==6:
    user.deleteAccount()
else:
    print("invalid input, Try Again!")



