# num1 = [1,2,3]
# num =sum(num1)/len(num1)
# print(num)

def AvgNum(num1):
    num3 = sum(num1)/len(num1)
    print(num3)

# nums = [1,2,3,4]
#AvgNum(nums)
mylist = []
while True:
    inp = int(input("Enter a number"))
    mylist.append(inp)
    inp2 = input("enter done") 
    if inp2 == 'done':
        break

AvgNum(mylist)

# def raisetopower(x,n):
#     x1=x ** n
#     print(x1)
    
    
# x = int(input("Enter a number"))
# n = int(input("raise to power"))

# raisetopower(x,n) 