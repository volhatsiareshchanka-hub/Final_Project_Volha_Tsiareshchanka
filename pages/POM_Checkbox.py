from playwright.sync_api import Page, expect

class CheckboxPage:
    SINGLE_URL = "https://www.qa-practice.com/elements/checkbox/single_checkbox"
    MULTIPLE_URL = "https://www.qa-practice.com/elements/checkbox/mult_checkbox"

    def __init__(self, page: Page):
        self.page = page
        self.submit_btn = page.get_by_role("button", name="Submit")
        self.result_text = page.locator("#result-text")

    def open_single_checkbox_tab(self) -> None:
        self.page.goto(self.SINGLE_URL)
        expect(self.submit_btn).to_be_visible()

    def open_multiple_checkboxes_tab(self) -> None:
        self.page.goto(self.MULTIPLE_URL)
        expect(self.submit_btn).to_be_visible()

    @property
    def single_checkbox(self):
        return self.page.locator("#id_checkbox_0")

    @property
    def single_checkbox_label(self):
        return self.page.locator("label[for='id_checkbox_0']")

    def multiple_checkbox(self, index: int):
        return self.page.locator(f"#id_checkboxes_{index}")

    def multiple_checkbox_label(self, index: int):
        return self.page.locator(f"label[for='id_checkboxes_{index}']")

    @property
    def all_multiple_checkboxes(self):
        return self.page.locator("input[name='checkboxes']")

    def submit(self) -> None:
        self.submit_btn.click()

    def check_single_checkbox(self) -> None:
        self.single_checkbox.check()

    def uncheck_single_checkbox(self) -> None:
        self.single_checkbox.uncheck()

    def check_multiple_checkbox(self, index: int) -> None:
        self.multiple_checkbox(index).check()

    def uncheck_multiple_checkbox(self, index: int) -> None:
        self.multiple_checkbox(index).uncheck()

    def check_multiple_checkboxes(self, indexes: list[int]) -> None:
        for index in indexes:
            self.check_multiple_checkbox(index)

    def is_single_checkbox_checked(self) -> bool:
        return self.single_checkbox.is_checked()

    def is_multiple_checkbox_checked(self, index: int) -> bool:
        return self.multiple_checkbox(index).is_checked()

    def is_submit_enabled(self) -> bool:
        return self.submit_btn.is_enabled()

    def single_checkbox_count(self) -> int:
        return self.page.locator("input[type='checkbox']").count()

    def multiple_checkboxes_count(self) -> int:
        return self.all_multiple_checkboxes.count()

    def get_single_checkbox_label_text(self) -> str:
        return self.single_checkbox_label.inner_text().strip()

    def get_multiple_checkbox_label_text(self, index: int) -> str:
        return self.multiple_checkbox_label(index).inner_text().strip()

    def check_result_contains(self, text: str) -> None:
        expect(self.result_text).to_contain_text(text)

    def result_exists(self) -> bool:
        return self.result_text.count() > 0

    def get_result_text(self) -> str:
        if self.result_text.count() > 0:
            return self.result_text.inner_text().strip()
        return ""