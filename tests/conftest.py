import pytest
from playwright.sync_api import Page

# from playwright.sync_api import Page, expect
# from pages.drop_down_page2 import DropDownPage
#
# @pytest.fixture
# def select_page(page: Page)

# from playwright.async_api import Page
# from pages.drop_down_page2 import DropDownPage
#
# @pytest.fixture
# def select_page(page: Page):
#     return DropDownPage(page)


# from pages.POM_Inputs import InputsPage
# @pytest.fixture
# def inputs_page(page: Page):
#     return InputsPage(page)

# from pages.POM_Popups import PopupsPage
# @pytest.fixture
# def popup_page(page: Page):
#     return PopupsPage(page)

from pages.POM_Checkbox import CheckboxPage
@pytest.fixture
def checkbox_page(page: Page):
    return CheckboxPage(page)