from functools import total_ordering
from test.test_wsgiref import hello_app

# x=float(input("请输入一个数字:"))
# y=float(input("请输入另一个数字:"))
# oper=input("请输入+ - * /任意一个运算符:")
# match oper:
#     case "+":
#         print(f"{x} + {y} = {x+y}")
#     case "-":
#         print(f"{x} - {y} = {x-y}")
#     case "*":
#         print(f"{x} * {y} = {x*y}")
#     case "/" if y!=0:
#         print(f"{x} / {y} = {x/y}")
#     case _:
#         print("输入错误  ")
# i=0
# while i<10:
#     print("人生苦短")
#     i=i+1
# else:
#     print("进程结束")
# msg=input("请输入元素：")
# for i in msg:
#     print(f"元素:{i}")
# else:
#     print("进程结束")
# m=int(input("请输入宽:"))
# n=int(input("请输入长度:"))
# for i in range(n):#控制行
#     for i in range(m):#控制列
#          print("*",end=" ")
#     print()
while True:
    username = input("Username: ")
    password = input("Password: ")
    if username == "" and password == "":
        print("Please enter both username and password")
        continue
    if username == "admin" and password == "666888":
        print("Welcome, admin!")
        break
    elif username == "zhangsan" and password == "123456":
        print("Welcome, admin!")
        break
    elif username == "taoge" and password == "888666":
        print("Welcome, admin!")
        break

    else:
        print("用户名或密码错误，请重新输入")
#break:只能够用在循环中，表示结束或跳出循环
#continue:使循环延续下去