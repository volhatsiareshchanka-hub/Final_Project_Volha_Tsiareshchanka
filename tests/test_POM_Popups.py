from tkinter import dialog

from playwright.sync_api import Page, expect
import time

from pages.POM_Popups import PopupsPage

URL = "https://www.qa-practice.com/elements/popup/modal"

def test_popups(popup_page, page: Page):
    popup_page.open()
    popup_page.open_modal()
    popup_page.select_checkbox()
    popup_page.submit_modal()
    popup_page.check_result("select me or not")


    # def open(self) -> None:
    #     self.page.goto(URL)
    #
    # def open_modal(self) -> None:
    #     self.open_modal.click()
    #
    # def select_checkbox(self) -> None:
    #     self.checkbox.check()
    #
    # def submit_modal(self):
    #     self.send_btn.click()
    #
    # def check_result(self, expected=None):
    #     expect(self.result).to_have_text(expected)



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
