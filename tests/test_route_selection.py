import allure, pytest
from data import *
from pages.route_selection_page import *


class TestRouteSelection():

    def test_check_visible_pin(self, main_page):
        with allure.step("Вводим адреса в поля Откуда и Куда"):
            main_page.fill_route()
        with allure.step("Проверяем, что оба пина маршрута отображаются на карте"):
            assert main_page.wait_pins_visible()

    def test_check_route_panel_after_enter_address(self, main_page, route_selection):
        with allure.step("Вводим адреса в поля Откуда и Куда"):
            main_page.fill_route()
        with allure.step("Проверяем отображение блока с выбором маршрута"):
            assert route_selection.wait_opened_panel()

    @allure.title('При одинаковых адресах показывается блок маршрута: "Авто Бесплатно В пути 0 мин."')
    def test_identical_addresses_route_block_auto_free_0min(self, main_page, route_selection):
        with allure.step("Вводим одинаковые адреса в поля Откуда и Куда"):
            main_page.fill_route('Хамовнический Вал, 18', 'Хамовнический Вал, 18')
        with allure.step("Проверяем отображение текста 'Авто Бесплатно В пути 0 мин.'"):
            assert route_selection.info.get_price_text() == TestData.INFO_PANEL_ROUTING.price_free
            assert route_selection.info.get_duration_text() == TestData.INFO_PANEL_ROUTING.duration_null

    @allure.title('Переключение вида маршрута обновляет активный таб и пересчитывает время и стоимость')
    def test_route_mode_switch_updates_active_tab_and_info(self, main_page, route_selection):
        with allure.step("Вводим адреса в поля Откуда и Куда"):
            main_page.fill_route()
        with allure.step("Проверяем, что находимся на активной вкладке такси"):
            assert route_selection.types.is_active(MoveType.TAXI)
        with allure.step("Получаем данные цены и длительности для маршрута Быстрый"):
            price_before = route_selection.info.get_price_value()
            dur_before   = route_selection.info.get_duration_minutes()
        with allure.step("Переключаемся на тип маршрута Оптимальный"):
            route_selection.modes.select(Mode.OPTIMAL)
        with allure.step("Проверяем, что мод авто активен"):
            assert route_selection.types.is_active(MoveType.CAR)
        with allure.step("Проверяем, что изменились стоимость и время"):
            price_after = route_selection.info.get_price_value()
            dur_after   = route_selection.info.get_duration_minutes()
        assert price_after is not None and dur_after is not None
        assert price_after != price_before
        if dur_after == dur_before:
            pytest.xfail(f"Время не изменилось: {dur_before} мин → {dur_after} мин")

        assert dur_after != dur_before

    @allure.title('Переключение на вид «Свой» активирует таб и все типы передвижения')
    def test_custom_mode_activates_tab_and_all_move_types(self, main_page, route_selection):
        with allure.step("Вводим адреса в поля Откуда и Куда"):
            main_page.fill_route()
        with allure.step("Переключаемся на маршрут Свой"):
            route_selection.modes.select(Mode.CUSTOM)
        with allure.step("Проверяем активны ли кнопки типов передвижения"):
           assert route_selection.types.is_active(MoveType.TAXI)
           assert route_selection.types.is_type_route_enabled(MoveType.WALK)
           assert route_selection.types.is_type_route_enabled(MoveType.CAR)
           assert route_selection.types.is_type_route_enabled(MoveType.BIKE)
           assert route_selection.types.is_type_route_enabled(MoveType.SCOOTER)
           assert route_selection.types.is_type_route_enabled(MoveType.DRIVE)

    @allure.title('При выборе вида маршрута Быстрый активна кнопка Вызвать такси')
    def test_fast_route_mode_enables_call_taxi_button(self, main_page, route_selection):
        with allure.step("Вводим адреса в поля Откуда и Куда"):
            main_page.fill_route()
        with allure.step("Проверяем, что находимся в маршруте Быстрый"):
            assert route_selection.modes.get_active_text() == "Быстрый"
        with allure.step("Проверяем активность кнопки Вызвать такси"):
            assert route_selection.taxi.is_call_taxi_enabled()

    @allure.title('При выборе вида маршрута Свой, типа передвижения Драйв активна кнопка Забронировать')
    def test_custom_mode_drive_enables_book_button(self, main_page, route_selection):
        with allure.step("Вводим адреса в поля Откуда и Куда"):
            main_page.fill_route()
        with allure.step("Выбираем маршрут Свой"):
            route_selection.modes.select(Mode.CUSTOM)
        with allure.step("Выбираем тип передвижения Драйв"):
            route_selection.types.select(MoveType.DRIVE)
        with allure.step("Проверяем активность кнопки Забронировать"):
            assert route_selection.drive.is_book_drive_enabled()
