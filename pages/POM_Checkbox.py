from playwright.sync_api import expect, Page

class CheckboxPage:

    URL = "https://www.qa-practice.com/elements/checkbox/single_checkbox"
    def __init__(self, page: Page):
        self.page = page
        self.checkbox = page.locator("#id_checkbox_0")
        self.submit_btn = page.get_by_role("button", name="Submit")
        self.result = page.locator("#result-text")

    def open(self) -> None:
        self.page.goto(self.URL)

    def check_checkbox(self) -> None:
        self.checkbox.check()

    def submit(self) -> None:
        self.submit_btn.click()

    def check_result(self, expected: str = "select me or not") -> None:
        expect(self.result).to_contain_text(expected)







# def test_open_google(page: Page) -> None:
#     page.goto("https://www.qa-practice.com/")
#     time.sleep(2)
#
# # Single checkbox
#     page.get_by_role("link", name="Text input").click()
#     page.get_by_role("link", name="Checkbox").click()
#     page.locator('#req_header').click()
#     time.sleep(2)
#     page.locator('#id_checkbox_0').check()
#     page.get_by_role("button", name="Submit").click()
#     expect(page.get_by_text("Selected checkboxes: select me or not")).to_be_visible()
#     time.sleep(2)




class PopupsPage:
    def __init__(self, page: Page):

        self.page = page
        self.open_modal_btn = page.locator('#content > button')
        self.modal = page.locator('#content')
        self.checkbox = page.locator('#id_checkbox_0')
        self.send_btn = page.get_by_role('button', name='Send')
        self.result = page.locator("#result-text")


    def open(self) -> None:
        self.page.goto(URL)

    def open_modal(self) -> None:
        self.open_modal_btn.click()

    def select_checkbox(self) -> None:
        self.checkbox.check()

    def submit_modal(self):
        self.send_btn.click()

    def check_result(self, expected:str) -> None:
        expect(self.result).to_have_text(expected)
