from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient

client = MongoClient()
db = client.cic

app = Flask(__name__)
app.secret_key = 'MI_CLAVE_SECRETA_123'

@app.route("/")
def home():
	if "usuario" in session:
		return "Bienvenido %s" % session["usuario"]

	return redirect("/login")

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