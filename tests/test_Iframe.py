from playwright.sync_api import Page, expect
import time


def test_iframe(page: Page):
    page.goto('https://www.qa-practice.com/elements/iframe/iframe_page')
    new_page = page.frame_locator('iframe')
    element = new_page.locator("//span[@class = 'navbar-toggler-icon']")
    element.click()
    time.sleep(5)
    expect(new_page.get_by_role("heading", name="About")).to_be_visible()
    time.sleep(2)

# def test_iframe_without_frame(page: Page):
#     page.goto('https://www.qa-practice.com/elements/iframe/iframe_page')
#     page.locator("//span[@class = 'navbar-toggler-icon']").click()
#     time.sleep(5)
#     expect(page.locator('#text-droppable')).to_have_text('Dropped!')
#     time.sleep(2)  //*[@id="navbarHeader"]/div/div/div[1]/p