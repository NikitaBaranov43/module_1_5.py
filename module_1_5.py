immutable_var = 1 , 2 ,3 ,4, 5 , 'privet' , False
print(immutable_var)
#immutable_var[3] = 19 # невозможно заменить,по причине неизменяемости типа данных в кортеже
#print(immutable_var)
mutable_list = [1, 2, 3, 4, 'poka', True]
print((mutable_list))
mutable_list[5] = 'izmenenie'
print(mutable_list)