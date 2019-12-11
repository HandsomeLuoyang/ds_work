import requests
import json
from PIL import Image
from io import BytesIO


def main():
    url = "https://restapi.amap.com/v3/staticmap"
    paras = {"key": "c51a51f65222b18a82f6e0e9e6e60c2d", "zoom": "9", "traffic": "1", "location": "106.550464,29.563761",
             "scale": "2", "size": "1080*960", "labels": "车祸发生点,2,0,16,0x000000,0xFBB612:106.550464,29.563761"}
    r = requests.get(url, params=paras)

    f = open("test.png", "wb")
    f.write(r.content)
    f.close()


if __name__ == "__main__":
    main()
