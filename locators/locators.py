from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # form field:
    FULL_NAME = (By.CSS_SELECTOR, "input[placeholder*='Full']")
    EMAIL = (By.CSS_SELECTOR, "input[placeholder*='name@']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[placeholder*='Current']")
    Permanent_Address = (By.CSS_SELECTOR, "textarea[id*='permanentAddress']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id*='submit']")

    # created form field:
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "p[id*='name']")
    CREATED_EMAIL = (By.CSS_SELECTOR, "p[id*='email']")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "p[id*='currentAddress']")
    CREATED_Permanent_Address = (By.CSS_SELECTOR, "p[id*='permanentAddress']")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEMS = ".//ancestor::span[@class='rct-text']//span[@class='rct-title']"
    #span[class='text-success']
    OUTPUT_RESULT_LIST = (By.CSS_SELECTOR, "span[class='text-success']")

