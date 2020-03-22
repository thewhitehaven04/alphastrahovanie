from BasePage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from Locators import MenuBar, Auto, BasePageLocators
from selenium.webdriver.common.action_chains import ActionChains


class IndividualsPage(BasePage):
    def open_eosago(self):
        actionchain = ActionChains(self.browser)
        auto_menu = self.browser.find_element(*MenuBar.CARS)
        self.browser.execute_script("arguments[0].scrollIntoView();", auto_menu) # для стабильности, 
        eosago_calc = self.browser.find_element(*Auto.EOSAGO) # без скроллинга экшн-чейн в половине случаев нажимал не на ту кнопку

        actionchain.move_to_element(auto_menu)
        actionchain.move_to_element(eosago_calc)
        actionchain.click()
        actionchain.perform()

    def close_cookie_popup(self):
        self.browser.find_element(*BasePageLocators.COOKIE_WARNING).click()
