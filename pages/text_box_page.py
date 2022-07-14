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

    def check_filled_forms(self):
        CREATED_FULL_name = self.element_is_present(self.locator.CREATED_FULL_NAME).text.split(":")[1]
        CREATED_email = self.element_is_present(self.locator.CREATED_EMAIL).text.split(":")[1]
        CREATED_CURRENT_address = self.element_is_present(self.locator.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        CREATED_Permanent_address = self.element_is_present(self.locator.CREATED_Permanent_Address).text.split(":")[1]
        return CREATED_FULL_name, CREATED_email, CREATED_CURRENT_address, CREATED_Permanent_address
