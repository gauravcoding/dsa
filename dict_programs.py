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