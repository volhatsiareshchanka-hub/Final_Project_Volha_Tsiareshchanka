from playwright.sync_api import Page, expect
import time

def test_tabs(context):
    page = context.new_page()
    page.goto('https://www.qa-practice.com/elements/new_tab/link')
    with context.expect_page() as new_page_info:
        page.locator('#new-page-link').click()
    new_tab = new_page_info.value
    expect(new_tab.locator('#result-text')).to_have_text('I am a new page in a new tab')
    time.sleep(5)



