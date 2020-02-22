import unittest
from featuredimg.core import crete_featured_img


class FeaturedImgTest(unittest.TestCase):
    def test_featured_img(self):
        self.assertIsNone(crete_featured_img('./test.jpg', 'test'))
