import time

from generator.generator import generated_person
from locators.locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locator = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locator.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locator.EMAIL).send_keys(email)
        self.element_is_visible(self.locator.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locator.Permanent_Address).send_keys(permanent_address)
        self.element_is_visible(self.locator.SUBMIT_BUTTON).click()
        time.sleep(2)
        return full_name, email, current_address, permanent_address

    def check_filled_forms(self):
        CREATED_FULL_name = self.element_is_present(self.locator.CREATED_FULL_NAME).text.split(":")[1]
        CREATED_email = self.element_is_present(self.locator.CREATED_EMAIL).text.split(":")[1]
        CREATED_CURRENT_address = self.element_is_present(self.locator.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        CREATED_Permanent_address = self.element_is_present(self.locator.CREATED_Permanent_Address).text.split(":")[1]
        return CREATED_FULL_name, CREATED_email, CREATED_CURRENT_address, CREATED_Permanent_address
