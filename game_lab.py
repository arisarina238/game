import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import random
import json
import re
import sys
from tkinter import filedialog


def create_window_with_background(window, background_image_path):
    """Создание окна с заданным фоном."""
    # Загрузка изображения для фона окна
    try:
        background_image = Image.open(background_image_path)  # Открываем изображение
        background_image = background_image.resize((1280, 720))  # Изменяем размер изображения
        background_photo = ImageTk.PhotoImage(background_image)
    except FileNotFoundError:
        print(f"Файл не найден: {background_image_path}")  # Сообщаем об ошибке
        background_photo = None

    # Установка фона, если изображение успешно загружено
    if background_photo is not None:
        background_label = tk.Label(window, image=background_photo)
        background_label.image = background_photo  # Сохраняем ссылку на изображение, чтобы избежать сборки мусора
        background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Занимаем всю область окна

    return window


def load_image(image_path, size):
    """Загрузка и изменение размера изображения."""
    image = Image.open(image_path)  # Загружаем изображение
    image = image.resize(size)
    return ImageTk.PhotoImage(image)


def open_window(window1, window2):
    """Функция для закрытия одного окна и открытия второго."""
    window1.withdraw()  # Скрыть первое окно
    window2.deiconify()  # Показать второе окно


def open_main_window():
    """Открытие основного окна приложения."""
    login_window.withdraw()
    main_window.deiconify()


def open_choice_window():
    """Открытие окна выбора после основного окна."""
    main_window.withdraw()
    choice_window.deiconify()


def open_win_window(computer_choice):
    """Функция для открытия окна в случае победы пользователя
    (если это последний раунд).
    """
    global photo_win1  # глобальная переменная для хранения изображения
    choice_window.withdraw()  # Скрыть окно выбора
    win_window.deiconify()

    # Создаем Canvas
    canvas_win1 = tk.Canvas(win_window, width=320, height=30, relief=tk.FLAT, borderwidth=0, highlightthickness=0)
    canvas_win1.place(x=460, y=105)

    # Загружаем изображение
    image = Image.open("images/choice+computer_win_window.png")
    photo_win1 = ImageTk.PhotoImage(image)  # сохраняем ссылку на изображение

    # Добавляем изображение на Canvas
    canvas_win1.create_image(0, 0, anchor=tk.NW, image=photo_win1)

    # Добавляем текст на Canvas
    canvas_win1.create_text(190, 15, text=f"Компьютер выбрал: {computer_choice}", font=("Arial", 14),
                            fill="white")


def open_lose_window(computer_choice):
    """Функция для открытия окна в случае проигрыша пользователя
    (если это последний раунд).
    """
    global photo_lose1  # глобальная переменная для хранения изображения
    choice_window.withdraw()
    lose_window.deiconify()

    # Создаем Canvas
    canvas_lose1 = tk.Canvas(lose_window, width=280, height=40, relief=tk.FLAT, borderwidth=0, highlightthickness=0)
    canvas_lose1.place(x=475, y=109)

    # Загружаем изображение
    image = Image.open("images/choice+computer_lose_window.png")
    photo_lose1 = ImageTk.PhotoImage(image)

    # Добавляем изображение на Canvas
    canvas_lose1.create_image(0, 0, anchor=tk.NW, image=photo_lose1)

    # Добавляем текст на Canvas
    canvas_lose1.create_text(135, 20, text=f"Компьютер выбрал: {computer_choice}", font=("Arial", 14),
                             fill="white")


def open_non_window(computer_choice):
    """Функция для открытия окна в случае результата "ничья"
    (если это последний раунд).
    """
    global photo_non1  # глобальная переменная для хранения изображения
    choice_window.withdraw()
    non_window.deiconify()

    canvas_non1 = tk.Canvas(non_window, width=270, height=50, relief=tk.FLAT, borderwidth=0, highlightthickness=0)
    canvas_non1.place(x=490, y=255)

    # Загружаем изображение
    image = Image.open("images/choice+computer_non_window.png")
    photo_non1 = ImageTk.PhotoImage(image)

    # Добавляем изображение на Canvas
    canvas_non1.create_image(0, 0, anchor=tk.NW, image=photo_non1)

    # Добавляем текст на Canvas
    canvas_non1.create_text(130, 25, text=f"Компьютер выбрал: {computer_choice}", font=("Arial", 14),
                            fill="white")


def open_mainnext_window(window):
    """Открытие основного окна или окна выбора в зависимости от флага.
    """
    if flag:  # Проверка значения глобальной переменной flag
        window.withdraw()
        main_window.deiconify()
    else:
        window.withdraw()
        choice_window.deiconify()


def open_window_rules(window):
    """Открытие окна с правилами игры и скрытие окна,
    которое было передано.
    """
    window.withdraw()
    rules_window.deiconify()


def open_window_advances(window):
    """Открытие окна с информацией о продвижениях и скрытие окна,
    которое было передано.
    """
    window.withdraw()
    advances_window.deiconify()


def open_window_statistics(window):
    """Открытие окна со статистикой игры и скрытие окна,
    которое было передано."""
    window.withdraw()  # Скрыть текущее окно
    statistics_window.deiconify()  # Показать окно со статистикой


def return_window_main(window):
    """Возврат к основному окну и скрытие окна,
    которое было передано."""
    window.withdraw()  # Скрыть текущее окно
    main_window.deiconify()  # Показать основное окно


# Функция для перехода на экран регистрации
def go_to_registration(event=None):
    """Функция для перехода на окно регистрации,
    если пользователь не зарегистрирован."""
    login_window.withdraw()
    registr_window.deiconify()


# Функция для перехода на экран входа
def go_to_login(event=None):
    """Функция для перехода на окно входа,
    если пользователь имеет аккаунт."""
    registr_window.withdraw()
    login_window.deiconify()


# Файл для хранения данных пользователей
USERS_FILE = 'users.json'
current_player_login = None  # Глобальная переменная для хранения логина текущего игрока


# Функция для загрузки пользователей из файла
def load_users():
    """Загрузка пользователей из файла JSON."""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as file:
            return json.load(file)
    return {}


# Функция для сохранения пользователей в файл
def save_users(users):
    """Сохранение пользователей в файл JSON."""
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=4)  # сохраняем данные пользователей в файл


