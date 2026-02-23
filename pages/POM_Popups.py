from playwright.sync_api import expect, Page

URL = "https://www.qa-practice.com/elements/popup/modal"

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



# def test_modal_popup(page: Page):
#     page.goto('https://www.qa-practice.com/elements/popup/modal')
#     time.sleep(2)
#     page.locator('#content > button').click()
#     time.sleep(2)
#     popup = page.locator('#content')
#     checkbox = popup.locator('#id_checkbox_0')
#     checkbox.check()
#     time.sleep(2)
#     button = popup.get_by_role('button', name='Send')
#     button.click()
#     time.sleep(2)
#     expect(page.locator('#result-text')).to_have_text('select me or not')












