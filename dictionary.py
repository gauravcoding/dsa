def newadd(dict):
    list=[]
    for key in dict:
        list.append(key)
    return list
# print(newadd({1:'Gaurav',2:'julie',3:'mahendra'}))
def sum_val(my_dict):
    list=[]
    for value in my_dict.values():
        list.append(value)
        print(list)
    return sum(list)
print(sum_val({'a':100,'b':200,'c':300}))
# merge two dictionary
def merge(dict1,dict2):
    dict1.update(dict2)
    return dict1
print(merge({1:'Abhishek',2:'Rohan'},{3:'julie',4:'Gaurav'}))