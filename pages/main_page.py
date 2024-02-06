import allure
from pages.base_page import BasePage
from locators.locators_academy import MaincLoc

from config.variables import URL, PASSWORD, EMAIL


class MainPage(BasePage):
    """Методы главной станицы"""

    @staticmethod
    def opening_the_main_page(page: BasePage):
        """Метод открытия главной страницы"""
        with allure.step('Открытие главной страницы'):
            page.open(URL)
        with allure.step('Ожидаемый результат: Отобразится заголовок главной страницы'):
            page.element_is_visible(locator=MaincLoc.get('Заголовок главной страницы'))
        return MainPage
    
    @staticmethod
    def click_the_authorization_button(page: BasePage):
        """Метод открытие модального окна авторизации"""
        with allure.step('Кликнуть кнопку "Войти"'):
            page.element_to_be_clickable(locator=MaincLoc.get('Кнопка (Авторизоваться)'))
            page.move_to_element_and_click(locator=MaincLoc.get('Кнопка (Авторизоваться)'))
        with allure.step('Ожидаемый результат: Открылось модальное окно "Вход"'):
            page.element_is_visible(locator=MaincLoc.get('Заголовок модального окна'))
        return MainPage
    
    @staticmethod
    def enter_a_value_in_the_email_field(page: BasePage):
        """Метод на ввод значения в поле 'Email'"""
        with allure.step('Ввести значение в поле "Email"'):
            page.element_to_be_clickable(locator=MaincLoc.get('Поле (Email)'))
            page.set_value(locator=MaincLoc.get('Поле (Email)'), value=EMAIL)
        with allure.step('Ожидаемый результат: В поле "Email" ввелось значение'):
            page.text_to_be_present_in_element_value(locator=MaincLoc.get('Поле (Email)'),
                                                     value=EMAIL)
        return MainPage
    
    @staticmethod
    def enter_a_value_in_the_password_field(page: BasePage):
        """Метод на ввод значения в поле 'Пароль'"""
        with allure.step('Ввести значение в поле "Пароль"'):
            page.element_to_be_clickable(locator=MaincLoc.get('Поле (Пароль)'))
            page.set_value(locator=MaincLoc.get('Поле (Пароль)'), value=PASSWORD)
        with allure.step('Ожидаемый результат: В поле "Пароль" ввелось значение'):
            page.text_to_be_present_in_element_value(locator=MaincLoc.get('Поле (Пароль)'),
                                                     value=PASSWORD)
        return MainPage
    
    @staticmethod
    def click_the_login_button(page: BasePage):
        """Метод на клик по кнопке 'Войти'"""
        with allure.step('Кликнуть кнопку "Войти"'):
            page.element_to_be_clickable(locator=MaincLoc.get('Кнопка (Войти)'))
            page.move_to_element_and_click(locator=MaincLoc.get('Кнопка (Войти)'))
        with allure.step('Ожидаемый результат: 1.Закрылось модальное окно "Вход" \
                         2.Отобразилось уведомление об успешной авторизации'):
            page.element_is_visible(locator=MaincLoc.get('Уведомление (Об успешной авторизации)'))
            page.element_is_not_visible(locator=MaincLoc.get('Заголовок модального окна'))
        return MainPage
