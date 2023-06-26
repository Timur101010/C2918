import time
import threading
from playsound import playsound

# Функция для воспроизведения звукового сигнала
def play_alarm_sound():
    playsound("alarm_sound.mp3")

# Класс для будильника
class Alarm:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.is_set = False

    def set_alarm(self):
        self.is_set = True
        print(f"Будильник установлен на {self.hour:02d}:{self.minute:02d}")

    def check_alarm(self):
        while self.is_set:
            current_time = time.localtime()
            if current_time.tm_hour == self.hour and current_time.tm_min == self.minute:
                print("Подъем! Вставайте!")
                threading.Thread(target=play_alarm_sound).start()
                self.is_set = False
            time.sleep(1)

# Класс для секундомера
class Stopwatch:
    def __init__(self):
        self.is_running = False
        self.elapsed_time = 0

    def start(self):
        if not self.is_running:
            self.start_time = time.time() - self.elapsed_time
            self.is_running = True
            print("Секундомер запущен.")

    def stop(self):
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
            self.is_running = False
            print("Секундомер остановлен.")
            print("Прошло времени:", self.elapsed_time, "сек.")

    def reset(self):
        self.elapsed_time = 0
        print("Секундомер сброшен.")

    def display_elapsed_time(self):
        if self.is_running:
            current_time = time.time() - self.start_time
        else:
            current_time = self.elapsed_time
        print("Прошло времени:", current_time, "сек.")

# Основная функция
def main():
    alarm = Alarm(7, 30)  # Установка будильника на 7:30
    stopwatch = Stopwatch()

    while True:
        print("\nВыберите действие:")
        print("1. Установить будильник")
        print("2. Запустить секундомер")
        print("3. Остановить секундомер")
        print("4. Сбросить секундомер")
        print("5. Показать прошедшее время секундомера")
        print("0. Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            alarm.set_alarm()
        elif choice == "2":
            stopwatch.start()
        elif choice == "3":
            stopwatch.stop()
        elif choice == "4":
            stopwatch.reset()
        elif choice == "5":
            stopwatch.display_elapsed_time()
        elif choice == "0":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
