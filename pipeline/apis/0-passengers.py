#!/usr/bin/env python3
"""Method that returns a list of ships with a given number of passengers."""

import requests

def availableShips(passengerCount):
    """
    Returns a list of ships that can carry the given number of passengers.
    """
    url = "https://swapi-api.alx-tools.com/api/starships/"
    matching_ships = []

    while url:
        response = requests.get(url)
        if response.status_code != 200:
            break

        data = response.json()
        for ship in data.get("results", []):
            passengers = ship.get("passengers", "0").replace(",", "").split(" ")[0]
            try:
                if passengers.isdigit() and int(passengers) >= passengerCount:
                    matching_ships.append(ship["name"])
            except ValueError:
                continue

        url = data.get("next")  # continue to next page

    return matching_ships
