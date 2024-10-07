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