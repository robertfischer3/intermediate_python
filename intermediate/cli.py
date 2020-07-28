import argparse

parser = argparse.ArgumentParser(
    description="Welcome to Homework 1!\nCommand descriptions.",
    epilog="Robert Fischer, 2020",
)

parser.add_argument("-p", "--policy", action="store", help="Policy command palete")
parser.add_argument("--brokenpipe", action="store", help="Broken pipe is a testing fixture"
)


def main(args=None):
    args = parser.parse_args(args=args)
    print(args.policy)
    print("launched...")
