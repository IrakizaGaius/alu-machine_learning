#!/usr/bin/env python3
"""Script that prints the upcoming launch in the correct format."""

import requests
from datetime import datetime, timezone

if __name__ == '__main__':
    """Fetches the next SpaceX launch and
    prints its details in a specific format."""
    launches_url = "https://api.spacexdata.com/v4/launches/upcoming"
    rockets_url = "https://api.spacexdata.com/v4/rockets/"
    launchpads_url = "https://api.spacexdata.com/v4/launchpads/"

    try:
        response = requests.get(launches_url)
        if response.status_code == 404:
            print("Not found")
        elif response.status_code == 403:
            print("Access forbidden")
        elif response.status_code == 200:
            data = response.json()

            # Sort by date_unix
            data.sort(key=lambda x: x.get("date_unix", float('inf')))
            next_launch = data[0]

            # Get launch details
            launch_name = next_launch.get("name", "N/A")
            d_utc = next_launch.get("date_utc", "")
            # Formatted Date
            f_date = (
                datetime.strptime(d_utc, "%Y-%m-%dT%H:%M:%S.%fZ")
                .strftime("%Y-%m-%d %H:%M:%S")
            )
            # Get rocket name
            rocket_id = next_launch.get("rocket")
            rocket_name = "N/A"
            if rocket_id:
                rocket_res = requests.get(rockets_url + rocket_id)
                if rocket_res.status_code == 200:
                    rocket_name = rocket_res.json().get("name", "N/A")

            # Get launchpad name and locality
            launchpad_id = next_launch.get("launchpad")
            launchpad_name = "N/A"
            locality = "N/A"
            if launchpad_id:
                pad_res = requests.get(launchpads_url + launchpad_id)
                if pad_res.status_code == 200:
                    pad_data = pad_res.json()
                    launchpad_name = pad_data.get("name", "N/A")
                    locality = pad_data.get("locality", "N/A")

            print(
                f"{launch_name} ({f_date}) {rocket_name} - "
                f"{launchpad_name} ({locality})"
            )

        else:
            print("Unexpected error: {}".format(response.status_code))
    except requests.RequestException as e:
        print("Error: {}".format(e))
