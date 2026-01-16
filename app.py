from tkinter import *

root = Tk()
root.geometry("1500x900")
root.title("Информация об устройствах")

zamok_image = PhotoImage(file="im/zamok.png")
lampo4ka_image = PhotoImage(file="im/lampo4ka.png")
sis_image = PhotoImage(file="im/sis.otop.png")
poliv_image = PhotoImage(file="im/poliv.png")
zamok_image2 = PhotoImage(file="im/zamok2.png")
lampo4ka_image2 = PhotoImage(file="im/lampo4ka2.png")
sis_image2 = PhotoImage(file="im/sis2.png")
poliv_image2 = PhotoImage(file="im/poliv2.png")

zamok_spec1 = """ФУНКЦИИ ЗАМКА:
Бесключевой доступ: Открытие с помощью отпечатка пальца, пин-кода, RFID-карты/брелка.

Удаленное управление и мониторинг: Проверка статуса замка (открыт/закрыт), открытие/блокировка из приложения. Важно: Удаленное открытие обычно требует Wi-Fi/Zigbee-модуля.

Выдача временных и гостевых ключей: Создание виртуальных ключей для гостей, курьеров или домработницы с ограничением по времени или количеству использований.

Журнал событий: Подробная история всех событий (кто, когда и каким способом открыл дверь).

Голосовое управление: Интеграция с умным домом для команд: "Алиса, открой входную дверь" (чаще работает как сценарий на снятие с охраны, а не прямое открытие).

Автоматическое запирание: Функция авто-блокировки через заданное время после открытия.

Сигнализация: Активация звукового сигнала при попытке взлома, неверном вводе кода или принудительном открытии.

Интеграция в сценарии умного дома:

"Я ушел" → закрытие замка, выключение света, отключение розеток.

"Добро пожаловать" → открытие двери по отпечатку → включение света в прихожей и коридоре.

Резервное питание: Возможность открыть дверь с помощью power bank при разряженных батарейках."""

lampo4ka_spec1 = """ФУНКЦИИ ЛАМПОЧКИ:
 Удаленное включение/выключение: Управляйте светом из любого места через смартфон.

Регулировка яркости: Плавное изменение яркости от 1% до 100% для создания нужной атмосферы.

Изменение цветовой температуры: Настройка света от теплого желтоватого (для отдыха) до холодного белого (для концентрации).

Смена цвета (RGB-модели): Создание цветной подсветки для вечеринок, праздников или выделения зон в интерьере.

Голосовое управление: Включение, выключение и настройка командой голоса через Алису, Siri, Google Assistant и др.

Расписание и таймеры: Автоматическое включение света в заданное время (например, утром как будильник или вечером для симуляции присутствия).

Сценарии и режимы: Создание предустановок ("Чтение", "Кино", "Романтический ужин") и привязка к другим устройствам.

Геолокация (Geofencing): Автоматическое включение света при вашем приближении к дому и выключение при уходе."""

sis_spec1 = """ФУНКЦИИ СИСТЕМЫ ОТОПЛЕНИЯ:
 Удаленное управление температурой: Изменение режима отопления с работы или из отпуска.

Гибкое программирование по расписанию: Установка разной температуры для разных дней недели и времени суток (ночью прохладнее, к приходу с работы — теплее).

Геолокационный режим (Geofencing): Система определяет, что вы выехали из дома, и переходит в экономичный режим, а при приближении — восстанавливает комфортную температуру.

Режим "Отпуск": Поддержание миниманой температуры для защиты от замерзания.

Адаптивное обучение: Некоторые модели учатся, как быстро прогревается дом, и включают котел вовремя, чтобы к вашему пробуждению было тепло.

Погодозависимое управление: Корректировка работы системы на основе уличной температуры (предварительный нагрев при похолодании).

Зональный контроль: Независимое управление температурой в разных комнатах (при наличии сервоприводов на радиаторах).

Мониторинг и аналитика: Отслеживание расхода энергии, получение отчетов и советов по экономии."""

