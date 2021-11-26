myList=["Cat","Dog",34]

print("Length of the list:"+str(len(myList)))
myList.append("Saniya")
print("Append something at the end:")
print(myList)
myList.insert(1,"Conestoga")
print("Insert something at 2nd position:")
print(myList)

print("Print the first element of the List:"+myList[0])
myList.pop()
print("Delete element from thr end of the list:")
print(myList)
myList.remove("Conestoga")
print("Remove element from 2nd position:")
print(myList)
