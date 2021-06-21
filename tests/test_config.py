from unittest import TestCase
from requests import Session
from betamax  import Betamax
from pathlib  import Path

with Betamax.configure() as config:
    fix_cassette = Path('tests/fixtures/k7')
    fix_cassette.mkdir(parents=True, exist_ok=True)
    config.cassette_library_dir = fix_cassette


class TestBaseConfig(TestCase):
    def setUp(self):
        self.session = Session()

        with Betamax(self.session) as vcr:
            vcr.use_cassette('cats_k7')
            self.response = self.session.get('https://http.cat/')