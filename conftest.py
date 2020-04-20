import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def pytest_addoption(parser):
    """
    This function add more parameters for test-environment
    It means that we add --browser_name and --language as params
    Some example: pytest -v -tb=line --reruns 1 --browser_name=firefox --language=it AU_3_6_6.py
    """
    parser.addoption('--browser_name',
                     action='store',
                     default="chrome",
                     help="Choose browser for testing")
    parser.addoption('--language',
                     action='store',
                     default="en",
                     help="Choose language for testing")



@pytest.fixture(scope="function")
def browser(request):
    """
    request is native pytest fixture for take some params from command line
    we use this fixture for each test-case; in this case we choose browser-type and language;
    we launch browser before test-case starts and we quit from it after all actions
    """
    browser_name = request.config.getoption("browser_name")
    prefer_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_argument('headless')
        options.add_experimental_option('prefs', {'intl.accept_languages': prefer_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", prefer_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("param '--browser_name' should be chose")
    print(f"start {browser_name} browser for test..")
    yield browser
    print("\nquit browser..")
    browser.quit()


