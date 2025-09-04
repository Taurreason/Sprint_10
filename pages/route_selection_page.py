from enum import Enum
from selenium.common.exceptions import TimeoutException

from locators.route_selection_locators import *
from pages.base_page import BasePage
from service import *
from data import *


        
class Mode(Enum):
    OPTIMAL = "Оптимальный"
    FAST    = "Быстрый"
    CUSTOM  = "Свой"

class MoveType(Enum):
    CAR     = "car"
    WALK    = "walk"
    TAXI    = "taxi"
    BIKE    = "bike"
    SCOOTER = "scooter"
    DRIVE   = "drive"

class RouteSelectionPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.modes = Modes(driver)
        self.types = Types(driver)
        self.info  = InfoPanel(driver)
        self.taxi  = TaxiActions(driver)
        self.drive = DriveActions(driver)

    def wait_opened_panel(self):
        return bool(self.find(PanelLocators.PANEL))
    

# Виды маршрута: Оптимальный, Быстрый, Свой
class Modes(BasePage):
    def select(self, mode: Mode):
        self.alt_click(ModesLocators.BY_ROUTE_TYPE(mode.value)) 

    def get_active_text(self):
        return self.find(ModesLocators.ACTIVE).text.strip()

# Типы передвижения: Машина, Пешком, Такси, Велосипед, Самокат, Двайв
class Types(BasePage):

    def _name(self, t: MoveType | str):
        return t.value if isinstance(t, MoveType) else str(t)
    
    def select(self, t: MoveType):
        name = self._name(t)
        # self.wait_for_element_visibility(TypesLocators.BY_MOVE_TYPE(name))
        self.alt_click(TypesLocators.BY_MOVE_TYPE(name))

    def is_active(self, t: MoveType | str):
        name = self._name(t)
        # найдётся, только если активен
        return bool(self.find(TypesLocators.BY_MOVE_TYPE_ACTIVE(name)))
    
    def is_type_route_enabled(self, t: MoveType | str):
        name = self._name(t)
        try:
            el = self.find(TypesLocators.BY_MOVE_TYPE(name))
            return self.is_enabled(el)
        except TimeoutException:
            return False

# Блок информации: Стоимость, Время в пути
class InfoPanel(BasePage):
    def get_price_text(self):
        return self.find(InfoLocators.PRICE).text.strip()

    def get_price_value(self):
        digits = "".join(ch for ch in self.get_price_text() if ch.isdigit())
        return int(digits) if digits else -1

    def get_duration_text(self) -> str:
        return self.find(InfoLocators.DURATION).text.strip()
    
    def get_duration_minutes(self):
        text = self.get_duration_text()
        digits = "".join(ch for ch in text if ch.isdigit())
        return int(digits) if digits else 0

# Кнопка Вызвать такси для типа Такси
class TaxiActions(BasePage):
    def call_taxi(self):
        self.click(TaxiLocators.CALL_TAXI)

    def is_call_taxi_enabled(self):
        return bool(self.is_enabled(TaxiLocators.CALL_TAXI))

# Кнопка Забронировать для типа Драйв
class DriveActions(BasePage):
    def book(self):
        self.click(DriveLocators.BOOK_BUTTON)

    def is_book_drive_enabled(self):
        return self.is_enabled(DriveLocators.BOOK_BUTTON)
    



