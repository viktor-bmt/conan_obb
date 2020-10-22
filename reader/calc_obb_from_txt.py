from Reader import Reader
import argparse
import os

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, help="specify input file", required=True)
    args = parser.parse_args()
    path = os.path.abspath(args.input)

    r = Reader(path)
    r.print_obb_params()