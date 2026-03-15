from playwright.sync_api import Page, expect

class PracticeFormPage:
    URL = "https://www.qa-practice.com/forms/practice-form"

    def __init__(self, page: Page):
        self.page = page

        # form fields
        self.first_name = page.locator("#firstName")
        self.last_name = page.locator("#lastName")
        self.email = page.locator("#userEmail")
        self.mobile = page.locator("#userNumber")
        self.date = page.locator("#dateOfBirthInput")

        # gender
        self.gender_female = page.locator("label[for='gender_1']")

        # submit
        self.submit_button = page.get_by_role("button", name="Submit")

        # result modal
        self.result_modal = page.locator(".modal-content")
        self.result_title = page.get_by_text("Thanks for submitting the form", exact=True)

    def open(self) -> None:
        self.page.goto(self.URL)
        expect(self.first_name).to_be_visible()

    def fill_form(self) -> None:
        self.first_name.fill("Olga")
        self.last_name.fill("Tsiareshchanka")
        self.email.fill("volha_tsiareshchanka@gmail.com")
        self.gender_female.click()
        self.mobile.fill("7277098233")

        self.date.fill("03 Mar 1989")
        self.page.keyboard.press("Tab")

    def submit_form(self) -> None:
        self.submit_button.click()

    def check_result_visible(self) -> None:
        expect(self.result_modal).to_be_visible()
        expect(self.result_title).to_be_visible()

    def get_result_text(self) -> str:
        return self.result_modal.inner_text()
