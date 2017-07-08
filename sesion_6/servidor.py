from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient
from datetime import datetime
import re

client = MongoClient()
db = client.cic

app = Flask(__name__)
app.secret_key = 'MI_CLAVE_SECRETA_123'

@app.route("/")
def home():
	if "usuario" in session:
		messages = db.mensajes.find({})
		return render_template("chat.html", messages=messages)

	return redirect("/login")

@app.route("/nuevo-mensaje", methods=["POST"])
def nuevo_mensaje():
	user = session["usuario"]
	date = datetime.now().isoformat()
	content = request.form["mensaje"]
	
	db.mensajes.insert_one({
		"user": user,
		"date": date,
		"content": content
	})

	# BOT
	pattern = "[\w\.\-\_]+@\w+\.\w+"
	#match = re.search(pattern, content)
	for match in re.finditer(pattern, content):
		email = match.group(0)
		db.mensajes.insert_one({
			"user": "BOT",
			"date": "???",
			"content": "Hola me encontre este correo %s >:)" % email
		})

	return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")
		
	usuario = request.form["usuario"]
	clave = request.form["clave"]
	
	doc_usuario = db.usuarios.find_one({ 
		"usuario": usuario,
		"clave": clave
	})

	if not doc_usuario:
		return render_template("login.html", error=True)

	# Activar la sesion
	session["usuario"] = doc_usuario["usuario"]

	return redirect("/")

app.run()