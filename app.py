from flask import Flask, render_template, request, redirect, session, url_for
from stanza import *
from flask_session import Session

app = Flask(__name__, template_folder="templates")
# Check Configuration section for more details
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)


lines = [] #TODO: move to session
stanzas = [] #TODO: move to session
envoi_type = "Bishop" #TODO: make this configurable


@app.route("/")
def index():
	if len(session["endwords"]) == 0:
		session["ew_counter"] = 0
		session["stanza_counter"] = 0
		session["completed_sestina"] = []
	return render_template("index.html", endwords_count=len(session["endwords"]))

@app.route("/addword", methods=["POST"])
def addWord():
	word = request.form['word']
	if len(word) > 0:
		session["endwords"].append(word)
	return redirect(url_for("index"))

@app.route("/removeword", methods=["POST"])
def removeWord():
	session["endwords"].pop(len(session["endwords"]) - 1)
	return redirect(url_for("index"))

@app.route("/clear", methods=["GET"])
def clearWords():
	session["endwords"].clear()
	lines.clear()
	stanzas.clear()
	session["completed_sestina"].clear()
	return redirect(url_for("index"))

@app.route("/write")
def writeSestina():
	if 0 <= session["stanza_counter"] <= 5: 
		current_stanza = getStanzaAtIndex(session["endwords"], session["stanza_counter"])
	elif session["stanza_counter"] == 6:
		current_stanza = getEnvoiStanza(session["endwords"], envoi_type)
	else:
		current_stanza = ["Your sestina is complete!"]
	return render_template("write.html", endwords=current_stanza, lines=lines, stanzas=session["completed_sestina"], lineindex=session["ew_counter"])

@app.route("/addline", methods=["POST"])
def addLine():
	lines.append(request.form['line'])
	if session["ew_counter"] >= 5:
		session["ew_counter"] = 0
		finished_stanza = lines.copy()
		stanzas.append(finished_stanza)
		session["completed_sestina"].append(finished_stanza)
		lines.clear()
		session["stanza_counter"] += 1
	else: 
		session["ew_counter"] += 1
	return redirect(url_for("writeSestina"))


if __name__ == '__main__':
	app.run(debug=True)