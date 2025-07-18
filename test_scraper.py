from reddit_scraper import fetch_image_post
from download_image import download_image
from add_credit import add_watermark
from caption_generator import generate_caption

# Step 1: Get post data
post = fetch_image_post("carporn")  # or "cars", "carporn", etc.

if not post:
    print("❌ Could not fetch a valid image post.")
else:
    # Step 2: Download image
    image_filename = "post.jpg"
    download_image(post["image_url"], image_filename)

    # Step 3: Add watermark (credit)
    credit_text = f"📸 u/{post['author']} | r/modifiedcars"
    watermarked_filename = "ready.jpg"
    add_watermark(image_filename, credit_text, watermarked_filename)

    # Step 4: Generate caption
    caption = generate_caption(post["title"], post["author"], "modifiedcars")

    # Final output
    print("✅ Done!")
    print("📷 Image ready: ", watermarked_filename)
    print("📝 Caption:\n", caption)
