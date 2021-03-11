import json

from GoogleNews import GoogleNews
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/search', methods=['GET'])
def search():
    google_news = GoogleNews()
    google_news.set_lang(lang="cn")
    google_news.search(request.args.get("key"))
    result = google_news.result()

    newses = list()
    for news in result:
        newses.append({"title": news["title"], "link": news["link"]})

    return render_template("index.html", data=json.dumps(newses))


if __name__ == '__main__':
    app.run(debug=True)
