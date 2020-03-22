from BasePage import BasePage
from selenium import webdriver
from Locators import EosagoCalculatorForm
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class EosagoFormPage(BasePage):
    def close_popup(self, pop_up_locator, close_button_locator):
        # закрытие поп-апа на странице электронного ОСАГО
        modal_window = self.browser.find_element(*pop_up_locator)
        WebDriverWait(self.browser, timeout=8).until(EC.visibility_of(modal_window))
        self.browser.find_element(*close_button_locator).click()

    def fill_in_the_form(self):
        # выбор категории
        eosago_category = Select(
            self.browser.find_element(*EosagoCalculatorForm.EOSAGO_CATEGORY)
        )
        eosago_category.select_by_index(2)

        WebDriverWait(self.browser, timeout=5).until(
            EC.element_to_be_clickable(EosagoCalculatorForm.MANUFACTURER)
        )
        manufacturer = self.browser.find_element(*EosagoCalculatorForm.MANUFACTURER)
        manufacturer.click()  # без предварительного клика send_keys отправлял сообщение не полностью
        manufacturer.send_keys("AUDI")

        eosago_elem = self.browser.find_element(*EosagoCalculatorForm.EOSAGO_CATEGORY)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", eosago_elem)

        # выбор модели
        model = self.browser.find_element(*EosagoCalculatorForm.MODEL)
        model.click()
        time.sleep(0.4) # некрасиво
        model.send_keys("R8")
        # выбрать год
        year = Select(self.browser.find_element(*EosagoCalculatorForm.YEAR))
        year.select_by_visible_text("2008")

        WebDriverWait(self.browser, timeout=5).until(
            EC.element_to_be_clickable(EosagoCalculatorForm.PURPOSE)
        )
        purpose = Select(self.browser.find_element(*EosagoCalculatorForm.PURPOSE))
        purpose.select_by_visible_text("Инкассация")

        #заполнить номер
        reg_plate_id = self.browser.find_element(*EosagoCalculatorForm.REG_PLATE_ID)
        reg_plate_id.send_keys("А")
        reg_plate_id.send_keys("123")
        reg_plate_id.send_keys("АР")

        #заполнить регион
        reg_plate_region = self.browser.find_element(
            *EosagoCalculatorForm.REG_PLATE_REGION
        )
        reg_plate_region.send_keys("079")

        #заполнить id и номер
        id_type = Select(self.browser.find_element(*EosagoCalculatorForm.CAR_ID_TYPE))
        id_type.select_by_visible_text("VIN")

        id_value = self.browser.find_element(*EosagoCalculatorForm.CAR_ID_VALUE)
        id_value.send_keys("123241")
        #отправить
        submit = self.browser.find_element(*EosagoCalculatorForm.EXIT)
        submit.click()

    def wait_for_loading(self):
        WebDriverWait(self.browser, timeout=5).until(EC.title_is("Электронное ОСАГО"))
