from flask import Flask, render_template, request, redirect, session, url_for
from flask_session import Session

app = Flask(__name__, template_folder="templates")
# Check Configuration section for more details
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)


endwords = [] #TODO: move to session
lines = [] #TODO: move to session


@app.route("/")
def index():
	session["ew_counter"] = 0
	return render_template("index.html", endwords=endwords, endwords_count=len(endwords))

@app.route("/addword", methods=["POST"])
def addWord():
	word = request.form['word']
	if len(word) > 0:
		endwords.append(word)
	return redirect(url_for("index"))

@app.route("/clear", methods=["GET"])
def clearWords():
	endwords.clear()
	lines.clear()
	return redirect(url_for("index"))

@app.route("/write")
def writeSestina():
	return render_template("write.html", endwords=endwords, lines=lines, lineindex=session["ew_counter"])

@app.route("/addline", methods=["POST"])
def addLine():
	lines.append(request.form['line'])
	session["ew_counter"] += 1 #TODO: this will go outside of array bounds.
	return redirect(url_for("writeSestina"))


if __name__ == '__main__':
	app.run(debug=True)