from functools import wraps
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By



from data import *


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 40
        self.wait = WebDriverWait(self.driver, self.timeout)

    @staticmethod
    def wait_for_element_visibility(func):
        @wraps(func)
        def wrapper(self, locator):
            self.wait.until(EC.visibility_of_element_located(locator))
            return func(self, locator)

        return wrapper
    
    @staticmethod
    def wait_for_element_presence(func):
        @wraps(func)
        def wrapper(self, locator):
            self.wait.until(EC.presence_of_element_located(locator))
            return func(self, locator)

        return wrapper
    
    @staticmethod
    def wait_for_elements_presence(func):
        @wraps(func)
        def wrapper(self, locator, *args, **kwargs):
            self.wait.until(EC.presence_of_all_elements_located(locator))
            return func(self, locator, *args, **kwargs)
        return wrapper
    
    @staticmethod
    def wait_for_element_clickability(func):
        @wraps(func)
        def wrapper(self, locator):
            self.wait.until(EC.element_to_be_clickable(locator))
            return func(self, locator)

        return wrapper

    @staticmethod
    def wait_for_element_invisibility(func):
        @wraps(func)
        def wrapper(self, locator):
            self.wait.until(EC.invisibility_of_element_located(locator))
            return func(self, locator)

        return wrapper
    
    @wait_for_elements_presence
    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def wait_open_url(self, url):
        return self.wait.until(EC.url_to_be(url))

    def open_url(self, url) -> bool:
        self.driver.get(url)
        return self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
    
    @wait_for_element_visibility
    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_in(self, root_webelement, locator, timeout=None):
        by, sel = locator
        wait = WebDriverWait(root_webelement, timeout or self.timeout)
        return wait.until(lambda r: r.find_element(by, sel))

    @wait_for_element_clickability
    def click(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @wait_for_element_clickability
    def alt_click(self, locator):
        self.find(locator).click()

    def find_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)

    def scroll_to_end(self, container_locator):
        el = self.find(container_locator)
        self.driver.execute_script(
            "arguments[0].scrollLeft = arguments[0].scrollWidth;", el
        )
    
    def _is_displayed(self, locator):
        return self.find(locator).is_displayed()
    
    def is_enabled(self, locator_or_element):
        """Простая проверка активности элемента."""
        el: WebElement = (
            self.find(locator_or_element) if isinstance(locator_or_element, tuple)
            else locator_or_element
        )
        # базовая selenium-проверка
        if not el.is_enabled():
            return False
        # если есть атрибут disabled — считаем неактивным
        if el.get_attribute("disabled") is not None:
            return False
        # если в class присутствует 'disabled' — считаем неактивным
        classes = (el.get_attribute("class") or "").lower()
        if "disabled" in classes:
            return False
        return True
    
    def hover(self, element=None, locator=None):
        # Навести курсор на элемент (можно передать сам элемент или локатор)
        if locator is not None:
            element = self.find(locator)
        self.scroll_into_view(element)
        ActionChains(self.driver).move_to_element(element).perform()
        return element

    def get_attr(self, element, name: str):
        return element.get_attribute(name)

    def visible_tooltip_by_id(self, tip_id: str):
        """Надёжно найти ReactTooltip по id, дождаться видимости."""
        locator = (By.CSS_SELECTOR, f'#{tip_id}.__react_component_tooltip, [id="{tip_id}"].__react_component_tooltip')
        return self.find(locator)
