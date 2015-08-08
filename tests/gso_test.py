import unittest

import gso


class GsoTestCase(unittest.TestCase):

    def setUp(self):
        self.app = gso.app.test_client()

    def tearDown(self):
        pass

    def test_logic(self):
        self.assertEqual(1, 1)

    def test_index_render(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
