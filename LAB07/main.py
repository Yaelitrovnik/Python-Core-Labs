# main.py

from myproject import say_hello, get_timestamp
import requests

def main():
    # Use package functions
    print(say_hello("Yael"))
    print(f"Current time: {get_timestamp()}")

    # Make an HTTP request using 'requests'
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        print("GitHub API status:", response.status_code)
        print("API headers:", response.headers['content-type'])
    else:
        print("Request failed with status:", response.status_code)

if __name__ == "__main__":
    main()
