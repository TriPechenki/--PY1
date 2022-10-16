money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while True:
    money_capital = money_capital + salary - spend
    if money_capital < 0:
        break
    elif money_capital == 0:
        month += 1
        break
    month += 1
    spend = spend * (1 + increase)  # Увеличение расходов

print(month) # Ну никак тут не выходит 3...
