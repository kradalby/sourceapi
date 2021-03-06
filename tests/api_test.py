import json
import unittest

import app as sourceapi

WORKING_SERVER = '216.52.148.47:27015'
NOT_WORKING_SERVER = 'fap.no:1337'


def create_payload(server):
    return dict(
        data=server
    )


class SourceAPITestCase(unittest.TestCase):

    def setUp(self) -> None:
        with sourceapi.app.app_context():
            sourceapi.db.create_all()
        self.app = sourceapi.app.test_client()

    def tearDown(self) -> None:
        pass

    def test_logic(self) -> None:
        self.assertEqual(1, 1)

    # pyre-fixme[15]: `fail` overrides method defined in `TestCase` inconsistently.
    # pyre-fixme[14]: `fail` overrides method defined in `TestCase` inconsistently.
    def fail(self) -> None:
        self.assertEqual(1, 2)

    def test_json_response_for_all_routes_v1_with_working_server(self) -> None:
        routes = (
            '/api/v1/all',
            '/api/v1/serverinfo',
            '/api/v1/playerinfo',
            '/api/v1/ping',
            # '/api/v1/rules',
        )

        payload = create_payload(WORKING_SERVER)

        for route in routes:
            response = self.app.post(
                route,
                data=json.dumps(payload),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(data['status'], 'success')

    def test_json_response_for_all_routes_v1_with_not_working_server(self) -> None:
        routes = (
            '/api/v1/all',
            '/api/v1/serverinfo',
            '/api/v1/playerinfo',
            '/api/v1/ping',
            '/api/v1/rules',
        )

        payload = create_payload(NOT_WORKING_SERVER)

        for route in routes:
            response = self.app.post(
                route,
                data=json.dumps(payload),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(data['status'], 'error')
            self.assertEqual(data['data'], 'The server did not respond')

    def test_json_response_for_all_routes_v1_with_missing_data(self) -> None:
        routes = (
            '/api/v1/all',
            '/api/v1/serverinfo',
            '/api/v1/playerinfo',
            '/api/v1/ping',
            '/api/v1/rules',
        )

        for route in routes:
            response = self.app.post(
                route,
                data=json.dumps({'dat': 'derp'}),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(data['status'], 'error')
            self.assertEqual(data['data'], 'Missing data field')

if __name__ == '__main__':
    unittest.main()
