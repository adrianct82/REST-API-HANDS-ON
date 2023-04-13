


# class Student():
#     def __init__(self,name: str ,age: int):
#         self.name = name
#         self.age = age

#     def __str__(self) -> str:
#         return (f"The name of this student is {self.name!r} and the age is {self.age}")
        


# stu = Student("Adrian", 35) 

# print(stu)


# SIMPLE DECORATORS
# # VERSION 1
# user = {"username": "jose", "access_level": "admin"}

# def get_admin_password():
#     return "1234"

# def make_secure(func):
#     def secure_function():
#         if user["access_level"] == "admin":
#             return func()
#         else:
#             return f"No admin permissions for {user['username']}."
#     return secure_function

# get_admin_password = make_secure(get_admin_password)

# print(get_admin_password())


# # VERSION 2
# import functools

# user = {"username": "jose", "access_level": "admin"}


# def make_secure(func):
#     @functools.wraps(func)
#     def secure_function():
#         if user["access_level"] == "admin":
#             return func()
#         else:
#             return f"No admin permissions for {user['username']}."
#     return secure_function

# @make_secure
# def get_admin_password():
#     return "1234"


# print(get_admin_password.__name__)
# print(get_admin_password())



# VERSION 3
import functools

user = {"username": "jose", "access_level": "admin"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kargs):
        if user["access_level"] == "admin":
            return func(*args, **kargs)
        else:
            return f"No admin permissions for {user['username']}."
    return secure_function

@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"



print(get_password("admin"))

