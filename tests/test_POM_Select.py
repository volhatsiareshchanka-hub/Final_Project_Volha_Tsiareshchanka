import pytest

from pages.POM_Select import (
    ProgrammingLanguage,
    TravelPlace,
    TravelWay,
    TravelTime,
)

pytestmark = [pytest.mark.ui, pytest.mark.select]

# SINGLE SELECT

@pytest.mark.smoke
@pytest.mark.positive
def test_single_select_label_is_correct(select_page):
    select_page.open_single_select_tab()
    assert select_page.get_single_label_text() == "Choose language*"


@pytest.mark.positive
@pytest.mark.parametrize(
    "value",
    [x.value for x in ProgrammingLanguage],
    ids=[x.name.lower() for x in ProgrammingLanguage],
)
def test_single_select_user_can_select_any_language(select_page, value):
    select_page.open_single_select_tab()
    select_page.select_language(value)

    assert select_page.get_selected_language_text() == value

@pytest.mark.positive
@pytest.mark.parametrize(
    "value",
    [x.value for x in ProgrammingLanguage],
    ids=[x.name.lower() for x in ProgrammingLanguage],
)
def test_single_select_result_is_displayed_after_submit(select_page, value):
    select_page.open_single_select_tab()
    select_page.select_language(value)
    select_page.submit()

    select_page.check_single_result_contains(value)


@pytest.mark.negative
def test_single_select_is_required(select_page):
    select_page.open_single_select_tab()
    select_page.submit()

    assert select_page.single_select_is_valid() is False
    assert select_page.single_select_validation_message() != ""


@pytest.mark.positive
def test_single_select_submit_button_is_enabled(select_page):
    select_page.open_single_select_tab()
    assert select_page.is_submit_enabled() is True


# MULTIPLE SELECTS

@pytest.mark.smoke
@pytest.mark.positive
def test_multiple_selects_labels_are_correct(select_page):
    select_page.open_multiple_selects_tab()

    assert select_page.get_place_label_text() == "Choose the place you want to go*"
    assert select_page.get_transport_label_text() == "Choose how you want to get there*"
    assert select_page.get_when_label_text() == "Choose when you want to go*"


@pytest.mark.positive
def test_multiple_selects_submit_button_is_enabled(select_page):
    select_page.open_multiple_selects_tab()
    assert select_page.is_submit_enabled() is True


@pytest.mark.positive
@pytest.mark.parametrize(
    "place, transport, when",
    [
        (TravelPlace.OCEAN.value, TravelWay.AIR.value, TravelTime.NEXT_WEEK.value),
        (TravelPlace.SEA.value, TravelWay.CAR.value, TravelTime.TODAY.value),
        (TravelPlace.MOUNTAINS.value, TravelWay.TRAIN.value, TravelTime.TOMORROW.value),
    ],
    ids=[
        "ocean_air_next_week",
        "sea_car_today",
        "mountains_train_tomorrow",
    ],
)
def test_multiple_selects_user_can_choose_options(select_page, place, transport, when):
    select_page.open_multiple_selects_tab()
    select_page.fill_multiple_selects(place, transport, when)

    assert select_page.multiple_selects_are_valid() is True


@pytest.mark.positive
def test_multiple_selects_result_is_displayed_after_submit(select_page):
    select_page.open_multiple_selects_tab()
    select_page.fill_multiple_selects(
        TravelPlace.OCEAN.value,
        TravelWay.AIR.value,
        TravelTime.NEXT_WEEK.value,
    )
    select_page.submit()

    select_page.check_multiple_result_phrase(
        "to go by air to the ocean next week"
    )


@pytest.mark.negative
def test_multiple_selects_are_required(select_page):
    select_page.open_multiple_selects_tab()
    select_page.submit()

    assert select_page.multiple_selects_are_valid() is False