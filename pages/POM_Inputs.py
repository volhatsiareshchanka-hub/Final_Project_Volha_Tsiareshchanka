from playwright.sync_api import Playwright, expect, Page

URL = "https://www.qa-practice.com/elements/input/simple"

class InputsPage:
    def __init__(self, page: Page):
        self.page = page
        self.inputs_link = page.get_by_role("link", name="Inputs")
        self.input_field = page.locator("#id_text_string")
        self.result_text = page.locator("#result-text")


    def open(self) -> None:
        self.page.goto(URL)

    def go_to_inputs(self) -> None:
        self.inputs_link.click()

    def submit_text(self, text: str) -> None:
        self.input_field.click()
        self.input_field.fill(text)
        self.input_field.press("Enter")

    def check_result(self, text: str) -> None:
        expect(self.result_text).to_contain_text(text)

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
