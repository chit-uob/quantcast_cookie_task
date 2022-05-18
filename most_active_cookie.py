import file_reader
from arg_parse import parse_argument

if __name__ == "__main__":
    cookie_path, date_string = parse_argument()
    file_reader.handle_file(cookie_path, date_string)