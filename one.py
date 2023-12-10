
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "https://stepik.org/lesson/236895/step/1"
browser = webdriver.Chrome()
try: 
    def get_time_fun():
        return math.log(int(time.time()))
    
    uncorrected_results = []

    
    browser.get(link)
    browser.implicitly_wait(5)
    browser.get("https://stepik.org/lesson/236895/step/1")
    #browser.find_element(By.CSS_SELECTOR, "ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button").click()
    
    #time.sleep(2)
    browser.find_element(By.ID, "id_login_email").send_keys("zigolenko@rambler.ru")
    
    browser.find_element(By.ID, "id_login_password").send_keys("561028")
    browser.find_element(By.CSS_SELECTOR, ".sign-form__btn").click()
    #browser.find_element(By.CSS_SELECTOR, "again-btn.white").click()
    #browser.find_element(By.CSS_SELECTOR, "nth-child(1)").click()
    #time.sleep(2)
    answer_place = WebDriverWait(browser, 10) \
        .until(EC.visibility_of_element_located((By.CSS_SELECTOR, ' textarea'))).send_keys(str(math.log(int(time.time()))))
    #time.sleep(2)
    #answer_place.send_keys(str(math.log(int(time.time()))))
    #time.sleep(2)
    submit_button = WebDriverWait(browser, 55) \
        .until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="submit-submission"]')))
    submit_button.click()
    
    option_text = WebDriverWait(browser, 55) \
        .until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="smart-hints__hint"]'))).text

    if option_text != "Correct!":
        uncorrected_results.append(option_text)

    assert "Correct!" == option_text, f'Error: {option_text}'

finally:
    # îæèäàíèå ÷òîáû âèçóàëüíî îöåíèòü ðåçóëüòàòû ïðîõîæäåíèÿ ñêðèïòà
    time.sleep(15)
    # çàêðûâàåì áðàóçåð ïîñëå âñåõ ìàíèïóëÿöèé
    browser.quit()




