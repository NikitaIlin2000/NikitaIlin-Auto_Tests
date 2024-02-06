from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, \
    StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger
from retry import retry

from config.variables import URL


class BasePage:
    """Базовые методы Selenium"""

    def __init__(self, driver):
        self.driver = driver
        self.url = URL
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(driver)

    def open(self, url: str = None):
        """
        Метод открывает страницу
        :param url: страница
        """
        url = url or self.url
        self.driver.get(url)
        return self
    
    @staticmethod
    def self_exception(err, locator=None):
        error = err.__class__.__name__

        match error:
            case 'InvalidSelectorException':
                raise Exception(f"Не валидный локатор {locator}")
            case "TimeoutException":
                raise Exception(f"Время ожидания вышло {locator}")
            case 'NoSuchElementException':
                raise Exception(f"Элемента нет на странице {locator}")
            case 'InvalidArgumentException':
                raise Exception(f"В метод передан не верный аргумент {locator}, возможно ожидали WebElement")
            case _:
                raise Exception("Неизвестная ошибка")
            
    def set_value(self, locator, value):
        """Метод на ввод значения в поле"""
        logger.info(f"Установить значение {value}")
        element = self.get_element_path(locator)
        element.send_keys(value)
        return self
            
    def element_to_be_clickable(self, locator):
        logger.info(f"Ожидать кликабельности элемента {locator}")
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
            return self
        except (TimeoutException, ElementClickInterceptedException):
            raise Exception(f"Время ожидания вышло, элемента нет на странице {locator}")
    
    def element_is_visible(self, locator):
        logger.info(f"Ожидать отображение элемента {locator}")
        try:
            self.wait.until(EC.visibility_of_element_located(locator=(By.XPATH, locator)))
            return self
        except BaseException as err:
            self.self_exception(err, locator)

    def element_is_not_visible(self, locator):
        logger.info(f"Проверить отсутствие отображения элемента {locator}")
        try:
            self.wait.until(EC.invisibility_of_element_located(locator=(By.XPATH, locator)))
            return self
        except TimeoutException:
            raise TimeoutException(f"Элемент {locator} присутствует на странице")
        
    def text_to_be_present_in_element_value(self, locator, value):
        """Проверить текст внутри поля для ввода (если текст не отображён в html)"""
        try:
            self.wait.until(EC.text_to_be_present_in_element_value((By.XPATH, locator), value))
        except(NoSuchElementException, TimeoutException):
            return False
        return True
    
    @retry((TimeoutException, NoSuchElementException), tries=5, delay=2)
    def get_element_path(self, locator: str) -> WebElement:
        """
        Найти элемент
        :param locator
        :return: element
        """
        try:
            return self.driver.find_element(By.XPATH, value=locator)
        except (TimeoutException, NoSuchElementException) as err:
            BasePage.self_exception(err, locator)
        except BaseException as err:
            BasePage.self_exception(err, locator)
    
    def move_to_element_and_click(self, locator: str):
        """Навести курсор на элемент и Нажать"""
        logger.info(f"Навести курсор на элемент и Нажать {locator}")
        for _ in range(3):
            try:
                element = self.get_element_path(locator=locator)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
                self.action.move_to_element(to_element=element).click(element).perform()
                break
            except self.self_exception(locator=locator, err='Не удалось навести курсор на элемент и нажать'):
                continue
        else:
            raise StaleElementReferenceException("Элемент стал устаревшим (StaleElementReferenceException)")
        return self
    