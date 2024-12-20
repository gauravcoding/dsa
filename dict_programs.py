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
#guess_number()


def prime_check(num):
      for item in range(2,int(num**0.5)+1):
            if num%item==0:
                  return f"{num} is Not Prime number !"
      return f"{num} is prime number !"
logging.info(prime_check(17))

def char_count(str):
      list=[]
      dict={}
      for item in str:
            if item in dict:
                  dict[item]+=1
            else:
                  dict[item]=1
      return dict
logging.info(char_count("Hello"))


def dict_to_list(dict):
      list=[]
      for items in dict:
            list.append(items)
      return list
dict={"Alice": 20,"Bob": 22,"Charlie": 21,"Diana": 23}
list=dict_to_list(dict)
print(list)


def list_to_dict(list):
      dict={}
      for index,ele in enumerate(list):
            dict[index] = ele
      return dict
list=[1,2,3,4,5,6 ]
dict=list_to_dict(list)
print(dict)

def str_to_list(str):
      list=[]
      for ele in str:
            list.append(ele)
      return list
logging.info(str_to_list("Gaurav"))


def list_to_string(list):
      str=""
      for ele in list:
            str+=ele
      return str
logging.info(list_to_string(["g","u","r","u"]))


def add(a,b):
      return a+b
logging.info(add(11,10))


def palindrome(str):
      if str==str[::-1]:
            return "Given string is Palindrome"
      else:
            return "Not A Palindrome String"
logging.info(palindrome("madam"))







































































