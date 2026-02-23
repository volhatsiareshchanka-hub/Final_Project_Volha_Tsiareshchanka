from playwright.sync_api import Page, expect
import time

from pages.POM_Checkbox import CheckboxPage

URL = "https://www.qa-practice.com/elements/checkbox/single_checkbox"

def test_check_checkbox(checkbox_page, page: Page ):
    checkbox_page.open()
    checkbox_page.check_checkbox()
    checkbox_page.submit()
    checkbox_page.check_result("select me or not")