poliv_spec1 = """ФУНКЦИИ АВТОПОЛИВА:
 Автоматический полив по расписанию: Полив в заданное время с заданной продолжительностью.

Интеллектуальный полив по данным с датчиков: Включение системы только при падении влажности почвы ниже установленного порога. Это ключевая функция для здоровья растений.

Погодная адаптация: Отмена или корректировка полива, если ожидается дождь (интеграция с онлайн-прогнозом) или если датчик дождя уже зафиксировал осадки.

Гибкое зонирование: Создание отдельных программ полива для разных групп растений (например, грядки, газон, цветники, теплица), требующих разного количества воды.

Удаленное управление и мониторинг: Запуск/остановка полива вручную из приложения, просмотр данных с датчиков.

Капельный полив (для сада): Точечная подача воды прямо к корням, что экономит воду и предотвращает болезни листьев.

Режимы полива: Возможность настраивать частоту (ежедневно, через день) и интенсивность.

Оповещения: Уведомления об окончании полива, обрыве линии, низком заряде батареи или аномально низкой влажности почвы.

Экономия воды: Главный результат работы системы — сокращение расхода воды до 50% по сравнению с ручным поливом."""

zamok_spec2 = """ЭЛЕКТРОННЫЙ ЗАМОК:

Тип установки: Накладной (проще установить) или встроенный (более эстетичный, сложный монтаж).

Способы отпирания:

Отпечаток пальца

Пин-код (цифровая клавиатура)

RFID-карта или брелок

Мобильное приложение (через Bluetooth/Wi-Fi)

Голосовые команды (через интеграцию)

Резерв: Механический ключ (обычно есть).

Стандарт связи: Bluetooth для работы вблизи, Wi-Fi или Zigbee для удаленного доступа и уведомлений.

Автоматизация: Интеграция в сценарии умного дома (закрыть все замки по команде "Я ушел").

Безопасность: Защита от взлома, ложных отпечатков; журнал событий (кто и когда открыл дверь).

Автономность: Работа от батареек, предупреждение о низком заряде."""

lampo4ka_spec2 = """УМНАЯ ЛАМПОЧКА:

Стандарт связи: Wi-Fi, Bluetooth, Zigbee или Z-Wave. Wi-Fi-лампы работают напрямую с роутером, Zigbee/Z-Wave требуют хаб (шлюз), но создают более стабильную сеть.

Тип цоколя: Чаще всего E27 (стандартный) или E14 (миньон).

Яркость: Измеряется в люменах (лм). Аналог 60 Вт лампы накаливания ≈ 600-800 лм.

Цветовая температура: Регулируемая от теплого (2700K) до холодного белого (6500K).

Цветность: Может быть монохромной (только белый) или RGB (полный спектр цветов).

Управление: Через мобильное приложение, голосовые помощники (Алиса, Siri, Google Assistant), автоматизация (расписание, восход/закат).

Энергоэффективность: Светодиодная (LED), низкое энергопотребление."""

sis_spec2 = """СИСТЕМА ОТОПЛЕНИЯ:

Центр системы: Умный термостат или контроллер котла.

Управление температурой: По расписанию, вручную через приложение, по геолокации (включение при приближении).

Датчики: Могут использовать внешние датчики температуры в разных комнатах для более точного контроля.

Стандарт связи: Wi-Fi, Zigbee, Z-Wave.

Интеграция: Работа с голосовыми помощниками и другими устройствами (например, открылись окна — отопление暂停илось).

Аналитика: Отчеты о потреблении энергии, советы по экономии.

Совместимость: Критически важно проверять совместимость с вашим котлом (газовый, электрический), типом системы (радиаторы, теплый пол) и напряжением."""

poliv_spec2 = """АВТО ПОЛИВ РАСТЕНИЙ:

Масштаб: Комнатные системы (капельницы для горшков) или садовые (шланги, разбрызгиватели, клапаны).

Управление:

По таймеру: Самый простой вариант.

По датчикам влажности: Полив только когда почва сухая (наиболее эффективно).

По погодным данным: Интеграция с онлайн-прогнозом для отмены полива в дождь.

Стандарт связи: Wi-Fi, Bluetooth, RF (радиочастота) для удаленных датчиков.

Автономность: Садовые системы часто работают от батарей или солнечных панелей.

Конструкция:

Контроллер (мозг системы)

Электромагнитные клапаны (открывают/закрывают воду)

Трубки/капельницы/разбрызгиватели

Датчики влажности, дождя"""

