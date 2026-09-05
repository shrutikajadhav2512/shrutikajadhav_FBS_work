# def login():
#     print("Time startd")
#     print("Logger added")
#     print("before logger")
#     print("Login done.")
#     print("timer stoped")
#     print("logger removed")
#     print("after login")
# login()
# def logout():
#     print("Logger added")
#     print("before logger")
#     print("Logout done.")
#     print("timer stoped")
#     print("logger removed")
#     print("after logout")
# logout()
# def admin_login():
#     print("Logger added")
#     print("before logger")
#     print("admin login done.")
#     print("timer stoped")
#     print("logger removed")
#     print("after logout")
# admin_login()
# #WE CAN STORE THE FUNTION IN VARIABLE..
# def demo():
#     print("I am from demo.")
# x=demo
# print(type(demo))
# print(type(x))
# demo()
# x()
# #PASS THE FUNCTION AS AN ARGUMENT TO ANATHOR FUNTION
# def fun1():
#     print("I am from function1")
# # fun1()
# def demofun(a):
#     print("I am from demofun")
#     a()
# demofun(fun1)
# #RETURN INNER FUNTION FROM OUTER FUNCTION..
# def outer():
#     print("outer is called")
#     def innerFunction():
#         print("Inner function is called")
#     return innerFunction
# s=outer()
# s()
# #Claosur
# def outer():
#     print("outer is called")
#     var="abc"
#     def innerFunction():
#         print("Inner function is called",var)
#     return innerFunction
# s=outer()
# s()
#DECORATOR
def demo1(fun):
    print("Decorator is called.")
    def wrapper():
        print("Before calling your function all task will be performend here..")
        fun()
        print("After calling your function all task will be performend here..")
    return wrapper
@demo1
def login():
    print("\n Login is Done\n")
@demo1
def logout():
    print("\n Logout is Done\n")
login()
logout()