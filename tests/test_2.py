import allure
from pages.main_page import MainPage
from loguru import logger


@allure.title('Тест на ввод значения в поле "Email"')
def test_2_entering_a_value_in_the_email_field(page):
    #Открытие главной страницы
    MainPage.opening_the_main_page(page=page)
    #Кликнуть кнопку "Авторизации"
    MainPage.click_the_authorization_button(page=page)
    #Ввод значения в поле "Email"
    MainPage.enter_a_value_in_the_email_field(page=page)
    message = '--------test_2_entering_a_value_in_the_email_field pass--------'
    logger.info(message)
    