devices_data = {
    "zamok": {
        "name": "Электронный замок",
        "image": zamok_image,
        "spec1": zamok_spec1,
        "spec2": zamok_spec2
    },
    "lampo4ka": {
        "name": "Умная лампочка",
        "image": lampo4ka_image,
        "spec1": lampo4ka_spec1,
        "spec2": lampo4ka_spec2
    },
    "sis": {
        "name": "Система отопления",
        "image": sis_image,
        "spec1": sis_spec1,
        "spec2": sis_spec2
    },
    "poliv": {
        "name": "Авто полив растений",
        "image": poliv_image,
        "spec1": poliv_spec1,
        "spec2": poliv_spec2
    }
}

current_device = None
selected_button = None
icon_buttons = {}

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=True)

right_icons_frame = Frame(main_frame, width=200, bg="")
right_icons_frame.pack(side=RIGHT, fill=Y, padx=5, pady=5)

center_frame = Frame(main_frame)
center_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

display_frame = Frame(center_frame, relief=GROOVE, bd=2)
display_frame.pack(side=TOP, fill=BOTH, expand=True)

buttons_frame = Frame(center_frame)
buttons_frame.pack(side=BOTTOM, fill=X, padx=10, pady=10)

image_btn = Button(buttons_frame, text="Изображение",
                   state=DISABLED, width=15, height=2)
image_btn.pack(side=LEFT, padx=5, pady=10)

spec_btn = Button(buttons_frame, text="Характеристики",
                  state=DISABLED, width=15, height=2)
spec_btn.pack(side=LEFT, padx=5, pady=10)

func_btn = Button(buttons_frame, text="Функции",
                  state=DISABLED, width=15, height=2)
func_btn.pack(side=LEFT, padx=5, pady=10)

Label(right_icons_frame, text="", font=("Arial", 14)).pack(pady=20)

def reset_all_buttons():
    for btn in icon_buttons.values():
        btn.config(bg="white", relief=RAISED)

def select_button(button):
    global selected_button

    if selected_button:
        selected_button.config(bg="white", relief=RAISED)

    button.config(bg="lightblue", relief=SUNKEN, fg="white")
    selected_button = button

def create_right_icon(parent, device_key, text, image):
    frame = Frame(parent, bg="")
    frame.pack(pady=15)

    icon = image.subsample(4, 4)

    tooltip = None
    tooltip_timer = None

    def on_enter(event):
        if btn != selected_button:
            btn.config(bg="lightblue", relief=SUNKEN)

        nonlocal tooltip_timer
        if tooltip_timer is None:
            tooltip_timer = root.after(500, show_tooltip)

    def on_leave(event):
        if btn != selected_button:
            btn.config(bg="white", relief=RAISED)
        else:
            btn.config(bg="lightblue", relief=SUNKEN, fg="white")

        nonlocal tooltip_timer
        if tooltip_timer:
            root.after_cancel(tooltip_timer)
            tooltip_timer = None

        nonlocal tooltip
        if tooltip:
            tooltip.destroy()
            tooltip = None

    def show_tooltip():
        nonlocal tooltip, tooltip_timer
        tooltip_timer = None

        x = btn.winfo_rootx()
        y = btn.winfo_rooty() + btn.winfo_height()

        tooltip = Toplevel(root)
        tooltip.wm_overrideredirect(True)
        tooltip.wm_geometry(f"+{x}+{y}")

        tooltip_frame = Frame(tooltip, bg="", relief=SOLID, borderwidth=1)
        tooltip_frame.pack()

        device_name = devices_data[device_key]["name"]
        label = Label(tooltip_frame, text=device_name,
                      bg="white", font=("Arial", 10, "bold"),
                      padx=10, pady=5)
        label.pack()

        tooltip.wm_attributes("-topmost", True)

    def on_click():
        nonlocal tooltip
        if tooltip:
            tooltip.destroy()
            tooltip = None

        select_button(btn)

        select_device(device_key)

    btn = Button(frame, image=icon, text=text, compound=TOP,
                 command=on_click,
                 width=120, height=120, bg="white", relief=RAISED,
                 font=("Arial", 10, "bold"), cursor="hand2")
    btn.image = icon
    btn.pack()

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    icon_buttons[device_key] = btn

    return btn

