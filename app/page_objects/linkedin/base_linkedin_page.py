from abc import ABC

from jobbot.app.page_objects.base_page import BasePage
from jobbot.app.page_objects.linkedin.linkedin_navigation_bar import LinkedinNavBar


class BaseLinkedinPage(BasePage, ABC):

    def __init__(self, driver):
        super().__init__(driver)
        self.nav_bar = LinkedinNavBar()
