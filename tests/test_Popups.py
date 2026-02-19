from tkinter import dialog

from playwright.sync_api import Page, expect
import time

def test_alert(page: Page):
    page.goto('https://the-internet.herokuapp.com/javascript_alerts')
    time.sleep(5)
    def handle_dialog(dialog):
        time.sleep(5)
        dialog.accept()
    page.on("dialog", handle_dialog)
    page.get_by_text('Click for JS Alert').click()
    expect(page.locator("#result")).to_have_text("You successfully clicked an alert")
    time.sleep(5)


def test_alert_confirm_accept(page: Page):
    page.goto('https://the-internet.herokuapp.com/javascript_alerts')
    time.sleep(2)
    def handle_dialog(dialog):
        time.sleep(3)
        dialog.accept()
    page.on("dialog", handle_dialog)
    page.get_by_text('Click for JS Confirm').click()
    expect(page.locator("#result")).to_have_text("You clicked: Ok")
    time.sleep(5)


def test_alert_confirm_cancel(page: Page):
    page.goto('https://the-internet.herokuapp.com/javascript_alerts')
    time.sleep(2)
    def handle_dialog(dialog):
        time.sleep(3)
        dialog.dismiss()
    page.on("dialog", handle_dialog)
    page.get_by_text('Click for JS Confirm').click()
    expect(page.locator("#result")).to_have_text("You clicked: Cancel")
    time.sleep(5)

def test_prompt_accept(page: Page):
    page.goto('https://the-internet.herokuapp.com/javascript_alerts')
    time.sleep(2)
    def handle_dialog(dialog):
        time.sleep(3)
        dialog.accept("Hello, World")
        time.sleep(3)
    page.on("dialog", handle_dialog)
    time.sleep(3)
    page.get_by_text('Click for JS Prompt').click()
    expect(page.locator("#result")).to_have_text("You entered: Hello, World")
    time.sleep(5)

def test_modal_popup(page: Page):
    page.goto('https://www.qa-practice.com/elements/popup/modal')
    time.sleep(2)
    page.locator('#content > button').click()
    time.sleep(2)
    popup = page.locator('#content')
    checkbox = popup.locator('#id_checkbox_0')
    checkbox.check()
    time.sleep(2)
    button = popup.get_by_role('button', name='Send')
    button.click()
    time.sleep(2)
    expect(page.locator('#result-text')).to_have_text('select me or not')

    page.get_by_role("link", name="Iframe Pop-Up").click()
    page.locator('#req_header').click()
    time.sleep(2)
    page.get_by_role("button", name="Launch Pop-Up").click()
    page.locator('#text-to-copy').get_by_text('I am the text you want to copy')
    time.sleep(2)
    page.get_by_role("button", name="Check").click()
    time.sleep(2)
    input_field = page.locator("#id_text_from_iframe")
    input_field.click()
    input_field.fill('Hello, Playwright')
    page.get_by_role("button", name="Submit").click()
    expect(page.locator('#check-result')).to_have_text('Nope. Better luck next time!')
    time.sleep(2)






