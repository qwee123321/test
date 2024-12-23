import tkinter as tk
from tkinter import messagebox

def on_button_click():
    user_input = entry.get()
    messagebox.showinfo("Информация", f"Вы ввели: {user_input}")

# Создаем основное окно
root = tk.Tk()
root.title("Простое приложение")
root.geometry("300x150")

# Создаем текстовое поле
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Создаем кнопку
button = tk.Button(root, text="Нажми меня", command=on_button_click)
button.pack(pady=10)

# Запускаем основной цикл приложения
root.mainloop()
