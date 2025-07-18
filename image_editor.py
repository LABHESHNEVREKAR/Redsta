from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

def add_watermark(image_url, author, subreddit):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    draw = ImageDraw.Draw(img)
    text = f"📸 u/{author} | r/{subreddit}"
    font = ImageFont.truetype("arial.ttf", 32)
    draw.text((10, img.height - 40), text, font=font, fill="white")
    output_path = "static/output.jpg"
    img.save(output_path)
    return output_path
