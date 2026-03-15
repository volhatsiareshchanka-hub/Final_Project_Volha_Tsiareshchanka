import pytest

pytestmark = [pytest.mark.ui, pytest.mark.popup]

# MODAL POPUP

@pytest.mark.smoke
@pytest.mark.positive
def test_modal_page_has_launch_popup_button(popup_page):
    popup_page.open_modal_tab()
    assert popup_page.launch_popup_btn.is_visible() is True


@pytest.mark.positive
def test_modal_launch_button_opens_popup(popup_page):
    popup_page.open_modal_tab()
    popup_page.open_popup()
    popup_page.modal_is_open()


@pytest.mark.positive
def test_modal_title_is_correct(popup_page):
    popup_page.open_modal_tab()
    popup_page.open_popup()
    assert popup_page.get_modal_title_text() == "I am a Pop-Up"


@pytest.mark.positive
def test_modal_checkbox_can_be_selected(popup_page):
    popup_page.open_modal_tab()
    popup_page.open_popup()
    popup_page.check_modal_checkbox()
    assert popup_page.is_modal_checkbox_checked() is True


@pytest.mark.negative
def test_modal_send_without_checkbox_shows_no_result(popup_page):
    popup_page.open_modal_tab()
    popup_page.open_popup()
    popup_page.click_modal_send()

    assert popup_page.modal_result_exists() is False


@pytest.mark.positive
def test_modal_send_selected_checkbox_displays_result(popup_page):
    popup_page.open_modal_tab()
    popup_page.open_popup()
    popup_page.check_modal_checkbox()
    popup_page.click_modal_send()

    popup_page.check_modal_result_contains("select me or not")


# IFRAME POPUP

@pytest.mark.smoke
@pytest.mark.positive
def test_iframe_page_has_launch_popup_button(popup_page):
    popup_page.open_iframe_tab()
    assert popup_page.launch_popup_btn.is_visible() is True


@pytest.mark.positive
def test_iframe_launch_button_opens_popup(popup_page):
    popup_page.open_iframe_tab()
    popup_page.open_popup()
    popup_page.iframe_popup_is_open()


@pytest.mark.positive
def test_iframe_contains_page_title(popup_page):
    popup_page.open_iframe_tab()
    popup_page.open_popup()
    assert popup_page.get_iframe_title_text() == "Iframe page title"


@pytest.mark.positive
def test_iframe_contains_text_to_copy(popup_page):
    popup_page.open_iframe_tab()
    popup_page.open_popup()
    assert "I am the text you want to copy" in popup_page.get_iframe_text()


@pytest.mark.positive
def test_iframe_check_button_opens_input_form(popup_page):
    popup_page.open_iframe_tab()
    popup_page.open_popup()
    popup_page.click_iframe_check()

    assert popup_page.input_form_is_visible() is True


@pytest.mark.positive
def test_iframe_correct_text_shows_correct_message(popup_page):
    popup_page.open_iframe_tab()
    popup_page.open_popup()
    popup_page.click_iframe_check()
    popup_page.submit_value("I am the text you want to copy")

    popup_page.check_correct_message()


@pytest.mark.negative
def test_iframe_incorrect_text_shows_error_message(popup_page):
    popup_page.open_iframe_tab()
    popup_page.open_popup()
    popup_page.click_iframe_check()
    popup_page.submit_value("Wrong text")

    popup_page.check_incorrect_message()