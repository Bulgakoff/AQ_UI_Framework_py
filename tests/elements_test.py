from pages.text_box_page import TextBoxPage


def test1(driver):
    text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
    text_box_page.open()
    text_box_page.fill_all_fields()
    output_FULL_name, output_email, output_CURRENT_address, output_Permanent_address = \
        text_box_page.check_filled_forms()
    print(output_Permanent_address)
    print(output_email)
    print(output_CURRENT_address)
    print(output_Permanent_address)
