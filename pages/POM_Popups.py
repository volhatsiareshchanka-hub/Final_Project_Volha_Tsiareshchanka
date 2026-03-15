from playwright.sync_api import Page, expect

class PopupsPage:
    MODAL_URL = "https://www.qa-practice.com/elements/popup/modal"
    IFRAME_URL = "https://www.qa-practice.com/elements/popup/iframe_popup"

    def __init__(self, page: Page):
        self.page = page

        # common
        self.launch_popup_btn = page.get_by_role("button", name="Launch Pop-Up")
        self.result_text = page.locator("#result-text")

        # modal
        self.modal_popup = page.locator(".modal.show .modal-content")
        self.modal_title = self.modal_popup.locator(".modal-title")
        self.modal_checkbox = self.modal_popup.locator("#id_checkbox_0")
        self.modal_send_btn = self.modal_popup.get_by_role("button", name="Send")

        # iframe popup
        self.iframe_popup = page.locator(".modal.show .modal-content")
        self.iframe_frame = page.frame_locator(".modal.show iframe")
        self.iframe_title = self.iframe_frame.locator("h1")
        self.iframe_text = self.iframe_frame.locator("body")
        self.iframe_check_btn = self.iframe_popup.get_by_role("button", name="Check")

        # form after clicking Check
        self.input_field = page.locator("input.form-control")
        self.submit_btn = page.get_by_role("button", name="Submit")

        # exact result block
        self.check_result = page.locator("#check-result")
        self.correct_message = page.locator("#check-result.alert-success")
        self.incorrect_message = page.locator("#check-result.alert-warning")

    # Open pages

    def open_modal_tab(self) -> None:
        self.page.goto(self.MODAL_URL)
        expect(self.launch_popup_btn).to_be_visible()

    def open_iframe_tab(self) -> None:
        self.page.goto(self.IFRAME_URL)
        expect(self.launch_popup_btn).to_be_visible()

    # Common

    def open_popup(self) -> None:
        self.launch_popup_btn.click()

    # Modal

    def modal_is_open(self) -> None:
        expect(self.modal_popup).to_be_visible()

    def get_modal_title_text(self) -> str:
        return self.modal_title.inner_text().strip()

    def check_modal_checkbox(self) -> None:
        self.modal_checkbox.check()

    def is_modal_checkbox_checked(self) -> bool:
        return self.modal_checkbox.is_checked()

    def click_modal_send(self) -> None:
        self.modal_send_btn.click()

    def modal_result_exists(self) -> bool:
        return self.result_text.count() > 0

    def check_modal_result_contains(self, text: str) -> None:
        expect(self.result_text).to_contain_text(text)

    # Iframe popup

    def iframe_popup_is_open(self) -> None:
        expect(self.iframe_popup).to_be_visible()

    def get_iframe_title_text(self) -> str:
        return self.iframe_title.inner_text().strip()

    def get_iframe_text(self) -> str:
        return self.iframe_text.inner_text()

    def click_iframe_check(self) -> None:
        expect(self.iframe_check_btn).to_be_visible()
        self.iframe_check_btn.click()


    # Form after Check

    def input_form_is_visible(self) -> bool:
        expect(self.input_field).to_be_visible()
        return self.input_field.is_visible()

    def fill_input(self, text: str) -> None:
        expect(self.input_field).to_be_visible()
        self.input_field.fill(text)

    def submit_form(self) -> None:
        expect(self.submit_btn).to_be_visible()
        self.submit_btn.click()

    def submit_value(self, text: str) -> None:
        self.fill_input(text)
        self.submit_form()

    def check_correct_message(self) -> None:
        expect(self.correct_message).to_be_visible()
        expect(self.correct_message).to_contain_text("Correct!")

    def check_incorrect_message(self) -> None:
        expect(self.incorrect_message).to_be_visible()
        expect(self.incorrect_message).to_contain_text("Nope. Better luck next time!")