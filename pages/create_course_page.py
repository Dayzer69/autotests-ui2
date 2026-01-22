from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent

class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Элемент загурзки картинки
        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')

        # Элементы хеддера станицы
        self.create_course_toolbar = CreateCourseToolbarViewComponent(page)

        # Блок полей с данными о курсе
        self.create_course_form = CreateCourseFormComponent(page)

        # Блок для добавления упражнений
        self.create_exercise_toolbar = CreateCourseExercisesToolbarViewComponent(page)
        self.create_exercise_form = CreateCourseExerciseFormComponent(page)

        # Отображение блока упражнений, когда упражнения не добвлены
        self.exercises_empty_view = EmptyViewComponent(page,'create-course-exercises')


    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )


    def click_delete_exercise_button(self, index: int):
        # Обратите внимание, что локатор инициализируется непосредственно в методе.
        # Это временное решение, так как с классическим подходом POM сложно работать с динамическими локаторами.
        # В текущей реализации мы не можем заранее объявить локатор на уровне класса, поскольку его значение
        # зависит от переданного индекса.
        # В дальнейшем мы будем использовать паттерн PageFactory для более удобной обработки таких случаев
        # и динамических элементов на странице.
        delete_exercise_button = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-delete-exercise-button"
        )
        delete_exercise_button.click()

    def check_visible_create_exercise_form(self, index: int, title: str, description: str):
        exercise_subtitle = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-subtitle-text"
        )
        exercise_title_input = self.page.get_by_test_id(
            f"create-course-exercise-form-title-{index}-input"
        )
        exercise_description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input"
        )

        expect(exercise_subtitle).to_be_visible()
        expect(exercise_subtitle).to_have_text(f"#{index + 1} Exercise")

        expect(exercise_title_input).to_be_visible()
        expect(exercise_title_input).to_have_value(title)

        expect(exercise_description_input).to_be_visible()
        expect(exercise_description_input).to_have_value(description)

    def fill_create_exercise_form(self, index: int, title: str, description: str):
        exercise_title_input = self.page.get_by_test_id(
            f"create-course-exercise-form-title-{index}-input"
        )
        exercise_description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input"
        )

        exercise_title_input.fill(title)
        expect(exercise_title_input).to_have_value(title)

        exercise_description_input.fill(description)
        expect(exercise_description_input).to_have_value(description)