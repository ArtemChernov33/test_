import unittest
from main import get_doc_owner_name, add_new_doc, delete_doc
import main

class TestFunc(unittest.TestCase):
    def setUp(self) -> None:
        print('Setup')

    def tearDown(self) -> None:
        print('Teardown')

    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name('11-2'),"Геннадий Покемонов")

    def test_add_new_doc(self):
        self.assertEqual(main.add_new_doc("pass", "1212", "Jorg", "2"), "2")

    def test_delete_doc(self):
        self.assertTrue(delete_doc("2207 876234"))

    