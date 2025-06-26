#!/usr/bin/env python3
"""
Script that displays number of launches per rocket
"""

import requests


def get_launches_per_rocket():
    """
    Displays the number of launches per rocket
    """
    url = "https://api.spacexdata.com/v4/launches"
    rocket_url = "https://api.spacexdata.com/v4/rockets"
    response = requests.get(url)
    launches = response.json()

    # Count launches per rocket
    launches_per_rocket = {}
    for launch in launches:
        rocket_id = launch["rocket"]
        launches_per_rocket[rocket_id] = launches_per_rocket.get(rocket_id, 0) + 1

    # Get rocket names
    rocket_names = {}
    for rocket_id in launches_per_rocket.keys():
        rocket_response = requests.get(f"{rocket_url}/{rocket_id}")
        rocket_data = rocket_response.json()
        rocket_names[rocket_id] = rocket_data["name"]

    # Format the output
    formatted_output = {
        rocket_names[rocket_id]: count
        for rocket_id, count in launches_per_rocket.items()
    }

    # Sort the output by number of launches (descending)
    sorted_launches_per_rocket = dict(
        sorted(formatted_output.items(), key=lambda item: item[1], reverse=True)
    )

    return sorted_launches_per_rocket


if __name__ == "__main__":
    result = get_launches_per_rocket()
    for rocket, count in result.items():
        print(f"{rocket}: {count}")
