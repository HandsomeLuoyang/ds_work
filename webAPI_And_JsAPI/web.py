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
        "110.550464,30.563761",
        "106.550464,27.563761",
        "104.550464,26.563761",
        "106.550464,31.563761",
        "108.550464,29.563761",
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
