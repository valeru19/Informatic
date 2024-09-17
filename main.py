import numpy as np
import matplotlib.pyplot as plt

# Функция для вычисления первых N чисел Фибоначчи
def fibonacci(n):
    fib = np.zeros(n, dtype=int)
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i-1] + fib[i-2]
    return fib

# Ввод количества чисел Фибоначчи
N = int(input("Введите количество чисел Фибоначчи: "))

# Вычисление чисел Фибоначчи
fib_numbers = fibonacci(N)

# Построение графика
plt.plot(range(N), fib_numbers, marker='o', color='b', label='Числа Фибоначчи')
plt.title("График чисел Фибоначчи")
plt.xlabel("Номер числа Фибоначчи")
plt.ylabel("Значение числа Фибоначчи")
plt.grid(True)
plt.legend()
plt.show()