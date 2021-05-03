# 1. 
    # Каждый день в кафе заходит от 5 до 20 покупателей. Каждый покупатель берёт от 1 до 3 чашек кофе.
    # Нужно написать функцию, которая будет генерировать тестовые данные при каждом вызове.

import random

def order_func():
    customers = random.randrange (5, 21)
    cups_of_coffe = random.randrange (1, 4)
    coffee_per_customer = [random.randrange (1, 4) for i in range(customers)]
    return coffee_per_customer

#print(order_func())
print(' ')



# 2.
    # Время работы кафе - с 9 до 20 часов.
    # К каждой покупке нужно добавить дату и время до минуты (2 отдельные переменные).

from datetime import date

sales = order_func()

def time_func(*args, **kwargs):
    today = str(date.today())                 
    time = []
    for i in sales:
       hours = random.randrange (9, 21)
       minutes = random.randrange (0,60) 
       time.append ((hours,  minutes))
    return dict(zip(time, sales))

print(time_func())
print(' ')



# 3.   
    #Кафе работает 5 дней в неделю. В конце недели надо составить отчёт по кол-ву клиентов и покупок.



def week_report():               #кол-во продаж за неделю
    total_sales = 0
    for i in range(5,21):
       i = random.randrange(1,4)
       total_sales += i
       total_sales_week = 0
       for total_sales in range(5):
           total_sales_week += total_sales
       return total_sales_week

print ('Всего продаж за неделю')            #не совсем рахобрался почему здесь за неделю меньше, чем за день
print (week_report())                       #'NoneType' object is not callable (used decorator)
print(' ')



# 5
    #После перерасчёта оказалось, что для окупаемости, каждый день в кафе должно продаваться не меньше 20 чашек кофе.
    #Надо написать декоратор, который будет проверять кол-во чашек кофе на каждый день.
def my_decoration(dayly_report):
    def wrapper():
        total_orders = 0
        customers = random.randrange (5, 21)
        for i in range(customers):
            i= random.randrange (1, 4)
            total_orders += i
            print ("Всего продаж за день", total_orders)
    return wrapper()


    #И если их было меньше 20, возвращать сообщение с ошибкой
@my_decoration
def dayly_report():
    try:
        a = total_orders / 20
    except Error:
        a < 1
print (a)