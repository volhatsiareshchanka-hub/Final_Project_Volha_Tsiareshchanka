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

# from pages.POM_Checkbox import CheckboxPage
# @pytest.fixture
# def checkbox_page(page: Page):
#     return CheckboxPage(page)

# Inputs
import os
from datetime import datetime

import pytest
from pages.POM_Inputs import InputsPage


@pytest.fixture
def inputs_page(page):
    return InputsPage(page)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            page.screenshot(
                path=f"screenshots/{item.name}_{timestamp}.png",
                full_page=True
            )

# Checkbox

import pytest
from pages.POM_Checkbox import CheckboxPage

@pytest.fixture
def checkbox_page(page):
    return CheckboxPage(page)

# Popup
import pytest
from pages.POM_Popups import PopupsPage


@pytest.fixture
def popup_page(page):
    return PopupsPage(page)

import pytest
from pages.POM_Buttons import ButtonsPage


@pytest.fixture
def buttons_page(page):
    return ButtonsPage(page)

import pytest
from pages.POM_Select import SelectPage


@pytest.fixture
def select_page(page):
    return SelectPage(page)

import pytest
from pages.POM_DragAndDrop import DragAndDropPage


@pytest.fixture
def drag_and_drop_page(page):
    return DragAndDropPage(page)

import pytest
from pages.POM_PracticeForm import PracticeFormPage


@pytest.fixture
def practice_form_page(page):
    return PracticeFormPage(page)