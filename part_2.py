import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


# Визначення функції та меж інтегрування
def f(x):
    return x ** 2

a, b = 0, 2
num_samples = 10000

# Генерація випадкових точок
x_rand = np.random.uniform(a, b, num_samples)
y_rand = np.random.uniform(0, f(b), num_samples)

# Підрахунок точок під кривою
points_under_curve = np.sum(y_rand < f(x_rand))

# Обчислення інтегралу методом Монте-Карло
monte_carlo_integral = (points_under_curve / num_samples) * (b - a) * f(b)
print(f"Monte Carlo Integral: {monte_carlo_integral}")

# Перевірка за допомогою quad
result, error = spi.quad(f, a, b)
print(f"Quad Integral: {result}, Error: {error}")

# Висновки щодо точності розрахунків
error_percentage = abs((monte_carlo_integral - result) / result) * 100
print(f"Різниця між методами: {error_percentage:.5f}%")

# Графік інтегрування
x_vals = np.linspace(-0.5, 2.5, 400)
y_vals = f(x_vals)

fig, ax = plt.subplots()
ax.plot(x_vals, y_vals, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x_vals[0], x_vals[-1]])
ax.set_ylim([0, max(y_vals) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')
plt.grid()
plt.show()

# Запис висновків у файл readme.md
with open("Readme.md", "w", encoding="utf-8") as file:
    file.write(f"# Домашнє завдання: Обчислення визначеного інтеграла методом Монте-Карло\n")
    file.write(f"\n## Опис задачі\n")
    file.write(f"Обчислено визначений інтеграл функції f(x) = x^2 на відрізку [0, 2] методом Монте-Карло.\n")
    file.write(f"\n## Порівняння результатів\n")
    file.write(f"Метод Монте-Карло: {monte_carlo_integral}\n")
    file.write(f"Метод quad (аналітичне значення): {result} (похибка: {error})\n")
    file.write(f"Відносна різниця між методами: {error_percentage:.5f}%\n")
    file.write(f"\n## Висновки\n")
    file.write(f"Метод Монте-Карло дав результат, близький до аналітичного значення, з невеликою похибкою. Точність залежить від кількості вибраних випадкових точок.\n")
