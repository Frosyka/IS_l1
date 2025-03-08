import numpy as np

# Матрица выигрышей
payoff_player1 = np.array([[1, 0], [0, 3]])  # Выигрыши Игрока 1
payoff_player2 = np.array([[3, 0], [1, 0]])  # Выигрыши Игрока 2

# Поиск чистых равновесий Нэша
def find_pure_nash(p1, p2):
    nash_equilibria = []
    for i in range(2):
        for j in range(2):
            is_nash = True
            # Проверяем Игрока 1
            if i == 0 and p1[1][j] > p1[0][j]:
                is_nash = False
            if i == 1 and p1[0][j] > p1[1][j]:
                is_nash = False
            # Проверяем Игрока 2
            if j == 0 and p2[i][1] > p2[i][0]:
                is_nash = False
            if j == 1 and p2[i][0] > p2[i][1]:
                is_nash = False
            if is_nash:
                nash_equilibria.append((i, j))
    return nash_equilibria

# Смешанное равновесие
def mixed_nash():
    p = 3/4  # Вероятность Игрока 1 выбрать Кино
    q = 1/4  # Вероятность Игрока 2 выбрать Кино
    expected_p1 = p * q * 1 + (1-p) * (1-q) * 3
    expected_p2 = p * q * 3 + (1-p) * (1-q) * 1
    return p, q, expected_p1, expected_p2

# Вывод результатов
pure_equilibria = find_pure_nash(payoff_player1, payoff_player2)
print("Чистые равновесия Нэша:")
for eq in pure_equilibria:
    actions = ["Комедии", "Боевик"]
    print(f"Игрок 1: {actions[eq[0]]}, Игрок 2: {actions[eq[1]]}, Выигрыши: ({payoff_player1[eq]}, {payoff_player2[eq]})")

p, q, exp_p1, exp_p2 = mixed_nash()
print("\nСмешанное равновесие Нэша:")
print(f"Игрок 1 выбирает Кино с вероятностью {p:.2f}, Концерт с вероятностью {1-p:.2f}")
print(f"Игрок 2 выбирает Кино с вероятностью {q:.2f}, Концерт с вероятностью {1-q:.2f}")
print(f"Ожидаемый выигрыш Игрока 1: {exp_p1:.2f}")
print(f"Ожидаемый выигрыш Игрока 2: {exp_p2:.2f}")
