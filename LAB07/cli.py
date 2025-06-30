# cli.py
import argparse
from myproject import say_hello, get_formatted_timestamp

def main():
    parser = argparse.ArgumentParser(description="MyProject CLI")
    parser.add_argument("name", help="Your name")
    args = parser.parse_args()

    print(say_hello(args.name))
    print("Time:", get_formatted_timestamp())

if __name__ == "__main__":
    main()