def is_valid_username(username):
    """Проверка корректности логина."""
    # Проверяем, что логин состоит из букв и цифр, длина от 3 до 20 символов
    return bool(re.match(r'^[\w]{3,20}$', username))

def is_valid_password(password):
    """Проверка корректности пароля."""
    # Проверяем, что пароль длиной от 7 до 20 символов, содержит хотя бы одну букву, одну цифру и один специальный символ
    return (6 < len(password) <= 20 and
            bool(re.search(r'[a-zA-Z]', password)) and
            bool(re.search(r'[0-9]', password)))


def is_valid_email(email):
    """Проверка корректности адреса электронной почты."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # регулярное выражение для проверки email
    return re.match(email_regex, email) is not None  # проверяем соответствие регулярному выражению


def register():
    """Регистрация нового пользователя."""
    email = entry_registr_email.get()
    username = entry_registr_username.get()
    password1 = entry_registr_password1.get()
    password2 = entry_registr_password2.get()

    if email and username and password1 and password2:  # проверяем, что все поля заполнены
        if not is_valid_email(email):
            messagebox.showerror("Ошибка", "Введите корректный адрес электронной почты.")
            return

        if not is_valid_username(username):
            messagebox.showerror("Ошибка", "Логин должен содержать хотя бы одну букву.")
            return

        if not is_valid_password(password1):
            messagebox.showerror("Ошибка",
                                 "Пароль должен содержать минимум 8 символов, включая хотя бы одну букву и одну цифру.")
            return

        users = load_users()  # загружаем существующих пользователей
        if username in users:  # проверяем, существует ли пользователь с таким именем
            messagebox.showerror("Ошибка", "Пользователь с таким именем уже существует.")
            return
        elif password1 != password2:
            messagebox.showerror("Ошибка", "Пароли не совпадают.")
            return

        # Сохраняем нового пользователя
        users[username] = {
            "email": email,
            "password": password1,
            "wins": 0,  # начальное количество побед
            "losses": 0  # начальное количество поражений
        }
        save_users(users)
        messagebox.showinfo("Успех", "Регистрация прошла успешно!")
        clear_entries()  # очищаем поля ввода
    else:
        messagebox.showwarning("Предупреждение", "Пожалуйста, заполните все поля.")


def login():
    """Вход пользователя в систему."""
    global current_player_login  # используем глобальную переменную
    username = entry_login_username.get()  # получаем логин из поля ввода
    password = entry_login_password.get()  # получаем пароль из поля ввода

    player_data = load_users()

    if player_data is None:
        player_data = {}

    if username in player_data:
        if player_data[username]["password"] == password:
            current_player_login = username  # Сохраняем логин игрока
            clear_entries()  # очищаем поля
            show_loading_screen()  # показать экран загрузки

            update_achievements_display()  # вызываем функцию для обновления достижений

        else:
            messagebox.showerror("Ошибка", "Неверный пароль.")
    else:
        messagebox.showerror("Ошибка", "Пользователь с таким именем не найден.")


# Функция для загрузки данных игроков
def load_player_data(file_path):
    """Загрузка данных игрока из JSON-файла."""
    if not os.path.exists(file_path):  # проверяем, существует ли указанный файл
        return None
    with open(file_path, 'r') as file:
        return json.load(file)  # загружаем и возвращаем данные из файла


# Функция для сохранения данных игрока в JSON-файл
def save_player_data(file_path, data):
    """Сохранение данных игрока в JSON-файл."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def get_player_login():
    """Получение логина игрока, либо из файла, либо создаем нового."""
    file_name = "users.json"  # имя файла для хранения данных игроков

    # Загружаем данные игроков
    player_data = load_player_data(file_name)

    if player_data is None:
        player_data = {}  # если данных нет, инициализируем пустой словарь

    # Проверяем, есть ли логины в файле
    if player_data:
        # Если есть логины, берем первый из них
        player_login = next(iter(player_data))
        print(f"Добро пожаловать обратно, {player_login}!")
    else:
        # Если нет логинов, создаем нового пользователя
        player_login = input("Введите логин для нового игрока: ")  # запрос логина у пользователя
        print(f"Создан новый аккаунт для {player_login}.")
        player_data[player_login] = {"email": "", "password": "", "wins": 0,
                                     "losses": 0}  # начальное количество побед и проигрышей

    # сохраняем данные в файл
    save_player_data(file_name, player_data)

    return player_login


def increase_wins():
    """Увеличение количества побед для текущего игрока."""
    if current_player_login is None:
        print("Ошибка: игрок не вошел в систему.")
        return

    users = load_users()

    if current_player_login in users:
        users[current_player_login]['wins'] += 1
        save_users(users)
        print(f"Количество побед для {current_player_login} увеличено. Теперь: {users[current_player_login]['wins']}")
    else:
        print(f"Ошибка: игрок {current_player_login} не найден.")


def increase_losses():
    """Увеличение количества проигрышей для текущего игрока."""
    if current_player_login is None:
        print("Ошибка: игрок не вошел в систему.")
        return

    users = load_users()
    if current_player_login in users:
        users[current_player_login]['losses'] += 1
        save_users(users)
        print(
            f"Количество проигрышей для {current_player_login} увеличено. Теперь: {users[current_player_login]['losses']}")
    else:
        print(f"Ошибка: игрок {current_player_login} не найден.")


def play_game(user_choice):
    """Игра с выбором пользователя и подсчетом побед."""
    computer_choice = random.choice(['Камень', 'Ножницы', 'Бумага'])

    global flag, count

    if count < num_rounds:
        if user_choice == computer_choice:
            open_non_window(computer_choice)
            flag = False
        elif (user_choice == 'Камень' and computer_choice == 'Ножницы') or \
                (user_choice == 'Ножницы' and computer_choice == 'Бумага') or \
                (user_choice == 'Бумага' and computer_choice == 'Камень'):
            open_win_window(computer_choice)
            increase_wins()  # Увеличиваем количество побед
            flag = False
        else:
            open_lose_window(computer_choice)
            increase_losses()  # Увеличиваем количество проигрышей
            flag = False
        update_achievements_display()  # Обновляем отображение достижений
        count += 1

        print("flag=false", count)

    else:
        if user_choice == computer_choice:
            open_non_window(computer_choice)
            flag = True
        elif (user_choice == 'Камень' and computer_choice == 'Ножницы') or \
                (user_choice == 'Ножницы' and computer_choice == 'Бумага') or \
                (user_choice == 'Бумага' and computer_choice == 'Камень'):
            open_win_window(computer_choice)
            flag = True
            increase_wins()  # Увеличиваем количество побед
        else:
            open_lose_window(computer_choice)
            flag = True
            increase_losses()  # Увеличиваем количество проигрышей
        update_achievements_display()  # Обновляем отображение достижений

        print("flag=true", count)


