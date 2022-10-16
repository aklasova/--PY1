money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
# если написать while money_capital >= spend - salary, то количество месяцев равно 5, что более корректно
while money_capital >= spend:
    money_capital -= spend
    money_capital += salary
    spend *= (1 + increase)
    month += 1
print(month)
