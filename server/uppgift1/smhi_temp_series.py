#!/usr/bin/env python3
"""
Functions to get temparature readings from smhi api
"""
import requests


def fetch_temp_data(url):
    """
    Fetch temparature timeseries from smhi

    url -> dict
    """
    res = requests.get(url)
    return res.json()


def temp_series(smhi_data):
    """
    Transform smhi-data to something easier to consume
    with matplotlib

    returns {station: String, temp: [], from: Int, to: Int}
    """
    consumable_data = {
        "station": smhi_data["station"]["name"],
        "temp": [],
        "from": smhi_data["value"][0]["date"],
        "to": smhi_data["value"][-1]["date"]
    }
    for temp_post in smhi_data["value"]:
        consumable_data["temp"].append(float(temp_post["value"]))
    return consumable_data


if __name__ == "__main__":

    def test():
        """
        Test stuff if run as program
        """
        temp_data = fetch_temp_data(
            ("https://opendata-download-metobs.smhi.se/api/version/" +
             "latest/parameter/1/station/52350/period/latest-day/data.json"))
        data = temp_series(temp_data)
        print(data)

    test()
