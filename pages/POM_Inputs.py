from playwright.sync_api import Page, expect


class InputsPage:
    TEXT_URL = "https://www.qa-practice.com/elements/input"
    EMAIL_URL = "https://www.qa-practice.com/elements/input/email"
    PASSWORD_URL = "https://www.qa-practice.com/elements/input/passwd"

    def __init__(self, page: Page):
        self.page = page
        self.result_text = page.locator("#result-text")

    @property
    def input_field(self):
        return self.page.locator("input.form-control")

    def open_text_tab(self) -> None:
        self.page.goto(self.TEXT_URL)
        expect(self.input_field).to_be_visible()

    def open_email_tab(self) -> None:
        self.page.goto(self.EMAIL_URL)
        expect(self.input_field).to_be_visible()

    def open_password_tab(self) -> None:
        self.page.goto(self.PASSWORD_URL)
        expect(self.input_field).to_be_visible()

    def fill_value(self, value: str) -> None:
        self.input_field.fill(value)

    def submit_with_enter(self) -> None:
        self.input_field.press("Enter")

    def submit_value(self, value: str) -> None:
        self.fill_value(value)
        self.submit_with_enter()

    def check_result_contains(self, text: str) -> None:
        expect(self.result_text).to_contain_text(text)

    def is_result_present(self) -> bool:
        return self.result_text.count() > 0

    def get_result_text(self) -> str:
        if self.result_text.count() > 0:
            return self.result_text.inner_text().strip()
        return ""

    def result_contains_text(self, text: str) -> bool:
        if self.result_text.count() == 0:
            return False
        return text in self.result_text.inner_text()

    def is_valid(self) -> bool:
        return self.input_field.evaluate("el => el.validity.valid")

    def is_value_missing(self) -> bool:
        return self.input_field.evaluate("el => el.validity.valueMissing")

    def get_validation_message(self) -> str:
        return self.input_field.evaluate("el => el.validationMessage")