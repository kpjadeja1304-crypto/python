list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("Concatenation:", list1 + list2)

del list1[3]
print("After deleting index 3 from list1:", list1)

list1.append("Java")
print("After adding Java:", list1)

list2[3] = 11
print("After updating list2:", list2)

del list2[2]
print("After deleting index 2 from list2:", list2)

for i in range(4):
    print("Welcome to Marwadi University")

print("Slicing list1[-2]:", list1[-2])
print("Slicing list2[1:3]:", list2[1:3])

print("Length of list2:", len(list2))
print("Max in list1:", max(list1))
print("Min in list2:", min(list2))

list2.append(100)
print("After append:", list2)

list2.extend([200, 300])
print("After extend:", list2)

temp = [10, 20, 30, 40]
temp.pop(2)
print("After pop:", temp)
temp.remove(20)
print("After remove:", temp)

list1.reverse()
print("Reversed list1:", list1)

list2.sort(reverse=True)
print("Descending list2:", list2)
