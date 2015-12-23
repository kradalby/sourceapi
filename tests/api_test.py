import json
import unittest

import app as sourceapi


class SourceAPITestCase(unittest.TestCase):

    def setUp(self):
        self.app = sourceapi.app.test_client()

    def tearDown(self):
        pass

    def test_logic(self):
        self.assertEqual(1, 1)

    def fail(self):
        self.assertEqual(1,2)


if __name__ == '__main__':
    unittest.main()
