def sum(num):
    even_total=0
    odd_total=0
    for ele in range(0,num+1):
        if ele%2==0:
            even_total+=ele
        else:
            odd_total+=ele
    return even_total,odd_total

print(sum(5))

def sum(num):
    eve_total=0
    od_total=0
    i=0
    list1=[]
    list2=[]
    while i<=num:
        if i%2==0:
            list1.append(i)
        else:
            list2.append(i)
        i+=1
    return list1,list2
even_list,odd_list=sum(10)
print(even_list.pop())
print(even_list)