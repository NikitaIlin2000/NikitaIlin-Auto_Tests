import allure
from pages.main_page import MainPage
from loguru import logger


@allure.title('Тест на ввод значения в поле "Пароль"')
def test_3_entering_a_value_in_the_password_field(page):
    #Открытие главной страницы
    MainPage.opening_the_main_page(page=page)
    #Кликнуть кнопку "Авторизации"
    MainPage.click_the_authorization_button(page=page)
    #Ввод значения в поле "Пароль"
    MainPage.enter_a_value_in_the_password_field(page=page)
    message = '--------test_3_entering_a_value_in_the_password_field pass--------'
    logger.info(message)
    