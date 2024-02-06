import allure
from pages.main_page import MainPage
from loguru import logger


@allure.title('Тест на открытие модального окна "Вход"')
def test_1_opening_a_modal_window_login(page):
    #Открытие главной страницы
    MainPage.opening_the_main_page(page=page)
    #Кликнуть кнопку "Авторизации"
    MainPage.click_the_authorization_button(page=page)
    message = '--------test_1_opening_a_modal_window_login pass--------'
    logger.info(message)
    