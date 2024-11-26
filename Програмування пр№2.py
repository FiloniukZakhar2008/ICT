hello = 'hello world'
name = 'Zakhar'
prizv = 'Filonyuk'
age = '16'

print(hello, type(hello))
print(name, type(name))
print(prizv, type(prizv))
print(age, type(age))

list = [hello, name, prizv, age, 55]
print(list)
print('_'*10)

one_type = type(list[0])
per_type = True  # Перемикач

# Перевірка чи всі типи однакові
for var in list:
    if type(var) != one_type: #!= не дорівнює
        per_type = False
        break

if per_type:
    print("good")
else:
    # Створення списку з зміннами
    filter_list = [var for var in list if type(var) == one_type]

    print("Типи відрізняються. Залишаємо тільки змінні одного типу:")
    print("Відфільтрований список:", filter_list)
