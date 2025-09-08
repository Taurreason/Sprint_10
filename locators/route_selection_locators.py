from selenium.webdriver.common.by import By



class PanelLocators:
    PANEL = (By.CSS_SELECTOR, ".type-picker.shown")

class ModesLocators:
    ACTIVE = (By.CSS_SELECTOR, ".type-picker.shown .modes-container .mode.active")


    @staticmethod
    def BY_ROUTE_TYPE(route_type):
        return (
            By.XPATH,
            "//div[contains(@class,'type-picker') and contains(@class,'shown')]"
            "//div[contains(@class,'modes-container')]"
            f"//div[contains(@class,'mode')][normalize-space()='{route_type}']"
        )
    
class TypesLocators:
    @staticmethod
    def BY_MOVE_TYPE(move_type):
        # move_type: 'car.', 'walk.', 'taxi.', 'bike.', 'scooter.', 'drive.'
        return (
            By.XPATH,
            "//div[contains(@class,'type-picker') and contains(@class,'shown')]"
            "//div[contains(@class,'types-container')]"
            f"//div[contains(@class,'type')][.//img[contains(@class,'type-icon') and contains(@src,'/{move_type}')]]"
        )

    def BY_MOVE_TYPE_ACTIVE(move_type):
        return (
            By.XPATH,
            # 1) родитель .type имеет класс active
            # 2) иконка содержит /{move_type}-active  (игнорируем хэш в конце)
            "//div[contains(@class,'type-picker') and contains(@class,'shown')]"
            "//div[contains(@class,'types-container')]"
            "//div[contains(@class,'type') and contains(@class,'active')]"
            f"[.//img[contains(@class,'type-icon') and contains(@src,'/{move_type}-active')]]"
        )

class InfoLocators:
    PRICE    = (By.XPATH, "//div[contains(@class,'results-text')]/div[contains(@class,'text')]")
    DURATION = (By.XPATH, "//div[contains(@class,'results-text')]/div[contains(@class,'duration')]")

# проверить 
class TaxiLocators:
    CALL_TAXI = (
        By.XPATH,
        "//div[contains(@class,'type-picker') and contains(@class,'shown')]"
        "//button[contains(@class,'button') and contains(@class,'round') and normalize-space()='Вызвать такси']"
    )

# проверить
class DriveLocators:
    BOOK_BUTTON = (By.XPATH, "//button[@type='button' and contains(@class,'button') and contains(@class,'round') and normalize-space()='Забронировать']")
