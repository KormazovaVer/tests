import unittest
import ya_api


class TestYaApi(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def tearDown(self):
        # Удаляем папку после прохождения теста на создание папки
        ya_api.delete_folder('test1')
        ya_api.delete_folder('test2')
        print('method tearDown')

    def test_create_folder(self):
        self.assertEqual(ya_api.create_folder('test1'), 201)

    def test_passed_create_folder(self):
        self.assertEqual(ya_api.create_folder('test2'), 409)




if __name__ == '__main__':
    unittest.main()