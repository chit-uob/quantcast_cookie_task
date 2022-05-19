from unittest import TestCase
from unittest.mock import patch
from io import StringIO

import file_reader


class Test(TestCase):
    def test_return_most_active_cookies_only_1(self):
        cookie_hashmap = {'a': 1, 'b': 2, 'c': 1}
        cookie_list = file_reader.find_most_active_cookies(cookie_hashmap)
        self.assertEqual(['b'], cookie_list)

    def test_return_most_active_cookies_more_than_1(self):
        cookie_hashmap = {'a': 1, 'b': 1, 'c': 1}
        cookie_list = file_reader.find_most_active_cookies(cookie_hashmap)
        self.assertEqual(['a', 'b', 'c'], cookie_list)

    def test_handle_file_no_cookie_on_that_day(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            file_reader.handle_file('test.csv', '2022-05-19')
        self.assertEqual("No cookie on '2022-05-19'\n", fake_out.getvalue())


    def test_handle_file_valid_cookie_file(self):
        cookie_list = file_reader.handle_file('test.csv', '2018-12-09')
        self.assertEqual(["AtY0laUfhglK3lC7"], cookie_list)

    def test_handle_file_invalid_cookie_file(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            file_reader.handle_file('test_incorrect_format.csv', '2018-12-09')
        self.assertEqual("cookies file is incorrectly formatted\n", fake_out.getvalue())