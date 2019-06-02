import matplotlib.pyplot as plt

fig, ax = plt.subplots ()

p = int(input('Введите шаг, на котором остановимся: '))
b = int(input('Введите первое число последовательности: '))
c = int(input('Введите второе число последовательности: '))
x = [b, c]
y = [1.5, 1.5]
for i in range (2,p):
    x.append(x[i-2]+x[i-1])
    y.append(x[i-1]/x[i-2])

print (x)
print (y)

ax.plot(x, y)
ax.plot ([0, x[i]], [1.61803398875, 1.61803398875])

plt.show()