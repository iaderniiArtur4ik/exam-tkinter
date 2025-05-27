import tkinter as tk
import math


class MovingCircle:
    def __init__(self, root):
        self.root = root
        self.root.title("Движение круга к точке клика")

        # Создаем холст
        self.canvas = tk.Canvas(root, width=500, height=400, bg='white')
        self.canvas.pack()

        # Начальные координаты круга
        self.circle_x = 250
        self.circle_y = 200
        self.circle_radius = 20

        # Создаем круг
        self.circle = self.canvas.create_oval(
            self.circle_x - self.circle_radius,
            self.circle_y - self.circle_radius,
            self.circle_x + self.circle_radius,
            self.circle_y + self.circle_radius,
            fill='blue'
        )

        # Целевая точка
        self.target_x = self.circle_x
        self.target_y = self.circle_y

        # Скорость движения
        self.speed = 3

        # Привязываем обработчик клика мыши
        self.canvas.bind('<Button-1>', self.set_target)

        # Запускаем анимацию
        self.animate()

    def set_target(self, event):
        """Устанавливаем новую целевую точку при клике"""
        self.target_x = event.x
        self.target_y = event.y

    def animate(self):
        """Анимация движения круга к целевой точке"""
        # Вычисляем расстояние до цели
        dx = self.target_x - self.circle_x
        dy = self.target_y - self.circle_y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        # Если расстояние больше скорости, двигаем круг
        if distance > self.speed:
            # Нормализуем вектор направления
            dx /= distance
            dy /= distance

            # Перемещаем круг
            self.circle_x += dx * self.speed
            self.circle_y += dy * self.speed

            # Обновляем позицию круга на холсте
            self.canvas.coords(
                self.circle,
                self.circle_x - self.circle_radius,
                self.circle_y - self.circle_radius,
                self.circle_x + self.circle_radius,
                self.circle_y + self.circle_radius
            )

        # Продолжаем анимацию
        self.root.after(20, self.animate)


# Создаем и запускаем приложение
root = tk.Tk()
app = MovingCircle(root)
root.mainloop()