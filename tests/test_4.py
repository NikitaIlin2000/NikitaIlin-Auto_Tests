import allure
from pages.main_page import MainPage
from loguru import logger


@allure.title('Тест на авторизацию пользователя')
def test_4_user_authorization(page):
    #Открытие главной страницы
    MainPage.opening_the_main_page(page=page)
    #Кликнуть кнопку "Авторизации"
    MainPage.click_the_authorization_button(page=page)
    #Ввод значения в поле "Email"
    MainPage.enter_a_value_in_the_email_field(page=page)
    #Ввод значения в поле "Пароль"
    MainPage.enter_a_value_in_the_password_field(page=page)
    #Кликнуть кнопку "Войти"
    MainPage.click_the_login_button(page=page)
    message = '--------test_4_user_authorization pass--------'
    logger.info(message)
    