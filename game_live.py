import tkinter as tk
from tkinter import ttk
import random
import string

from tkinter import ttk, filedialog
import tkinter as tk
from tkinter import ttk
import random
import string
import hashlib

login = "senya"
password = "2564"

def open_login_window():
    global login_window, login_entry, password_entry, error_label
    login_window = tk.Tk()
    login_window.title("Авторизация")
    login_window.geometry("300x150")
    login_window.configure(bg="#2E2E2E")  # Dark background color

    login_label = tk.Label(login_window, text="Логин:", padx=10, pady=5, bg="#2E2E2E", fg="white")  # Dark theme colors
    login_label.grid(row=0, column=0)

    login_entry = tk.Entry(login_window, bg="#2E2E2E", fg="white")  # Dark theme colors
    login_entry.grid(row=0, column=1)

    password_label = tk.Label(login_window, text="Пароль:", padx=10, pady=5, bg="#2E2E2E", fg="white")  # Dark theme colors
    password_label.grid(row=1, column=0)

    password_entry = tk.Entry(login_window, show="*", bg="#2E2E2E", fg="white")  # Dark theme colors
    password_entry.grid(row=1, column=1)

    login_button = tk.Button(login_window, text="Войти", command=check_credentials, bg="#2E2E2E", fg="white")  # Dark green button
    login_button.grid(row=2, column=0, columnspan=2, pady=10)

    error_label = tk.Label(login_window, text="", fg="red", bg="#2E2E2E")  # Dark theme colors
    error_label.grid(row=3, column=0, columnspan=2)

    login_window.bind("<Return>", check_credentials)
    login_window.mainloop()

def generate_random_number():
    random_number = random.randint(1, 100)
    random_label.config(text=f'Случайное число: {random_number}')

def generate_passwords(length_var, quantity_var):
    password_length = int(length_var.get())
    num_passwords = int(quantity_var.get())

    generated_passwords = []
    for _ in range(num_passwords):
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))
        generated_passwords.append(password)

    passwords_text.config(state=tk.NORMAL)
    passwords_text.delete('1.0', tk.END)
    passwords_text.insert(tk.END, '\n'.join(generated_passwords))
    passwords_text.config(state=tk.DISABLED)

def check_credentials(event=None):
    entered_login = login_entry.get()
    entered_password = password_entry.get()

    if entered_login == login and entered_password == password:
        login_window.destroy()
        initialize_main_window()
        sha1 = hashlib.sha1(entered_login.encode('utf-8')).hexdigest()
        sha2 = hashlib.sha1(entered_password.encode('utf-8')).hexdigest()
        print(f"login: {sha1}\npassword: {sha2}")
    else:
        error_label.config(text="Неправильный логин или пароль")

def initialize_main_window():
    root = tk.Tk()
    root.iconbitmap('C:\\Users\\1\\for_prog.jpg')
    root.title("Основное окно")
    root.geometry("500x400")
    root.style = ttk.Style()
    root.style.configure('new.TFrame', background='#2E2E2E')

    tab_control = ttk.Notebook(root)

    tab1 = ttk.Frame(tab_control, style='new.TFrame')
    tab_control.add(tab1, text='Генератор чисел')

    global random_label
    random_label = tk.Label(tab1, text='Нажмите кнопку для генерации числа', bg="#383838")
    random_label.pack(padx=10, pady=10)

    random_button = tk.Button(tab1, text='Сгенерировать число', command=generate_random_number, bg="#383838")
    random_button.pack(padx=10, pady=5)

    tab2 = ttk.Frame(tab_control, style='new.TFrame')
    tab_control.add(tab2, text='Генератор паролей')

    length_label = tk.Label(tab2, text='Длина пароля:', bg="#2E2E2E")
    length_label.grid(row=0, column=0, padx=10, pady=5)
    length_var = tk.StringVar()
    length_entry = tk.Entry(tab2, textvariable=length_var, bg="#2E2E2E")
    length_entry.grid(row=0, column=1, padx=10, pady=5)
    length_var.set('8')

    quantity_label = tk.Label(tab2, text='Количество паролей:', bg="#2E2E2E")
    quantity_label.grid(row=1, column=0, padx=10, pady=5)
    quantity_var = tk.StringVar()
    quantity_entry = tk.Entry(tab2, textvariable=quantity_var, bg="#2E2E2E")
    quantity_entry.grid(row=1, column=1, padx=10, pady=5)
    quantity_var.set('5')

    generate_button = tk.Button(tab2, text='Генерировать пароли',  bg="#383838",command=lambda: generate_passwords(length_var, quantity_var))
    generate_button.grid(row=2, column=0, columnspan=2, pady=10)

    global passwords_text
    passwords_text = tk.Text(tab2, height=10, width=40, state=tk.DISABLED, bg="#383838")
    passwords_text.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    tab3 = ttk.Frame(tab_control, style='new.TFrame')
    tab_control.add(tab3, text='Калькулятор')

    calculator_label = tk.Label(tab3, text='Введите выражение:', bg="#383838")
    calculator_label.grid(row=0, column=0, columnspan=4, padx=10, pady=5)

    calculator_entry = tk.Entry(tab3, bg="#383838")
    calculator_entry.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

    result_label = tk.Label(tab3, text='')
    result_label.grid(row=2, column=0, columnspan=4, padx=10, pady=5)

    result_label = tk.Label(tab3, text='')
    result_label.grid(row=2, column=0, columnspan=4, padx=10, pady=5)

    tab4 = ttk.Frame(tab_control, style='new.TFrame')
    tab_control.add(tab4, text='Текстовый редактор')

    text_editor = tk.Text(tab4,  bg="#383838",height=15, width=50)
    text_editor.pack(padx=10, pady=10)

    def save_text(text):
        file_name = tk.filedialog.asksaveasfilename(defaultextension=".txt",
                                                    filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_name:
            with open(file_name, 'w') as file:  # Use 'w' mode to write to the file
                file.write(text)

    # Inside initialize_main_window() function, add the save_button command
    save_button = tk.Button(tab4, text='Сохранить', bg="#383838",
                            command=lambda: save_text(text_editor.get("1.0", tk.END)))
    save_button.pack(pady=5)

    def button_click(value):
        current_expression = calculator_entry.get()
        calculator_entry.delete(0, tk.END)
        calculator_entry.insert(tk.END, current_expression + str(value))

    def clear_entry():
        calculator_entry.delete(0, tk.END)

    def calculate_expression():
        try:
            expression = calculator_entry.get()
            result = eval(expression)
            calculator_entry.delete(0, tk.END)
            calculator_entry.insert(tk.END, str(result))
            result_label.config(text=f'Результат: {result}', bg="#383838")

        except Exception as e:
            calculator_entry.delete(0, tk.END)
            calculator_entry.insert(tk.END, 'Ошибка')
            result_label.config(text='')

    def on_equals_button_click():
        calculate_expression()

    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
    ]

    row_val = 3
    col_val = 0
    for button in buttons:
        if button == '=':
            tk.Button(tab3, text=button,  bg="#383838",command=on_equals_button_click).grid(row=row_val, column=col_val, pady=5)
        else:
            tk.Button(tab3, text=button,  bg="#383838",command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val,
                                                                                        pady=5)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    tab_control.pack(expand=1, fill="both")

    root.mainloop()

open_login_window()
