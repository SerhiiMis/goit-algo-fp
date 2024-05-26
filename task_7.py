import random
import matplotlib.pyplot as plt

# Симуляція кидків двох кубиків
def simulate_dice_rolls(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        dice_sum = die1 + die2
        sums_count[dice_sum] += 1
    
    return sums_count

# Обчислення ймовірностей
def calculate_probabilities(sums_count, num_rolls):
    probabilities = {sum_value: count / num_rolls * 100 for sum_value, count in sums_count.items()}
    return probabilities

# Порівняння з аналітичними ймовірностями
def compare_probabilities(simulated_probs):
    analytical_probs = {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67,
        8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
    }
    
    print("Сума\tАналітична імовірність\tСимуляційна імовірність")
    for sum_value in range(2, 13):
        print(f"{sum_value}\t{analytical_probs[sum_value]:.2f}%\t\t\t{simulated_probs[sum_value]:.2f}%")

# Візуалізація результатів
def plot_probabilities(simulated_probs):
    sums = list(simulated_probs.keys())
    probs = list(simulated_probs.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(sums, probs, color='skyblue', edgecolor='black')
    plt.xlabel('Сума на кубиках')
    plt.ylabel('Імовірність (%)')
    plt.title('Імовірності сум при киданні двох кубиків (Метод Монте-Карло)')
    plt.xticks(sums)
    plt.grid(axis='y')
    plt.show()

# Основна функція
def main():
    num_rolls = 1000000  # Кількість кидків
    sums_count = simulate_dice_rolls(num_rolls)
    simulated_probs = calculate_probabilities(sums_count, num_rolls)
    compare_probabilities(simulated_probs)
    plot_probabilities(simulated_probs)

if __name__ == "__main__":
    main()
