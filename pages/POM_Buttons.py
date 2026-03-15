from playwright.sync_api import Page, expect

URL = "https://www.qa-practice.com/elements/button/simple"

class ButtonsPage:

    def __init__(self, page: Page):
        self.page = page

        # Navigation
        self.buttons_link = page.get_by_role("link", name="Buttons")
        self.simple_tab = page.get_by_role("link", name="Simple button")
        self.looks_like_tab = page.get_by_role("link", name="Looks like a button")
        self.disabled_tab = page.get_by_role("link", name="Disabled")

        # Elements
        self.click_button = page.get_by_role("button", name="Click")
        self.link_button = page.get_by_role("link", name="Click")
        self.submit_button = page.get_by_role("button", name="Submit")

        self.select_state = page.locator("#id_select_state")
        self.result_text = page.get_by_text("Submitted")

    # Navigation

    def open(self):
        self.page.goto(URL)

    def go_to_buttons(self):
        self.buttons_link.click()

    def open_simple_button_tab(self):
        self.simple_tab.click()

    def open_looks_like_button_tab(self):
        self.looks_like_tab.click()

    def open_disabled_tab(self):
        self.disabled_tab.click()

    # Actions

    def click_simple_button(self):
        self.click_button.click()

    def click_link_button(self):
        self.link_button.click()

    def enable_button(self):
        self.select_state.select_option("Enabled")

    def click_submit(self):
        self.submit_button.click()

    # Assertions

    def check_result(self):
        expect(self.result_text).to_be_visible()

    def submit_button_disabled(self):
        expect(self.submit_button).to_be_disabled()