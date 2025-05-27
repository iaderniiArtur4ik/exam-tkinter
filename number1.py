import tkinter as tk

def on_arrow_press(direction):
    print(direction)
    label.config(text=direction)

root = tk.Tk()
root.title("Кнопки со стрелками")

label = tk.Label(root, text="Нажмите кнопку", font=('Arial', 14))
label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack()

up_button = tk.Button(button_frame, text="↑", font=('Arial', 14),
                     command=lambda: on_arrow_press("верх"))
up_button.grid(row=0, column=1, padx=5, pady=5)

left_button = tk.Button(button_frame, text="←", font=('Arial', 14),
                       command=lambda: on_arrow_press("лево"))
left_button.grid(row=1, column=0, padx=5, pady=5)

down_button = tk.Button(button_frame, text="↓", font=('Arial', 14),
                       command=lambda: on_arrow_press("низ"))
down_button.grid(row=1, column=1, padx=5, pady=5)

right_button = tk.Button(button_frame, text="→", font=('Arial', 14),
                        command=lambda: on_arrow_press("право"))
right_button.grid(row=1, column=2, padx=5, pady=5)

root.mainloop()