items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості в порядку спадання
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            selected_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']

    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    # Створюємо таблицю для динамічного програмування
    dp = [0] * (budget + 1)
    item_selection = [[] for _ in range(budget + 1)]
    
    for item, details in items.items():
        cost = details['cost']
        calories = details['calories']
        
        for current_budget in range(budget, cost - 1, -1):
            if dp[current_budget - cost] + calories > dp[current_budget]:
                dp[current_budget] = dp[current_budget - cost] + calories
                item_selection[current_budget] = item_selection[current_budget - cost] + [item]

    max_calories = max(dp)
    best_budget = dp.index(max_calories)
    selected_items = item_selection[best_budget]

    return selected_items, best_budget, max_calories

# Введення бюджету
budget = 100

# Жадібний алгоритм
greedy_items, greedy_cost, greedy_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", greedy_items)
print("Загальна вартість:", greedy_cost)
print("Загальна калорійність:", greedy_calories)

# Алгоритм динамічного програмування
dp_items, dp_cost, dp_calories = dynamic_programming(items, budget)
print("\nАлгоритм динамічного програмування:")
print("Вибрані страви:", dp_items)
print("Загальна вартість:", dp_cost)
print("Загальна калорійність:", dp_calories)
