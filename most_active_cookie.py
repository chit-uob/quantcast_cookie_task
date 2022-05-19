#!/usr/bin/env python3

import sys
import file_reader
from arg_parse import parse_argument
import logging
logging.basicConfig(filename='usage.log', filemode="a", level=logging.INFO)

if __name__ == "__main__":
    cookie_path, date_string = parse_argument(sys.argv[1:])
    logging.info(f"Called with arguments {sys.argv[1:]}")
    most_active_cookie_list = file_reader.handle_file(cookie_path, date_string)
    logging.info(f"Results are:\n")
    for cookie in most_active_cookie_list:
        print(cookie)
        logging.info(cookie)