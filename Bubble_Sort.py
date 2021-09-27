
array=[3,1,4,2,0,8,5,10,7]

for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]>array[j]:
            temp=array[i]
            array[i]=array[j]
            array[j]=temp

print(array)