def handle_start_button():
    """Открывает окно для ввода количества раундов.
    Эта функция создает новое окно, в котором пользователь может ввести количество раундов для игры.
    После ввода и подтверждения, окно закрывается и начинается игра.
    """
    global num_rounds  # объявляем переменную num_rounds глобальной
    main_window.withdraw()
    round_input_window = tk.Toplevel()
    round_input_window.geometry("1280x720+200+200")
    round_input_window.title("Количество раундов")

    round_background_path = os.path.join("images", "ввод_раундов.png")

    round_input_window = create_window_with_background(round_input_window, round_background_path)

    # Создаем поле ввода для количества раундов
    round_input_entry = tk.Entry(round_input_window, bg="#252850", fg="white", insertbackground="white", width=5,
                                 font=("Arial", 20))
    round_input_entry.place(x=975, y=21)  # Устанавливаем позицию поля ввода

    def start_game():
        """Запускает игру после ввода количества раундов.
        Проверяет корректность введенного значения, инициализирует количество раундов и сбрасывает счетчик.
        Если ввод некорректен, выводит сообщение об ошибке.
        """
        global num_rounds, count  # объявляем переменные глобальными
        try:
            num_rounds = int(round_input_entry.get())
            if num_rounds <= 0:
                messagebox.showerror("Ошибка", "Количество раундов должно быть больше 0.")
                return
            count = 1  # сбрасываем счетчик раундов
            round_input_window.destroy()
            open_choice_window()  # Открываем окно выбора
        except ValueError:  # Обрабатываем случай, если ввод некорректен
            messagebox.showerror("Ошибка", "Некорректный ввод. Введите число.")

    image_input_start = "images/ввод_данных_кнопка_начать.png"
    size_input_start = (274, 80)  # Размер кнопки

    original_image = Image.open(image_input_start)
    resized_image = original_image.resize(size_input_start)
    photo_input_start = ImageTk.PhotoImage(resized_image)

    button = tk.Button(round_input_window, image=photo_input_start, command=start_game, width=274, height=80)
    button.image = photo_input_start  # Сохраняем ссылку на изображение, чтобы избежать его сборки мусора
    button.place(x=23, y=617)


def calculate_statistics():
    """Расчет статистики игроков для отображения."""
    users = load_users()
    statistics = []

    # Проходим по каждому пользователю и его данным
    for username, data in users.items():
        wins = data.get('wins', 0)  # получаем количество побед
        losses = data.get('losses', 0)  # получаем количество проигрышей
        total_games = wins + losses

        # Вычисляем процент побед и проигрышей
        if total_games > 0:
            win_percentage = (wins / total_games) * 100
            loss_percentage = (losses / total_games) * 100
        else:
            win_percentage = 0
            loss_percentage = 0

        if wins >= 10:  # Условие для отображения только игроков с 10 и более победами
            statistics.append({
                'username': username,
                'wins': wins,
                'losses': losses,
                'win_percentage': win_percentage,
                'loss_percentage': loss_percentage
            })

    # Сортируем статистику по количеству побед в порядке убывания
    statistics.sort(key=lambda x: x['wins'], reverse=True)

    # Добавляем нумерацию
    for index, stat in enumerate(statistics):
        stat['rank'] = index + 1  # Нумерация с 1

    return statistics


def display_statistics(statistics_window):
    """Отображение статистики игроков в указанном окне.
    Эта функция создает интерфейс для отображения статистики игроков, включая количество побед,
    проигрышей и проценты, в указанном окне."""

    statistics = calculate_statistics()

    # Создаем фрейм для статистики
    stats_frame = tk.Frame(statistics_window, bg="#000000")
    stats_frame.place(relx=0.5, rely=0.5, anchor='center')

    # Заголовки колонок
    headers = ["Рейтинг", "Логин", "Победы", "Проигрыши", "Процент побед", "Процент проигрышей"]
    for idx, header in enumerate(headers):
        label = tk.Label(stats_frame, text=header, fg="#FFFFFF", bg="#000000", font=('Arial', 16))
        label.grid(row=1, column=idx, padx=10, pady=5)

    # Ограничение на количество отображаемых игроков
    max_displayed_players = 8
    statistics_to_display = statistics[:max_displayed_players]

    # Заполняем данные
    for idx, stat in enumerate(statistics_to_display):
        tk.Label(stats_frame, text=stat['rank'], fg="#FFFFFF", bg="#000000", font=('Arial', 16)).grid(row=idx + 2,
                                                                                                      column=0, padx=10,
                                                                                                      pady=2)
        tk.Label(stats_frame, text=stat['username'], fg="#FFFFFF", bg="#000000", font=('Arial', 16)).grid(row=idx + 2,
                                                                                                          column=1,
                                                                                                          padx=10,
                                                                                                          pady=2)
        tk.Label(stats_frame, text=stat['wins'], fg="#FFFFFF", bg="#000000", font=('Arial', 16)).grid(row=idx + 2,
                                                                                                      column=2, padx=10,
                                                                                                      pady=2)
        tk.Label(stats_frame, text=stat['losses'], fg="#FFFFFF", bg="#000000", font=('Arial', 16)).grid(row=idx + 2,
                                                                                                        column=3,
                                                                                                        padx=10, pady=2)
        tk.Label(stats_frame, text=f"{stat['win_percentage']:.2f}%", fg="#FFFFFF", bg="#000000",
                 font=('Arial', 16)).grid(row=idx + 2, column=4, padx=10, pady=2)
        tk.Label(stats_frame, text=f"{stat['loss_percentage']:.2f}%", fg="#FFFFFF", bg="#000000",
                 font=('Arial', 16)).grid(row=idx + 2, column=5, padx=10, pady=2)


