from re import search
import flask
from flask import request, jsonify

from search import Similar

app = flask.Flask(__name__)
app.config["DEBUG"] = True

TITLE = "title"
CONTENT = "content"
FAKE = "FAKE"
REAL = "REAL"
covid_bert_small_model = None
main_bert_small_model = None
covid_bert_tiny_model = None
similar = Similar


@app.route('/', methods=['GET', 'POST'])
def home():
    return jsonify({"health": "API is Working"})

@app.route('/covid_bert_small', methods=['GET', 'POST'])
def covid_bert_small():
    news = request.json
    if(news == None or news[TITLE] == None or news[CONTENT] == None): return jsonify({"error": "Incorrect Schema"})
    y_pred = covid_bert_small_model.pred(news[TITLE], news[CONTENT])
    json = {}
    json["type"] = FAKE if y_pred[0] == 0 else REAL
    json["prob"] = y_pred[1]
    json["coloring"] = y_pred[2]
    print(json)
    return jsonify(json)

@app.route('/covid_bert_tiny', methods=['GET', 'POST'])
def main_bert_tiny():
    news = request.json
    if(news == None or news[TITLE] == None or news[CONTENT] == None): return jsonify({"error": "Incorrect Schema"})
    y_pred = covid_bert_tiny_model.pred(news[TITLE], news[CONTENT])
    json = {}
    json["type"] = FAKE if y_pred[0] == 0 else REAL
    json["prob"] = y_pred[1]
    json["coloring"] = y_pred[2]
    print(json)
    return jsonify(json)

@app.route('/main_bert_small', methods=['GET', 'POST'])
def main_bert_small():
    news = request.json
    if(news == None or news[TITLE] == None or news[CONTENT] == None): return jsonify({"error": "Incorrect Schema"})
    y_pred = main_bert_small_model.pred(news[TITLE], news[CONTENT])
    json = {}
    json["type"] = FAKE if y_pred[0] == 0 else REAL
    json["prob"] = y_pred[1]
    json["coloring"] = y_pred[2]
    print(json)
    return jsonify(json)


@app.route('/sim', methods=['GET', 'POST'])
def sim():
    news = request.json
    if(news == None or news[TITLE] == None or news[CONTENT] == None): return jsonify({"error": "Incorrect Schema"})
    full = news[TITLE] + " " + news[CONTENT]
    top_news = search.pred(full)
    json = {"sim": top_news}
    print(json)
    return jsonify(json)

@app.route('/main', methods=['GET', 'POST'])
def main():
    news = request.json
    print(news["title"])
    print(news['body'])
    return jsonify(news)

app.run(host='0.0.0.0', port=5000, debug=True)
