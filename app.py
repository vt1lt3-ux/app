from tkinter import *

root = Tk()
root.geometry("1000x800")

kamera_image = PhotoImage(file="im/kamera1.png")
kamera_image2 = PhotoImage(file="im/kamera2.png")
mk_image = PhotoImage(file="im/arduino.png")
mk_image2 = PhotoImage(file="im/stm.png")
dd_image = PhotoImage(file="im/dd1.png")
dd_image2 = PhotoImage(file="im/dd2.png")
termo_image = PhotoImage(file="im/termo1.png")
termo_image2 = PhotoImage(file="im/termo2.png")

def show_image(image):
    new_window = Toplevel(root)
    new_window.geometry("1920x1080")
    image_label = Label(new_window, image=image)
    image_label.pack(expand=True)

def show_camera_image():
    show_image(kamera_image)

def show_camera_image2():
    show_image(kamera_image2)

def show_mk_image():
    show_image(mk_image)

def show_mk_image2():
    show_image(mk_image2)

def show_dd_image():
    show_image(dd_image)

def show_dd_image2():
    show_image(dd_image2)

def show_termo_image():
    show_image(termo_image)

def show_termo_image2():
    show_image(termo_image2)

def show_specifications(device_type, text):
    spec_window = Toplevel(root)
    spec_window.title(f"Характеристики - {device_type}")
    spec_window.geometry("500x300")

    text_frame = Frame(spec_window)
    text_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    text_widget = Text(text_frame, wrap=WORD, font=("Arial", 11))
    scrollbar = Scrollbar(text_frame, command=text_widget.yview)
    text_widget.configure(yscrollcommand=scrollbar.set)

    text_widget.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    text_widget.insert(1.0, text)
    text_widget.config(state=DISABLED)
    Button(spec_window, text="Закрыть", command=spec_window.destroy).pack(pady=10)

camera_spec = """ХАРАКТЕРИСТИКИ КАМЕРЫ:
 высокая разрешающая способность, 30 кадров в секунду."""

mk_spec = """ХАРАКТЕРИСТИКИ МИКРОКОНТРОЛЛЕРА:
 Arduino: 16 МГц, 32 КБ памяти, множество функций."""

dd_spec = """ХАРАКТЕРИСТИКИ ДАТЧИКА ДВИЖЕНИЯ:
 10 метров обнаружения, с возможностью настройки."""

termo_spec = """ХАРАКТЕРИСТИКИ ТЕРМОМЕТРА:
 диапазон температур от -20°C до 100°C."""


video_camera_spec = """ВИДЕОКАМЕРА:

• Назначение: Видеонаблюдение
• Разрешение: Full HD
• Тип: Цифровая
• Подключение: Ethernet/Wi-Fi
• Запись: 24/7
• Питание: PoE/12V"""

ir_camera_spec = """ИНФРАКРАСНАЯ КАМЕРА:

• Назначение: Тепловидение
• Диапазон: 8-14 мкм
• Дальность: до 30 м
• Точность: ±2°C
• Режимы: Тепловая карта
• Питание: 12V DC"""

arduino_spec = """ARDUINO:

• Назначение: Прототипирование
• Ядро: ATmega328P
• Память: 32 КБ Flash
• Питание: 5V/7-12V
• Порты: 14 цифровых
• Интерфейсы: USB, UART"""

stm_spec = """STM:

• Назначение: Встраиваемые системы
• Ядро: ARM Cortex-M
• Память: до 1 МБ Flash
• Питание: 3.3V
• Скорость: до 400 МГц
• Интерфейсы: USB, CAN, Ethernet"""

ultrasonic_dd_spec = """УЛЬТРАЗВУКОВЫЕ ДАТЧИКИ:

• Принцип: Отражение УЗ-волн
• Дальность: 2-400 см
• Точность: ±1 см
• Угол: 15-30 градусов
• Частота: 40 кГц
• Питание: 5V DC"""

microwave_dd_spec = """МИКРОВОЛНОВЫЕ ДАТЧИКИ:

• Принцип: Допплер-эффект
• Дальность: до 20 м
• Частота: 5.8 ГГц
• Проникает: сквозь стены
• Нагрев: минимальный
• Питание: 12V DC"""

