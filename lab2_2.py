salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
budget=0
m_c=0
for a in range(months):
    budget=spend-salary
    if budget>0:
        m_c+=budget
    spend*=increase+1


print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(m_c))
