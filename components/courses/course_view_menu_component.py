from playwright.sync_api import Page, expect
from elements.button import Button

from components.base_component import BaseComponent


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = Button(page, 'course-view-menu-button', 'Course menu button')
        self.edit_menu_item = Button(page, 'course-view-edit-menu-item', 'Course edit button')
        self.delete_menu_item = Button(page, 'course-view-delete-menu-item', 'Course delete button')

    def click_edit(self, index: int):
        self.menu_button.click(nth=index)

        self.edit_menu_item.check_visible(nth=index)
        self.edit_menu_item.click(nth=index)

    def click_delete(self, index: int):
        self.menu_button.click(nth=index)

        self.delete_menu_item.check_visible(nth=index)
        self.delete_menu_item.click(nth=index)