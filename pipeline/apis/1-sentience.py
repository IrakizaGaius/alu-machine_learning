#!/usr/bin/env python3
"""Fetches a list of planets that are homeworlds to sentient species."""

import requests


def sentientPlanets():
    """Returns a list of planets that are homeworlds to sentient species.
    """
    url = "https://swapi-api.alx-tools.com/api/species/"
    sentient_homeworlds = set()

    while url:
        response = requests.get(url)
        if response.status_code != 200:
            break

        data = response.json()
        for species in data.get("results", []):
            if species.get("designation", "").lower() == "sentient":
                homeworld_url = species.get("homeworld")
                if homeworld_url:
                    # Get the planet's name from its URL
                    planet_response = requests.get(homeworld_url)
                    if planet_response.status_code == 200:
                        planet_data = planet_response.json()
                        sentient_homeworlds.add(planet_data.get("name"))

        url = data.get("next")  # move to next page

    return list(sentient_homeworlds)
