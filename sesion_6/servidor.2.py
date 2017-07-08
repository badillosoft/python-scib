from flask import Flask

app = Flask(__name__)

@app.route("/hola/<nombre>")
def hola(nombre):
	return "Hola %s" % nombre

app.run()