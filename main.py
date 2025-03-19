from flask import Flask, render_template
import requests
from datetime import datetime
app = Flask(__name__)

ulr = "https://api.npoint.io/c3ca1ffbce863c6b5d8c"
@app.route('/')
def get_all_posts():
    response = requests.get(ulr)
    data = response.json()
    year = datetime.now().year
    month = datetime.now().strftime("%B")
    day = datetime.now().day
    return render_template("index.html", posts=data, year=year, month=month, day=day)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post<post_id>')
def place_post(post_id):
    response = requests.get(ulr)
    data = response.json()
    year = datetime.now().year
    for post in data:
        if post['id'] == int(post_id):
            return render_template("post.html", title=post['title'], subtitle=post['subtitle'], content=post['body'], img_url=post['image_url'], year=year)

if __name__ == '__main__':
    app.run(debug=True)