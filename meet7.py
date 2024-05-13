# tabel kebenaran (logika bolean)
# not and or xor

# not

print("*****Logika NOT*****")
x = False
y = not x
print('value x =', x)
print('****NOT')
print('value y =', y)

# or (semua bernilai True, selama ada nilai true)
print("*****Logika NOT*****")
x = False
y = False
z = x or y
print(x, 'or', y, '=', z)
x = False
y = True
z = x or y
print(x, 'or', y, '=', z)
x = True
y = False
z = x or y
print(x, 'or', y, '=', z)
x = True
y = True
z = x or y
print(x, 'or', y, '=', z)

# or (semua bernilai True, selama ada nilai true)
print("*****Logika NOT*****")
x = False
y = False
z = x or y
print(x, 'or', y, '=', z)
x = False
y = True
z = x or y
print(x, 'or', y, '=', z)
x = True
y = False
z = x or y
print(x, 'or', y, '=', z)
x = True
y = True
z = x or y
print(x, 'or', y, '=', z)

# AND (hanya bernilai true jika keduanya true)
print("*****Logika AND*****")
x = False
y = False
z = x and y
print(x, 'and', y, '=', z)
x = False
y = True
z = x and y
print(x, 'and', y, '=', z)
x = True
y = False
z = x and y
print(x, 'and', y, '=', z)
x = True
y = True
z = x and y
print(x, 'and', y, '=', z)

# XOR
print("*****Logika XOR*****")
x = False
y = False
z = x ^ y
print(x, 'xor', y, '=', z)
x = False
y = True
z = x ^ y
print(x, 'xor', y, '=', z)
x = True
y = False
z = x ^ y
print(x, 'xor', y, '=', z)
x = True
y = True
z = x ^ y
print(x, 'xor', y, '=', z)
