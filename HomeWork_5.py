# 1. 
    # Каждый день в кафе заходит от 5 до 20 покупателей. Каждый покупатель берёт от 1 до 3 чашек кофе.

import random

customers = random.randrange (5,21)
coffee = random.randrange (1,4)

    # Нужно написать функцию, которая будет генерировать тестовые данные при каждом вызове.

def order_func():
    coffee_per_customer = [random.randrange (1,4) for i in range(customers)]
    return coffee_per_customer

#order_func()
#print(order_func())

print('')

# 2.
    # Время работы кафе - с 9 до 20 часов.
    # К каждой покупке нужно добавить дату и время до минуты (2 отдельные переменные).

#from datetime import datetime
#datetime_today = datetime.now().date() 

def time_func():
   time = []
   sales = order_func()
   for i in sales:
       hours = random.randrange (9, 21)
       minutes = random.randrange (0,60) 
       time.append ((hours,  minutes))
   return dict(zip(time, sales))

time_func()
print(time_func())
print('')

# 3.   
    #Кафе работает 5 дней в неделю. В конце недели надо составить отчёт по кол-ву клиентов и покупок.

def report_func():
    customers = 0
    coffee = 0
    for i in range(5):
      