def save_statistics(statistics):
    """Сохраняет статистику игроков в текстовый файл."""
    # Открываем диалоговое окно для выбора места сохранения файла
    output_file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",  # расширение по умолчанию
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],  # Типы файлов
        title="Сохранить статистику как"
    )

    # Проверяем, выбрал ли пользователь файл
    if output_file_path:
        try:
            with open(output_file_path, 'w', encoding='utf-8') as file:
                # Записываем заголовки
                file.write("Рейтинг, Логин, Победы, Проигрыши, Процент побед, Процент проигрышей\n")
                # Записываем данные игроков с нумерацией
                for index, stat in enumerate(statistics):
                    file.write(f"{index + 1}, {stat['username']}, {stat['wins']}, "
                               f"{stat['losses']}, {stat['win_percentage']:.2f}%, "
                               f"{stat['loss_percentage']:.2f}%\n")

            print(f"Статистика успешно сохранена в {output_file_path}")
        except Exception as e:
            print(f"Ошибка при сохранении статистики: {e}")


# Функция для получения достижений на основе количества побед
def check_achievements():
    """Проверяет достижения игрока на основе количества его побед.
    Эта функция загружает данные пользователей и проверяет, сколько побед
    у текущего игрока. На основе этого она возвращает список мотивационных предложений,
    соответствующих количеству побед."""

    if current_player_login is None:
        return []

    users = load_users()
    if current_player_login not in users:
        return []

    wins = users[current_player_login]['wins'] # получаем количество побед текущего игрока
    achievements = []

    if wins >= 200:
        achievements.append("Вы оставили яркий след!")
    elif wins >= 100:
        achievements.append("Превосходные навыки!")
    elif wins >= 50:
        achievements.append("Вы - настоящий герой игры!")
    elif wins >= 30:
        achievements.append("Противник не устоит!")
    elif wins >= 10:
        achievements.append("Вы на правильном пути!")
    elif wins >= 5:
        achievements.append("Продолжайте в том же духе!")
    elif wins >= 1:
        achievements.append("Вперед к победе")

    return achievements


def achievements_parts():
    """Получает достижения на основе количества побед игрока.
    Эта функция загружает данные пользователей и проверяет, сколько побед
    у текущего игрока. На основе этого она возвращает список достижений,
    соответствующих количеству побед."""
    if current_player_login is None:
        return []

    users = load_users()
    if current_player_login not in users:
        return []

    wins = users[current_player_login]['wins']

    achievements_parts = []

    if wins >= 200:
        achievements_parts.append("Легенда игры")
    elif wins >= 100:
        achievements_parts.append("Магистр")
    elif wins >= 50:
        achievements_parts.append("Супергерой")
    elif wins >= 30:
        achievements_parts.append("Непобедимый")
    elif wins >= 10:
        achievements_parts.append("Стратег")
    elif wins >= 5:
        achievements_parts.append("Удачливый старт")
    elif wins >= 1:
        achievements_parts.append("Начинающий")

    return achievements_parts


# Обновление отображения достижений
def update_achievements_display():
    """Обновляет отображение достижений игрока."""
    achievements = check_achievements()
    achievements_part = achievements_parts()

    # Формируем текст для достижений
    if achievements:
        achievements_text = "\n".join(achievements)
    else:
        achievements_text = "Нет достижений."

    if achievements_part:
        achievements_parts_text = "\n".join(achievements_part)
    else:
        achievements_parts_text = "Нет достижений."

    # Удаляем старый текст перед добавлением нового
    achievements_canvas.delete("text")
    achievements_canvas_part.delete("text")

    # Обновляем текст меток
    achievements_canvas.create_text(145, 37, anchor=tk.CENTER, text=achievements_text, fill="white",
                                    font=("BlackerSans Pro It Variable", 14), tags="text")

    achievements_canvas_part.create_text(80, 20, anchor=tk.CENTER, text=achievements_parts_text, fill="white",
                                         font=("BlackerSans Pro It Variable", 14), tags="text")


def show_loading_screen():
    """Отображает окно загрузки с фоновым изображением.
    Эта функция создает новое окно загрузки, устанавливает фоновое изображение
    и запускает таймер, чтобы через 5 секунд закрыть окно загрузки и открыть
    главное окно приложения"""
    # Создаем окно загрузки
    loading_window = tk.Toplevel(start_window)
    loading_window.geometry("1070x595+300+300")
    loading_window.title("Окно загрузки")

    login_window.withdraw()

    background_path_loading = os.path.join("images", "окно_загрузки.png")

    try:
        background_image_loading = Image.open(background_path_loading)

        loading_window.background_photo_loading = ImageTk.PhotoImage(background_image_loading)
    except FileNotFoundError:
        print(f"Файл не найден: {background_path_loading}")
        loading_window.background_photo_loading = None  # Установим значение по умолчанию

    # Установка фона
    if loading_window.background_photo_loading:
        background_label_loading = tk.Label(loading_window, image=loading_window.background_photo_loading)
        background_label_loading.place(relwidth=1, relheight=1)
    else:

        tk.Label(loading_window, text="Изображение не найдено", font=("Arial", 20)).pack()

    loading_window.after(5000, lambda: [loading_window.destroy(), open_main_window()])


def exit_game():
    """Выход из игры с подтверждением.
    Эта функция отображает диалоговое окно для подтверждения выхода из игры.
    Если пользователь подтверждает, закрывает главное окно и завершает программу"""
    # Подтверждение выхода
    if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти из игры?"):
        options_window.destroy()  # закрывает главное окно и завершает программу
        sys.exit()


def toggle_password_visibility1(entry, button):
    """Переключает видимость пароля для первого поля ввода.
    Эта функция проверяет текущее состояние видимости пароля в поле ввода
    и переключает его. Если пароль скрыт, он становится видимым,
    и изображение кнопки меняется на открытый замок. Если пароль виден,
    он скрывается, и изображение кнопки меняется на закрытый замок."""
    # Проверяем текущее состояние и переключаем его
    if entry.cget('show') == '*':
        entry.config(show='')  # Показываем пароль
        button.config(image=lock_open_image_resized1)  # Меняем изображение на открытый замок
    else:
        entry.config(show='*')  # Скрываем пароль
        button.config(image=lock_closed_image_resized1)  # Меняем изображение на закрытый замок


