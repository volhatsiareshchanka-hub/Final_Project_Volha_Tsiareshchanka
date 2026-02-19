from playwright.sync_api import Page, expect
import time
import pytest
import enum

class ProgramingLanguage(enum.Enum):
    PYTHON = 'Python'
    JAVASCRIPT = 'JavaScript'
    JAVA = 'Java'
    RUBY = 'Ruby'
    SHARP = 'C#'

# def test_single_select(page: Page):
#     page.goto("https://www.qa-practice.com/elements/select/single_select")
#     page.locator('#req_header').click()
#     page.locator('#id_choose_language').select_option('Python')
#     time.sleep(2)
#     page.get_by_role("button", name="Submit").click()
#     expect(page.get_by_text("You selected Python")).to_be_visible()
#     time.sleep(2)
#
#     page.get_by_role("link", name="Multiple selects").click()
#     page.locator('#req_header').click()
#     time.sleep(1)
#     page.locator('#id_choose_the_place_you_want_to_go').select_option('Ocean')
#     time.sleep(1)
#     page.locator('#id_choose_how_you_want_to_get_there').select_option('Air')
#     time.sleep(1)
#     page.locator('#id_choose_when_you_want_to_go').select_option('Next week')
#     time.sleep(1)
#     page.get_by_role("button", name="Submit").click()
#     expect(page.locator("#result"), "You selected to go by air to the ocean next week")
#     time.sleep(2)

# @pytest.mark.parametrize('value', ['Python', 'Java', 'Ruby'])
@pytest.mark.parametrize('value',[x.value for x in ProgramingLanguage])

def test_single_select(page: Page, value: str):
    page.goto("https://www.qa-practice.com/elements/select/single_select")
    time.sleep(2)
    page.locator('#req_header').click()
    # page.locator('#id_choose_language').select_option(ProgramingLanguage.JAVA)
    page.locator('#id_choose_language').select_option(value)
    time.sleep(2)
    page.get_by_role("button", name="Submit").click()
    expect(page.locator('#result-text'), ProgramingLanguage.JAVA)
    time.sleep(2)

    page.get_by_role("link", name="Multiple selects").click()
    page.locator('#req_header').click()
    time.sleep(1)
    page.locator('#id_choose_the_place_you_want_to_go').select_option('Ocean')
    time.sleep(1)
    page.locator('#id_choose_how_you_want_to_get_there').select_option('Air')
    time.sleep(1)
    page.locator('#id_choose_when_you_want_to_go').select_option('Next week')
    time.sleep(1)
    page.get_by_role("button", name="Submit").click()
    expect(page.locator("#result"), "You selected to go by air to the ocean next week")
    time.sleep(2)




