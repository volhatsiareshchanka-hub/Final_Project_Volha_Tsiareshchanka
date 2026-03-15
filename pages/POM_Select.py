import enum

from playwright.sync_api import Page, expect

class ProgrammingLanguage(enum.Enum):
    PYTHON = "Python"
    RUBY = "Ruby"
    JAVASCRIPT = "JavaScript"
    JAVA = "Java"
    SHARP = "C#"


class TravelPlace(enum.Enum):
    SEA = "Sea"
    OCEAN = "Ocean"
    MOUNTAINS = "Mountains"


class TravelWay(enum.Enum):
    CAR = "Car"
    TRAIN = "Train"
    AIR = "Air"


class TravelTime(enum.Enum):
    TODAY = "Today"
    TOMORROW = "Tomorrow"
    NEXT_WEEK = "Next week"


class SelectPage:
    SINGLE_URL = "https://www.qa-practice.com/elements/select/single_select"
    MULTIPLE_URL = "https://www.qa-practice.com/elements/select/mult_select"

    def __init__(self, page: Page):
        self.page = page

        # common
        self.submit_btn = page.get_by_role("button", name="Submit")

        # single select
        self.single_label = page.locator("label[for='id_choose_language']")
        self.single_select = page.locator("#id_choose_language")
        self.single_result = page.locator("#result-text")

        # multiple selects
        self.place_label = page.locator("label[for='id_choose_the_place_you_want_to_go']")
        self.transport_label = page.locator("label[for='id_choose_how_you_want_to_get_there']")
        self.when_label = page.locator("label[for='id_choose_when_you_want_to_go']")

        self.place_select = page.locator("#id_choose_the_place_you_want_to_go")
        self.transport_select = page.locator("#id_choose_how_you_want_to_get_there")
        self.when_select = page.locator("#id_choose_when_you_want_to_go")

        self.multiple_result = page.locator("#result-text, #result")

    # Open pages

    def open_single_select_tab(self) -> None:
        self.page.goto(self.SINGLE_URL)
        expect(self.single_select).to_be_visible()

    def open_multiple_selects_tab(self) -> None:
        self.page.goto(self.MULTIPLE_URL)
        expect(self.place_select).to_be_visible()

    # Single select actions

    def select_language(self, value: str) -> None:
        self.single_select.select_option(label=value)

    def get_single_label_text(self) -> str:
        return self.single_label.inner_text().strip()

    def get_selected_language_text(self) -> str:
        return self.single_select.locator("option:checked").inner_text().strip()

    # Multiple selects actions

    def select_place(self, value: str) -> None:
        self.place_select.select_option(label=value)

    def select_transport(self, value: str) -> None:
        self.transport_select.select_option(label=value)

    def select_when(self, value: str) -> None:
        self.when_select.select_option(label=value)

    def fill_multiple_selects(self, place: str, transport: str, when: str) -> None:
        self.select_place(place)
        self.select_transport(transport)
        self.select_when(when)

    def get_place_label_text(self) -> str:
        return self.place_label.inner_text().strip()

    def get_transport_label_text(self) -> str:
        return self.transport_label.inner_text().strip()

    def get_when_label_text(self) -> str:
        return self.when_label.inner_text().strip()

    # Common actions

    def submit(self) -> None:
        self.submit_btn.click()

    def is_submit_enabled(self) -> bool:
        return self.submit_btn.is_enabled()

    # Result helpers

    def check_single_result_contains(self, text: str) -> None:
        expect(self.single_result).to_contain_text(text)

    def check_multiple_result_contains(self, text: str) -> None:
        expect(self.multiple_result).to_contain_text(text)

    def check_multiple_result_phrase(self, phrase: str) -> None:
        expect(self.page.get_by_text(phrase, exact=False)).to_be_visible()

    def get_multiple_result_text(self) -> str:
        if self.page.locator("#result-text").count() > 0:
            return self.page.locator("#result-text").inner_text().strip()

        if self.page.locator("#result").count() > 0:
            return self.page.locator("#result").inner_text().strip()

        return ""

    # Validation helpers

    def single_select_is_valid(self) -> bool:
        return self.single_select.evaluate("el => el.validity.valid")

    def single_select_validation_message(self) -> str:
        return self.single_select.evaluate("el => el.validationMessage")

    def multiple_selects_are_valid(self) -> bool:
        return (
            self.place_select.evaluate("el => el.validity.valid")
            and self.transport_select.evaluate("el => el.validity.valid")
            and self.when_select.evaluate("el => el.validity.valid")
        )