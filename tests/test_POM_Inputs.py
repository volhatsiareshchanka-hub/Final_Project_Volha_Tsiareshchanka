from playwright.sync_api import Page, expect
import time

from pages.POM_Inputs import InputsPage

URL = "https://www.qa-practice.com/elements/input/simple"

def test_inputs(inputs_page, page: Page):
    inputs_page.open()
    inputs_page.go_to_inputs()
    inputs_page.submit_text("Playwright")
    inputs_page.check_result("Playwright")


# def test_open_google(page: Page) -> None:
#     page.goto("https://www.qa-practice.com/")
#     time.sleep(2)
#
#     page.get_by_role("link", name="Text input").click()
#     page.get_by_role("link", name="Inputs").click()
#     page.locator('#req_header').click()
#     time.sleep(2)
#     input_field = page.locator("#id_text_string")
#     input_field.click()
#     input_field.fill('Playwright')
#     input_field.press("Enter")
#     expect(page.get_by_text("Your input was: Playwright")).to_be_visible()
#     time.sleep(2)



