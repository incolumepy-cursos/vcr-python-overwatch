from .test_config import TestBaseConfig
from bs4      import BeautifulSoup



class TestCats(TestBaseConfig):
    def test_must_returns_heroes(self):

            html = BeautifulSoup(self.response.text, 'html.parser')

            cats = html.select('.ThumbnailGrid_thumbnail__177T1')
            names = {x.select_one('.Thumbnail_title__2iqYK').text: x.p.text for x in cats}
            # print(names)

            self.assertEqual(len(cats), 62)
            self.assertIn('Failed Dependency', names.values())
            self.assertIn('404', names)
            self.assertNotIn('Genji', names)
            self.assertIn('Not Found', names.values())
