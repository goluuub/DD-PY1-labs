def find_common_participants(group1, group2, separator=','):
    # Разбиваем строки по указанному разделителю
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))

    # Находим общих участников и сортируем их
    common_participants = sorted(participants1.intersection(participants2))

    return common_participants


# Примеры использования
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверяем работу функции с разделителем "|"
common = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(common)  # Выведет: ['Петров', 'Сидоров']

# Также демонстрируем работу с запятой как разделителем
participants_first_group2 = "Иванов,Петров,Сидоров"
participants_second_group2 = "Петров,Сидоров,Смирнов"
common2 = find_common_participants(participants_first_group2, participants_second_group2)
print(common2)  # Выведет: ['Петров', 'Сидоров']
