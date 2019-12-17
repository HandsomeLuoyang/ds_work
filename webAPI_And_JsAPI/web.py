import requests
import json


def get_shortest_panel():
    # 1.Get the api url.
    api_url = "https://restapi.amap.com/v3/direction/driving"
    # 2.Set the params.
    params = {
        "key": "c51a51f65222b18a82f6e0e9e6e60c2d",
        "destination": "106.550464,29.563761",
        "strategy": "2",
        "output": "JSON",
        "extensions": "base",
    }
    # 3.Set the positions.
    origin_list = [
        "106.738211,29.840777",
        "106.351097,29.75598",
        "106.711726,29.498983",
        "106.288054,29.536045",
        "106.444183,29.53087",
        "106.586582,29.352452",
        "106.478209,29.481837",
        "106.456811,29.258333",
    ]
    # 4.Get distance of positions.
    distance_dict = {}
    for i in origin_list:
        params["origin"] = i  # Pass in different origin position.
        rtn = requests.get(api_url, params=params)
        # Transform the json to the dict of python
        result = json.loads(rtn.content)
        distance = result["route"]["paths"][0]["distance"]  # Get the distance.
        distance_dict[i] = int(distance)
    # 5.Select the shortest panel.
    # Sort the dict bu value.
    distance_dict = sorted(distance_dict.items(), key=lambda kv: (kv[1], kv[0]))
    # print(distance_dict[0][0].split(","))
    return distance_dict[0][0].split(",")
    # 6.Give the panel to JS.


if __name__ == "__main__":
    get_shortest_panel()
