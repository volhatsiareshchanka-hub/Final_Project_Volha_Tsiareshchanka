import pytest

pytestmark = [pytest.mark.ui, pytest.mark.checkbox]

# SINGLE CHECKBOX

@pytest.mark.smoke
@pytest.mark.positive
def test_single_checkbox_page_has_one_checkbox(checkbox_page):
    checkbox_page.open_single_checkbox_tab()
    assert checkbox_page.single_checkbox_count() == 1


@pytest.mark.positive
def test_single_checkbox_label_is_correct(checkbox_page):
    checkbox_page.open_single_checkbox_tab()
    assert checkbox_page.get_single_checkbox_label_text() == "Select me or not"


@pytest.mark.positive
def test_single_checkbox_can_be_checked(checkbox_page):
    checkbox_page.open_single_checkbox_tab()
    checkbox_page.check_single_checkbox()
    assert checkbox_page.is_single_checkbox_checked() is True


@pytest.mark.positive
def test_single_checkbox_submit_button_is_enabled(checkbox_page):
    checkbox_page.open_single_checkbox_tab()
    assert checkbox_page.is_submit_enabled() is True


@pytest.mark.negative
def test_single_checkbox_without_selection_shows_no_result(checkbox_page):
    checkbox_page.open_single_checkbox_tab()
    checkbox_page.submit()

    assert checkbox_page.result_exists() is False

@pytest.mark.positive
def test_single_checkbox_selected_value_is_displayed_after_submit(checkbox_page):
    checkbox_page.open_single_checkbox_tab()
    checkbox_page.check_single_checkbox()
    checkbox_page.submit()

    checkbox_page.check_result_contains("select me or not")

# MULTIPLE CHECKBOXES

@pytest.mark.smoke
@pytest.mark.positive
def test_multiple_checkboxes_page_has_checkboxes(checkbox_page):
    checkbox_page.open_multiple_checkboxes_tab()
    assert checkbox_page.multiple_checkboxes_count() > 0


@pytest.mark.positive
@pytest.mark.parametrize(
    "index, expected_label",
    [
        (0, "One"),
        (1, "Two"),
        (2, "Three"),
    ],
    ids=[
        "checkbox_one",
        "checkbox_two",
        "checkbox_three",
    ],
)
def test_multiple_checkboxes_labels_are_correct(checkbox_page, index, expected_label):
    checkbox_page.open_multiple_checkboxes_tab()
    assert checkbox_page.get_multiple_checkbox_label_text(index) == expected_label


@pytest.mark.positive
@pytest.mark.parametrize(
    "index",
    [0, 1, 2],
    ids=["check_one", "check_two", "check_three"],
)
def test_multiple_checkbox_can_be_checked(checkbox_page, index):
    checkbox_page.open_multiple_checkboxes_tab()
    checkbox_page.check_multiple_checkbox(index)

    assert checkbox_page.is_multiple_checkbox_checked(index) is True


@pytest.mark.positive
def test_multiple_checkboxes_submit_button_is_enabled(checkbox_page):
    checkbox_page.open_multiple_checkboxes_tab()
    assert checkbox_page.is_submit_enabled() is True


@pytest.mark.negative
def test_multiple_checkboxes_without_selection_shows_no_result(checkbox_page):
    checkbox_page.open_multiple_checkboxes_tab()
    checkbox_page.submit()

    assert checkbox_page.result_exists() is False


@pytest.mark.positive
@pytest.mark.parametrize(
    "index, expected_result",
    [
        (0, "one"),
        (1, "two"),
        (2, "three"),
    ],
    ids=[
        "submit_one",
        "submit_two",
        "submit_three",
    ],
)
def test_single_selected_checkbox_is_displayed_after_submit(checkbox_page, index, expected_result):
    checkbox_page.open_multiple_checkboxes_tab()
    checkbox_page.check_multiple_checkbox(index)
    checkbox_page.submit()

    checkbox_page.check_result_contains(expected_result)