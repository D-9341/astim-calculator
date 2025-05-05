import os
import tkinter as tk
import tkinter.ttk as ttk
from pathlib import Path
from dotenv import load_dotenv
import psycopg2

CWD = Path(__file__).parents[0]
CWD = str(CWD)
load_dotenv(CWD + '\\vars.env')
PASSWORD = os.getenv('DB_PASS')

DIAM_MAP = {
    48: 0.15,
    57: 0.18,
    76: 0.24,
    89: 0.28,
    108: 0.34,
    133: 0.42,
    159: 0.50,
    219: 0.69,
    273: 0.86,
    325: 1.02,
    426: 1.34,
    530: 1.66,
    630: 1.98,
    720: 2.26,
    820: 2.57,
    920: 2.89,
    1020: 3.20,
    1220: 3.83,
    1420: 4.46,
}

_15MM_MAP = {
    48: 1.58,
    57: 1.88,
    76: 2.51,
    89: 2.93,
    108: 3.56,
    133: 4.39,
    159: 5.24,
    219: 7.22,
    273: 9.00,
    325: 10.72,
    426: 14.05,
    530: 17.47,
    630: 20.77,
    720: 24.74,
    820: 27.04,
    920: 30.33,
    1020: 33.63,
    1220: 40.22,
    1420: 46.82,
}

_20MM_MAP = {
    48: 2.11,
    57: 2.51,
    76: 3.34,
    89: 3.91,
    108: 4.75,
    133: 5.85,
    159: 6.99,
    219: 9.63,
    273: 12.00,
    325: 14.29,
    426: 18.73,
    530: 23.30,
    630: 27.69,
    720: 31.65,
    820: 36.05,
    920: 40.44,
    1020: 44.84,
    1220: 53.63,
    1420: 62.42,
}

_25MM_MAP = {
    48: 2.64,
    57: 3.13,
    76: 4.18,
    89: 4.89,
    108: 5.93,
    133: 7.31,
    159: 8.74,
    219: 12.03,
    273: 15.00,
    325: 17.86,
    426: 23.41,
    530: 29.12,
    630: 34.62,
    720: 39.56,
    820: 45.06,
    920: 50.55,
    1020: 56.05,
    1220: 67.04,
    1420: 78.03,
}

_30MM_MAP = {
    48: 3.17,
    57: 3.76,
    76: 5.01,
    89: 5.87,
    108: 7.12,
    133: 8.77,
    159: 10.48,
    219: 14.44,
    273: 18.00,
    325: 21.43,
    426: 28.09,
    530: 34.95,
    630: 41.54,
    720: 47.48,
    820: 54.07,
    920: 60.66,
    1020: 67.26,
    1220: 80.45,
    1420: 93.63,
}

_35MM_MAP = {
    48: 3.69,
    57: 4.39,
    76: 5.85,
    89: 6.85,
    108: 8.31,
    133: 10.23,
    159: 12.23,
    219: 16.85,
    273: 21.00,
    325: 25.00,
    426: 32.77,
    530: 40.77,
    630: 48.47,
    720: 55.39,
    820: 63.08,
    920: 70.78,
    1020: 78.47,
    1220: 93.85,
    1420: 109.24,
}

_40MM_MAP = {
    48: 4.22,
    57: 5.01,
    76: 6.68,
    89: 7.82,
    108: 9.48,
    133: 11.71,
    159: 14.06,
    219: 19.25,
    273: 24.00,
    325: 28.57,
    426: 37.45,
    530: 46.60,
    630: 55.39,
    720: 63.30,
    820: 72.09,
    920: 80.89,
    1020: 89.68,
    1220: 107.26,
    1420: 124.85,
}

_50MM_MAP = {
    48: 5.28,
    57: 6.26,
    76: 8.35,
    89: 9.78,
    108: 11.87,
    133: 14.62,
    159: 17.47,
    219: 24.07,
    273: 30.00,
    325: 35.72,
    426: 46.82,
    530: 58.25,
    630: 69.24,
    720: 79.13,
    820: 90.12,
    920: 101.11,
    1020: 112.10,
    1220: 134.08,
    1420: 156.06,
}

_60MM_MAP = {
    48: 6.33,
    57: 7.52,
    76: 10.02,
    89: 11.74,
    108: 14.24,
    133: 17.54,
    159: 20.97,
    219: 28.88,
    273: 36.00,
    325: 42.86,
    426: 56.18,
    530: 69.90,
    630: 83.08,
    720: 94.95,
    820: 108.14,
    920: 121.33,
    1020: 134.52,
    1220: 160.89,
    1420: 187.27,
}

