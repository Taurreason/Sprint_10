from selenium.webdriver.common.by import By


class MainPageLocators:

    MAP_EVENTS_PANE = By.CSS_SELECTOR, "ymaps[class*='ymaps-2-1-'][class*='events-pane']"

    FROM_INPUT_FIELD  = By.CSS_SELECTOR, "div.input-container > input#from.input"
    FROM_CLEAR_BUTTON = By.XPATH, "//input[@id='from']/following-sibling::button[contains(@class,'input-close-button')]"

    TO_INPUT_FIELD = By.CSS_SELECTOR, "label.label[for='to']"
    TO_CLEAR_BUTTON = By.CSS_SELECTOR, "div.input-container > button.input-close-button"

    # контейнер инпута "Откуда" в состоянии ошибки (красный)
    FROM_CONTAINER_ERROR = (
        By.XPATH,
        "//div[contains(@class,'input-container') and contains(@class,'error')][.//input[@id='from']]"
    )

    # сам инпут "Откуда" когда контейнер в ошибке
    FROM_INPUT_ERROR = (
        By.XPATH,
        "//input[@id='from' and ancestor::div[contains(@class,'input-container') and contains(@class,'error')]]"
    )

    # текст ошибки под полем "Откуда"
    FROM_ERROR_TEXT = (
        By.XPATH,
        "//input[@id='from']/parent::div/following-sibling::div[@class='error' and normalize-space()='Введите адрес']"
    )

    # маркер слева от строки "Откуда" (проверка красного цвета через CSS)
    FROM_ROW_MARKER = (
        By.XPATH,
        "//input[@id='from']/ancestor::div[contains(@class,'dst-picker-row')]//div[contains(@class,'dst-picker-marker')]"
    )

    TO_CONTAINER_ERROR = (
        By.XPATH,
        "//div[contains(@class,'input-container') and contains(@class,'error')][.//input[@id='to']]"
    )

    TO_INPUT_ERROR = (
        By.XPATH,
        "//input[@id='to' and ancestor::div[contains(@class,'input-container') and contains(@class,'error')]]"
    )

    TO_ERROR_TEXT = (
        By.XPATH,
        "//input[@id='to']/parent::div/following-sibling::div[@class='error' and normalize-space()='Введите адрес']"
    )

    TO_ROW_MARKER = (
        By.XPATH,
        "//input[@id='to']/ancestor::div[contains(@class,'dst-picker-row')]//div[contains(@class,'dst-picker-marker')]"
    )

    ROUTE_PIN_A = (By.XPATH, "//ymaps[contains(@class,'route-pin__label-a')]")
    ROUTE_PIN_B = (By.XPATH, "//ymaps[contains(@class,'route-pin__label-b')]")
