import pytest
from playwright.sync_api import Page

@pytest.mark.buttons
def test_simple_button(buttons_page):
    buttons_page.open()
    buttons_page.go_to_buttons()

    buttons_page.open_simple_button_tab()
    buttons_page.click_simple_button()

    buttons_page.check_result()


@pytest.mark.buttons
def test_looks_like_button(buttons_page):
    buttons_page.open()
    buttons_page.go_to_buttons()

    buttons_page.open_looks_like_button_tab()
    buttons_page.click_link_button()

    buttons_page.check_result()


@pytest.mark.buttons
def test_disabled_button(buttons_page):
    buttons_page.open()
    buttons_page.go_to_buttons()

    buttons_page.open_disabled_tab()

    # Check disabled by default
    buttons_page.submit_button_disabled()

    # Enable and submit
    buttons_page.enable_button()
    buttons_page.click_submit()

    buttons_page.check_result()