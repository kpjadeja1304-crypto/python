#large from 3
n1=int(input("Enter  1st number:"))
n2=int(input("Enter  2nd number:"))
n3=int(input("Enter  3rd number:"))

if n1>n2 and n1>n3:
    print(f"{n1} is largerst from 3")
elif n2>n1 and n2>n3:
    print(f"{n2} is largerst from 3")
elif n3>n1 and n3>n2:
    print(f"{n3} is largerst from 3")
else:
    print("All are equal")
