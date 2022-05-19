#!/usr/bin/env python3

import sys
import file_reader
from arg_parse import parse_argument
import logging
logging.basicConfig(filename='usage.log')

if __name__ == "__main__":
    cookie_path, date_string = parse_argument(sys.argv[1:])
    most_active_cookie_list = file_reader.handle_file(cookie_path, date_string)
    for cookie in most_active_cookie_list:
        print(cookie)