def toggle_password_visibility2(entry, button):
    """Переключает видимость пароля для второго поля ввода.
    Эта функция работает аналогично toggle_password_visibility1, но для
    второго поля ввода. Она меняет состояние видимости пароля и изображение
    кнопки в зависимости от текущего состояния."""
    # Проверяем текущее состояние и переключаем его
    if entry.cget('show') == '*':
        entry.config(show='')  # Показываем пароль
        button.config(image=lock_open_image_resized2)  # Меняем изображение на открытый замок
    else:
        entry.config(show='*')  # Скрываем пароль
        button.config(image=lock_closed_image_resized2)  # Меняем изображение на закрытый замок


# Создаем окно старта
start_window = tk.Tk()
start_window.geometry("1280x720+200+200")
start_window.title("Стартовое окно")

# Путь к изображению для фона основного окна
background_path = os.path.join("images", "back2.png")


try:
    background_image = Image.open(background_path)
    background_photo = ImageTk.PhotoImage(background_image)
except FileNotFoundError:
    print(f"Файл не найден: {background_path}")
    background_photo = None

background_label = tk.Label(start_window, image=background_photo)
background_label.place(relwidth=1, relheight=1)

image_welcome = "images/рады_видеть_тебя.png"
size_welcome = (406, 85)
photo_welcome = load_image(image_welcome, size_welcome)

start_label = tk.Label(start_window, image=photo_welcome)
start_label.place(x=452, y=229)

image_start = "images/Снимок экрана 2024-12-10 092956.png"
size_start = (270, 66)
button_photo = load_image(image_start, size_start)

# Кнопка "Старт"
start_button = tk.Button(start_window, image=button_photo, relief=tk.FLAT, borderwidth=0, highlightthickness=0,
                         command=lambda: open_window(start_window, options_window),
                         font=("Helvetica", 24), width=270, height=66)
start_button.place(x=509, y=475)


# Создаем окно с вариантами
options_window = tk.Toplevel(start_window)
options_window.geometry("1280x720+200+200")
options_window.title("Выбор действия")
options_window.withdraw()  # Скрыть окно с вариантами изначально

# Путь к изображению для фона окна выбора
options_background_path = os.path.join("images", "Прямоугольник 17.png")

options_window = create_window_with_background(options_window, options_background_path)

# Загружаем изображение
image_choice_title = "images\окно_выбора_кнб.png"
size_choice_title = (370, 200)
photo_choice_title = load_image(image_choice_title, size_choice_title)
# Создаем метку и вставляем в нее изображение
label = tk.Label(options_window, image=photo_choice_title, borderwidth=0, highlightthickness=0)
label.place(x=425, y=15)

# Кнопка "Войти"
image_options_login = "images/Вход.png"
size_options_login = (270, 66)
photo_options_login = load_image(image_options_login, size_options_login)
login_button = tk.Button(options_window, image=photo_options_login,
                         command=lambda: open_window(options_window, login_window),
                         font=("Helvetica", 18))
login_button.place(x=499, y=366)


image_options_registr = "images/Регистрация.png"
size_options_registr = (270, 66)
photo_options_registr = load_image(image_options_registr, size_options_registr)

register_button = tk.Button(options_window, image=photo_options_registr,
                            command=lambda: open_window(options_window, registr_window),
                            font=("Helvetica", 18))
register_button.place(x=499, y=467)


image_options_exit = "images/кнопка_выйти_из_игры.png"
size_options_exit = (274, 66)
photo_options_exit = load_image(image_options_exit, size_options_exit)
login_buttonexit = tk.Button(options_window, image=photo_options_exit,
                             command=exit_game,
                             font=("Helvetica", 18))
login_buttonexit.place(x=497, y=566)

# Создаем окно логина
login_window = tk.Toplevel(start_window)
login_window.geometry("1280x720+200+200")
login_window.title("Логин")
login_window.withdraw()  # Скрыть окно логина изначально

login_background_path = os.path.join("images", "Окно_входа.png")

login_window = create_window_with_background(login_window, login_background_path)

# Поля ввода для логина
entry_login_username = tk.Entry(login_window, width=45)
entry_login_username.place(x=505, y=325)

# Загружаем изображения замка
lock_closed_image3 = Image.open("images/замок_3.png")
lock_open_image3 = Image.open("images/замок_33.png")

lock_closed_image_resized3 = ImageTk.PhotoImage(lock_closed_image3.resize((24, 24)))  # Закрытый замок
lock_open_image_resized3 = ImageTk.PhotoImage(lock_open_image3.resize((20, 22)))  # открытый замок

button_toggle_password3 = tk.Button(login_window, image=lock_closed_image_resized3, width=24, height=24, relief=tk.FLAT,
                                    borderwidth=0,
                                    highlightthickness=0,
                                    command=lambda: toggle_password_visibility1(entry_login_password,
                                                                                button_toggle_password3))
button_toggle_password3.place(x=570, y=370)

# Поля ввода для пароля
entry_login_password = tk.Entry(login_window, show='*', width=45)
entry_login_password.place(x=505, y=410)

# Кнопка "Войти"
image_login_go = "images/войти_войти.png"
size_login_go = (280, 66)
photo_login_go = load_image(image_login_go, size_login_go)

tk.Button(login_window, width=280, height=58, image=photo_login_go, command=login).place(x=500, y=490)

# Создание Canvas с заданными размерами
canvas_width = 260
canvas_height = 58
canvas = tk.Canvas(login_window, width=canvas_width, height=canvas_height,
                   highlightthickness=0)
canvas.place(x=510, y=555)

# Загружаем изображение для фона гиперссылки
link_background_path = os.path.join("images", "Зарегистрироваться.png")
link_background_image = Image.open(link_background_path)
link_background_image = link_background_image.resize((canvas_width, canvas_height))
link_background_photo = ImageTk.PhotoImage(link_background_image)

# Добавляем изображение на Canvas
canvas.create_image(0, 0, anchor="nw", image=link_background_photo)

