import unittest
from featuredimg.core import featured_img


class FeaturedImgTest(unittest.TestCase):
    def test_featured_img(self):
        self.assertIsNone(featured_img())
