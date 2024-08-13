from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Настраиваем Selenium WebDriver, указывая путь к WebDriver
# Пример для ChromeDriver
browser = webdriver.Chrome()

try:
    # Открываем страницу
    browser.get("https://SunInJuly.github.io/execute_script.html")

    # Считываем значение x
    x_element = browser.find_element("id", "input_value")
    x = x_element.text

    # Вычисляем математическую функцию от x
    result = calc(x)

    # Проскроллим страницу вниз
    # WebDriver поддерживает выполнение JavaScript
    browser.execute_script("window.scrollBy(0, 100);")

    # Вводим результат в текстовое поле
    answer_input = browser.find_element("id", "answer")
    answer_input.send_keys(result)

    # Выбираем checkbox "I'm the robot"
    robot_checkbox = browser.find_element("id", "robotCheckbox")
    robot_checkbox.click()

    # Переключаем radiobutton "Robots rule!"
    robots_rule_radiobutton = browser.find_element("id", "robotsRule")
    robots_rule_radiobutton.click()

    # Нажимаем на кнопку "Submit"
    submit_button = browser.find_element("css selector", "button.btn")
    submit_button.click()

    # Ждем некоторое время, чтобы увидеть результат (опционально)
    time.sleep(10)

finally:
    # Закрываем браузер
    browser.quit()
