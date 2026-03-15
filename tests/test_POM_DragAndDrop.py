import pytest

pytestmark = [pytest.mark.ui, pytest.mark.dragndrop]

# BOXES

@pytest.mark.smoke
@pytest.mark.positive
def test_boxes_page_has_two_squares(drag_and_drop_page):
    drag_and_drop_page.open_boxes_tab()
    assert drag_and_drop_page.boxes_count() == 2

@pytest.mark.positive
def test_bottom_square_is_visible_and_draggable(drag_and_drop_page):
    drag_and_drop_page.open_boxes_tab()
    assert drag_and_drop_page.draggable_box_is_visible() is True


@pytest.mark.positive
def test_drag_and_drop_boxes_with_drag_to(drag_and_drop_page):
    drag_and_drop_page.open_boxes_tab()
    drag_and_drop_page.drag_box_to_target()
    drag_and_drop_page.check_box_drop_result()


@pytest.mark.positive
def test_drag_and_drop_boxes_manually(drag_and_drop_page):
    drag_and_drop_page.open_boxes_tab()
    drag_and_drop_page.drag_box_to_target_manually()
    drag_and_drop_page.check_box_drop_result()


@pytest.mark.positive
def test_bottom_square_can_be_dragged_only_once(drag_and_drop_page):
    drag_and_drop_page.open_boxes_tab()
    drag_and_drop_page.drag_box_to_target()

    first_result = drag_and_drop_page.get_box_drop_text()
    assert first_result == "Dropped!"

    drag_and_drop_page.drag_box_to_target()

    second_result = drag_and_drop_page.get_box_drop_text()
    assert second_result == "Dropped!"


# IMAGES

@pytest.mark.smoke
@pytest.mark.positive
def test_images_page_has_draggable_image(drag_and_drop_page):
    drag_and_drop_page.open_images_tab()
    assert drag_and_drop_page.image_drag_item_is_visible() is True


@pytest.mark.positive
def test_drag_and_drop_image(drag_and_drop_page):
    drag_and_drop_page.open_images_tab()
    drag_and_drop_page.drag_image_to_target()
    drag_and_drop_page.check_image_drop_result()