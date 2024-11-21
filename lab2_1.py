money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
b=0 #budget
m=0 #months
while True:
    m+=1
    if m==1:
        b=money_capital+salary-spend
    else:
        b=b+salary-spend
        spend*=1.05
    if b<spend:
        break
print("Количество месяцев, которое можно протянуть без долгов:", m)
