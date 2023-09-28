import re

# sign up 

# def email_log():
#     while True:
#         email = input("Enter your email")
#         check = re.compile("[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)")
#         check1 =check.search(email)
#         if check1:
#             print("valid email")
#             break
#         else:
#             print("what")
#             continue
#     return email

# def number():
#     while True:
#         number = input("Enter a number")
#         check2 = re.compile("^[0-9]{5}$")
#         check3 = check2.search(number)
#         if check3: 
#             print("valid")
#             break
#         else:
#             print("what men!")
#             continue
#     return number

# email_log()
# sign_up = input("Enter Sign up or login")
# mydict = {}
# while sign_up == "sign up":
#     Name = input("Enter your name")
#     if len(Name) >= 2:
#         print("valid name")
#         mydict['Name'] = Name 
#         email2 = email_log()
#         mydict["email"] = email2
#     else:
#         continue
#     num =number()
#     mydict['number'] = num
#     done =input("Enter done")
#     if done == "done":
#         print("you are welcome")
#         break

# print(mydict) 

myDiction ={
    "people":[{
        "name": "prosper",
        "email": "echezona@gmail.com",
        "number": 8178341114
    }
    ,{
        "name": "Collins",
        "email": "Collins@gmail.com",
        "number": 8133965437
    }
    ]
}

for i in myDiction["people"]:
    print(i)

# # else:
# #     email1 = input("Enter your email")
# #     check4 = re.compile("^[A_Za_z0_9]+@[a_z]{5}.com$")
# #     check5 =check4.search(email1)
# #     if check5:
# #         print("valid email")
# #     password = input("Enter Password")
# #     check6 = re.compile("^[A_Z]{1}[a_z0_9]+#")
# #     check7 = check6.search(password)
# #     done =input("Enter done")
# #     if done == "done":
# #         break