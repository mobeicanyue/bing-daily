import requests
import os
import time

dpis = ["1080x1920", "1920x1080", "4K"]
locations = [
    "de-DE",  # Germany
    # "en-CA",  # Canada
    # "en-GB",  # United Kingdom
    # "en-IN",  # India
    "en-US",  # United States
    "es-ES",  # Spain
    # "fr-FR",  # France
    # "it-IT",  # Italy
    "ja-JP",  # Japan
    "pt-BR",  # Brazil
    "zh-CN",  # China
]
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
}

def get_mkt_img(location):
    print(f"Getting {location} wallpaper...")
    # Get the image by the location
    url = f"https://bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt={location}"

    response = requests.get(url)
    data = response.json()  # Convert response data to JSON format

    imgs = {
        "message": data["images"][0]["copyright"],  # Message
        # 1080x1920
        "1080x1920": f"https://bing.com{data['images'][0]['urlbase']}_1080x1920.jpg",
        # 1920x1080
        "1920x1080": f"https://bing.com{data['images'][0]['urlbase']}_1920x1080.jpg",
        "4K": f"https://bing.com{data['images'][0]['urlbase']}_UHD.jpg",  # 4K
    }

    return imgs  # Return imgs data


def download_img(imgs, location):
    # Download the image
    for dpi in dpis:
        print(f"Downloading {location}-{dpi} wallpaper...")
        # Get the image url
        img_url = imgs[dpi]
        # Send the request to get the image
        img_response = requests.get(img_url)
        # Save the image
        with open(f"images/{location}-{dpi}.jpg", "wb") as f:
            f.write(img_response.content)
        print(f"Downloaded {dpi} wallpaper to images/{location}-{dpi}.jpg")
        time.sleep(1)
    # write the message to the file
    with open(f"images/{location}-message.txt", "w") as f:
        f.write(imgs["message"])
    time.sleep(1)

def get_img():
    for location in locations:
        imgs = get_mkt_img(location)
        download_img(imgs, location)


if __name__ == "__main__":
    # If the folder does not exist, create it
    os.makedirs("images", exist_ok=True)
    
    # Get the image
    get_img()
