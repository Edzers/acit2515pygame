import flask
from components import score

app = flask.Flask(__name__)

@app.route("/")
def home():
    scoreobj = score.Score()
    scoreobj.read_score()
    return flask.render_template("home.html", scores = scoreobj.scores)


if __name__ == '__main__':
    app.run(debug=True)
