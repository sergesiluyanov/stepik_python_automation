import math
from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Настраиваем Selenium WebDriver, указывая путь к WebDriver
browser = webdriver.Chrome()

try:
    # Открываем страницу
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    # Нажимаем кнопку
    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    button.click()

    # Переключаемся на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Ждем
    time.sleep(2)

    # Считываем значение x
    x_element = browser.find_element("id", "input_value")
    x = x_element.text

    # Вычисляем математическую функцию от x
    result = calc(x)

    # Вводим вычисленное значение в форму
    answer_input = browser.find_element("id", "answer")
    answer_input.send_keys(result)

    # Нажимаем submit
    submit_button = browser.find_element("css selector", "button.btn")
    submit_button.click()

    # Ждем 10 секунд
    time.sleep(10)

finally:


    # Закрываем браузер
    browser.quit()