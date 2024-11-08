def max_ele(list):
    list.sort(reverse=True)
    return list[-1]
# print(max_ele([45, 1,2,3,44,55,56]))
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')












def calculate(a, b):
    logging.debug(f'Calculating: {a} + {b}')
    return a + b

# result = calculate(5, 3)
# logging.info(f'Result: {result}')
def add(a,b=0,c=0):
    return a+b+c
# print(add(10,c=2,b=5))
def my_dict(list):
    dict1={}
    for ele in list:
        dict1[ele]="hi"
    return dict1
logging.info(my_dict([1,1,2,3,4,5]))
list=[1,2,3,4,5]
list.remove(5)
# print(list)
def swap(a,b):
    temp=b
    b=a
    a=temp
    return a,b
logging.info(swap(10,12))
def poitive(list):
    new_list=[]

