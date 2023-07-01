''' swap variables a and b 
(so that a refers to the object previously referred to by b and vice versa).'''
a = [1, 2, 3]
b = [3, 2, 1]
temp = a
a = b
b = temp
print (a, b)