electronic_termo_spec = """ЭЛЕКТРОННЫЙ ТЕРМОМЕТР:

• Тип: Цифровой
• Диапазон: -50...+150°C
• Точность: ±0.5°C
• Дисплей: LCD
• Питание: Батарея
• Время работы: до 2 лет"""

mercury_termo_spec = """РТУТНЫЙ ТЕРМОМЕТР:

• Тип: Аналоговый
• Диапазон: -35...+350°C
• Точность: ±1°C
• Чтение: Визуальное
• Без питания: Да
• Долговечность: Высокая"""

def show_camera_spec():
    show_specifications("Камера", camera_spec)

def show_mk_spec():
    show_specifications("Микроконтроллер", mk_spec)

def show_dd_spec():
    show_specifications("Датчик движения", dd_spec)

def show_termo_spec():
    show_specifications("Термометр", termo_spec)


def show_video_camera_spec():
    show_specifications("Видеокамера", video_camera_spec)

def show_ir_camera_spec():
    show_specifications("ИК-камера", ir_camera_spec)

def show_arduino_spec():
    show_specifications("Arduino", arduino_spec)

def show_stm_spec():
    show_specifications("STM", stm_spec)

def show_ultrasonic_spec():
    show_specifications("Ультразвуковые датчики", ultrasonic_dd_spec)

def show_microwave_spec():
    show_specifications("Микроволновые датчики", microwave_dd_spec)

def show_electronic_termo_spec():
    show_specifications("Электронный термометр", electronic_termo_spec)

def show_mercury_termo_spec():
    show_specifications("Ртутный термометр", mercury_termo_spec)

mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Сохранить...")
filemenu.add_command(label="Выход")

picturemenu = Menu(mainmenu, tearoff=0)
picturemenu.add_command(label="Камера", command=show_camera_image)
picturemenu.add_command(label="Микроконтроллер", command=show_mk_image)
picturemenu.add_command(label="Датчик движения", command=show_dd_image)
picturemenu.add_command(label="Термометр", command=show_termo_image)

specificationsmenu = Menu(mainmenu, tearoff=0)
specificationsmenu.add_command(label="Камера", command=show_camera_spec)
specificationsmenu.add_command(label="Микроконтроллер", command=show_mk_spec)
specificationsmenu.add_command(label="Датчик движения", command=show_dd_spec)
specificationsmenu.add_command(label="Термометр", command=show_termo_spec)

functionsmenu = Menu(mainmenu, tearoff=0)

functionsmenu2 = Menu(functionsmenu, tearoff=0)
functionsmenu3 = Menu(functionsmenu, tearoff=0)
functionsmenu4 = Menu(functionsmenu, tearoff=0)
functionsmenu5 = Menu(functionsmenu, tearoff=0)

functionsmenu2.add_command(label="Видеокамера", command=show_video_camera_spec)
functionsmenu2.add_separator()
functionsmenu2.add_command(label="Инфракрасная камера", command=show_ir_camera_spec)

functionsmenu3.add_command(label="Arduino", command=show_arduino_spec)
functionsmenu3.add_separator()
functionsmenu3.add_command(label="STM", command=show_stm_spec)

functionsmenu4.add_command(label="Ультразвуковые", command=show_ultrasonic_spec)
functionsmenu4.add_separator()
functionsmenu4.add_command(label="Микроволновые", command=show_microwave_spec)

functionsmenu5.add_command(label="Электронный", command=show_electronic_termo_spec)
functionsmenu5.add_separator()
functionsmenu5.add_command(label="Ртутный", command=show_mercury_termo_spec)

functionsmenu.add_cascade(label="Камера", menu=functionsmenu2)
functionsmenu.add_cascade(label="Микроконтроллер", menu=functionsmenu3)
functionsmenu.add_cascade(label="Датчик движения", menu=functionsmenu4)
functionsmenu.add_cascade(label="Термометр", menu=functionsmenu5)

mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Изображение", menu=picturemenu)
mainmenu.add_cascade(label="Характеристики", menu=specificationsmenu)
mainmenu.add_cascade(label="Функции", menu=functionsmenu)

root.mainloop()

