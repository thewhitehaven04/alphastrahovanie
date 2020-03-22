from selenium.webdriver.common.by import By

# Пустые классы оставлены ради соблюдения иерархии
class BasePageLocators:
    COOKIE_WARNING = (By.ID, "closeCookieInfo")


class IndividualsLocators(BasePageLocators):
    pass


class MenuBar(IndividualsLocators):
    CARS = (By.CSS_SELECTOR, 'div[class="calc__item js-calc-item"]:nth-of-type(1)')


class Auto(IndividualsLocators):
    EOSAGO = (
        By.CSS_SELECTOR,
        'div[class="calc-popup__item"]>a[href="/individuals/auto/eosago/calc/"]',
    )


class EosagoCalculatorPage(BasePageLocators):
    MODAL_WINDOW = (By.CSS_SELECTOR, 'div[data-remodal-id="calc_eosago_choose_popup"]')
    CLOSE_BUTTON = (By.CSS_SELECTOR, 'a[class="modal__close _desktop"]')


class EosagoCalculatorForm(EosagoCalculatorPage):
    EOSAGO_CATEGORY = (By.CSS_SELECTOR, "select.js-eosago-category-select")
    EOSAGO_TYPE = (By.CSS_SELECTOR, "select.js-eosago-type-select")
    MANUFACTURER = (By.CSS_SELECTOR, "input[name='brand_name']")
    MODEL = (By.CSS_SELECTOR, 'input[name="model_name"]')
    MODEL_AUTOCOMPLETE = (By.CSS_SELECTOR, "div+div+div.autocomplete-suggestions")
    YEAR = (By.CSS_SELECTOR, 'select[name="year"]')
    MOD = (By.CSS_SELECTOR, 'select[name="modification"]')
    PURPOSE = (By.CSS_SELECTOR, 'select[name="purposeName"')
    REG_PLATE_ID = (By.ID, "AUTO_NUMBER")
    REG_PLATE_REGION = (By.ID, "AUTO_REGION")
    NO_REGISTRATION_CHECKBOX = (By.ID, "NO_REGISTRATION")
    CAR_ID_TYPE = (By.CSS_SELECTOR, 'select[name="CarIdType"]')
    CAR_ID_VALUE = (By.CSS_SELECTOR, 'input[name="CarIdValue"]')
    EXIT = (By.CSS_SELECTOR, 'input[class*="js-eosago-step1-form-auto-submit"]')
