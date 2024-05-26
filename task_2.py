import turtle
import math

def draw_pythagoras_tree(t, branch_length, level, angle=45):
    if level == 0:
        return

    # Малюємо основну гілку
    t.forward(branch_length)

    # Ліва гілка
    t.left(angle)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1, angle)

    # Повертаємо до початкової позиції
    t.right(2 * angle)

    # Права гілка
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1, angle)

    # Повертаємо до початкової позиції
    t.left(angle)
    t.backward(branch_length)

def main():
    # Введення рівня рекурсії від користувача
    level = int(input("Введіть рівень рекурсії: "))

    # Налаштування вікна turtle
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Дерево Піфагора")

    # Налаштування 
    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання
    t.left(90)  # Починаємо малювати знизу вверх
    t.up()
    t.goto(0, -250)  # Початкова позиція
    t.down()

    # Малювання дерева Піфагора
    draw_pythagoras_tree(t, 100, level)

    # Завершення
    turtle.done()

if __name__ == "__main__":
    main()
