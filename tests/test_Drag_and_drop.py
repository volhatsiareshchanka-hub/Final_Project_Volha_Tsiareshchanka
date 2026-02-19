from playwright.sync_api import Page, expect
import time
import pytest

@pytest.mark.skip
def test_drag_and_drop(page: Page):
    page.goto("https://www.qa-practice.com/elements/dragndrop/boxes")
    page.locator('#req_header').click()
    time.sleep(3)
    source = page.locator('#rect-draggable')
    target = page.locator('#rect-droppable')
    source.drag_to(target)
    expect(page.locator('#text-droppable')).to_have_text('Dropped!')
    time.sleep(2)


def test_drag_and_drop_manual(page: Page):
    page.goto("https://www.qa-practice.com/elements/dragndrop/boxes")
    page.locator('#req_header').click()
    time.sleep(3)
    source = page.locator('#rect-draggable')
    target = page.locator('#rect-droppable')
    source.hover()
    time.sleep(1)
    page.mouse.down()
    time.sleep(1)
    target.hover()
    time.sleep(1)
    page.mouse.up()
    time.sleep(1)
    expect(page.locator('#text-droppable')).to_have_text('Dropped!')
    time.sleep(2)

    page.get_by_role("link", name="Images").click()
    page.locator('#req_header').click()
    time.sleep(1)
    source = page.locator('#rect-droppable1 img')
    target = page.locator('#rect-droppable2')
    source.drag_to(target)
    expect(page.locator('#rect-droppable2')).to_have_text('Dropped!')
    time.sleep(2)


