import streamlit as st
import datetime
import time

# Контактный список
contact_list = []

# Заголовок приложения
st.title("Интерактивный помощник")

# Информация о возможностях
st.write("""
Вот что я умею:
1. Порекомендовать фильм: "Какой фильм посмотреть?"
2. Посчитать выражение: "Сколько будет 2 + 2?" или "Сколько будет 3 * 4?"
3. Назвать сегодняшнюю дату: "Какое сегодня число?"
4. Добавить контакт: "Добавь контакт <имя> <телефон>"
5. Порекомендовать завтрак: "Что приготовить на завтрак?"
6. Показать время: "Который час?"
7. Рассказать анекдот: "Расскажи анекдот"
8. Показать контакты: "Покажи контакты"
""")

# Поле ввода команды
command = st.text_input("Введите команду", "")

# Обработка команд
if st.button("Отправить"):
    command = command.lower()
    if command == "какой фильм посмотреть?":
        movies = ["Inception", "Interstellar", "The Matrix", "The Shawshank Redemption", "Forrest Gump"]
        st.success(f"Рекомендую посмотреть: {', '.join(movies)}")

    elif command.startswith("сколько будет"):
        expression = command[len("сколько будет "):]
        try:
            result = eval(expression)
            st.success(f"Результат: {result}")
        except Exception as e:
            st.error("Ошибка в выражении.")

    elif command == "какое сегодня число?":
        today = datetime.date.today()
        st.success(f"Сегодняшняя дата: {today}")

    elif command.startswith("добавь контакт"):
        parts = command[len("добавь контакт "):].split()
        if len(parts) >= 2:
            name = " ".join(parts[:-1])
            phone = parts[-1]
            contact_list.append({'name': name, 'phone': phone})
            st.success(f"Контакт '{name}' с телефоном '{phone}' добавлен.")
        else:
            st.error("Введите корректное имя и телефон.")

    elif command == "покажи контакты":
        if contact_list:
            contacts = "\n".join([f"{c['name']}: {c['phone']}" for c in contact_list])
            st.success(f"Ваши контакты:\n{contacts}")
        else:
            st.info("Ваш список контактов пуст.")

    elif command == "что приготовить на завтрак?":
        breakfasts = [
            "Овсянка с фруктами",
            "Яичница с авокадо",
            "Тосты с арахисовым маслом и бананом",
            "Йогурт с гранолой и ягодами",
            "Смузи с бананом и шпинатом"
        ]
        st.success(f"Попробуйте на завтрак: {', '.join(breakfasts)}")

    elif command == "который час?":
        now = datetime.datetime.now().strftime("%H:%M:%S")
        st.success(f"Сейчас: {now}")

    elif command == "расскажи анекдот":
        jokes = [
            "Почему программисты не ходят в лес? Потому что медведи делают commit!",
            "Что сказал ноль восьмерке? Какой у тебя классный поясок!",
            "Почему компьютер пошел в бар? Чтобы обновить драйвер!"
        ]
        st.success(f"Вот анекдот для вас: {jokes[0]}")

    else:
        st.warning("Команда не распознана. Попробуйте снова.")
