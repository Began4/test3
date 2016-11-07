from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def hello1():
	return "my name is ttt"

@app.route("/name")
def hello():
	return "my name is"
	
@app.route("/name/<name>")
def name(name):
	return "my name is"+ name
	
@app.route("/firstname", methods =["GET"])
def get():
	var = request.args.get("firstname")
	return var

@app.route("/firstnamepost", methods =["POST"])
def post():
	var = request.form["firstname"]
	return var

@app.route("/hello/")
@app.route("/hello/<name>")
def hello4(name=None):
    return render_template('hello.html', name=name)
	
if __name__ == "__main__":
	app.run()

