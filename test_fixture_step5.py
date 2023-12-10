#Задание: параметризация тестов
#Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение. Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений. Ваша задача — реализовать автотест со следующим сценарием действий: 

#открыть страницу 
#авторизоваться на странице со своим логином и паролем (см. предыдущий шаг)
#ввести правильный ответ (поле перед вводом должно быть пустым)
#нажать кнопку "Отправить" 
#дождаться фидбека о том, что ответ правильный 
#
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Ответ на задание: The owls are not what they seem! OvO 
# для старта python -m pytest -v -s test_fixture_step5.py
# s, чтоб видеть print
# v, для того, чтобы запустить расширенный визуальный режим
uncorrected_results = []


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    #python -m pytest -v -s test_fixture_step5.py
    #browser.quit()
    

@pytest.mark.parametrize('link_task', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_find_ufo(browser, link_task):
    link = f"https://stepik.org/lesson/{link_task}/step/1?auth=login"
    browser.get(link)
    
    browser.find_element(By.ID, "id_login_email").send_keys("Вставь логин")
    
    browser.find_element(By.ID, "id_login_password").send_keys("Вставь пароль")
    browser.find_element(By.CSS_SELECTOR, ".sign-form__btn").click()
    
    answer_place = WebDriverWait(browser, 10) \
        .until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea'))).send_keys(str(math.log(int(time.time()))))
    
    submit_button = WebDriverWait(browser, 10) \
        .until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="submit-submission"]')))
    submit_button.click()
    
    option_text = WebDriverWait(browser, 10) \
        .until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="smart-hints__hint"]'))).text

    if option_text != "Correct!":
        uncorrected_results.append(option_text)

    assert "Correct!" == option_text, f'Error: {option_text}'