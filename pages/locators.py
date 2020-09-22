from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocals:
    BASKET_BUTTON = (By.XPATH, "//a[@class='btn btn-default']")
    BASKET_FORMSET = (By.ID, "#basket_formset")
    EMPTY_BASKET_MESSAGE = (By.ID, "content_inner")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_BASKET_NAME = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_BASKET_PRICE = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
