import json
import unittest

import app as sourceapi


class GsoTestCase(unittest.TestCase):

    def setUp(self):
        self.app = sourceapi.app.test_client()

    def tearDown(self):
        pass

    def test_logic(self):
        self.assertEqual(1, 1)

    def test_index_render(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_json_response_for_all_routes_v1(self):
        routes = (
            '/api/v1/all/',
            '/api/v1/serverinfo',
            '/api/v1/playerinfo',
            '/api/v1/ping',
            '/api/v1/rules',
        )

        test_server = 'z.fap.no:27015'

        for route in routes:
            response = self.app.post(route, json.dumps([test_server]))
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.content)


if __name__ == '__main__':
    unittest.main()
