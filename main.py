import time
def typing_speed_test():
    prompt = "Привет! Напиши этот текст как можно быстрее:"
    print(prompt)
    print("-------------------------------------------------------------")
    print()

    text = "Сегодня я решил попрактиковаться в скоростном наборе текста. Улучшение навыков печати на клавиатуре поможет мне стать более продуктивным и эффективным. Постоянная тренировка позволяет развивать мою печатную скорость и точность. Я настойчиво работаю над собой, чтобы достичь высоких результатов. Клавиатура становится моим лучшим другом, а слова печатаются без задержек и ошибок."

    print(text)
    print()

    input("Нажми Enter, чтобы начать: ")
    start_time = time.time()

    user_input = input()

    end_time = time.time()
    total_time = end_time - start_time

    words = len(text.split())
    characters = len(text)
    speed = words / total_time * 60

    print("-------------------------------------------------------------")
    print()
    print("Результаты:")
    print(f"Общее время: {round(total_time, 2)} секунд")
    print(f"Скорость: {round(speed, 2)} букв в секунду")
    print(f"Точность: {round((len(user_input) / characters) * 100, 2)}%")
    print()

typing_speed_test()


