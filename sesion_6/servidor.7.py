from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

client = MongoClient()
db = client.cic

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")
		
	usuario = request.form["usuario"]
	clave = request.form["clave"]
	
	usuario = db.usuarios.find_one({ 
		"usuario": usuario,
		"clave": clave
	})

	if not usuario:
		return render_template("login.html", error=True)

	# Activar la sesion

	return redirect("/")

app.run()