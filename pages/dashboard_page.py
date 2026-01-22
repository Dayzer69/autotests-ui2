from pages.base_page import BasePage
from components.navigation.navbar_component import NavBarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.charts.chart_view_component import ChartViewComponent
from playwright.sync_api import Page, expect


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)

        self.navbar = NavBarComponent(page)

        self.dashboard_toolbar = DashboardToolbarViewComponent(page)

        self.students_chart = ChartViewComponent(page, 'students', 'bar')
        self.activities_chart = ChartViewComponent(page, "activities", "line")
        self.scores_chart = ChartViewComponent(page, "scores", "scatter")
        self.courses_chart = ChartViewComponent(page, "courses", "pie")




