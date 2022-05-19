from unittest import TestCase
from unittest.mock import patch
from io import StringIO

import arg_parse


class Test(TestCase):
    def test_validate_date_incorrect_length(self):
        self.assertFalse(arg_parse.validate_date('2022-05-199'))

    def test_validate_date_incorrect_minus_character_placement(self):
        self.assertFalse(arg_parse.validate_date('2022005-19'))

    def test_validate_date_not_numeric(self):
        self.assertFalse(arg_parse.validate_date('2022-xo-19'))

    def test_validate_date_warn_month_greater_than_12(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            arg_parse.validate_date('2022-13-19')
            self.assertEqual(fake_out.getvalue(),
                             "Warning: the month you inputted '13' in '2022-13-19' is greater than 12\n")

    def test_validate_cookie_path_non_existing_path(self):
        self.assertFalse(arg_parse.validate_cookie_path("not_exist.txt"))

    def test_validate_cookie_path_valid_path(self):
        self.assertTrue(arg_parse.validate_cookie_path("test.txt"))

    def test_parse_argument_missing_cookie_path(self):
        with self.assertRaises(SystemExit) as system_exit:
            with patch('sys.stderr', new=StringIO()) as fake_out:
                arg_parse.parse_argument([])
        self.assertEqual(system_exit.exception.code, 2)
        self.assertIn("error: the following arguments are required: cookie_file_path\n", fake_out.getvalue())

    def test_parse_argument_missing_date(self):
        with self.assertRaises(SystemExit) as system_exit:
            with patch('sys.stderr', new=StringIO()) as fake_out:
                arg_parse.parse_argument(['test.txt'])
        self.assertEqual(system_exit.exception.code, 2)
        self.assertIn("please pass the date that you are searching for after -d\n", fake_out.getvalue())

    def test_parse_argument_correct(self):
        path, date = arg_parse.parse_argument(['test.txt', '-d', '2018-12-08'])
        self.assertEqual('test.txt', path)
        self.assertEqual('2018-12-08', date)
