from unittest import TestCase
from requests import Session
from betamax  import Betamax
from bs4      import BeautifulSoup
from pathlib  import Path

with Betamax.configure() as config:
    fix_cassette = Path('tests/fixtures/cassetes')
    fix_cassette.mkdir(parents=True, exist_ok=True)
    config.cassette_library_dir = fix_cassette


class TestCats(TestCase):
    def setUp(self):
        self.session = Session()

    def test_must_returns_heroes(self):
        with Betamax(self.session) as vcr:
            vcr.use_cassette('cats_cassette')
            response = self.session.get('https://http.cat/')

            html = BeautifulSoup(response.text, 'html.parser')

            cats = html.select('.ThumbnailGrid_thumbnail__177T1')
            names = {x.select_one('.Thumbnail_title__2iqYK').text: x.p.text for x in cats}
            # print(names)

            self.assertEqual(len(cats), 62)
            self.assertIn('Failed Dependency', names.values())
            self.assertIn('404', names)
            self.assertNotIn('Genji', names)
            self.assertIn('Not Found', names.values())
