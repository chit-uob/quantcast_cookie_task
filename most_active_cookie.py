import sys
import getopt


def parse_argument(argv):
    arg_dest = ""

    arg_help = "{0} -d <destination>".format(argv[0])

    try:
        opts, args = getopt.getopt(argv[1:], "hd:", ["help", "destination="])
    except:
        print(arg_help)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(2)
        elif opt in ("-d", "--output"):
            arg_dest = arg

    print('dest:', arg_dest)

if __name__ == "__main__":
    parse_argument(sys.argv)