def show_image_content():
    if current_device:
        for widget in display_frame.winfo_children():
            widget.destroy()

        content_frame = Frame(display_frame)
        content_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        name_label = Label(content_frame, text=devices_data[current_device]["name"],
                           font=("Arial", 18, "bold"))
        name_label.pack(side=TOP, pady=(0, 20))

        img_label = Label(content_frame, image=devices_data[current_device]["image"])
        img_label.pack(expand=True)

def show_spec_content():
    if current_device:
        for widget in display_frame.winfo_children():
            widget.destroy()

        content_frame = Frame(display_frame)
        content_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        name_label = Label(content_frame, text=devices_data[current_device]["name"],
                           font=("Arial", 18, "bold"))
        name_label.pack(side=TOP, pady=(0, 20))

        text_frame = Frame(content_frame)
        text_frame.pack(fill=BOTH, expand=True)

        text_widget = Text(text_frame, wrap=WORD, font=("Arial", 11))
        scrollbar = Scrollbar(text_frame, command=text_widget.yview)
        text_widget.configure(yscrollcommand=scrollbar.set)

        text_widget.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        text_widget.insert(1.0, devices_data[current_device]["spec2"])
        text_widget.config(state=DISABLED)

def show_func_content():
    if current_device:
        for widget in display_frame.winfo_children():
            widget.destroy()

        content_frame = Frame(display_frame)
        content_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        name_label = Label(content_frame, text=devices_data[current_device]["name"],
                           font=("Arial", 18, "bold"))
        name_label.pack(side=TOP, pady=(0, 20))

        text_frame = Frame(content_frame)
        text_frame.pack(fill=BOTH, expand=True)

        text_widget = Text(text_frame, wrap=WORD, font=("Arial", 11))
        scrollbar = Scrollbar(text_frame, command=text_widget.yview)
        text_widget.configure(yscrollcommand=scrollbar.set)

        text_widget.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        text_widget.insert(1.0, devices_data[current_device]["spec1"])
        text_widget.config(state=DISABLED)

def clear_display():
    for widget in display_frame.winfo_children():
        widget.destroy()

    image_btn.config(state=DISABLED)
    spec_btn.config(state=DISABLED)
    func_btn.config(state=DISABLED)

def select_device(device_key):
    global current_device
    current_device = device_key

    image_btn.config(state=NORMAL)
    spec_btn.config(state=NORMAL)
    func_btn.config(state=NORMAL)

    show_image_content()

image_btn.config(command=show_image_content)
spec_btn.config(command=show_spec_content)
func_btn.config(command=show_func_content)

create_right_icon(right_icons_frame, "zamok", "", zamok_image2)
create_right_icon(right_icons_frame, "lampo4ka", "", lampo4ka_image2)
create_right_icon(right_icons_frame, "sis", "", sis_image2)
create_right_icon(right_icons_frame, "poliv", "", poliv_image2)

mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть")
filemenu.add_command(label="Сохранить")
filemenu.add_command(label="Выход", command=root.quit)

devices_menu = Menu(mainmenu, tearoff=0)
devices_menu.add_command(label="Эл. замок",
                         command=lambda: [select_button(icon_buttons["zamok"]), select_device("zamok")])
devices_menu.add_command(label="Умная лампочка",
                         command=lambda: [select_button(icon_buttons["lampo4ka"]), select_device("lampo4ka")])
devices_menu.add_command(label="Система отопления",
                         command=lambda: [select_button(icon_buttons["sis"]), select_device("sis")])
devices_menu.add_command(label="Авто полив растений",
                         command=lambda: [select_button(icon_buttons["poliv"]), select_device("poliv")])

instruction_menu = Menu(mainmenu, tearoff=0)
instruction_menu.add_command(label="Эл. замок")
instruction_menu.add_command(label="Умная лампочка")
instruction_menu.add_command(label="Система отопления")
instruction_menu.add_command(label="Авто полив растений")

mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Устройства", menu=devices_menu)
mainmenu.add_cascade(label="Инструкция для пользователя", menu=instruction_menu)
mainmenu.add_cascade(label="Помощь")

clear_display()

root.mainloop()