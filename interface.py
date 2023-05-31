import tkinter as tk
from command_handlers.bot_commands import startListen

def interface():
    window = tk.Tk()

    # Задание заголовка окна
    window.title("Ok-Gosling")
    # Настройка размеров окна
    window.geometry("300x450")
    window.configure(bg="#333333")


    text_frame = tk.Frame(window, bg="#333333")
    text_frame.pack(fill=tk.BOTH, expand=True)

    # Загрузка и установка изображения на задний фон фрейма
    image = tk.PhotoImage(file=".\\back\\bg1.png")
    background_label = tk.Label(text_frame, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Создаю метку с текстом в основном окне
    text_label = tk.Label(text_frame, text="Добро пожаловать в Ok-Gosling", fg="white", bg="#3C3C3C",
                          font=("Arial", 14))
    text_label.pack(pady=100, anchor="n")


    listen_button = tk.Button(window, text="Нажмите \n чтобы говорить", command=startListen,
                              width=20, height=2, bg="#880F0F", fg="white")

    # Установка кнопки ниже центра окна
    listen_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    # Запуск главного цикла обработки событий
    window.mainloop()