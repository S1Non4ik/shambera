import tkinter as tk
from tkinter import messagebox
from dtb.dtb import *
from tkinter import ttk

query = """
SELECT brand FROM knowledge 
"""
cursor.execute(query)
brands = cursor.fetchall()


def main():
    root = tk.Tk()
    root.title("Авторизация")
    root.geometry("300x200")

    label_username = tk.Label(root, text="Имя пользователя:")
    label_username.pack(pady=5)

    entry_username = tk.Entry(root)
    entry_username.pack(pady=5)

    label_password = tk.Label(root, text="Пароль:")
    label_password.pack(pady=5)

    entry_password = tk.Entry(root, show="*")
    entry_password.pack(pady=5)

    def handle_login():
        usernames = entry_username.get()
        passwords = entry_password.get()

        if usernames == "root" and passwords == "root":
            messagebox.showinfo("Успех", "Вы успешно вошли в систему Администратором!")
            root.destroy()
            admin_menu()
        elif usernames == "user" and passwords == "123":
            messagebox.showinfo("Успех", "Вы успешно вошли в систему Пользователь!")
            root.destroy()
            user_menu()
        else:
            messagebox.showerror("Ошибка", "Неверное имя пользователя или пароль.")

    button_login = tk.Button(root, text="Войти", command=handle_login)
    button_login.pack(pady=20)

    root.mainloop()

def admin_menu():
    def add_data(data_type):
        def submit_data():
            data = [entry.get() for entry in entries]
            if all(data):
                try:
                    cursor = connection.cursor()
                    if data_type == "knowledge":
                        cursor.execute('''
                                    INSERT INTO knowledge (energy, time, dimensions, advantage, model)
                                    VALUES (%s, %s, %s, %s, %s)
                                    ''', data)
                    if data_type == "assortment":
                        cursor.execute('''
                                    INSERT INTO main (brand, model, price, volume, year)
                                    VALUES (%s, %s, %s, %s, %s)
                                    ''', data)
                    print('Данные добавлены в таблицу main.')

                    connection.commit()
                    cursor.close()
                    messagebox.showinfo("Успех", "Данные успешно добавлены.")
                    data_window.destroy()
                except Exception as e:
                    messagebox.showerror("Ошибка", str(e))
                    print(str(e))
            else:
                messagebox.showwarning("Предупреждение", "Пожалуйста, заполните все поля.")

        data_window = tk.Toplevel(root)
        data_window.title(f"Пополнить {'базу знаний' if data_type == 'knowledge' else 'main'}")

        entries = []
        for i in range(5):
            label = tk.Label(data_window, text=f"Поле {i + 1}:")
            label.pack()
            entry = tk.Entry(data_window)
            entry.pack()
            entries.append(entry)

        submit_button = tk.Button(data_window, text="Добавить", command=submit_data)
        submit_button.pack()

    root = tk.Tk()
    root.title("Меню администратора")
    root.geometry("300x300")


    knowledge_button = tk.Button(root, text="Пополнить базу знаний", command=lambda: add_data("knowledge"))
    knowledge_button.pack(pady=10)

    assortment_button = tk.Button(root, text="Пополнить ассортимент", command=lambda: add_data("assortment"))
    assortment_button.pack(pady=10)

    root.mainloop()

def user_menu():
    def show_selection():
        value1 = combo1.get()
        value2 = combo2.get()
        value3 = combo3.get()

        query = """
           SELECT * FROM knowledge 
           WHERE brand = %s
           AND year = %s;
           """

        query1 = """
           SELECT *
           FROM main
           WHERE price BETWEEN %s AND %s
           AND brand = %s
           AND year = %s;
           """

        query2 = """
        SELECT brand FROM knowledge 
        """
        print("1")
        if value2 == "10-15 тыс":
            print("4")
            cursor.execute(query1, (10000, 15000, value1, value3))
            rows = cursor.fetchall()
            print("7")
            cursor.execute(query, (value1, value3))
            results = cursor.fetchall()
            for row in rows:
                messagebox.showinfo("Выбор", f"Вам подойдёт: {row}, почему? Ответ: {results[0]}")

        print("2")
        if value2 == "15-20 тыс":
            print("5")
            cursor.execute(query1, (15000, 20000, value1, value3))
            rows = cursor.fetchall()
            print("8")
            cursor.execute(query, (value1, value3))
            results = cursor.fetchall()
            for row in rows:
                messagebox.showinfo("Выбор", f"Вам подойдёт: {row}, почему? Ответ: {results[0]}")

        print("3")
        if value2 == "25-30 тыс":
            print("6")
            cursor.execute(query1, (25000, 30000, value1, value3))
            rows = cursor.fetchall()
            print("9")
            cursor.execute(query, (value1,value3))
            results = cursor.fetchall()
            for row in rows:
                messagebox.showinfo("Выбор", f"Вам подойдёт: {row}, почему? Ответ: {results[0]}")

    root = tk.Tk()
    root.title("Выбор")
    root.geometry("300x300")

    label1 = tk.Label(root, text="Выберите бренд:")
    label1.pack(pady=10)

    combo1 = ttk.Combobox(root, state='readonly')
    combo1['values'] = ("LG", "Bosch", "Samsung", "Whirlpool", "Ariston", "Daewoo", "Haier")
    combo1.current(0)
    combo1.pack(pady=10)

    label2 = tk.Label(root, text="Выберите ценовую категорию:")
    label2.pack(pady=10)

    combo2 = ttk.Combobox(root, state='readonly')
    combo2['values'] = ("10-15 тыс", "15-20 тыс", "25-30 тыс")
    combo2.current(0)
    combo2.pack(pady=10)

    label3 = tk.Label(root, text="Выберите год производства:")
    label3.pack(pady=10)
    combo3 = ttk.Combobox(root, state='readonly')
    combo3['values'] = ("2019", "2020", "2021", "2022")
    combo3.current(0)
    combo3.pack(pady=10)


    select_button = tk.Button(root, text="Показать предложеное", command=show_selection)
    select_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()