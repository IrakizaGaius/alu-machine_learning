#!/usr/bin/env python3
"""Script that prints the location of a GitHub user."""

import sys
import requests
from datetime import datetime, timezone

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <GitHub API User URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        if response.status_code == 404:
            print("Not found")
        elif response.status_code == 403:
            reset_time = response.headers.get("X-RateLimit-Reset")
            if reset_time:
                reset_timestamp = int(reset_time)
                current_timestamp = int(datetime.now(timezone.utc).timestamp())
                min_rem = max((reset_timestamp - current_timestamp) // 60, 0)
                print("Reset in {} min".format(min_rem))
            else:
                print("Reset time unknown")
        elif response.status_code == 200:
            data = response.json()
            print(data.get("location", "No location found"))
        else:
            print("Unexpected error: {}".format(response.status_code))
    except requests.RequestException as e:
        print("Error: {}".format(e))