# Добавляем текст на Canvas
text_id = canvas.create_text(canvas_width / 2, canvas_height / 2, text="Нет аккаунта? Зарегистрироваться", fill="white",
                             anchor="center", font=("Arial", 12))

# Привязываем событие нажатия на гиперссылку
canvas.tag_bind(text_id, "<Button-1>", go_to_registration)


# Создаем окно регистрации
registr_window = tk.Toplevel(start_window)
registr_window.geometry("1280x720+200+200")
registr_window.title("Регистрация")
registr_window.withdraw()  # Скрыть окно регистрации изначально

# Загрузка изображения для фона окна регистрации
registr_background_path = os.path.join("images", "Окно_регистрации.png")
try:
    registr_background_image = Image.open(registr_background_path)
    registr_background_photo = ImageTk.PhotoImage(registr_background_image)
except FileNotFoundError:
    print(f"Файл не найден: {registr_background_path}")
    registr_background_photo = None  # Установим значение по умолчанию

# Установка фона для окна регистрации
background_registr = tk.Label(registr_window, image=registr_background_photo)
background_registr.place(relwidth=1, relheight=1)  # Занимает всю область окна


def clear_entries():
    """Функция для очистки полей ввода"""
    entry_registr_email.delete(0, tk.END)
    entry_registr_username.delete(0, tk.END)
    entry_registr_password1.delete(0, tk.END)
    entry_registr_password2.delete(0, tk.END)
    entry_login_username.delete(0, tk.END)
    entry_login_password.delete(0, tk.END)


# Поля ввода для регистрации
entry_registr_email = tk.Entry(registr_window, width=45)
entry_registr_email.place(x=500, y=242)

entry_registr_username = tk.Entry(registr_window, width=45)
entry_registr_username.place(x=500, y=320)

# Загружаем изображения замка для первого пароля
lock_closed_image1 = Image.open("images/замок_1.png")  # Закрытый замок для пароля 1
lock_open_image1 = Image.open("images/замок_11.png")  # Открытый замок для пароля 1

# Изменяем размер изображений для первого пароля
lock_closed_image_resized1 = ImageTk.PhotoImage(lock_closed_image1.resize((24, 24)))  # Закрытый замок
lock_open_image_resized1 = ImageTk.PhotoImage(lock_open_image1.resize((24, 24)))  # Открытый замок

# Загружаем изображения замка для второго пароля
lock_closed_image2 = Image.open("images/замок_2.png")  # Закрытый замок для пароля 2
lock_open_image2 = Image.open("images/замок_22.png")  # Открытый замок для пароля 2

# Изменяем размер изображений для второго пароля
lock_closed_image_resized2 = ImageTk.PhotoImage(lock_closed_image2.resize((18, 22)))  # Закрытый замок
lock_open_image_resized2 = ImageTk.PhotoImage(lock_open_image2.resize((18, 22)))  # Открытый замок

# Поле для ввода пароля 1
entry_registr_password1 = tk.Entry(registr_window, show='*', width=45)
entry_registr_password1.place(x=500, y=397)

# Кнопка для переключения видимости пароля 1
button_toggle_password1 = tk.Button(registr_window, image=lock_closed_image_resized1, width=24, height=24,
                                    relief=tk.FLAT, borderwidth=0,
                                    highlightthickness=0,
                                    command=lambda: toggle_password_visibility1(entry_registr_password1,
                                                                                button_toggle_password1))
button_toggle_password1.place(x=567, y=357)

# Поле для ввода пароля 2
entry_registr_password2 = tk.Entry(registr_window, show='*', width=45)
entry_registr_password2.place(x=500, y=480)

# Кнопка для переключения видимости пароля 2
button_toggle_password2 = tk.Button(registr_window, image=lock_closed_image_resized2, width=18, height=22,
                                    relief=tk.FLAT, borderwidth=0,
                                    highlightthickness=0,
                                    command=lambda: toggle_password_visibility2(entry_registr_password2,
                                                                                button_toggle_password2))
button_toggle_password2.place(x=690, y=442)

# Кнопка далее
image_regisrt_go = "images/регистрация_далее.png"
size_registr_go = (276, 58)
photo_registr_go = load_image(image_regisrt_go, size_registr_go)
# Кнопка Далее
tk.Button(registr_window, image=photo_registr_go, command=register, relief=tk.FLAT, borderwidth=0,
          highlightthickness=0).place(
    x=503, y=523)
# Кнопка "Назад"
image_registr_back = "images/регистрация_назад.png"
size_registr_back = (280, 66)
photo_registr_back = load_image(image_registr_back, size_registr_back)

tk.Button(registr_window, image=photo_registr_back, command=lambda: open_window(registr_window, options_window)).place(
    x=950, y=620)

# Создание Canvas с заданными размерами для гиперссылки "Уже есть аккаунт? Войти" в окне регистрации
canvas_reg_width = 275
canvas_reg_height = 27
canvas_reg = tk.Canvas(registr_window, width=canvas_reg_width, height=canvas_reg_height, highlightthickness=0)
canvas_reg.place(x=503, y=582)

# Загружаем изображение для фона гиперссылки "Войти"
link_reg_background_path = os.path.join("images",
                                        "Есть_аккаунт_вход.png")
link_reg_background_image = Image.open(link_reg_background_path)
link_reg_background_image = link_reg_background_image.resize(
    (canvas_reg_width, canvas_reg_height))
link_reg_background_photo = ImageTk.PhotoImage(link_reg_background_image)

# Добавляем изображение на Canvas для регистрации
canvas_reg.create_image(0, 0, anchor="nw", image=link_reg_background_photo)

# Добавляем текст на Canvas для регистрации
text_reg_id = canvas_reg.create_text(canvas_reg_width / 2, canvas_reg_height / 2, text="Уже есть аккаунт? Войти",
                                     fill="white",
                                     anchor="center", font=("Arial", 12))

# Привязываем событие нажатия на гиперссылку для входа
canvas_reg.tag_bind(text_reg_id, "<Button-1>", go_to_login)


# Создаем главное окно
main_window = tk.Toplevel(start_window)
main_window.geometry("1280x720+200+200")
main_window.title("Игра")
main_window.withdraw()  # Скрыть главное окно изначально

