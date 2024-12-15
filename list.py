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




















def searching(list,num):
    for ele in list:
        if num==ele:
            return f"{num} is in the list"
        else:
            return f"Error! {num} is not in the list"
result=searching([1,2,3,4,5],11)
print(result)











def bubble_sort(list):
    for n in range(len(list)-1,0,-1):
        for i in range(n):
            if list[i]>list[i+1]:
                list[i],list[i+1] =list[i+1],list[i]

    return list
result_list=bubble_sort([1,33,11,66,34,343,32,21])
print(result_list)


def minimum_number(list):
    smallest=list[0]
    for item in list:
        if item<smallest:
            smallest = item
    return smallest
print(minimum_number([12,33,5,1,99,45]))




def pos_neg(list):
    positive_count,negative_count=0,0
    for ele in list:
        if ele>=0:
            positive_count+=1
        else:
            negative_count+=1
    return positive_count,negative_count
print(pos_neg([10, -21, 4, -45, 66, -93, 1]))




























