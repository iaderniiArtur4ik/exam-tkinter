import tkinter as tk


def calculate():
    try:
        input_data = entry.get()

        numbers = [float(num) for num in input_data.split()]

        result = sum(numbers)

        result_label.config(text=f"Результат: {result}")
    except ValueError:
        result_label.config(text="Ошибка: введите числа через пробел")


root = tk.Tk()
root.title("Калькулятор сложения")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

calc_button = tk.Button(root, text="=", command=calculate, width=10, height=2)
calc_button.pack(pady=5)

result_label = tk.Label(root, text="Результат: ", height=2)
result_label.pack()

root.mainloop()