root = tk.Tk()
root.geometry('500x900')
root.title('Калькулятор')

diam_label = ttk.Label(root, text = 'Введите диаметр трубы')
diam_label.pack(pady = 10)
diam_entry = ttk.Entry(root)
diam_entry.pack(pady = 10)

length_label = ttk.Label(root, text = 'Введите длину / длины труб (через +)')
length_label.pack(pady = 10)
length_entry = ttk.Entry(root)
length_entry.pack(pady = 10)

thickness_label = ttk.Label(root, text = 'Введите толщину изоляции')
thickness_label.pack(pady = 10)
thickness_entry = ttk.Entry(root)
thickness_entry.pack(pady = 10)

astim_price_label = ttk.Label(root, text = 'Введите цену астима или оставьте поле пустым')
astim_price_label.pack(pady = 10)
astim_price_entry = ttk.Entry(root)
astim_price_entry.pack(pady = 10)

total_length = 0
tonnage = 0
price = 0

def calculate():
    """
    Calculate the total tonnage, price and length of astim based on input diam, length and thickness.
    Also calculate the total tonnage, price and length of all input.
    If some data is not entered, display error message and return.
    If the entered data is incorrect, display error message and return.
    If the operation is not supported, display error message and return.
    """
    global total_length, tonnage, price
    try:
        diam = int(diam_entry.get())
        if diam not in DIAM_MAP.keys():
            diam_label.config(text = 'Такого диаметра нет', foreground = 'red')
            root.after(2000, lambda: diam_label.config(text = 'Введите диаметр трубы', foreground = 'black'))
            return
        if '*' in length_entry.get() or '-' in length_entry.get() or '/' in length_entry.get():
            if '*' in length_entry.get():
                operation = 'умножение'
            elif '-' in length_entry.get():
                operation = 'вычитание'
            elif '/' in length_entry.get():
                operation = 'деление'
            length_label.config(text = f'Неподдерживаемая операция: {operation}', foreground = 'red')
            root.after(2000, lambda: length_label.config(text = 'Введите длину / длины труб (через +)', foreground = 'black'))
            return
        lengths = list(map(float, length_entry.get().split('+')))
        length = sum(lengths)
        thickness = thickness_entry.get()
        if thickness not in ['15', '20', '25', '30', '35', '40', '50', '60']:
            thickness_label.config(text = 'Такой толщины нет', foreground = 'red')
            root.after(2000, lambda: thickness_label.config(text = 'Введите толщину изоляции', foreground = 'black'))
            return
        astim_price = int(astim_price_entry.get() or 595)
        match thickness:
            case '15':
                astim_tonnage = round(length * _15MM_MAP[diam], 1)
            case '20':
                astim_tonnage = round(length * _20MM_MAP[diam], 1)
            case '25':
                astim_tonnage = round(length * _25MM_MAP[diam], 1)
            case '30':
                astim_tonnage = round(length * _30MM_MAP[diam], 1)
            case '35':
                astim_tonnage = round(length * _35MM_MAP[diam], 1)
            case '40':
                astim_tonnage = round(length * _40MM_MAP[diam], 1)
            case '50':
                astim_tonnage = round(length * _50MM_MAP[diam], 1)
            case '60':
                astim_tonnage = round(length * _60MM_MAP[diam], 1)
        msqr = round(DIAM_MAP[diam] * length, 1)
        tonnage += astim_tonnage
        price += astim_tonnage * astim_price
        total_length += length
        result_label.config(text = f'Тоннаж астима: {astim_tonnage} кг \
                            \nСтоимость: {astim_tonnage * astim_price} руб \
                            \nПлощадь трубы: {msqr} м^2\n\nОбщий тоннаж: {tonnage} кг\
                            \nОбщая стоимость: {price} руб\nОбщая длина: {total_length} м \
                            \nГидротэк: {round(total_length * 0.8, 1)} кг \
                            \nТоннаж клея: {round(tonnage * 0.1, 1)} кг')
        write_to_database_button.config(state = 'enabled')
        write_to_database_label.config(text = 'Название камеры')
        write_to_database_entry.config(state = 'enabled')
    except Exception:
        result_label.config(text = 'Некоторые данные не были введены', foreground = 'red')
        root.after(2000, lambda: result_label.config(text = '', foreground = 'black'))

ttk.Button(root, text = 'Рассчитать', command = calculate).pack(pady = 10)
result_label = ttk.Label(root, text = '', font = 'Arial 15')
result_label.pack(pady = 10)

