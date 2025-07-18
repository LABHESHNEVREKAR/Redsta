import requests

def download_image(image_url, filename="downloaded.jpg"):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"✅ Image saved as {filename}")
    else:
        print("❌ Failed to download image")
