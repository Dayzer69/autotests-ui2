from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.input import Input
from elements.text_area import TextArea


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title_input = Input(page, 'create-course-form-title-input', 'Course title')
        self.create_course_estimated_time_input = Input(
            page, 'create-course-form-estimated-time-input', 'Course estimated time'
        )
        self.create_course_description_textarea = TextArea(
            page, 'create-course-form-description-input', 'Course description'
        )
        self.create_course_max_score_input = Input(page, 'create-course-form-max-score-input', 'Course max score')
        self.create_course_min_score_input = Input(page, 'create-course-form-min-score-input', 'Course min score')

    def fill(self, title, estimated_time, description, max_score, min_score):
        self.create_course_title_input.fill(title)
        self.create_course_description_textarea.fill(description)
        self.create_course_estimated_time_input.fill(estimated_time)
        self.create_course_max_score_input.fill(max_score)
        self.create_course_min_score_input.fill(min_score)

    def check_visible(self, title, estimated_time, description, max_score, min_score):
        self.create_course_title_input.check_visible()
        self.create_course_title_input.check_has_value(title)

        self.create_course_description_textarea.check_visible()
        self.create_course_description_textarea.check_has_value(description)

        self.create_course_estimated_time_input.check_visible()
        self.create_course_estimated_time_input.check_has_value(estimated_time)

        self.create_course_max_score_input.check_visible()
        self.create_course_max_score_input.check_has_value(max_score)

        self.create_course_min_score_input.check_visible()
        self.create_course_min_score_input.check_has_value(min_score)