main_background_path = os.path.join("images", "main_window.png")
main_window = create_window_with_background(main_window, main_background_path)

# Кнопка старт (главное окно)
image_main_start = "images/main_start.png"
size_main_start = (447, 110)
photo_main_start = load_image(image_main_start, size_main_start)

tk.Button(main_window, image=photo_main_start, command=handle_start_button, relief=tk.FLAT, borderwidth=0,
          highlightthickness=0).place(x=414, y=595)

image_main_time = "images/настало_время_сражений.png"
size_main_time = (220, 90)
photo_main_time = load_image(image_main_time, size_main_time)

tk.Label(main_window, image=photo_main_time, relief=tk.FLAT, borderwidth=0,
         highlightthickness=0).place(x=1045, y=270)

# Кнопка выйти из аккаунта
image_main_exit = "images/main_window_выйтиизакка.png"
size_main_exit = (150, 60)
photo_main_exit = load_image(image_main_exit, size_main_exit)

tk.Button(main_window, image=photo_main_exit, command=lambda: open_window(main_window, options_window), relief=tk.FLAT,
          borderwidth=0,
          highlightthickness=0).place(x=1092, y=480)

statistics = Image.open("images/статистика.png")
statistics = statistics.resize((54, 54))
photo_statistics = ImageTk.PhotoImage(statistics)

tk.Button(main_window, image=photo_statistics, height=54, width=54,
          command=lambda: (open_window_statistics(main_window)),
          relief=tk.FLAT, borderwidth=0, highlightthickness=0).place(x=20, y=369)

advances = Image.open("images/достижения.png")
advances = advances.resize((55, 55))
photo_advances = ImageTk.PhotoImage(advances)

tk.Button(main_window, image=photo_advances, command=lambda: open_window_advances(main_window), height=55, width=55,
          relief=tk.FLAT, borderwidth=0, highlightthickness=0).place(x=20, y=280)

rules = Image.open("images/правила.png")
rules = rules.resize((53, 53))
photo_rules = ImageTk.PhotoImage(rules)
tk.Button(main_window, image=photo_rules, height=53, width=53, command=lambda: open_window_rules(main_window),
          relief=tk.FLAT, borderwidth=0, highlightthickness=0).place(x=20, y=198)

statistics = Image.open("images/статистика.png")
statistics = statistics.resize((54, 54))
photo_statistics = ImageTk.PhotoImage(statistics)
tk.Button(main_window, image=photo_statistics, height=54, width=54,
          command=lambda: (open_window_statistics(main_window), display_statistics(statistics_window)),
          relief=tk.FLAT, borderwidth=0, highlightthickness=0).place(x=20, y=369)

# Загрузка изображения
image_main_achievements = "images/достижения_текст.png"
size_main_achievements = (290, 75)
photo_main_achievements = load_image(image_main_achievements, size_main_achievements)

# Создаем Canvas для отображения достижений
achievements_canvas = tk.Canvas(main_window, width=290, height=75, bg='black', highlightthickness=0)
achievements_canvas.place(x=510, y=57)

# Добавляем изображение на Canvas
achievements_canvas.create_image(0, 0, anchor=tk.NW, image=photo_main_achievements)

# Добавляем изображение на Canvas
achievements_canvas.create_image(0, 0, anchor=tk.NW, image=photo_main_achievements)

# Загрузка изображения
image_main_achievements_part = "images/достижения_part.png"
size_main_achievements_part = (175, 58)
photo_main_achievements_part = load_image(image_main_achievements_part, size_main_achievements_part)

# Создаем Canvas для отображения достижений
achievements_canvas_part = tk.Canvas(main_window, width=175, height=55, bg='black', highlightthickness=0)
achievements_canvas_part.place(x=1070, y=405)

# Добавляем изображение на Canvas
achievements_canvas_part.create_image(0, 0, anchor=tk.NW, image=photo_main_achievements_part)



# Создаем окно выбора игрока
choice_window = tk.Toplevel(start_window)
choice_window.geometry("1280x720+200+200")
choice_window.title("Выбор игрока")
choice_window.withdraw()  # Скрыть окно правил изначально

choice_background_path = os.path.join("images", "Your Move.png")
choice_window = create_window_with_background(choice_window, choice_background_path)

# Кнопка камень
stone = Image.open("images/камень.png")
stone = stone.resize((135, 320))
stone_photo = ImageTk.PhotoImage(stone)

# Кнопка камень
tk.Button(choice_window, image=stone_photo, command=lambda: play_game('Камень'), relief=tk.FLAT, borderwidth=0,
          highlightthickness=0).place(x=345, y=235)

# Кнопка ножницы
scissors = Image.open("images/ножницы.png")
scissors = scissors.resize((135, 320))
scissors_photo = ImageTk.PhotoImage(scissors)

# Кнопка ножницы
tk.Button(choice_window, image=scissors_photo, command=lambda: play_game('Ножницы'), relief=tk.FLAT, borderwidth=0,
          highlightthickness=0).place(x=595, y=235)

# Кнопка бумага
paper = Image.open("images/бумага.png")
paper = paper.resize((135, 320))
paper_photo = ImageTk.PhotoImage(paper)

# Кнопка бумага
tk.Button(choice_window, image=paper_photo, command=lambda: play_game('Бумага'), relief=tk.FLAT, borderwidth=0,
          highlightthickness=0).place(x=842, y=235)



# Создаем окно правил
rules_window = tk.Toplevel(start_window)
rules_window.geometry("1280x720+200+200")
rules_window.title("Выбор игрока")
rules_window.withdraw()  # Скрыть окно правил изначально

rules_background_path = os.path.join("images", "окно_правила.png")
rules_window = create_window_with_background(rules_window, rules_background_path)

statistics1 = Image.open("images/статистика.png")
statistics1 = statistics1.resize((52, 52))
photo_statistics1 = ImageTk.PhotoImage(statistics1)

tk.Button(rules_window, image=photo_statistics1, command=lambda: open_window_statistics(rules_window), width=52,
          height=52,
          relief=tk.FLAT, borderwidth=0, highlightthickness=0).place(x=21, y=369)

