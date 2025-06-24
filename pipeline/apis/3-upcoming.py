#!/usr/bin/env python3
"""Script that prints the upcoming SpaceX launch."""

import requests
from datetime import datetime


def get_upcoming_launch():
    """Fetches and prints the next upcoming SpaceX launch."""
    # URLs for SpaceX API endpoints
    # These URLs are used to fetch upcoming launches, rockets, and launchpads
    # from the SpaceX API.
    launches_url = "https://api.spacexdata.com/v4/launches/upcoming"
    rockets_url = "https://api.spacexdata.com/v4/rockets/"
    launchpads_url = "https://api.spacexdata.com/v4/launchpads/"

    response = requests.get(launches_url)
    if response.status_code != 200:
        print("Error fetching launches")
        return

    data = response.json()
    data.sort(key=lambda x: x.get("date_unix", float("inf")))
    next_launch = data[0]

    launch_name = next_launch.get("name", "N/A")
    date_utc = next_launch.get("date_utc", "")
    local_dt = datetime.strptime(date_utc, "%Y-%m-%dT%H:%M:%S.%fZ")
    local_str = local_dt.isoformat()

    rocket_id = next_launch.get("rocket")
    rocket_name = "N/A"
    if rocket_id:
        rocket_res = requests.get(rockets_url + rocket_id)
        if rocket_res.status_code == 200:
            rocket_name = rocket_res.json().get("name", "N/A")

    launchpad_id = next_launch.get("launchpad")
    launchpad_name = "N/A"
    locality = "N/A"
    if launchpad_id:
        pad_res = requests.get(launchpads_url + launchpad_id)
        if pad_res.status_code == 200:
            pad_data = pad_res.json()
            launchpad_name = pad_data.get("name", "N/A")
            locality = pad_data.get("locality", "N/A")

    print(f"{launch_name} ({local_str}) {rocket_name} - {launchpad_name} ({locality})")

# This script fetches the next upcoming SpaceX launch and prints its details.
if __name__ == '__main__':
    """Main entry point for the script."""
    # Call the function to get and print the upcoming launch details
    get_upcoming_launch()
