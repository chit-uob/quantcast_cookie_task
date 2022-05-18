import getopt
import sys


def parse_argument(argv):
    destination_argument = ""
    help_message = "Correct usage:\n{0} -d <destination>".format(argv[0])

    try:
        opts, args = getopt.getopt(argv[1:], "hd:", ["help", "destination="])
    except:
        print(help_message)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(help_message)  # print the help message
            sys.exit(2)
        elif opt in ("-d", "-dest"):
            destination_argument = arg

    print('dest:', destination_argument)