import unittest

import YD

class TestYD(unittest.TestCase):

    def setUp(self) -> None:
        print('Setup')

    def tearDown(self) -> None:
        print('Teardown')

    def test_status_code(self):
        self.assertEqual(YD.create_folder('qwqz'), 201)
