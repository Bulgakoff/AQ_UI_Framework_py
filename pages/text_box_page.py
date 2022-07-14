import time

from locators.locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locator = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locator.FULL_NAME).send_keys("sqwe")
        self.element_is_visible(self.locator.EMAIL).send_keys("sadf@sdgfs.ru")
        self.element_is_visible(self.locator.CURRENT_ADDRESS).send_keys("asdfasdfa")
        self.element_is_visible(self.locator.Permanent_Address).send_keys("fsdfgfdgfg")
        self.element_is_visible(self.locator.SUBMIT_BUTTON).click()
        time.sleep(2)
