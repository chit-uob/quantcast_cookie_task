from unittest import TestCase
from unittest.mock import patch
from io import StringIO

import file_reader


class Test(TestCase):
    def test_print_most_active_cookies_only_1(self):
        cookie_hashmap = {'a': 1, 'b': 2, 'c': 1}
        with patch('sys.stdout', new=StringIO()) as fake_out:
            file_reader.print_most_active_cookies(cookie_hashmap)
        self.assertEqual('b\n', fake_out.getvalue())

    def test_print_most_active_cookies_more_than_1(self):
        cookie_hashmap = {'a': 1, 'b': 1, 'c': 1}
        with patch('sys.stdout', new=StringIO()) as fake_out:
            file_reader.print_most_active_cookies(cookie_hashmap)
        self.assertEqual('a\nb\nc\n', fake_out.getvalue())

    def test_handle_file_no_cookie_on_that_day(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            file_reader.handle_file('test.txt', '2022-05-19')
        self.assertEqual("No cookie on '2022-05-19'\n", fake_out.getvalue())


    def test_handle_file_valid_cookie_file(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            file_reader.handle_file('test.txt', '2018-12-09')
        self.assertEqual("AtY0laUfhglK3lC7\n", fake_out.getvalue())

    def test_handle_file_invalid_cookie_file(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            file_reader.handle_file('test_incorrect_format.txt', '2018-12-09')
        self.assertEqual("cookies file is incorrectly formatted\n", fake_out.getvalue())