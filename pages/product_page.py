from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "\"Add to basket\" button is not presented"

    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def product_name_in_message_should_be_the_same_as_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text in self.browser.find_element(
            *ProductPageLocators.PRODUCT_BASKET_NAME).text, "Product name is not the same you selected"

    def basket_price_should_be_equal_the_product_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text in self.browser.find_element(
            *ProductPageLocators.PRODUCT_BASKET_PRICE).text, "Product basket price is not equal product price"
