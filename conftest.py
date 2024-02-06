from pages.base_page import BasePage
from utils.setup_driver import SetupDriver
import pytest

from config.variables import URL


def pytest_addoption(parser):
    """command-line options"""
    parser.addoption('--host',
                     default=URL,
                     action='store',
                     help='host fo testing')
    parser.addoption('--browser',
                     default='chrome',
                     action='store',
                     help='browser for UI tests')
    parser.addoption('--visible',
                     default="False",
                     action='store',
                     help='headless option for UI')
    parser.addoption('--login',
                     default="nikitka.ilin.1997@mail.ru",
                     action='store',
                     help='login')
    parser.addoption('--password',
                     default="89038928711Qq",
                     action='store',
                     help='password')


@pytest.fixture
def params(request):
    params = {
        'host': request.config.getoption('--host'),
        'login': request.config.getoption('--login'),
        'password': request.config.getoption('--password')
    }

    return params


# Фикстура для получения host из командной строки
@pytest.fixture(scope='session')
def cmd_host(request):
    """Return data from cmd
    :request source_host
    :response: host
    """
    host = request.config.getoption('--host')
    return host


@pytest.fixture(scope='session')
def cmd_browser(request):
    """Фикстура для получения browser из командной строки"""
    browser_from_cmd = request.config.getoption('--browser')
    if browser_from_cmd == 'chrome' or 'firefox':
        return browser_from_cmd
    else:
        raise ValueError(f'Для тестирования в {browser_from_cmd} не настроена конфигурация')


@pytest.fixture(scope="session")
def path_to_driver(cmd_browser):
    return SetupDriver.path_to_chrome()

@pytest.fixture(scope="function")
def driver(cmd_browser, request, path_to_driver):
    driver = SetupDriver.setup_driver(cmd_browser=cmd_browser, request=request, path_to_driver=path_to_driver)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def page(driver):
    return BasePage(driver)