advances1 = Image.open("images/достижения.png")
advances1 = advances1.resize((52, 52))
photo_advances1 = ImageTk.PhotoImage(advances1)
# Кнопка "Назад"
tk.Button(rules_window, image=photo_advances1, command=lambda: open_window_advances(rules_window), height=52, width=52,
          relief=tk.FLAT, borderwidth=0, highlightthickness=0).place(x=21, y=282)

account = Image.open("images/аккаунт.png")
account = account.resize((52, 52))
photo_account = ImageTk.PhotoImage(account)

tk.Button(rules_window, image=photo_account, command=lambda: return_window_main(rules_window), height=52, width=52,
          relief=tk.FLAT, borderwidth=0, highlightthickness=0).place(x=20, y=451)



# Создаем окно с информацией о достижениях
advances_window = tk.Toplevel(start_window)
advances_window.geometry("1280x720+200+200")
advances_window.title("Выбор игрока")
advances_window.withdraw()  # Скрыть окно изначально

advances_background_path = os.path.join("images", "окно_достижения.png")
advances_window = create_window_with_background(advances_window, advances_background_path)

account2 = Image.open("images/аккаунт.png")
account2 = account2.resize((50, 50))
photo_account2 = ImageTk.PhotoImage(account2)

tk.Button(advances_window, image=photo_account2, command=lambda: return_window_main(advances_window), height=50,
          width=50,
          relief=tk.FLAT, borderwidth=0, highlightthickness=0).place(x=23, y=450)

statistics2 = Image.open("images/статистика.png")
statistics2 = statistics2.resize((50, 50))
photo_statistics2 = ImageTk.PhotoImage(statistics2)

tk.Button(advances_window, image=photo_statistics2, command=lambda: open_window_statistics(advances_window), width=50,
          relief=tk.FLAT, borderwidth=0, highlightthickness=0).place(x=23, y=370)

rules2 = Image.open("images/правила.png")
rules2 = rules2.resize((53, 53))
photo_rules2 = ImageTk.PhotoImage(rules2)

tk.Button(advances_window, image=photo_rules2, command=lambda: open_window_rules(advances_window), height=53, width=53,
          relief=tk.FLAT, borderwidth=0, highlightthickness=0).place(x=20, y=198)


# Создаем окно статистики
statistics_window = tk.Toplevel(start_window)
statistics_window.geometry("1280x720+200+200")
statistics_window.title("Выбор игрока")
statistics_window.withdraw()  # Скрыть окно изначально

statistics_background_path = os.path.join("images", "окно_статстика.png")
statistics_window = create_window_with_background(statistics_window, statistics_background_path)

advances3 = Image.open("images/достижения.png")
advances3 = advances3.resize((55, 55))
photo_advances3 = ImageTk.PhotoImage(advances3)
# Кнопка "Назад"
tk.Button(statistics_window, image=photo_advances3, command=lambda: open_window_advances(statistics_window), height=55,
          width=55,
          relief=tk.FLAT, borderwidth=0, highlightthickness=0).place(x=19, y=280)

rules3 = Image.open("images/правила.png")
rules3 = rules3.resize((53, 53))
photo_rules3 = ImageTk.PhotoImage(rules3)
tk.Button(statistics_window, image=photo_rules3, height=53, width=53,
          command=lambda: open_window_rules(statistics_window),
          relief=tk.FLAT, borderwidth=0, highlightthickness=0).place(x=20, y=197)

account3 = Image.open("images/аккаунт.png")
account3 = account3.resize((50, 50))
photo_account3 = ImageTk.PhotoImage(account3)
# Кнопка "Назад"
tk.Button(statistics_window, image=photo_account3, command=lambda: return_window_main(statistics_window), height=50,
          width=50,
          relief=tk.FLAT, borderwidth=0, highlightthickness=0).place(x=23, y=450)

# Кнопки
image_path_save = "images/статистика_save.png"
size_save = (225, 60)
photo_save_statistics_button = load_image(image_path_save, size_save)
statistics = calculate_statistics()
tk.Button(statistics_window, image=photo_save_statistics_button, command=lambda: save_statistics(statistics),
          relief=tk.FLAT, borderwidth=0, highlightthickness=0).place(x=806, y=525)

# Создаем окна победы
win_window = tk.Toplevel(start_window)
win_window.geometry("1280x720+200+200")
win_window.title("Выбор игрока")
win_window.withdraw()  # Скрыть окно изначально

win_background_path = os.path.join("images", "победа.png")
win_window = create_window_with_background(win_window, win_background_path)

# Кнопка рестарт
image_win = "images/restart_win.png"
size_win = (284, 79)
photo_win = load_image(image_win, size_win)

tk.Button(win_window, image=photo_win, height=79, width=284, command=lambda: open_mainnext_window(win_window),
          relief=tk.FLAT, borderwidth=0, highlightthickness=0).place(x=981, y=629)

# Создаем окно поражения
lose_window = tk.Toplevel(start_window)
lose_window.geometry("1280x720+200+200")
lose_window.title("Выбор игрока")
lose_window.withdraw()  # Скрыть окно логина изначально

lose_background_path = os.path.join("images", "поражение.png")
lose_window = create_window_with_background(lose_window, lose_background_path)

# Кнопка рестарт
image_lose = "images/restart_lose.png"
size_lose = (283, 81)
photo_lose = load_image(image_lose, size_lose)

tk.Button(lose_window, image=photo_lose, height=81, width=283, command=lambda: open_mainnext_window(lose_window),
          relief=tk.FLAT, borderwidth=0, highlightthickness=0).place(x=979, y=629)

# Создаем окно ничья
non_window = tk.Toplevel(start_window)
non_window.geometry("1280x720+200+200")
non_window.title("Выбор игрока")
non_window.withdraw()  # Скрыть окно изначально

non_background_path = os.path.join("images", "ничья.png")

non_window = create_window_with_background(non_window, non_background_path)

# Кнопка рестарт
image_non = "images/restart_non.png"
size_non = (284, 79)
photo_non = load_image(image_non, size_non)


tk.Button(non_window, image=photo_non, height=79, width=284, command=lambda: open_mainnext_window(non_window),
          relief=tk.FLAT, borderwidth=0, highlightthickness=0).place(x=983, y=626)

# Запускаем главный цикл приложения
start_window.mainloop()
