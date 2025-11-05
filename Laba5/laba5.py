import matplotlib.pyplot as plt
import numpy as np
import pygame
import faker
import PyInstaller
import speech_recognition as sr
import panda3d
import openai
import arcade
import moderngl
from faker import Faker

try:
    fake = Faker('uk_Ua')
    print("випадкове ім'я:", fake.name())
    print("випадкова адреса:", fake.address())
except Exception as e:
    print("Помилка з Faker:", e)

try:
    arr = np.array([1, 2, 3, 4, 5])
    print("Середнє значення:", np.mean(arr))
except Exception as e:
    print("Помилка з NumPy:", e)

try:
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.title("Простий графік")
    plt.savefig("plot.png")
    plt.close()
    print("Графік збережено у plot.png")
except Exception as e:
    print("Помилка з Matplotlib:", e)

try:
    pygame.init()
    print("PyGame успішно ініціалізовано!")
    pygame.quit()
except Exception as e:
    print("Помилка з PyGame:", e)

try:
    r = sr.Recognizer()
    print("SpeechRecognition готовий до роботи.")
except Exception as e:
    print("Помилка з SpeechRecognition:", e)