def clear_memory():
    """
    Resets all variables to their initial values, clears all input fields and 
    labels, and disables the 'Записать в базу данных' button.
    """
    global tonnage, price, total_length
    tonnage = price = total_length = 0
    result_label.config(text = '')
    write_to_database_button.config(state = 'disabled')
    write_to_database_label.config(text = '')
    write_to_database_entry.config(state = 'disabled')
    write_to_database_entry.delete(0, tk.END)
    diam_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    thickness_entry.delete(0, tk.END)
    astim_price_entry.delete(0, tk.END)

ttk.Button(root, text = 'Очистить память', command = clear_memory).pack(pady = 10)

def write_to_database(tonnage, price, total_length, name):
    """
    Writes the calculated results to the database.

    Inserts a new record into the 'results' table with the provided name, 
    total tonnage, total price, total length, hydrotec, and glue tonnage. 
    After inserting, it retrieves the generated ID of the new record and 
    updates the result label with a confirmation message.

    Parameters
    ----------
    tonnage: float
        The total tonnage of astim.
    price: float
        The total price of astim.
    total_length: float
        The total length of the pipes.
    name: str
        The name of the record to be inserted.
    """

    conn = psycopg2.connect(host = 'localhost', database = 'astim', user = 'postgres', password = PASSWORD, port = 5432)
    cur = conn.cursor()
    cur.execute("INSERT INTO results (name, total_tonnage, total_price, total_length, hydrotec, glue_tonnage) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id",
                (name, tonnage, price, total_length, round(total_length * 0.8, 1), round(tonnage * 0.1, 1)))
    conn.commit()
    result = cur.fetchone()[0]
    result_label.config(text = f'Запись с ID {result} добавлена')

def remove_from_database(id):
    """
    Removes a record from the database.

    Deletes a record from the 'results' table with the specified ID.

    Parameters
    ----------
    id: int
        The ID of the record to be deleted.
    """

    conn = psycopg2.connect(host = 'localhost', database = 'astim', user = 'postgres', password = PASSWORD, port = 5432)
    cur = conn.cursor()
    cur.execute("DELETE FROM results WHERE id = %s", (id))
    conn.commit()

def get_from_database(id):
    """
    Retrieves a record from the database by its ID.

    Given a record ID, queries the 'results' table and updates the result label with the values of the record.
    If a record with the given ID does not exist, the result label is updated with an error message.

    Parameters
    ----------
    id: int
        The ID of the record to be retrieved.
    """
    conn = psycopg2.connect(host = 'localhost', database = 'astim', user = 'postgres', password = PASSWORD, port = 5432)
    cur = conn.cursor()
    cur.execute("SELECT * FROM results WHERE id = %s", (id))
    result = cur.fetchone()
    try:
        result_label.config(text = f'Общий тоннаж астима: {result[2]} кг\nОбщая стоимость: {result[3]} руб\nОбщая длина: {result[4]} м\nГидротэк: {result[5]} кг\nТоннаж клея: {result[6]} кг', foreground = 'black')
    except Exception:
        result_label.config(text = 'Записи с данным ID не существует', foreground = 'red')

write_to_database_label = ttk.Label(root, text = '')
write_to_database_label.pack(pady = 10)
write_to_database_entry = ttk.Entry(root, state = 'disabled')
write_to_database_entry.pack(pady = 10)
write_to_database_button = ttk.Button(root, text = 'Записать в базу данных', command = lambda: write_to_database(tonnage, price, total_length, write_to_database_entry.get()), state = 'disabled')
write_to_database_button.pack(pady = 10)

get_from_database_label = ttk.Label(root, text = 'Введите ID записи для её просмотра')
get_from_database_label.pack(pady = 10)
get_from_database_entry = ttk.Entry(root)
get_from_database_entry.pack(pady = 10)
get_from_database_button = ttk.Button(root, text = 'Посмотреть записанные данные', command = lambda: get_from_database(get_from_database_entry.get()))
get_from_database_button.pack(pady = 10)

remove_from_database_label = ttk.Label(root, text = 'Введите ID записи для удаления')
remove_from_database_label.pack(pady = 10)
remove_from_database_entry = ttk.Entry(root)
remove_from_database_entry.pack(pady = 10)
remove_from_database_button = ttk.Button(root, text = 'Удалить из базы данных', command = lambda: remove_from_database(remove_from_database_entry.get()))
remove_from_database_button.pack(pady = 10)

root.mainloop()
