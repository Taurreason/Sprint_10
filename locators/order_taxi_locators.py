from selenium.webdriver.common.by import By


class TariffTaxiLocators:
    @staticmethod
    def CARD_TARIFF(name: str):
        # Карточка тарифа с названием в заголовке или в alt иконки
        return (
            f"//div[contains(@class,'tcard')]"
            f"[.//div[contains(@class,'tcard-title') and normalize-space()='{name}']"
            f" or .//img[@alt='{name}']]"
        )

    @staticmethod
    def CARD(name: str):
        # Вся карточка
        return (By.XPATH, TariffTaxiLocators.CARD_TARIFF(name))

    # кликаем по кнопке внутри карточки с нужным заголовком
    @staticmethod
    def CARD_BY_TITLE(title: str):
        return (
            By.XPATH,
            f'//div[contains(@class,"tcard")][.//div[contains(@class,"tcard-title") and normalize-space()="{title}"]]//button[contains(@class,"tcard-i")]'
        )

    @staticmethod
    def CARD_ACTIVE_BY_TITLE(title: str):
        return (
            By.XPATH,
            f'//div[contains(@class,"tcard") and contains(@class,"active")]'
            f'[.//div[contains(@class,"tcard-title") and normalize-space()="{title}"]]'
        )    

    @staticmethod
    def CARD_CONTAINER_BY_TITLE(title: str):
        return (By.XPATH,
            f'//div[contains(@class,"tcard")][.//div[contains(@class,"tcard-title") and normalize-space()="{title}"]]')

    @staticmethod
    def INFO_BTN_IN_CARD(title: str):
        return (By.XPATH,
            f'{TariffTaxiLocators.CARD_CONTAINER_BY_TITLE(title)[1]}//button[contains(@class,"tcard-i")]')

    @staticmethod
    def TOOLTIP_BY_ID(tt_id: str):
        return (By.CSS_SELECTOR, f'#{tt_id}.__react_component_tooltip, [id="{tt_id}"].__react_component_tooltip')

    ALL_TITLES    = (By.CSS_SELECTOR, ".tcard .tcard-title")
    ACTIVE_TITLE  = (By.CSS_SELECTOR, ".tcard.active .tcard-title")
    CONTAINER     = (By.CSS_SELECTOR, '.tariff-cards')

    # внутренности тултипа
    TOOLTIP_TITLE   = (By.CSS_SELECTOR, '.i-floating .i-title')
    TOOLTIP_PREFIX  = (By.CSS_SELECTOR, '.i-floating .i-dPrefix')
    TOOLTIP_POSTFIX = (By.CSS_SELECTOR, '.i-floating .i-dPostfix')

    TARIFF_PICKER = (By.CSS_SELECTOR, ".tariff-picker.shown")
    TARIFF_CARDS  = (By.CSS_SELECTOR, ".tariff-cards")


class TaxiOrderPanelLocator:
    PANEL = (By.CSS_SELECTOR, ".tariff-picker.shown")

class FormLocators: 

    FORM              = (By.CSS_SELECTOR, '.form')
    BUTTON_ORDER_TAXI = (By.CSS_SELECTOR, 'button.smart-button')

    # --- Блок "Телефон" ---
    PHONE_BUTTON      = (By.CSS_SELECTOR, '.form .np-button')                 # кликабельная область

    # --- Блок "Способ оплаты" ---
    PAYMENT_BUTTON    = (By.CSS_SELECTOR, '.form .pp-button')                 # кликабельная область

    # --- Комментарий водителю ---
    COMMENT_INPUT     = (By.CSS_SELECTOR, '.form .input-container #comment.input')

    # --- Требования к заказу: шапка/контейнер ---
    REQS_CONTAINER  = (By.CSS_SELECTOR, '.form .reqs')
    # REQS_HEADER       = (By.CSS_SELECTOR, '.form .reqs .reqs-header')
    REQS_OPEN       = (By.CSS_SELECTOR, '.form .reqs.open')
    REQS_ARROW      = (By.CSS_SELECTOR, '.form .reqs .reqs-header .reqs-arrow')

    SWITCH_LAPTOP_SLIDER = (
    By.XPATH,
    '//div[contains(@class,"r-sw-label") and normalize-space()="Столик для ноутбука"]'
    '/ancestor::div[contains(@class,"r-sw-container")]'
    '//span[contains(@class,"slider")]'
    )


