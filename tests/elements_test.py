
from pages.text_box_page import TextBoxPage


def test1(driver):
    text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
    text_box_page.open()
    text_box_page.fill_all_fields()



