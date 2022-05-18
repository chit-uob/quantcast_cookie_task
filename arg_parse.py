import argparse


def parse_argument():
    arguments_parser = argparse.ArgumentParser(description="return the most active cookie for specified day")
    arguments_parser.add_argument("cookie_file_path", help="the file path of the cookie file")
    arguments_parser.add_argument("-d", metavar="date", help="the date you are searching for")
    arguments = arguments_parser.parse_args()

    # If not date passed in
    if not arguments.d:
        print("please pass the date that you are searching for after -d")
        arguments_parser.print_usage()

    return arguments.cookie_file_path, arguments.d
