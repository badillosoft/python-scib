from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")
		
	usuario = request.form["usuario"]
	clave = request.form["clave"]
	# TODO: Validar usuario y clave
	if usuario == "pepe" and clave == "123":
		print "Ingresando con %s (%s)" % (usuario, clave)
		return redirect("/")
	
	return render_template("login.html", error=True)

app.run()