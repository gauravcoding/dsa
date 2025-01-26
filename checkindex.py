def get_index(list,target):
    pairs_of_index=[]
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]+list[j]==target:
                pairs_of_index.append((i,j))
    return pairs_of_index
if __name__=="__main__":
    print(get_index([1,2,3,4,5,6,7],9))