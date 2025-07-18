from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_image_path, text, output_image_path):
    image = Image.open(input_image_path).convert("RGB")
    draw = ImageDraw.Draw(image)

    # Use a truetype font or fallback
    try:
        font = ImageFont.truetype("arial.ttf", 28)
    except IOError:
        font = ImageFont.load_default()

    # New: use textbbox instead of deprecated textsize
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    width, height = image.size
    x = width - text_width - 20
    y = height - text_height - 20

    # Optional: Draw background rectangle for readability
    draw.rectangle(
        [(x - 10, y - 5), (x + text_width + 10, y + text_height + 5)],
        fill=(0, 0, 0, 180)
    )

    draw.text((x, y), text, fill=(255, 255, 255), font=font)
    image.save(output_image_path)
    print(f"✅ Watermark added and saved as {output_image_path}")
