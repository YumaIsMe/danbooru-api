import unittest
from danbooru.danbooru import Danbooru

class TestDanbooru(unittest.TestCase):
    def setUp(self):
        self.api = Danbooru()  

    def test_search_posts(self):
        posts = self.api.search_posts(tags='cute', limit=1)
        self.assertIsInstance(posts, list)
        self.assertGreater(len(posts), 0)

    def test_get_post(self):
        post_id = 1 
        post = self.api.get_post(post_id)
        self.assertIsInstance(post, dict)
        self.assertIn('id', post)

    def test_get_tags(self):
        tags = self.api.get_tags(tag_name='cute', limit=1)
        self.assertIsInstance(tags, list)
        self.assertGreater(len(tags), 0)

if __name__ == '__main__':
    unittest.main()