# class RequirementsLocators:
#     # шапка блока
#     PANEL_TOGGLE = (By.XPATH, "//*[contains(@class,'type') and contains(@class,'picker')]"
#                                "//*[contains(@class,'requirements') or .//text()[contains(.,'Требования к заказу')]]"
#                                " | //*[contains(@class,'requirements') and .//text()[contains(.,'Требования к заказу')]]")

#     # контейнер раскрытого блока (fallback по тексту/классам)
#     PANEL_BODY = (By.XPATH, "//*[contains(@class,'requirements') and not(contains(@class,'hidden'))]"
#                             " | //*[.//text()[contains(.,'Требования к заказу')]]/ancestor::*[contains(@class,'picker')][1]")

    # --- Элементы по названию пункта (работают для любого тарифа) ---

    # переключатель (toggle) по подписи
    # @staticmethod
    # def TOGGLE_BY_LABEL(label: str):
    #     return (By.XPATH, f"//*[normalize-space()='{label}']"
    #                       f"/following::*[self::button or self::*[name()='button'] or self::div or self::span]"
    #                       f"[contains(@class,'switch') or contains(@class,'toggle') or @role='switch'][1]")

    # # минус, значение и плюс у счётчика по подписи (например «Пломбир»)
    # @staticmethod
    # def COUNTER_MINUS(label: str):
    #     return (By.XPATH, f"//*[normalize-space()='{label}']"
    #                       f"/following::*[self::button or self::span][normalize-space()='−' or normalize-space()='-'][1]")

    # @staticmethod
    # def COUNTER_PLUS(label: str):
    #     return (By.XPATH, f"//*[normalize-space()='{label}']"
    #                       f"/following::*[self::button or self::span][normalize-space()='+'][1]")

    # @staticmethod
    # def COUNTER_VALUE(label: str):
    #     return (By.XPATH, f"//*[normalize-space()='{label}']"
    #                       f"/following::*[self::span or self::div or self::input][contains(@class,'value') or @role='spinbutton' or number(.)=number(.)][1]")
    


class OrderHeaderLocators:
    HEADER        = (By.CSS_SELECTOR, ".order-header-content")
    TITLE         = (By.XPATH, "//div[contains(@class,'order-header-title') and normalize-space()='Поиск машины']")
    TIME          = (By.CSS_SELECTOR, ".order-header-content .order-header-time")

    # Группа "Отменить": кнопка + подпись
    CANCEL_BUTTON    = (By.XPATH, "//div[contains(@class,'order-btn-group')][.//img[@alt='close']]//button")

    CANCEL_LABEL     = (By.XPATH, "//div[contains(@class,'order-btn-group')][.//img[@alt='close']]//div[last()]")

    # Группа "Детали": кнопка + подпись
    DETAILS_BUTTON   = (By.XPATH, "//div[contains(@class,'order-btn-group')][.//img[@alt='burger']]//button")
    DETAILS_LABEL    = (By.XPATH, "//div[contains(@class,'order-btn-group')][.//img[@alt='burger']]//div[last()]")


class CompletedOrderLocators:

    ORDER_NUMBER       = (By.CSS_SELECTOR, ".order-header-content .order-number .number")

    DRIVER_BUTTON   = (By.XPATH, "//div[@class='order-btn-group'][.//div[contains(@class,'order-btn-rating')]]//div[contains(@class,'order-button')]")
    DRIVER_NAME     = (By.XPATH,  "//div[@class='order-btn-group'][.//div[contains(@class,'order-btn-rating')]]/div[normalize-space()]")

    CANCEL_BUTTON   = (By.XPATH, "//div[@class='order-btn-group'][.//img[@alt='close'] and .//div[normalize-space()='Отменить']]//button")
    CANCEL_LABEL    = (By.XPATH, "//div[@class='order-btn-group'][.//img[@alt='close'] and .//div[normalize-space()='Отменить']]/div[normalize-space()='Отменить']")

    DETAILS_BUTTON  = (By.XPATH, "//div[@class='order-btn-group'][.//img[@alt='burger'] and .//div[normalize-space()='Детали']]//button")
    DETAILS_LABEL   = (By.XPATH, "//div[@class='order-btn-group'][.//img[@alt='burger'] and .//div[normalize-space()='Детали']]/div[normalize-space()='Детали']")

class OrderDetailsLocators:

    EXTRA_PRICE_TEXT = (
        By.XPATH,
        "//div[contains(@class,'order-details-row')]"
        "[.//div[contains(@class,'o-d-h') and normalize-space()='Еще про поездку']]"
        "//div[contains(@class,'o-d-sh')]"
    )
