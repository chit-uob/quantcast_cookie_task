import argparse


def validate(cookie_file_path, date):
    validate_cookie_path(cookie_file_path)
    validate_date(date)


def validate_cookie_path(cookie_file_path):
    try:
        with open(cookie_file_path, "r") as f:
            pass
    except FileNotFoundError:
        print(f"The file path '{cookie_file_path}' is incorrect")
        exit(-1)
    except OSError:
        print(f"The file path '{cookie_file_path}' cannot be read")
        exit(-1)


def validate_date(date):
    if not len(date) == 10 or \
            not date[4] == "-" or not date[7] == "-":
        print(f"Incorrect date format '{date}', it should be in yyyy-mm-dd such as 2022-05-18")
        exit(-1)

    year_str = date[0:4]
    month_str = date[5:7]
    day_str = date[8:10]

    if not year_str.isnumeric() or not month_str.isnumeric() or not day_str.isnumeric():
        print(f"Incorrect date format '{date}', it should be in yyyy-mm-dd such as 2022-05-18")
        exit(-1)

    if int(month_str) > 12:
        print(f"Warning: the month you inputted '{month_str}' in '{date}' is greater than 12")


def parse_argument():
    arguments_parser = argparse.ArgumentParser(description="return the most active cookie for specified day")
    arguments_parser.add_argument("cookie_file_path", help="the file path of the cookie file")
    arguments_parser.add_argument("-d", metavar="date:yyyy-mm-dd", help="the date you are searching for")
    arguments = arguments_parser.parse_args()

    # If not date passed in
    if not arguments.d:
        print("please pass the date that you are searching for after -d")
        arguments_parser.print_usage()
        exit(2)

    validate(arguments.cookie_file_path, arguments.d)

    return arguments.cookie_file_path, arguments.d
