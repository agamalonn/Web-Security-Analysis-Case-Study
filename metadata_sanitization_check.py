from PIL import Image
import urllib.request
import os

def verify_privacy(image_url):
    local_file = "test_asset.jpg"
    try:
        urllib.request.urlretrieve(image_url, local_file)
        with Image.open(local_file) as img:
            exif = img._getexif()
            print("[V] Success: No metadata detected." if not exif else "[X] Warning: Metadata found.")
        os.remove(local_file)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    verify_privacy("https://cdn.target-platform.co.il/assets/sample.jpg")
