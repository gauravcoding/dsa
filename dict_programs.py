import logging
logging.basicConfig(level=logging.INFO)
dict1={"name":["Gaurav","Raman","Deepak"],
      "age":[21,22,23]}
dict2={1:2,3:9,5:24}
dict2.update(dict1)
logging.info(dict2)
logging.info(dict1.get("name"))


def generator(n):
      for i in range(1,n):
            yield i

gen=generator(10)
logging.info(next(gen))
logging.info(next(gen))


class Bankaccount:
      def __init__(self,name,acc,balance=0):
            self.name=name
            self.acc=acc
            self.balance=balance
      def credit(self,amount):
            self.amount=amount
            self.balance+=self.amount
      def debit(self,amount):
            self.amount=amount
            if self.amount<=self.balance:
                  self.balance-=self.amount
            else:
                  print("Insufficient Balance!")
      def ShowBalance(self):
            print(f"Hi {self.name} your account number that was ending with XXXX-{self.acc} has {self.balance} RS")
A1=Bankaccount("Gaurav",7419)
#A1.credit(10000)
A1.ShowBalance()
A1.debit(11000)
A1.ShowBalance()

class Internet_banking:
    def __init__(self, ID, Password):
        self.ID = ID
        self.__Password = Password

    def show_details(self):
        print(f"Your ID is {self.ID} and your password is {self.get_password()}")

    def get_password(self):
        return self.__Password

customer1 = Internet_banking("gaurav89", "Gaurav@122")
customer1.show_details()

def sum_marks(dict):
      sum_dict={}
      for name,values in dict.items():
            sum_dict[name]=sum(values)
      return sum_dict
result=sum_marks({"Gaurav":[10,11,12],"Raman":[15,16,17]})
print(result)
result["Gaurav"]=11
print(result)



def make_changes(Dict):
      Dict["Gaurav"]=[33,44,55]
      Dict["Raman"].append(33)
      return Dict
print(make_changes({"Gaurav":[10,11,12],"Raman":[15,16,17]}))


class A:
      VarA="hello this is VarA"
class B:
      VarB="hello this is VarB"
class C(A,B):
      VarC="This is Var c"
C1=C()
logging.info(C1.VarA)

#Guessing Number

import random
def guess_number():
      guess_left=5
      number=random.randint(1,101)
      print("Hello welcome to the game")

      while guess_left>0:
            try:
                  guess_number=int(input("Enter a number: "))
                  if guess_number<number:
                        print("Input is low!")
                  elif guess_number>number:
                        print("Input is high!")
                  else:
                        print(f"Congratulation your input is right in {7-guess_left+1}")
                        return
                  guess_left-=1
            except ValueError:
                  print("Error! Invalid input")
      print("You're out of input")
guess_number()



























































