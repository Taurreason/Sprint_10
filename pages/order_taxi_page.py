from enum import Enum, StrEnum
import pytest
from locators.order_taxi_locators import *
from locators.route_selection_locators import InfoLocators
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from service import *
from data import *


class Tariff(StrEnum):
    WORKER     = "Рабочий"
    SLEEPY     = "Сонный"
    VACATION   = "Отпускной"
    TALKATIVE  = "Разговорчивый"
    COMFORTING = "Утешительный"
    GLOSSY     = "Глянцевый"


class OrderTaxiPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.tariffs = Tariffs(driver)
        self.form = OrderForm(driver)
        self.popup = OrderTaxiPopup(driver)
        self.completed = CompletedOrderPopup(driver)
        self.details = DetailsCompletedOrderTaxi(driver)


    def wait_opened_panel(self):
        self.find_present(TaxiOrderPanelLocator.PANEL)
        return True


class Tariffs(BasePage):

    @staticmethod
    def _title(tariff):
        return tariff.value if hasattr(tariff, "value") else str(tariff)

    def ensure_selected(self, title: str):
        # выбираем карточку, только если она ещё не активна
        try:
            if self.get_active_text() == title:
                return
        except Exception:
            pass
        self.click(TariffTaxiLocators.CARD_CONTAINER_BY_TITLE(title))
        self.find_present(TariffTaxiLocators.CARD_ACTIVE_BY_TITLE(title))

    def get_all_titles(self):
        return [e.text.strip() for e in self.find_all(TariffTaxiLocators.ALL_TITLES)]
    
    def select(self, tariff: Tariff | str):
        name = tariff.value if isinstance(tariff, Tariff) else str(tariff)
        self.click(TariffTaxiLocators.CARD_BY_TITLE(name))
        self.find_present(TariffTaxiLocators.CARD_ACTIVE_BY_TITLE(name))

    def get_active_text(self):
        return self.find(TariffTaxiLocators.ACTIVE_TITLE).text.strip()

    def get_active(self):
        txt = self.get_active_text()
        for t in Tariff:
            if t.value == txt:
                return t
        return None

    def is_active(self, tariff: Tariff | str):
        expected = tariff.value if isinstance(tariff, Tariff) else str(tariff)
        return self.get_active_text() == expected


    # Навести на кнопку i и вернуть web-элемент тултипа
    def open_info(self, tariff):
        title = self._title(tariff)
        # 1) сначала активируем карточку
        self.ensure_selected(title)
        # 2) находим кнопку 'i'
        btn = self.find(TariffTaxiLocators.INFO_BTN_IN_CARD(title))
        self.hover(btn)
        tip_id = self.get_attr(btn, "data-for") 
        return self.visible_tooltip_by_id(tip_id)
        
    def get_tooltip_for(self, tariff):
        tip = self.open_info(tariff)

        title_el  = self.find_in(tip, TariffTaxiLocators.TOOLTIP_TITLE)
        prefix_el = self.find_in(tip, TariffTaxiLocators.TOOLTIP_PREFIX)
        postfix_el= self.find_in(tip, TariffTaxiLocators.TOOLTIP_POSTFIX)

        title  = (self.get_attr(title_el, "textContent")  or title_el.text).strip()
        prefix = (self.get_attr(prefix_el, "textContent") or prefix_el.text).strip()
        html   =  self.get_attr(postfix_el, "innerHTML")  or ""

        postfix = " ".join(s.strip() for s in html.replace("<br>", "\n").splitlines() if s.strip())
        return {"title": title, "prefix": prefix, "postfix": postfix}

        
class OrderForm(BasePage):

    def is_form_below_tariffs(self, tolerance_px: int = 1):
        cards = self.find(TariffTaxiLocators.CONTAINER)
        form  = self.find(FormLocators.FORM)

        try:
            from selenium.webdriver import ActionChains
            ActionChains(self.driver).move_by_offset(0, 0).perform()
        except Exception:
            pass

        cards_bottom = cards.rect['y'] + cards.rect['height']
        form_top     = form.rect['y']
        return form_top >= cards_bottom - tolerance_px
    
    def sections_present(self):
        try:
            self.find(FormLocators.PHONE_BUTTON)
            self.find(FormLocators.PAYMENT_BUTTON)
            self.find(FormLocators.COMMENT_INPUT)
            self.find(FormLocators.REQS_CONTAINER)
            return True
        except TimeoutException:
            return False
        
    def click_requirements_order_taxi(self):
        self.click(FormLocators.REQS_ARROW)

    def activate_switch_laptop_slider(self):
        self.scroll_to_end(TariffTaxiLocators.TARIFF_CARDS)
        self.click(FormLocators.SWITCH_LAPTOP_SLIDER)
        
    def click_order_button_taxi(self):
        self.click(FormLocators.BUTTON_ORDER_TAXI)

    def get_price_text(self):
        return self.find(InfoLocators.PRICE).text.strip()

class OrderTaxiPopup(BasePage):

    def check_header_order_taxi_popup(self):
        return self.find(OrderHeaderLocators.HEADER)
    
    def check_header_order_taxi_popup_text(self):
        return self.find(OrderHeaderLocators.TITLE).text.strip()

    def check_button_details_in_order_taxi_popup(self):
        return self.find(OrderHeaderLocators.DETAILS_BUTTON)
    
    def check_button_cancel_in_order_taxi_popup(self):
        return self.find(OrderHeaderLocators.CANCEL_BUTTON)
    
    def check_counter_time_in_order_taxi_popup(self):
        return self.find(OrderHeaderLocators.TIME)
    
    def details_label_text(self):
        return self.find(OrderHeaderLocators.DETAILS_LABEL).text.strip()

    def cancel_label_text(self):
        return self.find(OrderHeaderLocators.CANCEL_LABEL).text.strip()
    

class CompletedOrderPopup(BasePage):

    def get_order_number(self):
        return self.find(CompletedOrderLocators.ORDER_NUMBER).text.strip()

    def wait_until_order_assigned(self):
        self.wait_for_element_invisibility(CompletedOrderLocators.ORDER_NUMBER)

    def completed_details_label_text(self):
        return self.find(CompletedOrderLocators.DETAILS_LABEL).text.strip()

    def completed_cancel_label_text(self):
        return self.find(CompletedOrderLocators.CANCEL_LABEL).text.strip()
    
    def check_button_completed_details_in_order_taxi_popup(self):
        return self.find(CompletedOrderLocators.DETAILS_BUTTON)
    
    def check_button_completed_cancel_in_order_taxi_popup(self):
        return self.find(CompletedOrderLocators.CANCEL_BUTTON)
    
    def driver_info_in_order_taxi_popup(self):
        return self.find(CompletedOrderLocators.DRIVER_BUTTON)
    
    def click_cancel_button_in_order_taxi_popup(self):
        self.alt_click(CompletedOrderLocators.CANCEL_BUTTON)
    
class DetailsCompletedOrderTaxi(BasePage):

    def click_on_details_in_popup_completed_order(self):
        self.click(CompletedOrderLocators.DETAILS_BUTTON)

    def get_extra_price_text(self):
        return self.find(OrderDetailsLocators.EXTRA_PRICE_TEXT).text.strip()
    
    def get_extra_price_value(self):
        digits = "".join(ch for ch in self.get_extra_price_text() if ch.isdigit())
        return int(digits) if digits else -1
    