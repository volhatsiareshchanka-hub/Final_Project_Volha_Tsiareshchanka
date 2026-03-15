from playwright.sync_api import Page, expect


class DragAndDropPage:
    BOXES_URL = "https://www.qa-practice.com/elements/dragndrop/boxes"
    IMAGES_URL = "https://www.qa-practice.com/elements/dragndrop/images"

    def __init__(self, page: Page):
        self.page = page

        # boxes tab
        self.box_drop_area = page.locator("#rect-droppable")
        self.box_drag_item = page.locator("#rect-draggable")
        self.box_drop_text = page.locator("#text-droppable")

        # images tab
        self.image_drag_item = page.locator("#rect-droppable1 img")
        self.image_target_area = page.locator("#rect-droppable2")

    # Open pages

    def open_boxes_tab(self) -> None:
        self.page.goto(self.BOXES_URL)
        expect(self.box_drag_item).to_be_visible()
        expect(self.box_drop_area).to_be_visible()

    def open_images_tab(self) -> None:
        self.page.goto(self.IMAGES_URL)
        expect(self.image_drag_item).to_be_visible()
        expect(self.image_target_area).to_be_visible()

    # Boxes actions

    def drag_box_to_target(self) -> None:
        self.box_drag_item.drag_to(self.box_drop_area)

    def drag_box_to_target_manually(self) -> None:
        self.box_drag_item.hover()
        self.page.mouse.down()
        self.box_drop_area.hover()
        self.page.mouse.up()

    def check_box_drop_result(self) -> None:
        expect(self.box_drop_text).to_have_text("Dropped!")

    def get_box_drop_text(self) -> str:
        return self.box_drop_text.inner_text().strip()

    def boxes_count(self) -> int:
        return self.page.locator("#rect-droppable, #rect-draggable").count()

    def draggable_box_is_visible(self) -> bool:
        return self.box_drag_item.is_visible()

    # Images actions

    def drag_image_to_target(self) -> None:
        self.image_drag_item.drag_to(self.image_target_area)

    def check_image_drop_result(self) -> None:
        expect(self.image_target_area).to_contain_text("Dropped!")

    def get_image_target_text(self) -> str:
        return self.image_target_area.inner_text().strip()

    def image_drag_item_is_visible(self) -> bool:
        return self.image_drag_item.is_visible()