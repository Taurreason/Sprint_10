class Service:

    def __init__(self, url):
        self._base_url = url.rstrip('/')

    @property
    def main(self):
        return f'{self._base_url}'

site = Service('https://ez-route.stand.praktikum-services.ru/')
