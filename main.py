import speech_recognition as sr
import pyttsx3

# Инициализируем объекты распознавания речи и синтеза речи
recognizer = sr.Recognizer()
synthesizer = pyttsx3.init()

# Функция для распознавания голоса
def recognize_speech():
    with sr.Microphone() as source:
        print("Скажите что-нибудь...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        print(f"Вы сказали: {text}")
        return text
    except sr.UnknownValueError:
        print("Извините, не удалось распознать речь.")
    except sr.RequestError:
        print("Извините, возникла проблема с обращением к сервису распознавания речи.")

# Функция для синтеза речи
def speak(text):
    synthesizer.say(text)
    synthesizer.runAndWait()

# Основной цикл работы ассистента
while True:
    command = recognize_speech()

    if command and "пока" in command:
        print("До свидания!")
        speak("До свидания!")
        break
    else:
        print("Не понятно, попробуйте еще раз.")
        speak("Не понятно, попробуйте еще раз.")
