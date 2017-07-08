from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def login():
	return render_template("login.html")

@app.route("/login", methods=["POST"])
def foo():
	usuario = request.form["usuario"]
	clave = request.form["clave"]
	# TODO: Validar usuario y clave
	print "Ingresando con %s (%s)" % (usuario, clave)
	return redirect("/")

app.run()