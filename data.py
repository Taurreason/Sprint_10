from dataclasses import dataclass, field
from typing import Optional



@dataclass
class RoutingAddress:
    from_field: str
    to_field: str

@dataclass
class InfoPanelRoute:
    price_free: Optional[str] = None
    duration_null: Optional[str] = None

@dataclass
class TariffTaxiOrder:
    tariff_worker: Optional[str] = None
    tariff_sleepy: Optional[str] = None
    tariff_vacation: Optional[str] = None
    tariff_talkative: Optional[str] = None
    tariff_comforting: Optional[str] = None
    tariff_glossy: Optional[str] = None

@dataclass
class TariffTooltip:
    title: str
    prefix: str
    postfix_parts: list[str]

@dataclass
class FormTaxiOrder:
    phone: Optional[str] = None
    payment: Optional[str] = None
    comment: Optional[str] = None


# Тестовая сборка
class TestData:

    ROUTING_ADDRESS = RoutingAddress(
        from_field='Хамовнический Вал, 18',
        to_field='Зубовский бульвар, 37'
    )

    INFO_PANEL_ROUTING = InfoPanelRoute(
        duration_null = 'В пути 0 мин.',
        price_free = 'Авто Бесплатно'
    )

    TARIFF_TAXI_ORDER = TariffTaxiOrder(
        tariff_worker= 'Рабочий',
        tariff_sleepy= 'Сонный',
        tariff_vacation= 'Отпускной',
        tariff_talkative='Разговорчивый',
        tariff_comforting='Утешительный',
        tariff_glossy='Глянцевый'
    )

    # Имена тарифов и их тултипы — «истина» из ТЗ
    TARIFFS: dict[str, TariffTooltip] = {
        "Рабочий": TariffTooltip(
            title="Рабочий",
            prefix="Для деловых особ, которых отвлекают",
            postfix_parts=[
                "нет доступа к асоциальным сетям",
                "Выдвижной столик для ноутбука",
            ],
        ),
        "Сонный": TariffTooltip(
            title="Сонный",
            prefix="Для тех, кто не выспался",
            postfix_parts=[
                "спутник с тремя высшими образованиями",
                "обсудить любую тему",
            ],
        ),
        "Отпускной": TariffTooltip(
            title="Отпускной",
            prefix="Если пришла пора отдохнуть",
            postfix_parts=[
                "массажное кресло",
                "маски для лица и патчи",
            ],
        ),
        "Разговорчивый": TariffTooltip(
            title="Разговорчивый",
            prefix="Если мысли не выходят из головы",
            postfix_parts=[
                "кресло-кровать",
                "плавно, чтобы вы дремали",
            ],
        ),
        "Утешительный": TariffTooltip(
            title="Утешительный",
            prefix="Если хочется свернуться калачиком",
            postfix_parts=[
                "мягкий плед и носовые платки",
                "Персональное ведёрко с мороженым",
            ],
        ),
        "Глянцевый": TariffTooltip(
            title="Глянцевый",
            prefix="Если нужно блистать",
            postfix_parts=[
                "неоновая подсветка",
                "верификацию на инстаграммность",
            ],
        ),
    }
    TARIFF_NAMES: list[str] = list(TARIFFS.keys())

    FORM_TAXI_ORDER = FormTaxiOrder(
        phone= '',
        payment='',
        comment= '123'
    )
