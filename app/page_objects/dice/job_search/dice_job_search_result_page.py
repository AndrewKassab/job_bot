from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from dice_ai.app.enum.dice.employment_type import DiceEmploymentType
from dice_ai.app.enum.dice.dice_posted_date import DicePostedDate
from dice_ai.app.enum.dice.dice_work_settings import DiceWorkSetting
from dice_ai.app.page_objects.dice.base_dice_page import BaseDicePage
from dice_ai.app.page_objects.dice.job_search.dice_job_description_page import DiceJobDescriptionPage


class DiceJobSearchResultPage(BaseDicePage):

    __JOB_LINKS_LOCATOR = (By.XPATH, "//a[@data-cy='card-title-link']")
    __NEXT_BUTTON_LOCATOR = (By.XPATH, "//li[contains(@class,'pagination-next')]")
    __JOBS_PER_PAGE_SELECT_LOCATOR = (By.ID, "pageSize_2")

    def __init__(self, driver):
        super().__init__(driver)

    def toggle_work_settings_option(self, work_setting: DiceWorkSetting):
        list_element = self.find_element((By.CSS_SELECTOR, f"button[aria-label='Filter Search Results by {work_setting.value}']"))
        list_element.click()
        self.driver.refresh()
        return self

    def set_posted_date(self, posted_date: DicePostedDate):
        posted_date_element = self.find_element(
            (By.XPATH, f"//button[contains(text(),'{posted_date.value}')]"))
        posted_date_element.click()
        self.driver.refresh()
        return self

    def toggle_employment_type(self, employment_type: DiceEmploymentType):
        employment_type_element = self.find_element((By.CSS_SELECTOR, f"li[data-cy-value='{employment_type.value}']"))
        employment_type_element.click()
        self.driver.refresh()
        return self

    def toggle_easy_apply(self):
        easy_apply_element = self.find_element(
            (By.CSS_SELECTOR, f"button[aria-label='Filter Search Results by Easy Apply']"))
        easy_apply_element.click()
        self.driver.refresh()
        return self

    def maximize_jobs_per_page(self):
        jobs_per_page_select = self.find_element(self.__JOBS_PER_PAGE_SELECT_LOCATOR)
        select = Select(jobs_per_page_select)
        select.select_by_visible_text('100')
        return self

    def get_number_of_jobs_on_page(self):
        job_links = self.find_elements(self.__JOB_LINKS_LOCATOR)
        return len(job_links)

    def select_job_at_index(self, index) -> DiceJobDescriptionPage:
        job_links = self.find_elements(self.__JOB_LINKS_LOCATOR)
        job_links[index].click()

        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])

        return DiceJobDescriptionPage(self.driver)

    def click_next_page(self):
        next_page_element = self.find_element(self.__NEXT_BUTTON_LOCATOR)
        next_page_element.click()
        return self

    def is_next_page_available(self):
        next_page_element = self.find_element(self.__NEXT_BUTTON_LOCATOR)
        return 'disabled' in (next_page_element.get_attribute('class').split())

    def is_job_at_index_applied(self, index):
        job_links = self.find_elements(self.__JOB_LINKS_LOCATOR)
        job_at_index_link = job_links[index]
        card_header_div = job_at_index_link.find_element(By.XPATH, "ancestor::div[contains(@class, 'card-header')]")

        applied_elements = card_header_div.find_elements(By.XPATH, ".//div[contains(@class, 'ribbon-status-applied')]")

        if applied_elements:
            return True
        return False
