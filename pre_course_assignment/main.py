from flask import Flask

from flask import Flask, render_template, url_for
app = Flask(__name__)

import random, os
from os import listdir

@app.route('/')
def hello():
    repo = "https://github.com/jensen-jx/pre-course-assignment"
    quote = get_random_quote()
    img = get_random_image()
    return render_template('index.html', img = img, quote = quote, repo = repo)

def get_random_quote() -> str:
    quotes = [
        "Logic will get you from A to B. Imagination will take you everywhere.",
        "There are 10 kinds of people. Those who know binary and those who don't.",
        "There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies.",
        "It's not that I'm so smart, it's just that I stay with problems longer",
        "It is pitch dark. You are likely to be eaten by a grue."
    ]

    num = random.randint(0, 4)
    return quotes[num]


def get_random_image() -> str:
    num = random.randint(0, 4)
    image_names = listdir("./static/images")
    selected = image_names[num]
     
    return  url_for('static', filename=f"/images/{selected}")  

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000, debug=False)