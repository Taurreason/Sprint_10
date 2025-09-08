from selenium.common.exceptions import TimeoutException

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from service import *
from data import *


class MainPage(BasePage):

    def __init__(self, *args):
        super().__init__(*args)
        self.open_url(site.main)

    def click_on_from_field(self):
        self.click(MainPageLocators.FROM_INPUT_FIELD)

    def enter_data_from_field(self, text):
        self.find(MainPageLocators.FROM_INPUT_FIELD).send_keys(text)

    def click_on_to_field(self):
        self.click(MainPageLocators.TO_INPUT_FIELD)

    def enter_data_to_field(self, text):
        self.find(MainPageLocators.TO_INPUT_ERROR).send_keys(text)

    def clear_data_from_field(self):
        self.click(MainPageLocators.FROM_CLEAR_BUTTON)

    def clear_data_to_field(self):
        self.click(MainPageLocators.TO_CLEAR_BUTTON)


    def wait_pins_visible(self):
        try:
            self.find(MainPageLocators.ROUTE_PIN_A)
            self.find(MainPageLocators.ROUTE_PIN_B)
            return True
        except TimeoutException:
            return False

   # "Откуда"
    def is_from_input_in_error(self) -> bool:
        return self._is_displayed(MainPageLocators.FROM_CONTAINER_ERROR)

    def is_from_error_text_visible(self) -> bool:
        return self._is_displayed(MainPageLocators.FROM_ERROR_TEXT)

    def get_from_marker_color(self) -> str:
        return self.find(MainPageLocators.FROM_ROW_MARKER) \
                   .value_of_css_property("background-color")

    def is_from_marker_red(self) -> bool:
        return self.get_from_marker_color() in ("rgb(252, 54, 59)", "rgba(252, 54, 59, 1)")

    # "Куда"
    def is_to_input_in_error(self) -> bool:
        return self._is_displayed(MainPageLocators.TO_CONTAINER_ERROR)

    def is_to_error_text_visible(self) -> bool:
        return self._is_displayed(MainPageLocators.TO_ERROR_TEXT)

    def get_to_marker_color(self) -> str:
        return self.find(MainPageLocators.TO_ROW_MARKER) \
                   .value_of_css_property("background-color")

    def is_to_marker_blue(self) -> bool:
        return self.get_to_marker_color() in ("rgb(47, 128, 237)", "rgba(47, 128, 237, 1)")
    

    def fill_route(self, from_addr = None, to_addr = None):
        from_addr = from_addr or TestData.ROUTING_ADDRESS.from_field
        to_addr = to_addr or TestData.ROUTING_ADDRESS.to_field
        self.click_on_from_field()
        self.enter_data_from_field(from_addr)
        self.click_on_to_field()
        self.enter_data_to_field(to_addr)
