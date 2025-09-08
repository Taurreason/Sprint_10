import allure, pytest
from pages.order_taxi_page import Tariff
from data import *



cases = list(TestData.TARIFFS.items())


class TestOrderTaxi:

    @allure.title('Открывается форма заказа со всеми 6 тарифами, "Рабочий" активный')
    def test_check_all_tariff_taxi_work_active(self, taxi_order_page, order_taxi):
        with allure.step("Открыть панель заказа"):
          order_taxi.wait_opened_panel()
        with allure.step("Получаем все тарифы"):
            shown = set(order_taxi.tariffs.get_all_titles())
            expected = {t.value for t in Tariff}
        
        assert shown == expected
        with allure.step("Выбираем тариф Рабочий, проверяем, что он активен"):
            order_taxi.tariffs.select(Tariff.WORKER)   
        assert order_taxi.tariffs.is_active(Tariff.WORKER)
        assert order_taxi.tariffs.get_active() == Tariff.WORKER


    @pytest.mark.parametrize("title,exp", cases, ids=[name for name, _ in cases])
    @allure.title('Тултип тарифа «{title}» соответствует ТЗ')
    def test_tariff_tooltip(self, taxi_order_page, order_taxi, title, exp):
        XFAIL_TITLES = {"Сонный", "Разговорчивый"}

        if title in XFAIL_TITLES:
            pytest.xfail("Текст префикса в UI не совпадает с ТЗ")
        with allure.step("Открыть панель заказа"):
            order_taxi.wait_opened_panel()
        with allure.step(f"Навести на i в тарифе «{title}» и получить тексты тултипа"):
            data = order_taxi.tariffs.get_tooltip_for(title)
        assert data["title"] == exp.title
        assert exp.prefix in data["prefix"]
        for part in exp.postfix_parts:
            assert part in data["postfix"]

    @allure.title('Под тарифами отображается блок с информацией')
    def test_form_blocks_below_tariffs(self, taxi_order_page, order_taxi):
        with allure.step("Открыть панель заказа"):
            order_taxi.wait_opened_panel()
        with allure.step("Проверяем, что блок информации под тарифами, все секции присутствуют"):
            assert order_taxi.form.is_form_below_tariffs()
            assert order_taxi.form.sections_present()

    @allure.title('Заказ такси с выбранным параметром Столик для ноутбука')
    def test_worker_taxi_with_laptop_table(self, taxi_order_page, order_taxi):
        with allure.step("Открыть панель заказа"):
            order_taxi.wait_opened_panel()
        with allure.step("Выбрать тариф 'Рабочий'"):
            order_taxi.tariffs.select(Tariff.WORKER)
        with allure.step("Раскрываем выпадашку требований"):
            order_taxi.form.click_requirements_order_taxi()
        with allure.step("Выбираем наличие столика для ноутбука"):
            order_taxi.form.activate_switch_laptop_slider()
        with allure.step("Нажимаем кнопку Заказать"):
            order_taxi.form.click_order_button_taxi()
        with allure.step("Проверяем таймер обратного отсчета в попапе"):
            assert order_taxi.popup.check_counter_time_in_order_taxi_popup()
        with allure.step("Проверяем название заголовка 'Поиск машины'"):
            assert order_taxi.popup.check_header_order_taxi_popup_text() == 'Поиск машины'
        with allure.step("Проверяем наличие кноки 'Детали'"):
            assert order_taxi.popup.check_button_details_in_order_taxi_popup()
            assert order_taxi.popup.details_label_text() == 'Детали'
        with allure.step("Проверяем наличие кнопки 'Отменить'"):
            assert order_taxi.popup.check_button_cancel_in_order_taxi_popup()
            assert order_taxi.popup.cancel_label_text() == 'Отменить'


    @allure.title("После завершения поиска показывается попап заказа (кнопки и номер)")
    def test_order_popup_after_search(self, completed_order_taxi, order_taxi):
        with allure.step("Ждем окончания поиска"):
            order_taxi.completed.wait_until_order_assigned()
        with allure.step("Проверяем элементы попапа"):
            assert order_taxi.completed.check_button_completed_details_in_order_taxi_popup()
            assert order_taxi.completed.check_button_completed_cancel_in_order_taxi_popup()
            assert order_taxi.completed.completed_cancel_label_text()  == "Отменить"
            assert order_taxi.completed.completed_details_label_text() == "Детали"
            assert order_taxi.completed.driver_info_in_order_taxi_popup()            


    @allure.title("Кнопка «Детали»: в блоке «Ещё про поездку» показана та же цена, что и при выборе тарифа")
    def test_order_details_shows_selected_tariff_price(self, taxi_order_page, completed_order_taxi, order_taxi):
        order_taxi.details.click_on_details_in_popup_completed_order()

        assert order_taxi.details.get_extra_price_value() == taxi_order_page

    @pytest.mark.xfail(reason="Кнопка 'Отменить' не закрывает попап", strict=True)
    @allure.title("Отмена заказа такси кнопкой 'Отменить'")
    def test_cancel_order_taxi(self, completed_order_taxi, order_taxi):
        order_taxi.completed.click_cancel_button_in_order_taxi_popup()
        assert order_taxi.popup.check_header_order_taxi_popup() == False
