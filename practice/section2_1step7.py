from selenium import webdriver
import time
import os

# Настраиваем Selenium WebDriver, указывая путь к WebDriver
browser = webdriver.Chrome()

try:
    # Открываем страницу
    browser.get("http://suninjuly.github.io/file_input.html")

    # Заполняем текстовые поля: имя, фамилия, email
    first_name = browser.find_element("name", "firstname")
    first_name.send_keys("Ivan")

    last_name = browser.find_element("name", "lastname")
    last_name.send_keys("Ivanov")

    email = browser.find_element("name", "email")
    email.send_keys("ivan@example.com")

    # Создаем временный текстовый файл для загрузки
    file_name = "test.txt"
    file_path = os.path.join(os.getcwd(), file_name)

    with open(file_path, "w") as file:
        file.write("This is a test file")

    # Загружаем файл
    file_input = browser.find_element("id", "file")
    file_input.send_keys(file_path)

    # Нажимаем кнопку "Submit"
    submit_button = browser.find_element("css selector", "button.btn")
    submit_button.click()

    # Ждем некоторое время, чтобы увидеть результат (опционально)
    time.sleep(10)

finally:
    # Удаляем временный файл после выполнения задачи
    if os.path.exists(file_path):
        os.remove(file_path)

    # Закрываем браузер
    browser.quit()
