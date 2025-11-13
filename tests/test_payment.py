import allure
import pytest
import time
from allure_commons.types import AttachmentType

# --- ШАГИ ТЕСТА 1 ---
@allure.title("Тест 1: Логин в систему для оплаты")
@allure.step("Шаг 1: Открыть страницу логина")
def step_login_open_page():
    allure.attach("Страница логина открыта", name="Скрин страницы логина", attachment_type=AttachmentType.TEXT)

@allure.step("Шаг 2: Ввести логин и пароль")
def step_login_enter_creds():
    allure.attach("Логин: user@example.com, Пароль: ****", name="Учётные данные", attachment_type=AttachmentType.TEXT)

@allure.step("Шаг 3: Нажать 'Войти'")
def step_login_submit():
    allure.attach("Вход выполнен", name="Подтверждение входа", attachment_type=AttachmentType.TEXT)

def test_login_for_payment():
    step_login_open_page()
    step_login_enter_creds()
    step_login_submit()
    assert True, "Логин прошёл"

# --- ШАГИ ТЕСТА 2 ---
@allure.title("Тест 2: Добавление товара в корзину перед оплатой")
@allure.step("Шаг 1: Открыть страницу товара")
def step_add_product_open():
    allure.attach("Товар 'Книга'", name="Страница товара", attachment_type=AttachmentType.TEXT)

@allure.step("Шаг 2: Нажать 'Добавить в корзину'")
def step_add_product_click():
    allure.attach("Товар добавлен", name="Подтверждение добавления", attachment_type=AttachmentType.TEXT)

@allure.step("Шаг 3: Проверить корзину")
def step_add_product_check_cart():
    allure.attach("Корзина: 1 товар", name="Содержимое корзины", attachment_type=AttachmentType.TEXT)

def test_add_product_to_cart(): 
    step_add_product_open()
    step_add_product_click()
    step_add_product_check_cart()
    assert False, "Искусственный провал для получения статуса Failed"

# --- ШАГИ ТЕСТА 3 ---
@allure.title("Тест 3: Переход к оплате из корзины")
@allure.step("Шаг 1: Открыть корзину")
def step_checkout_open_cart():
    allure.attach("Корзина открыта", name="Открытие корзины", attachment_type=AttachmentType.TEXT)

@allure.step("Шаг 2: Нажать 'Оформить заказ'")
def step_checkout_click():
    allure.attach("Переход к оплате", name="Оформление", attachment_type=AttachmentType.TEXT)

@allure.step("Шаг 3: Проверить страницу оплаты")
def step_checkout_verify_page():
    allure.attach("Страница оплаты загружена", name="Проверка страницы", attachment_type=AttachmentType.TEXT)

def test_checkout_from_cart(): # ТЕСТ 3: НЕИЗВЕСТНЫЙ (ДОЛГИЙ, Job 2)
    time.sleep(180) # <--- ОСТАВЛЕНО! (Для прерывания таймаутом)
    step_checkout_open_cart()
    step_checkout_click()
    step_checkout_verify_page()
    assert True, "Переход к оплате успешен"

# --- ШАГИ ТЕСТА 4 ---
@allure.title("Тест 4: Выбор метода оплаты")
@allure.step("Шаг 1: Открыть страницу методов оплаты")
def step_payment_method_open():
    allure.attach("Методы: Карта, PayPal", name="Методы оплаты", attachment_type=AttachmentType.TEXT)

@allure.step("Шаг 2: Выбрать 'Кредитная карта'")
def step_payment_method_select():
    allure.attach("Выбрано 'Кредитная карта'", name="Выбор метода", attachment_type=AttachmentType.TEXT)

@allure.step("Шаг 3: Подтвердить выбор")
def step_payment_method_confirm():
    allure.attach("Метод подтверждён", name="Подтверждение", attachment_type=AttachmentType.TEXT)

def test_select_payment_method(): # ТЕСТ 4: НЕИЗВЕСТНЫЙ (ДОЛГИЙ, Job 2)
    time.sleep(180) # <--- ОСТАВЛЕНО!
    step_payment_method_open()
    step_payment_method_select()
    step_payment_method_confirm()
    assert True, "Метод оплаты выбран"

# --- ШАГИ ТЕСТА 5 ---
@allure.title("Тест 5: Подтверждение оплаты")
@allure.step("Шаг 1: Ввести данные карты")
def step_payment_enter_details():
    allure.attach("Карта: 4111****1111, CVV: ***", name="Данные карты", attachment_type=AttachmentType.TEXT)

@allure.step("Шаг 2: Нажать 'Оплатить'")
def step_payment_submit():
    allure.attach("Оплата отправлена", name="Отправка", attachment_type=AttachmentType.TEXT)

@allure.step("Шаг 3: Проверить подтверждение оплаты")
def step_payment_verify():
    allure.attach("Оплата успешна, заказ #12345", name="Подтверждение", attachment_type=AttachmentType.TEXT)

def test_confirm_payment(): # ТЕСТ 5: НЕИЗВЕСТНЫЙ (ДОЛГИЙ, Job 2)
    time.sleep(180) # <--- ОСТАВЛЕНО!
    step_payment_enter_details()
    step_payment_submit()
    step_payment_verify()
    assert True, "Оплата подтверждена"
