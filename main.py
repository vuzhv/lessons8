#Словарь - можем указувати назву для значення далі по цьому ключу можемо обращатись до нього і використовувати

country = {4: 3}              # ключ до числа 3 це 4
print(country[4])             # ключи можуть бути кортежі но строки не можуть

#Словарі удобні для описування чогось

slovar = {'code': 'UA', 'name': 'Ukrain', 'population': 45}
print(slovar['code'])

inf = dict(code='UA', name='Ukarin', population=45)           #другий спосіб зробити словарь


for keys in slovar:               #виводяться тільки ключі
    print(keys)

print(slovar.items())        #items - список де кожен елемент це кортеж що состоїть з двух елементів ключ і елемент

for key, value in slovar.items():          # виводить key(ключ) -  value(значення, елемент)
    print(key, "-", value)


print(slovar.get('name'))                #get - аналогічний квадратним скобкам
#slovar.clear()                           #clear - очищає словарь
slovar.pop('name')                       #pop - удаляє определьонний елмент
slovar.popitem()                         #popitem - кожен раз удаляє останній елемент
print(slovar.keys())                     #keys - виводить тільки ключі
print(slovar.values())                   #values - виводить значення
print(slovar.items())                    #items - виводить і ключ і значення як отдельний кортеж
slovar['code'] = 'None'                  #обновлення словаря за ключом або slovar.update()


#Словарі удобні для описання обьекта

person = {
    'user_1':{
        'first_name': 'John',
        'last_name': 'Marley',
        'age': '32',
        'adress': ['м. Київ', 'NEW', '21'],
        'grades': {'math': 4, 'science': 3}

    },
    'user_2':{

    }
}

print(person['user_1']['adress'][1])
