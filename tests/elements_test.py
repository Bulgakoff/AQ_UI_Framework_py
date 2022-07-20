from pages.elements_page import CheckBoxPage
from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:
        def test1(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_FULL_name, output_email, output_CURRENT_address, output_Permanent_address = \
                text_box_page.check_filled_forms()
            assert full_name == output_FULL_name, "данные full_name не равны"
            assert email == output_email, "данные email не равны"
            assert current_address == output_CURRENT_address, "данные current_address не равны"
            assert permanent_address == output_Permanent_address, "данные permanent_address не равны"

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_all_fields()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_chekckboxes()
            output_result = check_box_page.get_output_result()
            print(input_checkbox)
            print(output_result)
            assert input_checkbox == output_result
