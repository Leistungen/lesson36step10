from selenium.webdriver.common.by import By
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."


def test_dobavlenie_v_korzinu(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket"), "Отсутствует кнопка корзины"

