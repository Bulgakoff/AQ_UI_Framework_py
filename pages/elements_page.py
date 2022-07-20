import random
import time

from generator.generator import generated_person
from locators.locators import TextBoxPageLocators, CheckBoxPageLocators
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


class CheckBoxPage(BasePage):
    locator = CheckBoxPageLocators()

    def open_all_fields(self):
        self.element_is_visible(self.locator.EXPAND_ALL_BUTTON).click()
        # self.element_is_visible(self.locator.EXPAND_ALL_BUTTON)

    def click_random_checkbox(self):
        item_list = self.element_are_visible(self.locator.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
                # print(item.text)
            else:
                break

    def get_checked_chekckboxes(self):
        checked_list = self.element_are_presents(self.locator.CHECKED_ITEMS)
        data_checked = []
        for box in checked_list:
            title_item = box.find_element_by_xpath(self.locator.TITLE_ITEMS)
            data_checked.append(title_item.text)
        return data_checked

    def get_output_result(self):
        result_list = self.element_are_presents(self.locator.OUTPUT_RESULT_LIST)
        data_checked = []
        for item in result_list:
            data_checked.append(item.text)
        return data_checked





