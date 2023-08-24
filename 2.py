# import time
#
#
# def fn(x, y, z):
#     print(x, 'eto x')
#     print(b, 'eto b')
#     time.sleep(1)
#     return x * 10
#
#
# b = 10
# a = fn(2, 1, 3)
# print(a)
#
#
# #y1 = ([1], {2: 'dava'}, {3, 54})# это распаковка кортэжа
# #el1, el2, el3 = t1
# #print(el1, el2, el3)
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#def fn(y, x=0, z=0):
#    print(x, y, z)
#    return x * 10
#
#
#b = 10
#a = fn(x=1, y=2, z=3)
#print(a)
#-----------------------------------------------------------------------------------
# def fn(*args):
#     print(args[1])#можно без индекса
#     return 1
#
#
# b = 10
# a = fn(1,2,3)
# print(a)
#-----------------------------------------------------------------------------------
# import time
#
#
# def fn(x, y, z, **kwargs):
#     print(kwargs)
#     if 'test_case' in kwargs:
#         print('eto test func')
#         print(f'sleep for {kwargs.get("time_sleep")}')
#         time.sleep(kwargs.get('time_sleep'))
#     return 1
#
#
# b = 10
# a = fn(1, 2, 3, test_case=True, Time_sleep=3)
# print(a)
#-----------------------------------------------------------------------------------
# random_int = range(100)
# some_list = []
# some_list.append([*random_int])
# print(some_list)
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
# phone_operators = {'25': "Life", "29": "A1", "33": "MTS" }
#
#
# def chek_operator(any_number):
#     if len(any_number) == 13:
#         code = any_number[4:6]
#         print(code, 'eto code')
#         result = phone_operators.get(code)
#         return result
#     else:
#         raise Exception("Wrong number")
#
#
# phone_number = input("Enter your number, start with '+':")
# operator = chek_operator(phone_number)
# print(operator)
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
# def fn(a, b):
#     summa = a + b
#     subtract = a - b
#     multiply = a * b
#     division = a / b
#     return summa, subtract, multiply, division
#
#
# result = fn(1, 2)
# print(result)
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
# def fn(a, b, c, /, d):# / - он дает понять что нужно передать обязательно
#     print(a, b, c, d)
#
#
# fn(1, 2, 3, d=50)
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

def fn(x, y):
    print(x, y)
    def inner():
        print(x,y,"in inner")

    inner()
    return  x, y

fn(1, 2)
