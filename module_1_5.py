immutable_var  = (1, 2, 'a', 'b')
print(immutable_var)
# immutable_var[0] = 100 # Ошибка буквально сообщает нам, что кортеж не поддерживает обращение по элементам.
immutable_var = ([1, 2], 'a', 'b')
print(immutable_var)
immutable_var[0][0] = 5
print(immutable_var)
Mutable_list = [1, 2, 'a', 'b', 'Modified']
print(Mutable_list)
Mutable_list[2] = 3
print(Mutable_list)