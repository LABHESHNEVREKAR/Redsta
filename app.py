from flask import Flask, render_template, request, send_file
from reddit_scraper import fetch_image_post
from caption_generator import generate_caption
from image_editor import add_watermark

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    caption = None
    image_path = None
    error = None  # For error message

    if request.method == "POST":
        subreddit = request.form["subreddit"]
        post = fetch_image_post(subreddit)

        if post is None:
            error = "❌ No valid image found in that subreddit. Try again."
        else:
            caption = generate_caption(post['title'], post['author'], subreddit)
            image_path = add_watermark(post['image_url'], post['author'], subreddit)

    return render_template("index.html", caption=caption, image_path=image_path, error=error)

@app.route("/download")
def download():
    return send_file("static/output.jpg", as_attachment=True)

# ✅ This part is required to start the server
if __name__ == "__main__":
    app.run(debug=True)
