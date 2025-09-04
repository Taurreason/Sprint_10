import allure
import pytest

from selenium import webdriver

from pages.main_page import MainPage
from pages.route_selection_page import *
from pages.order_taxi_page import *
from service import *



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver  # возвращаем драйвер тесту
    driver.quit()
    
@pytest.fixture
def main_page(driver):
    with allure.step('Открываем главную страницу'):
        return MainPage(driver)
    

@pytest.fixture
def route_selection(driver):
    with allure.step('Открываем блок выбора маршрута'):
        return RouteSelectionPage(driver)

@pytest.fixture
def order_taxi(driver):
    return OrderTaxiPage(driver)

@pytest.fixture
def info_panel(driver):
    return InfoPanel(driver)

@pytest.fixture
def order_taxi_tariffs(driver):
    return Tariffs(driver)

@pytest.fixture
def route_types(driver):
    return Types(driver)

@pytest.fixture
def taxi_order_page(driver):
    with allure.step('Открываем главную страницу'):
        main_page = MainPage(driver)
        main_page.fill_route(
        TestData.ROUTING_ADDRESS.from_field,
        TestData.ROUTING_ADDRESS.to_field
        )
    with allure.step('Переходим к блоку выбора маршрута, выбираем тип Быстрый'):
        route_page = RouteSelectionPage(driver)
        route_page.modes.select(Mode.FAST)
        route_page.types.select(MoveType.TAXI)
        price_value = route_page.info.get_price_value()
    with allure.step('Ждём активность кнопки и жмём «Вызвать такси»'):
        route_page.taxi.is_call_taxi_enabled()
        route_page.taxi.call_taxi()
    return price_value


@pytest.fixture
def completed_order_taxi(driver, taxi_order_page):
        order_taxi = OrderTaxiPage(driver)
        with allure.step("Открыть панель заказа"):
            order_taxi.wait_opened_panel()
        with allure.step("Выбрать тариф 'Рабочий'"):
            order_taxi.tariffs.select(Tariff.WORKER)
        with allure.step("Нажимаем кнопку Заказать"):
            order_taxi.form.click_order_button_taxi()       
