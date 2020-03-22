from IndividualsPage import IndividualsPage
from selenium import webdriver
from EosagoFormPage import EosagoFormPage
from Locators import EosagoCalculatorPage
from selenium.webdriver.support import expected_conditions as EC
import timeit, time, threading


class SyntheticTest:
    def __init__(self, browser, url, maximized=True):
        self.browser = browser
        self.url = url
        if maximized:
            self.browser.maximize_window()

    def test_scenario(self):

        individuals_page = IndividualsPage(self.browser, self.url)
        individuals_page.open()
        # Открыть всплывающее меню и перейти на страницу ОСАГО
        individuals_page.close_cookie_popup()
        individuals_page.open_eosago()

        eosago_form_page = EosagoFormPage(self.browser, self.browser.current_url)
        # Закрытие поп-апа
        eosago_form_page.close_popup(
            EosagoCalculatorPage.MODAL_WINDOW, EosagoCalculatorPage.CLOSE_BUTTON
        )
        # Заполенние формы
        eosago_form_page.fill_in_the_form()
        eosago_form_page.wait_for_loading()
        self.quit_browser()

    def quit_browser(self):
        self.browser.quit()


def init_test():
    setup = """\
from TestRun import SyntheticTest
from selenium import webdriver
url = "https://www.alfastrah.ru/"
browser = webdriver.Chrome()
test = SyntheticTest(browser,url)"""
    print(
        f'Execution time:{timeit.timeit(setup=setup, stmt="test.test_scenario()", number=1)}'
    )
    threading.Timer(60, init_test).start()


if __name__ == "__main__":
    init_test()
