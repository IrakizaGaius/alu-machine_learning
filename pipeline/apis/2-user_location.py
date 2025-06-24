#!/usr/bin/env python3
"""Script that prints the location of a GitHub user."""

import sys
import requests
from datetime import datetime

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
                current_timestamp = int(datetime.utcnow().timestamp())
                minutes_remaining = max((reset_timestamp - current_timestamp) // 60, 0)
                print(f"Reset in {minutes_remaining} min")
            else:
                print("Reset time unknown")
        elif response.status_code == 200:
            data = response.json()
            print(data.get("location", "No location found"))
        else:
            print(f"Unexpected error: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error: {e}")
